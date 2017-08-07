from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# from django.cof import settings
# from django.conf.urls.static import static

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL,
# document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
