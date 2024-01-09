from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import movie
from .forms import Movieforms
# Create your views here.
def index(request):
    cinema=movie.objects.all()
    content={
        'movie_list':cinema,
    }
    return render(request,'index.html',content)
def details(request,movie_id):
    cinema= movie.objects.get(id=movie_id)
    return render(request,'details.html',{'key':cinema})
    #return HttpResponse(f"it's Movie number {movie_id}")

def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        cinema=movie(name=name,desc=desc,year=year,img=img )
        cinema.save()
    return render(request,'add.html')

def update(request,id):
    movie_dat=movie.objects.get(id=id)
    formdat=Movieforms(request.POST or None,request.FILES,instance=movie_dat)
    if formdat.is_valid():
        formdat.save()
        return redirect('/')
    return render(request,'edit.html',{'form':formdat,'movie':movie_dat})
def delete (request, id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html',)