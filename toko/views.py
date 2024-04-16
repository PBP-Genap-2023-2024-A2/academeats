from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from toko.models import Toko
from toko.forms import TokoForm
from makanan.models import Makanan

def info_toko(request,id):
    toko=Toko.objects.get(pk=id)
    menu=Makanan.objects.filter(toko=toko)
    
    context={'toko':toko, 'menu':menu}
    return render(request, 'info_toko.html', context)


def create_toko(request):
    form = TokoForm(request.POST or None)
   
    if form.is_valid() and request.method == "POST":
       toko=form.save(commit=False)
       toko.user=request.user
       toko.save()
       return redirect('main:index')
    
    context = {'form':form}
    return render(request,'create_toko.html', context)

def edit_toko(request, id):
    toko = Toko.objects.get(pk = id)
    form = TokoForm(request.POST or None, instance=toko)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:index'))
    
    context = {'form': form}
    return render(request, "edit_toko.html", context)