from django.conf.urls import url
from miapp import views

# TEMPLATE TAGGING
app_name = 'miapp'

urlpatterns = [
	url('relative/', views.relative, name='relative'),
	url('other/', views.other, name='other'),
]