from typing import Callable

from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView

from main.models import Client, City, MaritalStatus, Citizenship, Disability


class ClientListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all().order_by('surname')
        return context


class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/'
    template_name = 'delete.html'


class ClientCreateView(CreateView):
    model = Client
    success_url = '/'
    fields = '__all__'
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['marital_statuses'] = MaritalStatus.objects.all()
        context['citizenships'] = Citizenship.objects.all()
        context['disabilities'] = Disability.objects.all()
        return context


class ClientUpdateView(CreateView):
    model = Client
    success_url = '/'
    fields = '__all__'
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Client.objects.get(pk=self.kwargs['pk'])
        context['cities'] = City.objects.all()
        context['marital_statuses'] = MaritalStatus.objects.all()
        context['citizenships'] = Citizenship.objects.all()
        context['disabilities'] = Disability.objects.all()
        return context
