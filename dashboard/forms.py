from django import forms
from .models import Student
from django.forms import ModelForm, TextInput, Textarea, FileField, DateField, ChoiceField

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
            'name', 
            'father_name',
            'mother_name',
            'address',
            'phone',
            'phone2',
            'birthdate',
            'standard',
            'student_photo',
            'addhar_card',
            )
        widgets = {
            'name' : TextInput(attrs={'class':'form-control',  'placeholder' : "Enter Name"}),
            'father_name' : TextInput(attrs={'class':'form-control',  'placeholder' : "Enter Father's Name"}),
            'mother_name' : TextInput(attrs={'class':'form-control',  'placeholder' : "Enter Mother's Name"}),
            'address': Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'phone': TextInput(attrs={'class':'form-control', 'placeholder':'Input Phone Number'}),
            'phone2': TextInput(attrs={'class':'form-control', 'placeholder':'Input Phone Number'}),
            'birthdate': DateField(),
            'standard': ChoiceField(choices=(    
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ),
        'student_photo': FileField(attrs={'class':'btn', 'btn-mdb-color', 'btn-rounded', 'float-left'}),
        'addhar_card': FileField(attrs={'class':'btn', 'btn-mdb-color', 'btn-rounded', 'float-left'})
        )   
        }
