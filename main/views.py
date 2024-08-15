import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import NewEntryForm
from .models import entry, tag

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
        
