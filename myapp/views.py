from django.shortcuts import render
from django.http import HttpResponse
from .models import Des
# Create your views here.

def index(request):
    
    des1 = Des()
    des1.name = 'tpt'
    des1.price = 200
    des1.desc = 'famous for tirumala'
    des1.img = 'destination_4.jpg'

    des2 = Des()
    des2.name = 'tpt'
    des2.price = 200
    des2.desc = 'famous for tirumala'
    des2.img = 'destination_5.jpg'  

    des3 = Des()
    des3.name = 'tpt'
    des3.price = 200
    des3.desc = 'famous for tirumala'
    des3.img = 'destination_3.jpg'

    dests = [des1, des2, des3]


    return render(request, 'index.html', {'dests' : dests})