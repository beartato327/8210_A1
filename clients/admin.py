from django.contrib import admin

from .models import Client, Comment, Vehicle


class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

class VehicleAdmin(admin.ModelAdmin):
    list_display =['client','make','model','latest_update']

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Vehicle, VehicleAdmin)

