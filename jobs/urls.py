from django.urls import include, path
from .views import JobsCreate, JobsList, JobsDetail, JobsUpdate, JobsDelete


urlpatterns = [
    path('create/', JobsCreate.as_view(), name='create-jobs'),
    path('', JobsList.as_view()),
    path('<int:pk>/', JobsDetail.as_view(), name='retrieve-jobs'),
    path('update/<int:pk>/', JobsUpdate.as_view(), name='update-jobs'),
    # path('delete/<int:pk>/', JobsDelete.as_view(), name='delete-jobs')
]