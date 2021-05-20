from django.shortcuts import render


def index(request):
	my_dict = {'string':'hello world', 'num':100}
	return render(request, 'miapp/index.html', my_dict)

def other(request):
	return render(request, 'miapp/other.html')

def relative(request):	
	return render(request, 'miapp/relative_url_templates.html')