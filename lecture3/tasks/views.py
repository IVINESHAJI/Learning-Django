from django import forms
from django.shortcuts import render

# Create your views here.


tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form) :
    task = forms.CharField(label = "New Task")
    priority = forms.IntegerField(label = "Priority", min_value= 1, max_value= 99)

def index(request) :
    return render(request ,"tasks/index.html" , {
        "tasks" : tasks 
    })

def add(request) :

    if request.method == "POST" : 
        form = NewTaskForm(request.POST) #request.POST has the data the user submitted

        if form.is_valid() :
            task = form.cleaned_data["tasks"] #Access the answer submitted as tasks
            tasks.append(task)

        else : 
            return render(request , "tasks/add.html" , {
                "form" : NewTaskForm()
            })

    return render(request , "tasks/add.html", {
        "form" : NewTaskForm()
    })