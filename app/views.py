from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'amrita','age':22}
    return render(request,'data_render.html',context=d)
def conditions(request):
    m={'a':20,'b':90,'c':10}
    return render(request,'conditions.html',context=m)