from django import forms
from .models import Employee

# Model Meta is basically the inner class of your model class.

# Model Meta is basically used to change the behavior of 
# your model fields like changing order options,
# verbose_name and lot of other options. 
# It’s completely optional to add Meta class in your model.


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. CODE',
        }
    