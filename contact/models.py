from django.db import models


class Contact(models.Model):
    """
    Подписка по email
    Необходимо раскомментировать в шаблоне часть отвечающую за подписку
    """

    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
