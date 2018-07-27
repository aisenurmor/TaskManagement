from django.conf.urls import url
from .views import user_create, user_login, user_logout, user_edit_profile, user_list, user_delete, user_change_password, user_profile, user_upload_photo

urlpatterns = [
    url(r'^user_create/$', view=user_create, name='user_create'),
    url(r'^user_login/$', view=user_login, name='user_login'),
    url(r'^user_logout/$', view=user_logout, name='user_logout'),
    url(r'^user_upload_photo/$', user_upload_photo, name='user_upload_photo'),
    url(r'^user_edit_profile/$', view=user_edit_profile, name='user_edit_profile'),
    url(r'^user_list/$', view=user_list, name='user_list'),
    url(r'^delete/(?P<username>[-\w]+)/$', view=user_delete, name='user_delete'),
    url(r'^password_change/$', view=user_change_password, name='password_change'),
    url(r'^(?P<username>.+)/$', user_profile, name='user_profile')
]