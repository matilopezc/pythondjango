from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('categoria_lista/', views.CategoriaLista.as_view()),
    path('producto_lista/', views.ProductoLista.as_view()),
    url(r'^producto_detalle/(?P<pk>[0-9]+)/$',views.ProductoDetalle.as_view()),
    url(r'^categoria_detalle/(?P<pk>[0-9]+)/$',views.CategoriaDetalle.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)