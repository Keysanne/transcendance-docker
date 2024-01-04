from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .tournamentViews import tournamentList, addContestant, removeContestant, tournamentStart, tournamentMatchResult, tournamentEnd, contestantList, userReady, matchStart

urlpatterns = [
	path('list/', tournamentList, name='tournament-list'),
	path('<int:tpk>/contestant-list/', contestantList, name='contestant-list'),
	path('<int:tpk>/add-contestant/<int:upk>/', addContestant, name='add-contestant'),
	path('<int:tpk>/remove-contestant/<int:upk>/', removeContestant, name='remove-contestant'),
	path('<int:pk>/start/', tournamentStart, name='tournament-start'),
	path('<int:tpk>/user/<int:upk>/ready/', userReady, name='user-ready'),
	path('<int:tpk>/match-start/', matchStart, name='match-start'),
	path('<int:pk>/match-result/', tournamentMatchResult, name='tournament-match-result'),
	path('<int:pk>/end/', tournamentEnd, name='tournament-end'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
