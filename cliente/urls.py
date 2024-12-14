from django.urls import path, include
from . import views
from .views import UserViewSet, RegisterUserView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('', views.task_list, name='lista_tarefas'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('add/', views.add_task, name='add_task'),
    path('delete/task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('atualizar/task/<int:id>/', views.atualizar_tasks, name='atualizar_task'),
]

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns += [
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('password-reset/', PasswordResetView.as_view(), name="password-reset"),
#     path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
# ]