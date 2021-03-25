from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from new.models import reg


def index(request):
    obj=reg.objects.all()
    return render(request,'index.html',{'obj':obj})



def reg_check(request):
    if request.method=="POST":
        name=request.POST['name']
        number = request.POST['number']
        email=request.POST['email']
        password = request.POST['password']
        data=reg(name=name,number=number,email=email,password=password)

        data.save()
        user = reg.objects.values()
#       print(user)
        ud=list(user)
        return JsonResponse({'status': "save kar diya bhai",'ud':ud})
    else:
        return JsonResponse({'status': "bhai teri method post nahi h check akr le"})
def login(request):
    return render(request,'login.html',{'msg':'Login Page'})
def login_check(request):
    if request.method == "POST":
        number=request.POST['number']
        password=request.POST['password']
        if reg.objects.filter(number=number,password=password):
            return JsonResponse({'status':'Login Success'})
        else:
            return JsonResponse({'status':'Invalid Details'})

def delete(request):
    if request.method == "POST":
        id=request.POST.get('id')
        print(id)
        pi=reg.objects.get(id=id)
        pi.delete()
        return JsonResponse({'status':'Delete'})
    else:
        return JsonResponse({'status':'error'})

def update(request):
    if request.method == "POST":
        id=request.POST.get('id')

        pi=reg.objects.get(id=id)
        d={"id":pi.id,"name":pi.name,"number":pi.number,"email":pi.email,"password":pi.password}
        return JsonResponse(d)
    else:
        return JsonResponse({'status':'error'})

def doupdate(request):
    if request.method == "POST":
        id=request.POST.get('id')


        pi=reg.objects.get(id=id)
        pi.name=request.POST['name']
        pi.number = request.POST['number']
        pi.email = request.POST['email']
        pi.password = request.POST['password']
        pi.save()



        return JsonResponse({'status':'Update'})
    else:
        return JsonResponse({'status':'error'})