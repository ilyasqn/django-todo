from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)