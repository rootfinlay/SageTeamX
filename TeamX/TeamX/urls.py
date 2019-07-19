#from django.http import HttpResponse, HttpResponseNotFound
from django.conf.urls import handler404, handler500
from django.contrib.auth import views
from django.core.mail import send_mail
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from TeamXapp.views import (
    base,
    index,
    login,
    all_teams,
    about,
    help,
    contact,
    dashboard,
    team_details,
    all_people,
    all_developers,
    all_testers,
    all_product_owners,
    people_details,
    a
)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', login),
    path('admin/', admin.site.urls),
    path('', index),
    path('', base),
    path('all_teams/' , all_teams    , name ='all_teams'), 
    path('about/'     , about        , name ='about'), 
    path('help/'      , help         , name ='help'), 
    path('contact/'   , contact      , name ='contact'), 
    path('dashboard/' , dashboard    , name ='dashboard'),
    url(r'(?P<pk>\d+)/$', team_details , name = 'team_details'), 
    url(r'(?P<mypk>\d+)/$', people_details , name = 'people_details'),     
    path('all_people/' , all_people     , name ='all_people'), 
    path('all_developers/' , all_developers     , name ='all_developers'), 
    path('all_testers/' , all_testers     , name ='all_testers'), 
    path('all_product_owners/' , all_product_owners    , name ='all_product_owners'),
    path('easteregg/', a)

]

handler500 = 'TeamXapp.views.error_500'
handler404 = 'TeamXapp.views.error_404'
