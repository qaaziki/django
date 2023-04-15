from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView
)
from django.urls import reverse_lazy
from .models import Product
from .forms import CreateProductForm


# TemplateView класс позволяет использовать к нашему приложению шаблоны
class AboutUsMagazin(TemplateView):
    # установка пути к шаблону
    template_name = "info/about_us.html"


# класс ListView создает список чего либо
class GetAllProduct(ListView):
    # аттребут model выберает все записи в классе Product
    model = Product
    template_name = "index.html"
    # аттребут context_object_name связывает с переменной в  шоблоне для отоброжения
    context_object_name = "products"

    # Метод get_queryset с помощью него можем выберать что именно отображать в моделях
    def get_queryset(self):
        return Product.objects.filter(is_active=True)


# Класс CreateView работа с формами для добовление товара
class CreateProductView(CreateView):
    model = Product
    template_name = "create_product.html"
    # аттребут form_class указывает на форму которая взаимодействует с классом CreateProductView
    form_class = CreateProductForm
    # аттребут success_url = reverse_lazy нужен для построения маршрута
    success_url = reverse_lazy("main")
    # аттребут raise_exception выдает исключения (ошибки)
    raise_exception = True


class DeliteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy("main")
    template_name = "index.html"
    raise_exception = True


class UpdateProductView(UpdateView):
    model = Product
    template_name = "update_product.html"
    form_class = CreateProductForm
    raise_exception = True
    success_url = reverse_lazy("main")
    context_object_name = "prod_item"


class DetaleProductView(DetailView):
    model = Product
    template_name = "detale_product.html"
    raise_exception = True
    success_url = reverse_lazy("main")
    context_object_name = "product_item"


