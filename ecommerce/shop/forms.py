from django import forms

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3','cols':'5',
		'style':'resize:none;'}))

class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Enter Your Username'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Enter Your Password'}))