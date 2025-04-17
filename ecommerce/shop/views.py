from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm

# Create your views here.

def home_page(request):
	return render(request, 'home_page.html')

def about_us_page(request):
	context = {
		'message':'this is about us page'
	}

	return render(request, 'about_us_page.html',context)


def contact_us_page(request):

	contact_form = ContactForm

	if request.method == 'POST':
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('message'))

	context = {
		'contact_us' : 'hello, This is Marjan!!!',
		'contact_form' : contact_form
	}
	return render(request, 'contact_us_page.html',context)

def login_page(request):
	print(request.user.is_authenticated)
	login_form = LoginForm(request.POST or None)

	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			print('2222222222222222222')

	context = {
		'login_form' : login_form,		
	}

	return render(request, 'auth/login.html', context)



def register_page(request):
	pass