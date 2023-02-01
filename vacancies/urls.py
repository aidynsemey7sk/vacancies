from django.urls import path
from vacancies.views import index, add_vacancy, add_time, add_chat, add_client, create_vacancy, \
    create_client, create_chat, create_time, update_vacancy, remove_vacancy, remove_client, remove_chat, remove_time
#
# # from vacancies.views import index, by_vacancy, VacancyCreateView, add_vacancy, add_company
# from vacancies.views import index,  add_company, add_vacancy, by_vacancy, \
#     get_vacancies, by_company,get_chats, get_clients, by_chat, by_client, custom_add_chat, add_client
#
urlpatterns = [
    path('', index, name='index'),
    path('add-vacancy/', add_vacancy, name='add_vacancy'),
    path('create-vacancy/', create_vacancy, name="create_vacancy"),

    path('add-time/<int:vacancy_id>/', add_time, name='add_time'),
    path('add-chat/<int:vacancy_id>/', add_chat, name='add_chat'),
    path('add-client/<int:vacancy_id>/', add_client, name='add_client'),

    path('create-client/', create_client, name="create_client"),
    path('create-chat/', create_chat, name="create_chat"),
    path('create-time/', create_time, name="create_time"),

    path('update-vacancy/<int:vacancy_id>/', update_vacancy, name='update_vacancy'),
    path('update-vacancy/<int:vacancy_id>/', update_vacancy, name='update_vacancy'),

    path('remove-vacancy/<int:vacancy_id>/', remove_vacancy, name='remove_vacancy'),
    path('remove-time/<int:vacancy_id>/', remove_time, name='remove_time'),
    path('remove-client/<int:vacancy_id>/', remove_client, name='remove_client'),
    path('remove-chat/<int:vacancy_id>/', remove_chat, name='remove_chat'),



# Company
#     path('', index, name='index'),
#     path('add_company/', add_company, name="add_company"),
#     path('company/<int:company_id>/', by_company, name="by_company"),
#
#
#     # Vacancy
#     path('vacancy/', get_vacancies, name="get_vacancies"),

#     path('vacancy/<int:vacancy_id>/', by_vacancy, name='by_vacancy'),
#
#     # Chats
#     path('chats', get_chats, name="get_chats"),
#     path('chats/<int:chat_id>/', by_chat, name="by_chat"),
#     path('add_my_chat/', custom_add_chat, name="custom_add_chat"),
#
#     # Clients
#     path('clients', get_clients, name="get_clients"),
#     path('clients/<int:client_id>/', by_client, name="by_client"),
#
#
#     # path('add/', VacancyCreateView.as_view(), name="add"),
#     # path('add/', VacancyUpdateView.as_view(), name="add"),
#     # path("int:advertising_id/", by_advertising)
]