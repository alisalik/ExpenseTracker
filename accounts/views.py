from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import UserProfile
from accounts.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
import uuid
# Create your views here.

def Base(request):
    permission_classess=(IsAuthenticated,)
    return render(request,"base.html")


class RegisterView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self, request, *args,**kwargs):
        queryset = UserProfile.objects.all()
        serializer = UserSerializer()
        return Response({'serializer': serializer})

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['is_active']=False
            uutoken=str(uuid.uuid4())
            serializer.validated_data['uutoken']=uutoken
            emails=serializer.validated_data['email']
            serializer.save()
            send_emailconf(emails,uutoken)
            return redirect('email_conf')
        else:
            return Response(serializer.errors)

def email_confirm(request):
    return render(request,'email_conf.html')

def verify_email(request,uutoken):

    profile_obj=UserProfile.objects.filter(uutoken=uutoken)
    print(profile_obj)
    print(uutoken)
    if not profile_obj:
        return Response('Invalid token please resend confirmation')
    profile_obj.is_active=True
    for obj in profile_obj:
        obj.is_active=True
        obj.save()
    messages.success(request, 'Your account has been verified.')
    return render(request,'success.html')

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            messages.success(request,'Logged in successfully!!!')
            return redirect('dboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect("login")


def send_emailconf(emails,uutoken):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/profile/verify/{uutoken}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [emails]
    send_mail(subject, message , email_from ,recipient_list )
