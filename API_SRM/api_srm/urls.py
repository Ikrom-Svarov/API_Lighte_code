from django.urls import path

from .views import LeadList, LeadCreate, LeadRetrieve , StudentList, StudentCreate, StudentRetrieve, IncomeCreate, IncomeList, IncomeRetrieve
from .views import ExpenseList, ExpenseCreate, ExpenseRetrieve, DebtorViewSet, Нet_profitList





urlpatterns = [
    path('LeadList/', LeadList.as_view(), ),
    path('LeadCreate/', LeadCreate.as_view()),
    path('LeadRetrieve/<slug:slug>/', LeadRetrieve.as_view()),



    path('StudentList/', StudentList.as_view()),
    path('StudentCreate/', StudentCreate.as_view()),
    path('StudentRetrieve/<slug:slug>/', StudentRetrieve.as_view()),


    path('PaymentCreate/', IncomeCreate.as_view()),


    path('IncomeList/',IncomeList.as_view() ),
    path('IncomeCreate/', IncomeCreate.as_view()),
    path('IncomeRetrieve/<slug:slug>/', IncomeRetrieve.as_view()),


    path('ExpenseList/', ExpenseList.as_view()),
    path('ExpenseCreate/', ExpenseCreate.as_view()),
    path('ExpenseRetrieve/<slug:slug>/', ExpenseRetrieve.as_view()),


    path('Нet_profitList/', Нet_profitList.as_view()),


    path('DebtorsList/', DebtorViewSet.as_view({'get': 'list',})),
    path('DebtorsRetrieve/<slug:slug>/', DebtorViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),

    
]