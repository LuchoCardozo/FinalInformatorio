from django.shortcuts import render
from time import timezone
from .models import Noticia, Categoria , Comentario
from  django.http.response import Http404



# Create your views here.


def index(request):
    return render(request, 'index.html')


def notices(request):
   lista_noticias = Noticia.objects.all().order_by('creado')
   context = {
          "noticias": lista_noticias,    
          }
   return render(request, 'notices.html', context)


def noticeDetail(request,id):
    try: 
       noticia = Noticia.objects.get(id = id)
       lista_comentarios = Comentario.objects.filter(aprobado=True)
       
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')
   
    context= {
        "noticia": noticia,
        "comentarios": lista_comentarios
    }
    return render (request , 'noticeDetail.html', context)