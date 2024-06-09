from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from forum.models import Forum, Kategori, Message
from utils.decorators import has_profile_only


def forum_home(request):

    if request.GET.get("q"):
        forums = Forum.objects.filter(judul__contains=request.GET.get("q"))
    elif request.GET.get("kategori"):
        kategori = Kategori.objects.get(nama=request.GET.get("kategori"))
        forums = Forum.objects.filter(kategori=kategori)
    else:
        forums = Forum.objects.all().order_by('judul')

    categories = Kategori.objects.all()
    paginator = Paginator(forums, 10)

    page_number = request.GET.get("page") or 1
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
    }

    return render(request,  'forum-home.html', context)


def create_new_forum(request):

    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        kategori = request.POST.getlist("kategori")

        forum = Forum.objects.create(judul=judul, deskripsi=deskripsi, kreator=request.user)

        for k in kategori:
            forum.kategori.add(Kategori.objects.get(pk=int(k)))

        forum.save()

        return HttpResponseRedirect(reverse('forum:home'))

    categories = Kategori.objects.all()

    return render(request, 'create_forum.html', {'categories': categories})


@has_profile_only
def edit_forum(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)

    if request.method == 'POST':
        forum.judul = request.POST.get('judul')
        forum.deskripsi = request.POST.get('deskripsi')

        forum.save()

        return HttpResponseRedirect(reverse('forum:home'))

    return render(request, 'edit_forum.html', {'forum': forum})

def buat_pesan(request, forum_id, reply_to=None):
    forum = Forum.objects.get(pk=forum_id)

    if request.method == 'POST':
        pesan = request.POST.get('pesan')

        if reply_to != 0:
            try:
                membalas_ke = Message.objects.get(pk=reply_to)
                message = Message(forum=forum, pesan=pesan, membalas_ke=membalas_ke, pengirim=request.user)
            except:
                return HttpResponseNotFound()
        else:
            message = Message(forum=forum, pesan=pesan, pengirim=request.user)

        message.save()

        forum.jumlah_pesan = forum.jumlah_pesan + 1
        forum.save()

        return HttpResponseRedirect(reverse('forum:page', args=[forum.pk]))

    return render(request, 'buat_pesan.html', {})

def forum_page(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)
    categories = Kategori.objects.all()
    return render(request, 'forum_page.html', {'forum': forum, 'categories': categories})


@csrf_exempt
def delete_forum(request, forum_id):

    try:
        forum = Forum.objects.get(pk=forum_id)
        forum.delete()
    except Forum.DoesNotExist:
        return HttpResponse(status=500)
    return HttpResponse(status=200)

@csrf_exempt
def get_all_replies(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)
    replies = Message.objects.filter(forum=forum)
    return HttpResponse(serializers.serialize('json', replies), content_type='application/json')
