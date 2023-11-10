from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Lead, Student, Income, Expense
from .serializers import  ApiLead, ApiStudent, ApiIncome, ApiExpense
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend 



#Менеджер
class LeadList(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = ApiLead
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['full_name', 'phone_number', 'created_date']  


class LeadCreate(CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = ApiLead


class LeadRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = ApiLead
    lookup_field = 'slug'



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ApiStudent
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'created_date', 'studying_time', 'is_graduate','format', 'teacher'] 

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = ApiStudent

class StudentRetrieve(RetrieveUpdateDestroyAPIView):
    queryset  = Student.objects.all()
    serializer_class = ApiStudent
    lookup_field = 'slug'   




# Менедежер | Администратор
class IncomeCreate(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = ApiIncome




# Администратор

class IncomeList(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = ApiIncome
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'student']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        total_income = sum(income.value for income in queryset)
        response_data = {
            'total_income': total_income,
            'income': serializer.data,
        }
        return Response(response_data)

    

  

class IncomeRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = ApiIncome
    lookup_field = 'slug'






class ExpenseList(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class  = ApiExpense
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['flow_type', 'date_of_payment', 'created_date']
   
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        total_expense = sum(expense.value for expense in queryset)  
        response_data = {
            'total_expense': total_expense,
            'expense_list': serializer.data,
        }

        return Response(response_data)



class ExpenseCreate(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ApiExpense

class ExpenseRetrieve(RetrieveUpdateDestroyAPIView):
    queryset =  Expense.objects.all()
    serializer_class = ApiExpense
    lookup_field =  'slug'



# чистая прибыль
class Нet_profitList(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = ApiIncome
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_date',]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(**self.request.query_params.dict())

    def list(self, request):
        expenses = Expense.objects.all()
        incomes = self.filter_queryset(self.get_queryset())

        expense_serializer = ApiExpense(expenses, many=True)
        income_serializer = ApiIncome(incomes, many=True)

        total_income = sum(income.value for income in incomes)
        total_expenses = sum(expense.value for expense in expenses)
        net_profit = total_income - total_expenses

        combined_data = {
            'net_profit': net_profit,
            'expenses': expense_serializer.data,
            'incomes': income_serializer.data,
        }

        return Response(combined_data)

    




      





# должники
class DebtorViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(remainder__gt=0)
    serializer_class = ApiStudent
    filter_backends = [DjangoFilterBackend]
    filterset_filelds = []
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        remainder = sum(student.remainder for student in queryset) 


        response_data = {
            'debtor_sum': remainder,
            'debtor_list': serializer.data,
        }

        return Response(response_data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    




