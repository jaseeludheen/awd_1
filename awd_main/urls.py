
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'), 

    # Include the URLs from the dataentry app
    path('dataentry/', include('dataentry.urls')),

    path('emails/', include('emails.urls')),

    path('image-compression/', include('image_compression.urls')),  

    path('stock-autocomplete/', include('stockanalysis.urls')),

    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
