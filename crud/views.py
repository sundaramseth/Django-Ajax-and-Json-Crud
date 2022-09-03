from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import CrudUser
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class CrudView(ListView):
    model = CrudUser
    template_name = 'templates/home.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        lastname1 = request.GET.get('lastname',None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        email1 = request.GET.get('email',None)

        obj = CrudUser.objects.create(
            name = name1,
            lastname = lastname1,
            address = address1,
            age = age1,
            email = email1
        )

        user = {'id':obj.id,'name':obj.name,'lastname':obj.lastname, 'address':obj.address,'age':obj.age, 'email':obj.email}

        data = {
            'user': user
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        lastname1 = request.GET.get('lastname',None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        email1 = request.GET.get('email',None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.lastname = lastname1
        obj.address = address1
        obj.age = age1
        obj.email = email1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'lastname':obj.lastname, 'address':obj.address,'age':obj.age, 'email':obj.email}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)