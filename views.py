from django.shortcuts import render
from .models import Registration
from .forms import RegForm


# Create your views here.


def home(request):
    context = {}
    return render(request, 'indexes/prince.html', context)

def signy(request):
    form = RegForm
    context = {'form': form}
    return render(request, 'forms/form.html', context)

# def reg(request):
#     form = RegForm
#     context = {'form': form}
#     return render(request, 'forms/hostel.html', context)
