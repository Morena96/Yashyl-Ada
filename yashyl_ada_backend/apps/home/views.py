from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from .forms import ContactForm
from .models import ContactUs
from ... import settings


class HomeView(SuccessMessageMixin, CreateView):
    model = ContactUs
    form_class = ContactForm
    success_url = '/'
    template_name = 'app/home/index.html'
    success_message = _('Thanks for contact us!')

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        message = f"""
        Email: {data.get('email')}
        Company: {data.get('company')}
        Phone: {data.get('phone')}
        Text:
        {data.get('text')}
        """
        send_mail(
            subject=_('Contact from site'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            html_message=message,
            message=message,
        )

        return super().post(request, args, kwargs)
