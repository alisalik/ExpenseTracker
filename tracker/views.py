from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import generics
from tracker.models import Expense
from accounts.models import UserProfile
from tracker.serializers import ExpenseSerializer,detailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .permissions import UpdateOwnTask

# Create your views here.


def testview(request):
    return render(request,'test.html')

class CreateExpenseView(generics.ListCreateAPIView):

    serializer_class = ExpenseSerializer
    permission_classes=(IsAuthenticated,UpdateOwnTask,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        queryset = Expense.objects.filter(owner=request.user)
        serializer = ExpenseSerializer()
        #expenseinfo(request)
        return Response({'serializer': serializer})



    def create(self,request,*args,**kwargs):

        #print(ldata)
        serializer = self.get_serializer(data=request.data)
        inc=UserProfile.objects.filter(name=request.user)[:1].get()
        #print(inc.total_income)
        if serializer.is_valid():
            if serializer.validated_data['credit']==True :
                serializer.validated_data['balance']=inc.total_income+serializer.validated_data['amount']
                serializer.validated_data['owner']=request.user
                print(request.user)

                #ldata.balance+=serializer.validated_data['amount']
                #print(ldata.balance)
                #data.balance=serializer.validated_data['balance']


            elif serializer.validated_data['debit']==True:
                #print(Expense.balance)
                serializer.validated_data['balance']=inc.total_income-serializer.validated_data['amount']
                serializer.validated_data['owner']=request.user
                #ldata.balance-=serializer.validated_data['amount']
                #print(ldata.balance)
                #data.balance=serializer.validated_data['balance']

            serializer.save()

            return redirect('detail-account')
        else:
            return Response(serializer.errors)


class ExpenseinfoView(generics.ListAPIView):

    serializer_class = detailSerializer
    permission_classes=(IsAuthenticated,UpdateOwnTask,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail.html'
    #print(request.data)
    def get(self,request,*args,**kwargs):
        queryset = Expense.objects.filter(owner=request.user).last()
        #queryset=queryset.reverse()[:1].get()
        print(queryset)
        q1 = Expense.objects.filter(owner=request.user)
        #print(queryset)
        #serialized = ExpenseSerializer(queryset,many=True).data
        #print("i am inside")
        context={'Amount':queryset.amount,'Debit':queryset.debit,
                    'Credit':queryset.credit,'Balance':queryset.balance,
                    'data':q1}
        return render(request,'detail.html',context)
