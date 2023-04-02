from django.shortcuts import render, redirect
from .models import Level
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def level(request):
    level = Level.objects.all()
    context = {
        'level':level,
    }
    return render(request, 'level-page.html', context)


@login_required
def addLevel(request):
    level = Level.objects.all
    context = {
        'level':level,
    }
    return render(request, 'add-level.html', context)

@login_required
def add(request):
    title = request.POST.get('newLevel')
    if level != '':
        newlevel = Level.objects.create(title=title)
        newlevel.save()
    return redirect('/levels')

def cancelAdd(request):
    return redirect('/levels')

@login_required
def delete(request, pk):
    level = Level.objects.get(pk=pk)
    level.delete()
    return redirect('/levels')

@login_required
def deleteLevel(request, pk):
    level = Level.objects.get(pk=pk)
    context = {'level':level}
    return render(request, 'delete-level.html', context)

def cancelDelete(request):
    return redirect('/levels')
