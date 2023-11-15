from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='HomePage'),
    path('results/',views.results,name="results")
]
 