#! coding=utf-8
from django.conf.urls import url
from hostinfo import views as h_views

urlpatterns =[ 
    #url(r"^$",h_views.index,name='index'),
    url(r"^$",h_views.listp,name='index'),
    url(r"^add/$",h_views.add,name="add"),
    url(r"^host/command/$",h_views.Command,name="command"),
    url(r"^host/(?P<pk>\d+)$",h_views.Actions,name="actions"),
    url(r"^host/(?P<ip>.+)/tomre$",h_views.TomRe,name="tomre"),
    url(r"^host/(?P<ip>.+)/tomlog$",h_views.TomLog,name="tomlog"),
]
