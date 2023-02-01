import requests
from vacancies.models import Vacancy, Schedule
import datetime
day = datetime.datetime.now().date()



now = datetime.datetime.now()
current_time = now.strftime("%H:%M:00")

def send_telegram(message) -> str:
    try:
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" \
                  + chat_id + "&text=" + str(message)
        results = requests.get(url_req)
        return results.json()
    except Exception as ex:
        print(ex)


def send_bot():
    schedule = Schedule.objects.get(day=day)
    vacancies = Vacancy.objects.filter(schedule=schedule.id)
    res_lst = []

    for vacancy in vacancies:
        message = {"chat_id": vacancy.chat.chat_id, "client": vacancy.client.account_id,
                   "vacancy": vacancy.text}

        send_telegram(message)

        # for v in vacancy.time.all():
        #     print(type(current_time), type(v))
        #     print(current_time, str(v))
        #     if current_time == str(v):
        #         print(v)
        #         print(message)
        #         send_telegram(message)



        #     print(v.name)
        # for v in vacancy.chat.all():
        #     print(v.chat_id)
        # for v in vacancy.time.all():
        #     print(v.time)
        break



    # data = Company.objects.all().values("day", "from_time", "before_time", "quantity_per_day", "chats__chat_id" ,
    #                                     "chats__id", "chats__name", "client__name", "client__client_id", "vacancy__text",
    #                                     "vacancy__title",
    #                                     )
    #
    # for d in data:
    #     message = {"client": d["client__client_id"], "chat_id": d["chats__chat_id"], "vacancy": d["vacancy__text"]}
    #     send_telegram(message)
