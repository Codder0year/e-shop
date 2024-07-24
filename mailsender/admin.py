from django.contrib import admin


from .models import Client, Message, MailingAttempt, SpamServis


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title',)


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'attempt_date', 'status', 'server_response')
    list_filter = ('status',)
    search_fields = ('server_response',)


@admin.register(SpamServis)
class SpamServisAdmin(admin.ModelAdmin):
    list_display = ('first_send_date', 'frequency', 'status', 'message')
    list_filter = ('status', 'frequency')
    search_fields = ('message__title',)
