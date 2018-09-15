from django.conf.urls import url
from . import views

#从当期文件下引入views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/$', views.register),
    url(r'^quit/$', views.quit),
    url(r'^blog/$', views.blog),
    url(r'^base/$', views.base),
    url(r'^blog=(\d+)/$', views.content),
    url(r'^blog/cat=(\d+)/$', views.category),
    url(r'^login/$', views.login),
    url(r'^home/$', views.home),
    url(r'^contact/$', views.contact),
    url(r'^blog/search/$', views.search),
    url(r'^share/$', views.share),
    url(r'^autoplay/$', views.autoplay),
]

