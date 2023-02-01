from django.forms import ModelForm
from django import forms

from vacancies.models import Vacancy, Chat, TelegramClient, VacancyTime


class VacancyForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   "placeholder": "Введите название вакансии"}))

    text = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   "placeholder": "Введите текст вакансии"}))

    class Meta:
        model = Vacancy
        fields = ("title", 'text')


class TimeForm(ModelForm):
    time = forms.TimeField(widget=forms.TextInput(attrs={
        'type': "time"
    }))

    class Meta:
        model = VacancyTime
        fields = ("time",)


class ChatForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   "placeholder": "Введите название чата"}))
    chat_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   "placeholder": "Введите ID чата"}))

    class Meta:
        model = Chat
        fields = ('name', "chat_id")


class ClientForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   "placeholder": "Введите имя телеграм аккаунта"}))
    account_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   "placeholder": "Введите ID телеграм аккаунта"}))

    class Meta:
        model = TelegramClient
        fields = ('name', "account_id")
