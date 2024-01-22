from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CusOrders, CusRatingFeedback,UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1', 'password2']
        


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'location']  # Include other fields as needed


class CusOrdersUpd(forms.ModelForm):
    class Meta:
        model = CusOrders
        fields = ['quantity']
        
        
class CusRatFeedForm(forms.ModelForm):
    class Meta:
        model = CusRatingFeedback
        fields = ['ratings', 'feedback']