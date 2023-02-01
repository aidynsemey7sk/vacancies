# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from vacancies.models import Chat
#
#
# @api_view(['POST'])
# def add_chat(request):
#     data = request.data
#     print(data)
#
#     res_lst = []
#     for dt in data["chat_list"]:
#         chat = Chat(name=dt['name'], chat_id=dt['chat_id'], rule=0)
#         res_lst.append(chat)
#     Chat.objects.bulk_create(res_lst,
#                              batch_size=1000,
#                              ignore_conflicts=True)
#
#     return Response("")
