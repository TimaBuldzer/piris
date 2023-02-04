from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView

from main.models import Client


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
    template_name = 'create.html'
    fields = '__all__'


class ClientUpdateView(UpdateView):
    model = Client
    success_url = '/'
    template_name = 'update.html'
    fields = '__all__'
