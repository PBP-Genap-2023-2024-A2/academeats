from django.core.paginator import Paginator
from django.shortcuts import render

from forum.models import Forum, Kategori


# @login_required(login_url='user-profile:login-user')
def forum_home(request):
    forums = Forum.objects.all().order_by('judul')
    categories = Kategori.objects.all()
    paginator = Paginator(forums, 10)
    forum_dibuat = Forum.objects.filter(kreator=request.user).order_by('pk')[:5]

    page_number = request.GET.get("page") or 1
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'forum_dibuat': forum_dibuat
    }

    return render(request,  'home.html', context)


def create_new_forum(request):

    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        kategori = request.POST.getlist("kategori")

        forum = Forum.objects.create(judul=judul, deskripsi=deskripsi, kreator=request.user)

        for k in kategori:
            forum.kategori.add(Kategori.objects.get(pk=int(k)))

        forum.save()

    categories = Kategori.objects.all()

    return render(request, 'create_forum.html', {'categories': categories})


def forum_page(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)
    return render(request, 'forum_page.html', {'forum': forum})


def delete_forum(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)
    forum.delete()