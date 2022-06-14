from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



urlpatterns=[
    url(r'^$', views.home,name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/', views.update_project, name='upload'),
    url(r'^review/(?P<pk>\d+)',views.add_review,name='review'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)