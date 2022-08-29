from urllib import request
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import Noticia, Comentario
from django.http.response import Http404
from .forms import FormComment
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')


def notices(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticia": lista_noticias,
    }
    return render(request, 'notices.html', context)


def noticeDetail(request, id):
    try:
        noticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentario.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComment()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComment(request.POST)
        if form.is_valid():
            comment = Comentario(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticia
            )
            comment.save()
            return redirect("Noticia", id=noticia.id)

    context = {
        "form":form,
        "noticia": noticia,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticeDetail.html', context)


@login_required
def commentAproved(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
    except Comentario.DoesNotExist:
        raise Http404("Inexistente")

    comentario.aprpove()
    return redirect("Noticia", id=comentario.noticia.id)
