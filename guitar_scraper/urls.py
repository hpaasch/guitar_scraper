
from django.conf.urls import url
from django.contrib import admin

from tab_app.views import tab_detail_view, tab_search_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tab_search_view, name='tab_search_view'),
    url(r'^detail$', tab_detail_view, name='tab_detail_view'),

]
