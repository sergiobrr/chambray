from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Contact
from .forms import ContactForm
# Create your views here.

class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact/contact_create.html'
    model = Contact 
    success_url = '/contacts/thankyou/'

    def get_success_url(self):
        self.object.send_itself()
        url = super(ContactCreateView, self).get_success_url()
        return url + self.object.sender_email + '/'


class ThankyouView(TemplateView):
    template_name = 'contact/thankyou.html'

    def get_context_data(self, sender=None):
        context = {'sender': sender}
        return context

