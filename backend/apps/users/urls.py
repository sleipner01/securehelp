from django.urls import path, include
from apps.users import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('api/users', views.UserViewSet, basename='users')
router.register('api/register', views.RegistrationViewSet, basename='register')
router.register('api/login', views.LoginViewSet, basename='login')
router.register('api/refresh', views.RefreshViewSet, basename='refresh')
router.register('api/documents', views.DocumentViewSet, basename='documents')
# router.register('api/blacklist', views.LogoutViewSet, basename='blacklist')

urlpatterns = [*router.urls,
               path("api/verify-email/<uidb64>/<token>/",
                    views.VerificationView.as_view(), name="verify-email"),
               path("api/document-download/<int:pk>/",
                    views.DocumentDownloadView.as_view(), name="document-download"),
               path("api/refugee-documents/<refugee_username>/",
                    views.GetDocumentsForRefugeeView.as_view(), name="refugee-documents"),
               path('api/reset-password/<uidb64>/<token>/',
                    views.ResetPasswordView.as_view(), name='password-reset'),
               path('api/request-reset-password/',
                    views.PasswordResetEmailView.as_view(), name='password-reset-email'),
               path('api/reset-password-validate/',
                    views.SetNewPasswordView.as_view(), name='password-reset-valid'),
               path('api/blacklist/', 
                    views.LogoutView.as_view(), name='token_blacklist'),
               ]
