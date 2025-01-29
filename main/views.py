import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import NewEntryForm, NewTag
from .models import entry, tag

def main_page(request):
    return redirect("/main/")

def new_tag(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            n = tag.objects.create(
                name = request.POST['tagName'],
                color = request.POST['nColor'],
            )
            n.save()
            return HttpResponseRedirect("/main/")
        return HttpResponseRedirect("/main/")
    else:
        return HttpResponseRedirect("/login/")

def new_entry(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            n = entry.objects.create(
                content = request.POST['content'],
                deadline = request.POST['deadline'],
                priority = 1,
                )
            if request.POST['aTag'] != '':
                n.tag = tag.objects.get(pk=request.POST['aTag'])            
            n.save()
            return HttpResponseRedirect("/main/")
        return HttpResponseRedirect("/main/")
    else:
        return HttpResponseRedirect("/login/")

def active_task_view(request):
    if request.user.is_authenticated:
        tag_id = 0
        if request.method == "POST":
            if request.POST.__contains__("id"):
                done_entry = entry.objects.get(id = request.POST["id"])
                done_entry.status = True
                done_entry.save()
            elif request.POST.__contains__("tag"):
                tag_id = int(request.POST["tag"])
        active_tasks = []
        task_color = []
        for task in entry.objects.all():
            if task.status == False:
                if tag_id == 0 or task.tag_id == tag_id:
                    active_tasks.append(task)
                    if task.tag_id != None:
                        current_tag = tag.objects.get(id = task.tag_id)
                        task_color.append(current_tag.color)
                    else:
                        task_color.append("#282828")
        task_list = zip(active_tasks, task_color)
        context = {"task_list": task_list, "tag_list": tag.objects.all(), "title": "Pending Tasks", "user": request.user}
        return render(request, "list_tasks.html", context)
    else:
        return HttpResponseRedirect("/login/")

def done_task_view(request):
    if request.user.is_authenticated:
        tag_id = 0
        if request.method == "POST":
            if request.POST.__contains__("id"):
               done_entry = entry.objects.get(id = request.POST["id"])
               done_entry.status = False
               done_entry.save()
            elif request.POST.__contains__("tag"):
                tag_id = int(request.POST["tag"])
        done_tasks = []
        task_color = []
        for task in entry.objects.all():
            if task.status == True:
                if tag_id == 0 or task.tag_id == tag_id:
                    done_tasks.append(task)
                    if task.tag_id != None:
                        current_tag = tag.objects.get(id = task.tag_id)
                        task_color.append(current_tag.color)
                    else:
                        task_color.append("#282828")
        task_list = zip(done_tasks, task_color)
        context = {"task_list": task_list, "tag_list": tag.objects.all(), "title": "Done Tasks"}
        return render(request, "list_tasks.html", context)
    else:
        return HttpResponseRedirect("/login/")