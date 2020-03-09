from django.conf.urls import url

from user import views

app_name = 'user'

urlpatterns = [
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/change/$', views.ChangeProfile.as_view(), name='change_profile'),
]
