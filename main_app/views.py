from django.shortcuts import render, redirect
from .models import Widget
from .forms import FillForm

# Create your views here.


def index(request):
    model = Widget
    widget_list = Widget.objects.all()
    form = FillForm()
    return render(request, 'index.html', {'widget_list': widget_list, 'form': form})


def add_data(request):
    form = FillForm(request.POST)
    form.save()
    return redirect('index')
