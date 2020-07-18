from app import urls as app_urls
from django.urls import path
from app import views

app_name='app'
urlpatterns = [
    path('api/v1/applicants', views.ApplicantListCreateAPIView.as_view(), name='applicant-list'),
    path('api/v1/applicants/<int:pk>', views.ApplicantRetrieveUpdateDestroyAPIView.as_view(), name='applicant-detail'),

    path('api/v1/vacancies', views.VacancyListCreateAPIView.as_view(), name='vacancy-list'),
    path('api/v1/vacancies/<int:pk>', views.VacancyRetrieveUpdateDestroyAPIView.as_view(), name='vacancy-detail'),

    path('api/v1/resumes', views.ResumeListCreateAPIView.as_view(), name='resume-list'),
    path('api/v1/resumes/<int:pk>', views.ResumeRetrieveUpdateDestroyAPIView.as_view(), name='resume-detail'),

    path('api/v1/departments', views.DepartmentListCreateAPIView.as_view(), name='department-list'),
    path('api/v1/departments/<int:pk>', views.DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='deparment-detail'),
]
