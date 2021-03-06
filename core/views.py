from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation

from .models import Service, Employee, Feature, Plan, Client
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['featurescolumn1'] = Feature.objects.order_by('?').all()[:3]
        context['featurescolumn2'] = Feature.objects.order_by('?').all()[3:6]
        context['plans'] = Plan.objects.all()
        context['clients'] = Client.objects.order_by('?').all()
        context['lang'] = lang
        translation.activate(lang)

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso!'))

        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar o e-mail.'))

        return super(IndexView, self).form_invalid(form, *args, **kwargs)


