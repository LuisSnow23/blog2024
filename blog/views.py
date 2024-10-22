from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publicacion

# Create your views here.
class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'
    
class VistaDetalleBlog(DetailView):
    model = Publicacion
    template_name = 'detalle_pub.html'
    context_object_name = 'publicacion'
    
class VistaCrearBlog(CreateView):
    model = Publicacion
    template_name = 'nueva_pub.html'
    fields = ['titulo','autor', 'cuerpo']
    
class VistaEditarBlog(UpdateView):
    model = Publicacion
    template_name = 'editar_pub.html'
    fields = ['titulo','cuerpo']
    
class VistaEliminarBlog(DeleteView):
     model = Publicacion
     template_name = 'eliminar_pub.html'
     success_url = reverse_lazy('inicio')