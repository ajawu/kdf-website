from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Contact
from .forms import ContactForm
from .tasks import send_email_task


class LandingPageView(TemplateView):
    template_name = 'landing/home.html'


class ContactPageView(CreateView):
    model = Contact
    template_name = 'landing/home.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save()
        send_email_task.delay(self.object.id)
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'landing/about.html'
