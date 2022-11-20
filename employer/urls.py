from django.urls import include, path
from .views import EmployerCreate, EmployerList, EmployerDetail, EmployerUpdate, EmployerDelete


urlpatterns = [
    path('create/', EmployerCreate.as_view(), name='create-employer'),
    path('', EmployerList.as_view()),
    path('<int:pk>/', EmployerDetail.as_view(), name='retrieve-employer'),
    path('update/<int:pk>/', EmployerUpdate.as_view(), name='update-employer'),
    path('delete/<int:pk>/', EmployerDelete.as_view(), name='delete-employer')
]