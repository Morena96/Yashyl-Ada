from django.contrib import admin

from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'company', )


admin.site.register(ContactUs, ContactUsAdmin)
