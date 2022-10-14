from django.urls import path
#now import the views.py file into this code
from . import views
from . import models
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (projectList,ProjectCreate,ProjectDetail,ProjectUpdate,ProjectDelete,ProjectForm)


urlpatterns=[
  path('',views.index),
  path('home_view/',views.home_view),
  path('list_view/',views.list_view),
  path('create_view/',views.create_view),
  path('<int:id>/',views.detail_view),
  path('<int:id>/update',views.update_view),
  path('<id>/delete',views.delete_view ),
  path('admin/', admin.site.urls),
  path('model_create/', ProjectCreate.as_view(template_name='model_create_form.html')),
  path('project_list/', projectList.as_view(template_name='project_list.html')),
  path('detail/<pk>/', ProjectDetail.as_view(template_name='model_detail_form.html')),
  path('<pk>/update_model/', ProjectUpdate.as_view(template_name='model_create_form.html')),
  path('<pk>/delete_model/', ProjectDelete.as_view(template_name='model_delete_form.html')),
  path('model/', ProjectForm.as_view(template_name='model_form.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)