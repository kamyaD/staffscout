from django.urls import path
from .views import index

# router = routers.DefaultRouter()
# router.register(r'users', views.LoginView)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', index),
    path('login', index),
    path('signup', index),
    
]
