from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^track/$', views.addTrack, name="addTrack"),
	url(r'^tracks/$', views.listTrack, name="listTrack"),
	url(r'^genre/$', views.addGenre, name="addGenre"),
	url(r'^allgenre/$', views.listGenre, name="listGenre"),
]




