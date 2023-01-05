from django.urls import include, path
from .views import JobsCreate, JobsList, JobsDetail, JobsUpdate, JobsDelete,SpecialismsList,SpecialitiesList

urlpatterns = [
    path('create/', JobsCreate.as_view(), name='create-jobs'),
    path('', JobsList.as_view()),
    path('<int:pk>/', JobsDetail.as_view(), name='retrieve-jobs'),
    path('update/<int:pk>/', JobsUpdate.as_view(), name='update-jobs'),
    path('list-specialism/', SpecialismsList.as_view(), name='list-specialism'),
     path('list-specialties/', SpecialitiesList.as_view(), name='list-specialties'),
   
]