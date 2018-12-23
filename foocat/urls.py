from django.conf.urls import url
from foocat import views

urlpatterns = [
    url(r'hello$', views.say_hello),
]