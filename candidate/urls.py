from django.urls import include, path
from .views import CandidateCreate, CandidateList, CandidateDetail, CandidateUpdate, CandidateDelete, CreateCandidateJobApplication,ListCandidateJobApplication,ListCandidateProfiles,CandidateProfileDetail,ProfilesUpdate,CreateProfiles


urlpatterns = [
    path('create/', CandidateCreate.as_view(), name='create-candidate'),
    path('', CandidateList.as_view()),
    path('<int:pk>/', CandidateDetail.as_view(), name='retrieve-candidate'),
    path('update/<int:pk>/', CandidateUpdate.as_view(), name='update-candidate'),
    path('delete/<int:pk>/', CandidateDelete.as_view(), name='delete-candidate'),
    path('create-create-job-interested/', CreateCandidateJobApplication.as_view(), name='create-jobs-interested-in'),
    path('list-jobs-interested/', ListCandidateJobApplication.as_view(), name='list-jobs-interested'),
    path('list-profiles/', ListCandidateProfiles.as_view(), name='list-profiles'),
    path('profile/<int:pk>/', CandidateProfileDetail.as_view(), name='retrieve-profile'),
    path('profile/update/<int:pk>/', ProfilesUpdate.as_view(), name='update-candidate'),
    path('profile/create/', CreateProfiles.as_view(), name='create-candidate'),
    
    
   
]