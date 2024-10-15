from django.urls import path
from .views import VistaListaBlog, VistaDetalleBlog

urlpatterns = [
    path('', VistaListaBlog.as_view(), name='inicio'),
    path('pub/<int:pk>/', VistaDetalleBlog.as_view(), name='detalle_pub'),
]