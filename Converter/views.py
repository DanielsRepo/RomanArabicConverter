from Converter.forms import ConverterForm
from Converter.mixins import AjaxFormMixin
from django.views.generic import TemplateView, FormView


class Index(TemplateView):
    template_name = 'Converter/index.html'

    def get_context_data(self, **kwargs):
        context = {'form': ConverterForm()}
        return context


class Conversion(AjaxFormMixin, FormView):
    form_class = ConverterForm
    success_url = '/'

