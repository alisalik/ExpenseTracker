from django.urls import path,include
#from rest_framework.routers import DefaultRouter
from .views import RegisterView,loginView,logoutView,Base,verify_email,email_confirm

#router = DefaultRouter()
#router.register(r"profiles",UserViewset)

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('verify/<uutoken>',verify_email,name='verify'),
    path('email-conf/',email_confirm,name='email_conf'),
    path('login/',loginView,name='login'),
    path('logout',logoutView,name='logout'),
    path('tracks/',include('tracker.urls')),
    path('dashboard',Base,name='dboard')
]
