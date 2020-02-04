
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	url('^$', views.button),
	url('^output', views.output, name='script'),
]