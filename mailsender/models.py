from django.db import models


# Create your models here.

class Client(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, default='не указан')
    comment = models.TextField(default='')

    def __str__(self):
        return self.name


class Message(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default='')


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failure', 'Failure'),
    ]

    mailing = models.ForeignKey('SpamServis', on_delete=models.CASCADE, related_name='attempts')
    attempt_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"


class SpamServis(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ]

    FREQUENCY_CHOICES = [
        ('1', 'Every Minute'),
        ('5', 'Every 5 Minutes'),
        ('15', 'Every 15 Minutes'),
        ('30', 'Every 30 Minutes'),
        ('60', 'Every Hour'),
        ('1440', 'Daily'),  # 1440 minutes in a day
    ]

    first_send_date = models.DateTimeField()
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Mailing {self.id} - {self.status}"