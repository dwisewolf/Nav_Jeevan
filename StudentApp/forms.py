from django import forms  
from .models import Students

class StuForm(forms.ModelForm):  

    class Meta:
        model = Students
        fields = ['name','password','resImage']

# class AddAuthPersonModelForm(forms.ModelForm):
#     class Meta:
#         model = AddAuthPerson
#         fields = ['person']

#         widgets = {
#             'person': forms.TextInput(attrs={'placeholder': 'Enter New Person Name','class':'form-control'})
#         }

class StuLoginForm(forms.ModelForm):  

    class Meta:
        model = Students
        fields = ['name','password']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Enter Password'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Student Name'}),
        }
        labels = {
            'name': ('Student Name'),
            'password':('Password'),
            }
