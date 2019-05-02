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

    def form_valid(self, form):
        # check if google recaptcha was ok
        if self.request.recaptcha_is_valid:
            return super(ContactCreateView, self).form_valid(form)
        else:
            return super(ContactCreateView, self).form_invalid(form)


    def get_success_url(self):
        self.object.send_itself()
        url = super(ContactCreateView, self).get_success_url()
        return url + self.object.sender_email + '/'


class ThankyouView(TemplateView):
    template_name = 'contact/thankyou.html'

    def get_context_data(self, sender=None):
        context = {'sender': sender}
        return context

