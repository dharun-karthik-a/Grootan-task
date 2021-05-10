from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
import json
#utils
def tolist(lst,k):
	l=[]
	for dic in lst:
		l.append(dic[k])
	return l



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('result'))
    else:
        return HttpResponseRedirect(reverse('login'))
        


def result(request):
    if request.user.is_authenticated:
        response = requests.get("https://hello.free.beeceptor.com/task")
        data = response.json()
        #data=[{'name': 'Dharun', 'age': 10, 'dob': '20-10-2020', 'firstName': 'Dharun', 'lastName': 'Karthik', 'more': {'address_line1': 'Adress  Line 1 will be displayed here', 'address_line2': 'Adress  Line 2 will be displayed here', 'address_line3': 'Adress  Line 3 will be displayed here', 'phone': '+91-9943962784'}}, {'name': 'Darshan', 'age': 10, 'dob': '20-10-2020', 'firstName': 'Darshan', 'lastName': 'M R', 'more': {'address_line1': 'Adress  Line 1 will be displayed here', 'address_line2': 'Adress  Line 2 will be displayed here', 'address_line3': 'Adress  Line 3 will be displayed here', 'phone': '+91-908086992'}}]
        json_list = json.dumps(data)
        nameAge=zip(tolist(data,"name"),tolist(data, "age"))
        return render(request,"result.html",{
            "nameAge":nameAge,
            "data":json_list
        })
    else:
        return HttpResponseRedirect(reverse('login'))
