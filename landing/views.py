from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Contact
from .forms import ContactForm
from .tasks import send_email_task


class LandingPageView(TemplateView):
    template_name = 'landing/home.html'


class ContactPageView(CreateView):
    model = Contact
    template_name = 'landing/contacts.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        self.object = form.save()
        send_email_task.delay(self.object.id)
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'landing/about.html'


class EquipmentPageView(TemplateView):
    template_name = 'landing/equipments.html'


class ContactView(TemplateView):
    template_name = 'landing/contacts.html'


class ServicesView(TemplateView):
    template_name = 'landing/services.html'
