from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.consulta_list),
    #path('admin/', admin.site.urls),
]
