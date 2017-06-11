from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'create_user', views.UserCreateViewSet,
                base_name='create_user')
router.register(r'user_details', views.UserDetailViewSet,
                base_name='user_details')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api_root$', views.APIRoot.as_view()),
    url(r'', include(router.get_urls())),
    url(r'user_login$', csrf_exempt(views.UserLoginView.as_view())),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
