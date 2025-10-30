
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'), 

    # Include the URLs from the dataentry app
    path('dataentry/', include('dataentry.urls')),



]
