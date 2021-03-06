from django.conf.urls import patterns, url

from locations import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),    
    url(r'^$', views.StopsView.as_view(), name='stops'),
    url(r'^stops/$', views.StopsView.as_view(), name='stops'),
    url(r'^stops/(?P<stop_id>\d+)/routes/$', views.stopRoutes, name='stop_routes'),     
    url(r'^routes/(?P<route_id>\d+)/vehicles/$', views.routeVehicles, name='route_vehicles'),
    url(r'^routes/$', views.RoutesView.as_view(), name='routes'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<vehicle_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<route_id>\d+)/pull/$', views.pull, name='pull'),
)