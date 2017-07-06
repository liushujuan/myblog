from django.conf.urls import url
from . import views
app_name = 'app'

urlpatterns = [
    url(r'^$', views.get_blogs, name='index'),
    url(r'^detail/(\d+)/$',views.get_detail, name='detail'),
    ]