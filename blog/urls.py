from django.urls import path
from .views import (VistaListaBlog, VistaDetalleBlog, VistaCrearBlog, VistaEditarBlog, VistaEliminarBlog)

urlpatterns = [
    path('', VistaListaBlog.as_view(), name='inicio'),
    path('pub/<int:pk>/', VistaDetalleBlog.as_view(), name='detalle_pub'),
    path('pub/nueva/', VistaCrearBlog.as_view(), name='nueva_pub'),
    path('pub/<int:pk>/editar/', VistaEditarBlog.as_view(), name='editar_pub'),
    path('pub/<int:pk>/eliminar/', VistaEliminarBlog.as_view(), name='eliminar_pub'),
]