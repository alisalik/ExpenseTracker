from django.urls import path
from tracker.views import CreateExpenseView,ExpenseinfoView,testview

urlpatterns=[
    path('tracker/',CreateExpenseView.as_view(),name='expense'),
    path('test/',testview,name='test'),
    path('details/',ExpenseinfoView.as_view(),name='detail-account')
]
