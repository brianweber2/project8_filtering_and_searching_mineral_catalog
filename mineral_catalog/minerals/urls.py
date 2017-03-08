from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^group_results/(?P<group>\w+)$', views.mineral_group_filter,
        name='group_filter'),
    url(r'^search/', include('haystack.urls')),
    url(r'^search_results$', views.mineral_search, name='search'),
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<letter>[a-zA-Z]+)$', views.mineral_list_letter_filter,
        name='letter_filter'),
    url(r'(?P<pk>\d+)$', views.mineral_detail, name='detail')
]
