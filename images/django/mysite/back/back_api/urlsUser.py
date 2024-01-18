from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .userViews import UserCreate, UserConnect, UserList, UserDetail, UserUpdate, UserDelete, createTournament, Update2FA, Keycheck, verif_mail, verif_mail_key
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
	path('create/', UserCreate, name='create-user'),
	path('connect/', UserConnect, name='connect-user'),
	path('<int:pk>/update-2fa/', Update2FA, name='update-2fa'),
	path('leaderboard/', UserList),
	path('<int:pk>/', UserDetail, name='retrieve-user'),
	path('update/<int:pk>/', UserUpdate, name='update-user'),
	path('delete/<int:pk>/', UserDelete, name='delete-user'),
	path('<int:pk>/createtournament/', createTournament, name='delete-user'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('<int:pk>/key/', Keycheck, name='Keycheck'),
	path('<int:pk>/verif_mail/', verif_mail, name='verif_mail'),
	path('<int:pk>/verif_mail_key/', verif_mail_key, name='verif_mail_key'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
