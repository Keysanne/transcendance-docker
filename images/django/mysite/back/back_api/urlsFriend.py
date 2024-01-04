from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .friendViews import createRequest, acceptRequest, denyRequest, blockRequest, unfriend, viewRequest, listRequest

urlpatterns = [
	path('<int:pk>/invite/<str:username>/', createRequest, name='create-request'),
	path('<int:pk>/accept/<str:username>/', acceptRequest, name='accept-request'),
	path('<int:pk>/deny/<str:username>/', denyRequest, name='deny-request'),
	path('<int:pk>/block/<str:username>/', blockRequest, name='block-request'),
	path('<int:pk>/unfriend/<str:username>/', unfriend, name='unfriend'),
	path('<int:pk>/pending/', viewRequest, name='view-pending-request'),
	path('<int:pk>/list/', listRequest, name='list-request'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
