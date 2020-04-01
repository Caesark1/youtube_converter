from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.views.generic import CreateView
from .utils import send
from .tasks import send_some_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "main/contact.html"

    def form_valid(self, form):
        form.save() 
        send_some_email.delay(form.instance.email,form.instance.youtube)
        return super().form_valid(form)