from django.contrib import admin
from django.urls import path
from myapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = 'createpage.html')),
    path('datalist/', views.create, name = 'create') 
]
