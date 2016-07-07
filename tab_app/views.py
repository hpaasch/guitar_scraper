from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def tab_search_view(request):
    song = request.GET.get('song')
    search_url = 'http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}'.format(song)
    content = requests.get(search_url).text
    souper = BeautifulSoup(content, 'html.parser')
    results = str(souper.find(class_='tabslist'))
    pagination = str(souper.find(class_='paging'))  # this pagination doesn't work
    pager = souper.select('a[href^=?tabtype]')  # from here modifies the URL, but to what end?
    for page in pager:
        new_url = 'http://www.guitartabs.cc/search.php' + page['href']  # this is the correct URL, but how to get it into
    return render(request, 'index.html', {'results': results, 'pagination': pagination})

def tab_detail_view(request, url):
    song_url = 'http://www.guitartabs.cc/' + url
    content = requests.get(song_url).text  # grabs a string of html-y text
    souper = BeautifulSoup(content, "html.parser")
    results = str(souper.find(class_='tabcont'))
    pagination = ''
    if results == 'None':
        results = str(souper.find_all(class_='tabslist')[1])  # index the 2nd table
        pagination = str(souper.find(class_='paging'))  #this pagination works great
    return render(request, 'detail.html', {'results': results, 'pagination': pagination})
