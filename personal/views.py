from ast import Return
from contextlib import redirect_stderr
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from personal.models import contactus

def say_hello(request):
    if request.method =="POST":
         name = request.POST.get('name')
         print(name)
         email=request.POST.get('email')
         phone= request.POST.get('phone')
         subject = request.POST.get('subject')
         desc= request.POST.get('desc')
         context=contactus(name=name,email=email,phone=phone,subject=subject,desc=desc)
         context.save()
        #  return redirect('/')
    return render(request,'index.html')
    # return HttpResponse("home paage")


def contact(request):
    
        #  return render(request,'about.html')
    return render(request,'#contact')



# Create your views here.

#requst->response
#request handler
#action
def about(request):
#     if request.method =="Post":
#          name = request.POST.get('name')
#          print(name)
#          email=request.POST.get('email')
#          phone= request.POST.get('phone')
#          subject = request.POST.get('subject')
#          desc= request.POST.get('desc')
#          context=contactus(name=name,email=email,phone=phone,subject=subject,desc=desc)
#          context.save()
#          return redirect('/about')
    return render(request,'about.html')
    # return HttpResponse("this is abou the page")
   