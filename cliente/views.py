from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode
from rest_framework.exceptions import ValidationError

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error":"Email é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://127.0.0.1:8000/reset-password/{uid}/{token}"
            send_mail(
                "Redefinição de senha",
                f"Clique no link para redefinir sua senha: {reset_link}",
                "exemploemail@gmail.com",
                [email],
            )
            return Response({"message":"Link de redefinição de senha enviado!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error":"Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
      
        try:
            user_id = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=user_id)
            if not default_token_generator.check_token(user, token):
                return Response({"error":"Token inválido ou expirado"}, status=status.HTTP_400_BAD_REQUEST)

            new_password = request.data.get('pssword')
            if not new_password:
                return Response({"error":"Nova senha é obrigatória"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({"message":"Senha redefinida com sucesso!"}, status=status.HTTP_200_OK)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error":"Link inválido"}, status=status.HTTP_400_BAD_REQUEST)
