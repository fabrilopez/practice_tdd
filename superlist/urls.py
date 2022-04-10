from django.urls import include, re_path


from lists import views

urlpatterns = [
    re_path(r'^$', views.home_page, name='home'),
]
