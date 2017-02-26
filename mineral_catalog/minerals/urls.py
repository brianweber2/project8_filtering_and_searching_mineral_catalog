from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^results$', views.mineral_search, name='search'),
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<letter>[a-zA-Z]+)$', views.mineral_list_letter_filter,
        name='letter_filter'),
    url(r'(?P<pk>\d+)$', views.mineral_detail, name='detail')
]
