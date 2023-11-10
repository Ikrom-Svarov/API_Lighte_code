from rest_framework import serializers
from .models import Lead, Course, Student, Employee, LearningFormat, Income, PaymentMethod, Currency, Expense



class ToCource(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title']


class ToEmployee(serializers.ModelSerializer):
    class Meta:
        model  = Employee
        fields = ['full_name']


class ToLearningFormat(serializers.ModelSerializer):
    class Meta:
        model = LearningFormat
        fields = ['title']
    

class ToPaymentMethod(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['title']

class ToCurrency(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['title']


class ToStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name']


    
class ApiLead(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['cource'] = ToCource(instance.course).data
        return representation



class ApiStudent(serializers.ModelSerializer):

    def get_studying_time(self, obj):
        studying_time_mapping = {
            1: 'Утро',
            2: 'День',
            3: 'Вечер',
            4: 'Ночь',
        }
        return studying_time_mapping.get(obj.studying_time)
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['course'] = ToCource(instance.course).data
        representation['teacher'] = ToEmployee(instance.teacher).data
        representation['format'] = ToLearningFormat(instance.format).data
        representation['studying_time'] = self.get_studying_time(instance)

        return representation
    





class ApiIncome(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields =  '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['payment_method'] = ToPaymentMethod(instance.payment_method).data
        representation['currency'] = ToCurrency(instance.currency).data
        representation['student'] = ToStudent(instance.student).data
        representation['course'] = ToCource(instance.course).data
        return representation



class ApiExpense(serializers.ModelSerializer):
    def get_flow_type(self, obj):
        flow_type_mapping = {
            1: 'Постоянный',
            2: 'Одноразовый',
            3: 'Сотрудник',
            4: 'Возврат',
        }
        return flow_type_mapping.get(obj.flow_type)
    
    class Meta:
        model = Expense
        fields  = '__all__'
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['flow_type'] = self.get_flow_type(instance)
        return representation
    




