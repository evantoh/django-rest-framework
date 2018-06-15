from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^api/merch/$', views.MerchList.as_view()),


]