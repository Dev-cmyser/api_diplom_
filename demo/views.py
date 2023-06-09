from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from .utils import get_tokens_for_user
from .serializers import * 
# Create your views here.
import json
from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from  django.http.request import QueryDict

@api_view(['POST'])
def add_task(request):
    item = TaskSerializer(data=request.data)
    params =  request.data
    # validating for already existing data

    print(params, type(params))
    if type(params) == QueryDict:
        params = dict(params)
        params = list(params.keys())
        params = json.loads(params[0])
        

    print(params, type(params))
    user = User.objects.get(username=params['user']['username'])

    # print(user)
    apps = []
    for app in params['apps']:
        app = App.objects.get(name=app)
    #    print(app)
        apps.append(app)
    #print(apps) 
    
    if params:
        try:
            task, created  = Task.objects.update_or_create(id=params['id'],user=user,defaults={'name': params['name'],
                    'is_completed': params['is_completed']})
            task.apps.set(apps) 
            print(task)
        except KeyError:
            task, created = Task.objects.get_or_create(user=user, name=params['name'])
            task.apps.set(apps)
            print(task.id)
            params['id'] = task.id

        return JsonResponse(params)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_tasks(request):
     
        # checking for the parameters from the URL
    if request.query_params:
        params =  request.query_params.dict()
        user = params['user']
        user = User.objects.get(username=user)

        #= **request.query_params.dict()
        params =  {'user': user.id}
        items = Task.objects.filter(**params)
    else:
        items = Task.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = TaskSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_task(request, pk):
    item = Task.objects.get(pk=pk)
    data = TaskSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_task(request, pk):
    item = get_object_or_404(Task, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class LoginView(APIView):
    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        email = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return JsonResponse({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


      
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True) #Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.urls import reverse_lazy
from django.views.generic import CreateView

from demo.forms import RegisterUserForm
from django.shortcuts import render
from demo.models import User

def register(request):
    pass
class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

def about(request):
    return render(request, 'demo/about.html')
def contact(request):
    return render(request, 'demo/contact.html')

def tasks(request):
    return render(request, 'demo/tasks.html')
