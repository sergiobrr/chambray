from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
# Create your views here.

class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact/contact_create.html'
    model = Contact   
