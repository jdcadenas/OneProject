from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ContactMeForm
from .models import ContactMe


class ContactMeListView(ListView):
    model = ContactMe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = ContactMe.objects.all()

        return context


class ContactMeCreateView(CreateView):
    model = ContactMe
    form_class = ContactMeForm

    template_name = "contactme/contactme_form.html"


class ContactMeUpdateView(UpdateView):
    model = ContactMe
    form_class = ContactMeForm

    template_name = "contactme/contactme_form.html"


class ContactMeDeleteView(DeleteView):
    model = ContactMe
    success_url = '/contactme'
