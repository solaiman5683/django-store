from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return render(request, 'hello.html', {
        'name': 'Sulaiman Hosain',
        'age': '24',
        'hobbies': ['Coding', 'Reading', 'Watching Movies'],
    })
