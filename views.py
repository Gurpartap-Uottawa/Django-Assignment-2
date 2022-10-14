from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.http import HttpResponse
from .forms import InputForm
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView,FormView)
from django.views.generic.detail import DetailView
from .models import projectModel
 
def index(request):
  return HttpResponse("Hello Geeks")

def home_view(request):
  context ={}
  # create object of form
  form = InputForm(request.POST or None, request.FILES or None)
  # check if form data is valid
  if form.is_valid():
    # save the form data to model
    form.save()
  context['form']= form
  return render(request, "home.html", context)

def list_view(request):
  # dictionary for initial data with
  # field names as keys
  context ={}

  # add the dictionary during initialization
  context["dataset"] = projectModel.objects.all()
        
  return render(request, "list_view.html", context)

class projectList(ListView):
 
  # specify the model for list view
  model = projectModel

def create_view(request):
  # dictionary for initial data with
  # field names as keys
  context ={}

  # add the dictionary during initialization
  form = InputForm(request.POST or None)
  if form.is_valid():
      form.save()
        
  context['form']= form
  return render(request, "create_view.html", context)

def list_view(request):
  # dictionary for initial data with
  # field names as keys
  context ={}

  # add the dictionary during initialization
  context["dataset"] = projectModel.objects.all()
        
  return render(request, "list_view.html", context)

def detail_view(request, id):
  # dictionary for initial data with
  # field names as keys
  context ={}

  # add the dictionary during initialization
  context["data"] = projectModel.objects.get(id = id)
      
  return render(request, "detail_view.html", context)

def update_view(request, id):
  # dictionary for initial data with
  # field names as keys
  context ={}

  # fetch the object related to passed id
  obj = get_object_or_404(projectModel, id = id)

  # pass the object as instance in form
  form = InputForm(request.POST or None, instance = obj)

  # save the data from the form and
  # redirect to detail_view
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/" + str(id))

  # add form dictionary to context
  context["form"] = form

  return render(request, "update_view.html", context)

def delete_view(request, id):
  # dictionary for initial data with
  # field names as keys
  context ={}

  # fetch the object related to passed id
  obj = get_object_or_404(projectModel, id = id)


  if request.method =="POST":
    # delete object
    obj.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/list_view")

  return render(request, "delete_view.html", context)

class ProjectCreate(CreateView):
 
  # specify the model for create view
  model = projectModel

  # specify the fields to be displayed
  fields = ['title', 'description']
  success_url = 'prject_list/'

class ProjectDetail(DetailView):
  # specify the model to use
  model = projectModel

class ProjectUpdate(UpdateView):
  # specify the model you want to use
  model = projectModel
  
  # specify the fields
  fields = ["title","description"]

  # can specify success url
  # url to redirect after successfully
  # updating details
  success_url ="/project_list/"

class ProjectDelete(DeleteView):
  # specify the model you want to use
  model = projectModel
    
  # can specify success url
  # url to redirect after successfully
  # deleting object
  success_url ="/project_list/"

class ProjectForm(FormView):
  # specify the Form you want to use
  form_class = InputForm
    
  # specify name of template
  template_name = "model_form.html"

  # can specify success url
  # url to redirect after successfully
  # updating details
  success_url ="/thanks/"
