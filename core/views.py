from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductModelForm
from django.urls import reverse_lazy


class IndexView(ListView):
    models = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class CreateProductView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('index')


class UpdateProductView(UpdateView):
    pass
