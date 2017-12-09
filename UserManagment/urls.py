from django.conf.urls import url
from UserManagment import views



urlpatterns = [

    url(r'update', views.update_user_data),
    url(r'users', views.user_list),
    url(r'^(?P<status>\w+)/(?P<id>\d+)$', views.user_by_status_and_id),
    url(r'^(?P<userName>\w+)$', views.user_by_user_name),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
]