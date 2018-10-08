from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from . import views

urlpatterns=[
    
    # url('^$',views.login,name = 'login'),
    url('^profile/(\d+)',views.profile,name = 'profile'),
    url('^$',views.home,name='home'),
    url('^$',views.registration_form,name='registration_form'),
    url(r'^new/comment$', views.new_comment, name='new-comment'),
    url(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)