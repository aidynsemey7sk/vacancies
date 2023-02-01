from vacancies.models import Vacancy, Schedule, VacancyTime, Chat, TelegramClient
from vacancies.forms import VacancyForm, ClientForm, ChatForm, TimeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime


def index(request):
    day = datetime.datetime.now().date()
    schedule = Schedule.objects.filter(day=day)
    if schedule:
        schedule = Schedule.objects.get(day=day)
    else:
        Schedule.objects.create()
        schedule = Schedule.objects.get(day=day)
    vacancies = Vacancy.objects.filter(schedule_id=schedule.id)
    return render(request, 'home.html', {"vacancies": vacancies})


def add_vacancy(request):
    day = datetime.datetime.now().date()
    schedule = Schedule.objects.get(day=day)
    if request.method == "POST":
        some_var = request.POST.getlist('vacancies')
        for x in some_var:
            obj = Vacancy.objects.get(id=x)
            obj.schedule_id = schedule.id
            obj.save()
        return HttpResponseRedirect('/vacancies')

    vacancies = Vacancy.objects.exclude(schedule_id=schedule.id)
    return render(request, 'vacancies/vacancies.html', {"vacancies": vacancies})


def add_time(request, vacancy_id):
    if request.method == "POST":
        times = request.POST.getlist('times')
        for x in times:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            vacancy.time.add(x)
        return HttpResponseRedirect('/vacancies')
    vac = Vacancy.objects.filter(id=vacancy_id).values('time__time')
    res = []
    for i in vac:
        res.append(i['time__time'])
    times = VacancyTime.objects.exclude(time__in=list(res))
    return render(request, 'times/add_time.html', {"times": times})


def add_chat(request, vacancy_id):
    if request.method == "POST":
        chats = request.POST.getlist('chats')
        for x in chats:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            vacancy.chat_id = x
            vacancy.save()
        return HttpResponseRedirect('/vacancies')
    vac = Vacancy.objects.filter(id=vacancy_id).values('chat__id')
    res = []
    for i in vac:
        res.append(i['chat__id'])
    chats = Chat.objects.exclude(id__in=list(res))
    return render(request, 'chats/add_chat.html', {"chats": chats})


def add_client(request, vacancy_id):
    if request.method == "POST":
        clients = request.POST.getlist('clients')
        for x in clients:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            vacancy.client_id = x
            vacancy.save()
        return HttpResponseRedirect('/vacancies')
    vac = Vacancy.objects.filter(id=vacancy_id).values('client__id')

    res = []
    for i in vac:
        res.append(i['client__id'])
    clients = TelegramClient.objects.exclude(id__in=list(res))
    return render(request, 'clients/add_client.html', {"clients": clients})


def create_vacancy(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies/')
    else:
        form = VacancyForm()

    return render(request, "vacancies/create_vacancy.html", {"form": form})


def update_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    form = VacancyForm(request.POST, instance=vacancy)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/vacancies/')
    else:
        form = VacancyForm(instance=vacancy)

    return render(request, 'vacancies/update_vacancy.html', {'form': form})


def create_time(request):
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies')
    else:
        form = TimeForm()

    return render(request, "times/create_time.html", {"form": form})


def create_chat(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies')
    else:
        form = ChatForm()

    return render(request, "chats/create_chat.html", {"form": form})


def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies')
    else:
        form = ClientForm()

    return render(request, "clients/create_client.html", {"form": form})


def remove_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy.schedule = None
    vacancy.save()
    return HttpResponseRedirect('/vacancies')


def remove_client(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy.client = None
    vacancy.save()
    return HttpResponseRedirect('/vacancies')


def remove_chat(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy.chat = None
    vacancy.save()
    return HttpResponseRedirect('/vacancies')


def remove_time(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy.time.clear()
    vacancy.save()
    return HttpResponseRedirect('/vacancies')

