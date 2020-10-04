from django.conf.urls import url, include
from rest_framework import routers
from users import views

api_router = routers.DefaultRouter()
# api_router.register(r'allusers', views.ViewUsersData, basename='alluser')
api_router.register(r'userlists', views.users_list, basename='userlist')
api_router.register(r'profilelist', views.profile_list, basename='profilelist')
api_router.register(r'users/<int:pk>/', views.user_detail,
                    basename='userdetail')
api_router.register(r'profiles/<int:pk>/',
                    views.profile_detail, basename='profiledetail')
api_router.register(r'userdelete', views.user_delete, basename='userdelete')

urlpatterns = [
    url('', include(api_router.urls)),
    # url(r'^api/users$', views.users_list),
    # url(r'^api/users/<int:pk>/', views.users_detail),
    # url(r'^api/users/published$', views.UsersViewSet),
    # url(r'^api/profile$', views.profile_list),
    # url(r'^api/profile/<int:pk>/', views.profile_detail),
]
