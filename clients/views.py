from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView
from .forms import ClientCreateForm, ClientUpdateForm
from .models import Client
from .filters import ClientFilter


# Create your views here.
class NewClientView(CreateView):
    form_class = ClientCreateForm
    template_name = 'client_create.html'

    def form_valid(self, form):
        client = form.save(commit=False)
        client.save()
        return HttpResponseRedirect(reverse('home'))


class UpdateClientView(UpdateView):
    form_class = ClientUpdateForm
    template_name = 'client_update.html'
    success_url = '/'
    model = Client

    def form_valid(self, form):
        client = form.save(commit=False)
        client.save()
        return HttpResponseRedirect(reverse('home'))

    def get_object(self, queryset=None):
        obj = Client.objects.get(id=self.kwargs['pk'])
        return obj

    def dispatch(self, request, *args, **kwargs):
        return super(UpdateClientView, self).dispatch(request, *args, **kwargs)


class ClientListView(ListView):
    model = Client
    paginate_by = 100
    template_name = 'client_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def search(request):
    orderby = request.GET.get('orderby', 'client_name')
    client_list = Client.objects.all().order_by(orderby)
    client_filer = ClientFilter(request.GET, queryset=client_list)
    return render(request, 'client_search.html', {'filter': client_filer, 'orderby': orderby})


class ClientSearchView(ListView):
    template_name = 'client_search.html'
    model = Client

    def get_context_data(self, **kwargs):
        context = super(ClientSearchView, self).get_context_data(**kwargs)
        context.update({
            'all_genres': Client.objects.all(),
            'page_title': 'Latest'
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Client.objects.filter(client_name__icontains=query)
        else:
            return Client.objects.all()
