from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from home.models import ContactUs
from home.forms import ContactUsForm

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"


class ContactUsCreateView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    url_redirect = success_url

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = '[CREATE] No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context