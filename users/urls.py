from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet,UserLogin, RegisterView, UserDetail,UserUpdate
# from jobs import views


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-user-login/', UserLogin.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('list-users/', UserViewSet.as_view(), name='list-users'),
    path('get-single-user/<int:pk>/', UserDetail.as_view(), name='get-single-user/'),
    path('update-user/<int:pk>/', UserUpdate.as_view(), name='update-user'),

    # path('users/<int:pk>/', UserDetail.as_view()),
    
]