from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
	return render(request, 'home_page.html')


def contact_us_page(request):

	if request.method == 'POST':
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('message'))

	context = {
		'contact_us' : 'hello, This is Marjan!!!'
	}
	return render(request, 'contact_us_page.html',context)