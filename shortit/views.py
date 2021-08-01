from django.http.response import HttpResponse
from django.shortcuts import render,redirect
import string
import random
from .models import all_urls
# Create your views here.
def shortme(request):
    k=request.GET.get("q")
    t=all_urls.objects.filter(normal_url=k)
    if t.exists():
        return HttpResponse("https://shortiturls.herokuapp.com/tiny/"+str(t[0].short_url))
    else:
        y=fun()
        r=all_urls.objects.create(normal_url=k,short_url=y)
        r.save()
        return HttpResponse("https://shortiturls.herokuapp.com/tiny/"+str(y))
def go_to(request,text):
    t=all_urls.objects.filter(short_url=text)
    if t.exists():
        return redirect(t[0].normal_url)
    else:
        return render(request,"error.html")
def fun():
    N = 10
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    urls = all_urls.objects.filter(short_url=res)
    while len(urls)!=0:
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
        urls = all_urls.objects.filter(short_url=res)
    return (str(res))