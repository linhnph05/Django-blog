from django.urls import path
from . import views
from django.views.generic import RedirectView


app_name = 'blog'
urlpatterns = [
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('blog/', views.post_list, name='post_list'),
    #path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('blog/tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/project/<int:id>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
]