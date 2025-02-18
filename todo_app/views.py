from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Task
from . forms import Todoforms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name = 'task_view.html'
    context_object_name = 'tasks'
class TaskDetailView(DetailView):
    model = Task
    template_name='task_detail.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})
def task_view(request):
    tasks=Task.objects.all()
    print(tasks)
    name = priority = date = None
    if request.method == 'POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
    if name and priority and date:
        obj=Task(name=name,priority=priority,date=date)
        obj.save()

    return render(request, 'task_view.html',{'tasks':tasks})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})


def update(request,taskid):
    task =Task.objects.get(id=taskid)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})