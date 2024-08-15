import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import NewEntryForm, NewTag
from .models import entry, tag

def new_tag(request):
    if request.method == "POST":
        form = NewTag(request.POST)
        if form.is_valid():
            n = tag.objects.create(
                name = request.POST['name'],
                color = request.POST['color'],
            )
            n.save()
    else:
        form = NewTag()
    return render(request, "new_tag.html", {"form": form})

def new_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            n = entry.objects.create(
                content = request.POST['content'],
                deadline = request.POST['deadline'],
                priority = request.POST['priority'],
             )
            if request.POST['tag'] != '':
                n.tag = tag.objects.get(pk=request.POST['tag'])            
            n.save()
            #return HttpResponseRedirect("/ok/")
    else:
        form = NewEntryForm()
    return render(request, "new_entry.html", {"form": form})

def active_task_view(request):
    active_tasks = []
    for task in entry.objects.all():
        if task.status == False:
            active_tasks.append(task)
    task_list = {"task_list": active_tasks}
    return render(request, "list_tasks.html", task_list)

def done_task_view(request):
    done_tasks = []
    for task in entry.objects.all():
        if task.status == True:
            done_tasks.append(task)
    task_list = {"task_list": done_tasks}
    return render(request, "list_tasks.html", task_list)