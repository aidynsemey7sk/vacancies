from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_chat_constraint',
                fields=['name', 'chat_id']
            )]


class TelegramClient(models.Model):
    name = models.CharField(max_length=100)
    account_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class VacancyTime(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False)

    def __str__(self):
        return str(self.time)


class Schedule(models.Model):
    day = models.DateField(auto_now=True, unique=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=3000)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="schedule", null=True)

    client = models.ForeignKey(TelegramClient, on_delete=models.CASCADE, related_name="schedule", null=True)
    # client = models.ManyToManyField(TelegramClient)
    time = models.ManyToManyField(VacancyTime)
    # chat = models.ManyToManyField(Chat)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="schedule", null=True)

    # created_at = models.DateTimeField(auto_now=True)
    # enable = models.BooleanField(default=False)
    # quantity_per_day = models.IntegerField()



#
#
# class Chat(models.Model):
#     name = models.CharField(max_length=100)
#     chat_id = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 name='unique_chat_constraint',
#                 fields=['name', 'chat_id']
#             )]
#
#
# class TelegramClient(models.Model):
#     name = models.CharField(max_length=100)
#     client_id = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# class Vacancy(models.Model):
#     title = models.CharField(max_length=300)
#     text = models.CharField(max_length=3000)
#     # created_at = models.DateTimeField(auto_now=True)
#     enable = models.BooleanField(default=False)
#     quantity_per_day = models.IntegerField()
#
#     def __str__(self):
#         return self.title
#
#
# class VacancyTime(models.Model):
#     my_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
#
#     def __str__(self):
#         return str(self.my_time)
#
# class Company(models.Model):
#     # vacancy_id = models.ManyToManyField(Vacancy, related_name='vacancy')
#     vacancy = models.ForeignKey(Vacancy, related_name='vacancy', on_delete=models.CASCADE)
#     # chat_id = models.ManyToManyField(Chat)
#     chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
#     # client_id = models.ManyToManyField(TelegramClient)
#     client= models.ForeignKey(TelegramClient, on_delete=models.CASCADE)
#
#     time_id = models.ManyToManyField(VacancyTime)
#
#     day = models.DateField(auto_now=True)
#     # from_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
#     # before_time = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False)
#     # quantity_per_day = models.IntegerField()
#
#     # class Meta:
#     #     constraints = [
#     #         models.UniqueConstraint(
#     #             name='unique_company_constraint',
#     #             fields=['vacancy', 'chats', 'client']
#     #         )]
#
#
#
#
#
#
# "test_shat_1	878701021	4"
# "test_chat_2	611061870	3"
#
#
# """Aidyn	917658224
# Max	917658345"""
#
# """aa1 = Advertisements(text="Объявление 1", from_time=time(11, 30), enamble=True, before_time=time(16, 30), quantity_per_day=3, before_day=datetime(2023, 1, 29))"""