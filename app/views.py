from django.shortcuts import render
from django.http import HttpResponse

import requests
#will helps us to navigate to a particular website

from bs4 import BeautifulSoup
from app.models import Web
#BeautifulSoup helps ups to read the data present in the html code

# Create your views here.

def web_scrap_view(request):
    data=requests.get("https://www.google.com").text
    #print(data)
    soup=BeautifulSoup(data,'html.parser')
    #print(soup.prettify())
    all_links=soup.find_all('img')#so many links
    for i in all_links:
        href_list=i.get('src')#www.data.com
        all_link_names=i.string#data
        Web.objects.create(hrefvalue=href_list,linkname=all_link_names)
    
    alldetails=Web.objects.all()
    return render(request,"home.html",{'alldetails':alldetails})


















