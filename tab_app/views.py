from django.shortcuts import render

def tab_search_view(request):
    return render(request, 'index.html', {})
