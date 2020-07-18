from django.shortcuts import render
from app.models import Applicant, Vacancy, Department, Resume
from app.serializers import (
    ApplicantSerializer,
    DepartmentSerializer,
    VacancySerializer,
    ResumeSerializer,
)
from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly,
)

# Create your views here.
class ApplicantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes  = [IsAuthenticated,IsAdminUser,]



class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes  = [IsAuthenticated,IsAdminUser]


class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes  = [IsAuthenticated,IsAdminUser]



class VacancyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes  = [IsAuthenticatedOrReadOnly,IsAdminUser]


class VacancyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes  = [IsAuthenticatedOrReadOnly,]



class ResumeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer



class ResumeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes  = [IsAuthenticated,IsAdminUser,]

