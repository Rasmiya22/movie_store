from django.shortcuts import render, redirect

from . models import movies
from . forms import movieform



def demo(request):
    movie_list=movies.objects.all()
    return render(request,"index.html",{'movie_list':movie_list})

def details(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year = request.POST.get('year', )


        img = request.FILES['img']
        movi=movies(name=name,desc=desc,year=year,img=img)
        movi.save()
    return render(request,'add.html')

def update(request,movie_id):
    mov=movies.objects.get(id=movie_id)
    form=movieform(request.POST or None , request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mov':mov})


def delete(request,movie_id):
    if request.method == "POST":
        movs = movies.objects.get(id=movie_id)
        movs.delete()
        return redirect('/')
    return render(request,'delete.html')



