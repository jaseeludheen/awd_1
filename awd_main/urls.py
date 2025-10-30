
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'), 

    # Include the URLs from the dataentry app
    path('dataentry/', include('dataentry.urls')),



]
