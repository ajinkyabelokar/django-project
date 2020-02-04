from django.shortcuts import render 
from selenium import webdriver
import requests

def button(request):

	return render(request,'home.html')
	
def output(request):
		
	data=requests.get("https://google.com")
	print(data.text)
	data=data.text
	return render(request,'home.html',{'data':data})
	
def IE():

	#from selenium import webdriver
	
	# open IE 
	driver = webdriver.Ie("E:\drivers\IEDriverServer.exe")

	driver.maximize_window()

	driver.implicitly_wait(20)

	driver.get("http://www.facebook.com")
		
	title = self.driver.title
	
	self.assertTrue("Facebook" == self.driver.title) 
	
	#print (title)
	#title=title.text
	#return render (request, 'selenium.html', {'title':title})
	#return render(request,'selenium.html')
