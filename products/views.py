from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from products.models import *


def index(request):
    return render(
        request,
        template_name='index.html'
    )


def product(request):
    return render(
        request,
        'shop-details.html'
    )