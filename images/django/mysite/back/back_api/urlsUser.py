from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .userViews import UserCreate, UserConnect, UserDetail, UserUpdate, UserDelete, CreateTournament, StartGame, EndGame, GameHistory, GameFullHistory

urlpatterns = [
	path('create/', UserCreate, name='create-user'),
	path('connect/', UserConnect, name='connect-user'),
	path('<int:pk>/', UserDetail, name='retrieve-user'),
	path('update/<int:pk>/', UserUpdate, name='update-user'),
	path('delete/<int:pk>/', UserDelete, name='delete-user'),
	path('<int:pk>/createtournament/', CreateTournament, name='delete-user'),
	path('<int:pk>/startgame/', StartGame, name='start-game'),
	path('<int:gpk>/endgame/', EndGame, name='end-game'),
	path('<int:pk>/gamehistory/', GameHistory, name='game-history'),
	path('<int:pk>/gamefullhistory/', GameFullHistory, name='game-full-history'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
