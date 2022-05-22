from ast import If
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from matplotlib.style import use
from .forms import *

# Create your views here.
from django.views.generic import View

class index(View):
    def get(self,request):
        
        sl = {}
        if 'login' in request.session:
            sl['login']=request.session['login']
        sl['users']=users.objects.all()

        if 'login' in request.session:
            sl['login']=request.session['login']
            user = users.objects.get(name=sl['login'])
            place = places.objects.filter(usersname=user)
            if len(place)>0:
                place_to_html=[]
                for i in place:
                    place_to_html.append(SaveFile(instance=i))
                sl['place']=place_to_html

       

        return render(request,"main/index.html",context=sl)

class izbr(View):
    def get(self,request):
        context={}
        if 'login' in request.session:
            context['login']=request.session['login']
            user = users.objects.get(name=context['login'])
            place = places.objects.filter(usersname=user)
            if len(place)>0:
                place_to_html=[]
                for i in place:
                    place_to_html.append(SaveFile(instance=i))
                context['place']=place_to_html
        return render(request,"main/index.html",context=context)

# region Авторизация
class loginA(View):
    def get(self,request):
        slovar = {'form': AUsersForm}
        return render(request,"main/autorisation.html",context=slovar)
    def post(self,request):
        newuser = AUsersForm(request.POST)
        if newuser.is_valid():
            request.session.set_expiry(3600*24*30)
            request.session['login']=request.POST['name']
            return HttpResponseRedirect('/')
        else:
            slovar = {'form': newuser} 
            return render(request,"main/autorisation.html",context=slovar) 

class loginR(View):
    def get(self,request):
        slovar = {'form': UsersForm}
        return render(request,"main/registration.html",context=slovar)
    def post(self,request):
        newuser = UsersForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return HttpResponseRedirect('/login')
        else:
            slovar = {'form': newuser} 
            return render(request,"main/registration.html",context=slovar) 

class logout(View):
    def get(self,request):
        if 'login' in request.session:
            request.session.flush()
        return HttpResponseRedirect('/')
# endregion

class saveplace(View):
    def post(self,request):
        print('ok')
        userforplace = users.objects.get(name =request.session['login'])
        newplace = places()
        newplace.name = request.POST['name']  
        newplace.latitude = request.POST['latitude']     
        newplace.longtitude = request.POST['longtitude']   
        newplace.description = request.POST['description']    
        newplace.usersname = userforplace      
        newplace.save()
        return HttpResponseRedirect('/')

class deleteplace(View):
    def post(self, request):
        # print('asdasdasdasdasdasd')
        id = request.POST['id']
        place = places.objects.get(id=id)
        place.delete()
        return HttpResponse('/')

def delete(request):
    id = request.GET['id']
    place = places.objects.get(id=id)
    place.delete()

    response = {

    }
    return JsonResponse(response)

def getInfo(request):
    id = request.GET['id']
    place = places.objects.get(id=id)

    response = {
        'name': place.name,
        'longtitude': place.longtitude,
        'latitude': place.latitude,
        'description': place.description
    }
    return JsonResponse(response)


# def delete(request, id):
#     place = places.objects.get(id=id)
#     place.delete()
#     return HttpResponseRedirect('/')
    