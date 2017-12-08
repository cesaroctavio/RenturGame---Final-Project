"""practica13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import login,logout_then_login,logout
from miapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.index, name ='index_view'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$',views.Singup.as_view(),name ='Signup_view'),
    url(r'^login/$',login,{"template_name":'login.html'},name='login'),
    url(r'^cerrar/$',logout_then_login,name='logout'),
    url(r'^registro_juego/$',views.RegistroJuego.as_view()),
    url(r'^detail_juego/(?P<pk>[-_\w]+)/$',views.Juego_detail.as_view()),
    url(r'^jsonVideojuego/$',views.jsonVideojuego, name='wsPersona_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
