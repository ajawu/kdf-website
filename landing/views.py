from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from .tasks import send_email_task


class LandingPageView(CreateView):
    model = Contact
    template_name = 'landing/landing_page.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save()
        send_email_task.delay(self.object.id)
        return super().form_valid(form)
