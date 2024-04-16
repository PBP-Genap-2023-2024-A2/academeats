from django.shortcuts import render, redirect
from makanan.models import Makanan
from toko.models import Toko
from makanan.forms import MakananForm

def tambah_makanan(request):
    form = MakananForm(request.POST or None)
   
    if form.is_valid() and request.method == "POST":
       toko_id=request.GET()
       makanan=form.save(commit=False)
       makanan=request.user
       makanan.save()
       return redirect('main:index')
    
    context = {'form':form}
    return render(request,'tambah_makanan.html', context)
   
   