from django.conf.urls import url, include
from rest_framework import routers
from .views import UsersNestedViewSet, ProfileListView, ProfileViewSet, UserListView, UsersViewSet

# api_router = routers.SimpleRouter()
# api_router.register(r'users', UsersViewSet, basename='user')

urlpatterns = [
    url(r'^usersnested/$', UsersNestedViewSet.as_view()),
    url(r'^profile/$', ProfileListView.as_view()),
    url(r'^profile/(?P<pk>\d+)/$', ProfileViewSet.as_view()),
    url(r'^users/$', UserListView.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UsersViewSet.as_view()),
    # url('', include(api_router.urls)),
    # url(r'^api/users$', views.users_list),
    # url(r'^api/users/<int:pk>/', views.users_detail),
    # url(r'^api/users/published$', views.UsersViewSet),
    # url(r'^api/profile$', views.profile_list),
    # url(r'^api/profile/<int:pk>/', views.profile_detail),
]
