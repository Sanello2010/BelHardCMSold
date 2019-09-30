from django.urls import path
from . import views
from .views import *




urlpatterns = [
    path('vacancies/', vacancies_list, name='vacancies_list'),
    path('vacancy/<str:slug>/', vacancy_detail, name='vacancy_detail_url'),
    path('resumes/', resumes_list, name='resume_list_url'),
    path('resume_detail/<str:slug>/', resume_detail, name='resume_detail_url'),
    path('resume_detail/<str:slug>/accepted_vacancies/', accepted_vacancies, name='accepted_vacancies_url'),
    path('resume_detail/<str:slug>/rejected_vacancies/', rejected_vacancies, name='rejected_vacancies_url'),
    path('accept_reject/', views.accept_reject),

]
