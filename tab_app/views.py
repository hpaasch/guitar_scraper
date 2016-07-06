from django.shortcuts import render
from urllib.parse import urlparse  # new library!!!
import requests
from bs4 import BeautifulSoup


def tab_search_view(request):
    song = request.GET.get('song')
    search_url = 'http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}'.format(song)
    content = requests.get(search_url).text
    souper = BeautifulSoup(content, 'html.parser')
    results = str(souper.find(class_='tabslist'))  # need for loop to get all results
    # results = str(souper.find(id='song'))
    # souper.find_all('a', class_='title')
    # for link in links:
    #     link_url = link.attrs['href']
    #     print(urlparse(link_url).path)

    return render(request, 'index.html', {'results': results})


def tab_detail_view(request, url):
    song_url = 'http://www.guitartabs.cc/' + url
    content = requests.get(song_url).text  # grabs a string of html-y text
    souper = BeautifulSoup(content, "html.parser")
    results = str(souper.find(class_='tabcont'))
    return render(request, 'detail.html', {'results': results})
