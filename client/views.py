from django.shortcuts import render

from .models import Vacancy, Resume

from django.http import HttpResponse



def vacancies_list(request):

    vacancies = Vacancy.objects.all()
    return render(request, 'client/client_vacancies.html', context={'vacancies': vacancies})


def vacancy_detail(request, slug):
    vacancy = Vacancy.objects.get(slug__iexact=slug)
    first_flag = 1 if bool(vacancy.in_waiting_for_resume.all() or vacancy.reject_for_resume.all()) else 0
    second_flag = 1 if bool(vacancy.in_waiting_for_resume.all() or vacancy.accept_for_resume.all()) else 0
    return render(request, 'client/client_vacancy_detail.html', context={
        'vacancy': vacancy,
        'first_flag': first_flag,
        'second_flag': second_flag
    })


def resumes_list(request):

    resumes = Resume.objects.all()
    return render(request, 'client/client_resumes.html', context={'resumes': resumes})


def resume_detail(request, slug):

    resume = Resume.objects.get(slug__iexact=slug)
    return render(request, 'client/client_resume_detail.html', context={'resume': resume})


def accepted_vacancies(request, slug):########################

    resume = Resume.objects.get(slug__iexact=slug)
    return render(request, 'client/client_accepted_vacancies.html', context={'resume': resume})


def rejected_vacancies(request, slug):##############################

    resume = Resume.objects.get(slug__iexact=slug)
    return render(request, 'client/client_rejected_vacancies.html', context={'resume': resume})


def accept_reject(request):#

    if request.GET['flag'] == 'accept' and Vacancy.objects.get(slug__iexact=request.GET['slug']).in_waiting_for_resume.all():
        print(request.GET['slug'], 1)
        r = Vacancy.objects.get(slug__iexact=request.GET['slug']).in_waiting_for_resume.get()
        v = Vacancy.objects.get(slug__iexact=request.GET['slug'])
        r.vacancies_accept.add(v)
        r.vacancies_in_waiting.remove(v)
        r.save()
        return HttpResponse('accept_server')

    elif request.GET['flag'] == 'reject' and Vacancy.objects.get(slug__iexact=request.GET['slug']).in_waiting_for_resume.all():
        print(request.GET['slug'],2)
        r = Vacancy.objects.get(slug__iexact=request.GET['slug']).in_waiting_for_resume.get()
        v = Vacancy.objects.get(slug__iexact=request.GET['slug'])
        r.vacancies_reject.add(v)
        r.vacancies_in_waiting.remove(v)
        r.save()
        return HttpResponse('reject_server')

    elif request.GET['flag'] == 'accept' and Vacancy.objects.get(slug__iexact=request.GET['slug']).reject_for_resume.all():
        print(request.GET['slug'],3)
        r = Vacancy.objects.get(slug__iexact=request.GET['slug']).reject_for_resume.get()
        v = Vacancy.objects.get(slug__iexact=request.GET['slug'])
        r.vacancies_accept.add(v)
        r.vacancies_reject.remove(v)
        r.save()
        return HttpResponse('accept_server')

    elif request.GET['flag'] == 'reject' and Vacancy.objects.get(slug__iexact=request.GET['slug']).accept_for_resume.all():
        print(request.GET['slug'], 4)
        r = Vacancy.objects.get(slug__iexact=request.GET['slug']).accept_for_resume.get()
        v = Vacancy.objects.get(slug__iexact=request.GET['slug'])
        r.vacancies_reject.add(v)
        r.vacancies_accept.remove(v)
        r.save()
        return HttpResponse('reject_server')


# Create your views here.
