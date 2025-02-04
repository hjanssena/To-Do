from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import entry, tag

def main_page(request):
    return redirect("/main/")

def new_tag(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            n = tag.objects.create(
                name = request.POST['tagName'],
                color = request.POST['nColor'],
                uid = request.user,
            )
            n.save()
        return HttpResponseRedirect("/main/")
    else:
        return HttpResponseRedirect("/login/")

def new_entry(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            n = entry.objects.create(
                content = request.POST['content'],
                deadline = request.POST['deadline'],
                uid = request.user,
                )
            if request.POST['aTag'] != '':
                n.tag = tag.objects.get(pk=request.POST['aTag'])            
            n.save()
        return HttpResponseRedirect("/main/")
    else:
        return HttpResponseRedirect("/login/")

def active_task_view(request):
    if request.user.is_authenticated:
        #Process user setting a task as done
        if request.method == "POST":
            if request.POST.__contains__("id"):
                done_entry = entry.objects.get(id = request.POST["id"])
                done_entry.status = True
                done_entry.save()
        #Get the user's tasks and assign them their tag color.
        active_tasks = []
        task_color = []
        for task in entry.objects.filter(uid = request.user).order_by("deadline"):
            if task.status == False:
                active_tasks.append(task)
                if task.tag_id != None: #If no tag is assigned, then assign a default color
                    current_tag = tag.objects.get(id = task.tag_id)
                    task_color.append(current_tag.color)
                else:
                    task_color.append("#282828")
        task_list = zip(active_tasks, task_color) #We zip the lists to iterate them at the same time on the template
        context = {"task_list": task_list, "tag_list": tag.objects.filter(uid = request.user), "title": "Pending Tasks", "user": request.user}
        return render(request, "list_tasks.html", context)
    else:
        return HttpResponseRedirect("/login/")

def done_task_view(request):
    if request.user.is_authenticated:
        #Process user setting a task as done
        if request.method == "POST":
            if request.POST.__contains__("id"):
                done_entry = entry.objects.get(id = request.POST["id"])
                done_entry.status = True
                done_entry.save()
        #Get the user's tasks and assign them their tag color.
        active_tasks = []
        task_color = []
        for task in entry.objects.filter(uid = request.user).order_by("deadline"):
            if task.status == True:
                active_tasks.append(task)
                if task.tag_id != None: #If no tag is assigned, then assign a default color
                    current_tag = tag.objects.get(id = task.tag_id)
                    task_color.append(current_tag.color)
                else:
                    task_color.append("#282828")
        task_list = zip(active_tasks, task_color) #We zip the lists to iterate them at the same time on the template
        context = {"task_list": task_list, "tag_list": tag.objects.filter(uid = request.user), "title": "Finished Tasks", "user": request.user}
        return render(request, "list_tasks.html", context)
    else:
        return HttpResponseRedirect("/login/")