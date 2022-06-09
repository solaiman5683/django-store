from django.shortcuts import render
from django.http import HttpResponse 
from store.models import Product, OrderItem

# Create your views here.


def hello(request):
    query_set = Product.objects.select_related('collection').all()

    return render(request, 'hello.html', {
        'name': 'Sulaiman Hosain',
        'age': '24',
        'hobbies': ['Coding', 'Reading', 'Watching Movies'],
        'products': list( query_set )
    })
