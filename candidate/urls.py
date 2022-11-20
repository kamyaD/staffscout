from django.urls import include, path
from .views import CandidateCreate, CandidateList, CandidateDetail, CandidateUpdate, CandidateDelete


urlpatterns = [
    path('create/', CandidateCreate.as_view(), name='create-candidate'),
    path('', CandidateList.as_view()),
    path('<int:pk>/', CandidateDetail.as_view(), name='retrieve-candidate'),
    path('update/<int:pk>/', CandidateUpdate.as_view(), name='update-candidate'),
    path('delete/<int:pk>/', CandidateDelete.as_view(), name='delete-candidate')
]