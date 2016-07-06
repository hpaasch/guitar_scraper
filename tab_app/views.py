from django.shortcuts import render
from urllib.parse import urlparse  # new library!!!
import requests
from bs4 import BeautifulSoup


def tab_search_view(request):
    pass


def tab_detail_view(request):
    url = 'http://www.guitartabs.cc/tabs/u/u2/with_or_without_you_tab.html'
    content = requests.get(url).text  # grabs a string of html-y text
    souper = BeautifulSoup(content, "html.parser")
    results = str(souper.find(class_='tabcont'))
    return render(request, 'index.html', {'results': results})
