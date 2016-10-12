from django.conf.urls import url

from signprot import views

urlpatterns = [
	url(r'^$', views.BrowseSelection.as_view(), name='index'),
	url(r'^statistics',  views.GProtein, name='gprotein'),
    url(r'^ginterface/(?P<protein>[^/]*?)/$', views.Ginterface, name='render'),
    url(r'^ginterface[/]?$', views.TargetSelection.as_view(), name='targetselection'),
    url(r'^(?P<slug>[-\w]+)/$', views.signprotdetail, name='signprotdetail'),
]
