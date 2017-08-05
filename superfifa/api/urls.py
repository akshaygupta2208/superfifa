from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'user_details', UserDetailViewSet,
                base_name='user_details')

router.register(r'league', LeagueViewSet,
                base_name='league')

router.register(r'team', TeamViewSet,
                base_name='team')

router.register(r'chairman', ChairmanViewSet,
                base_name='chairman')

router.register(r'scout', ScoutViewSet,
                base_name='scout')

router.register(r'coach', CoachViewSet,
                base_name='coach')

router.register(r'office', OfficeViewSet,
                base_name='office')

router.register(r'player', PlayerViewSet,
                base_name='player')

router.register(r'mediacompany', MediaCompanyViewSet,
                base_name='mediacompany')

router.register(r'journalist', JournalistViewSet,
                base_name='journalist')

router.register(r'news', NewsViewSet,
                base_name='news')
#router.register(r'player-list/(\d+)/$', UserPlayerListViewSet, base_name='user-player-list')
router.register(r'player-list', UserPlayerListViewSet, base_name='user-player-list')
# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.get_urls())),
    url(r'user-login', csrf_exempt(UserLoginView.as_view())),
    url(r'release-player$', csrf_exempt(ReleasePlayerView.as_view())),
    url(r'chat/(?P<user>[a-zA-Z0-9\w]+)$', csrf_exempt(ChatView.as_view())),
    url(r'chat-log$', csrf_exempt(ChatLogView.as_view())),
    url(r'player-list1/(\d+)$', get_player_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
