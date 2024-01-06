from django.shortcuts import render, get_object_or_404
from .models import Post, Project
from django.http import Http404
from django.views.generic import ListView
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .forms import SearchForm
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/post/index.html'
    extra_context = {'active_page': 'blog'}


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request,
                  'blog/post/index.html',
                  {'form': form,
                   'query': query,
                   'results': results})

def post_list(request, tag_slug=None):
    #Display list
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    active_page = 'blog'

    #Search
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + \
SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')
    return render(request, 'blog/post/index.html', {'posts': posts, 'active_page': active_page, 'tag': tag, 'form': form,
                   'query': query,
                   'results': results})

def post_detail(request, year, month, day, post):
    active_page = 'blog'
    posts = Post.published.all()
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids) \
        .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags', '-publish')[:4]
    return render(request,'blog/post/post1.html',{'posts': posts, 'post': post, 'active_page': active_page, 'similar_posts': similar_posts})

def project_list(request):
    projects = Project.published.all()
    active_page = 'project'
    return render(request, 'blog/post/projects.html', {'projects': projects, 'active_page': active_page})

def project_detail(request, id):
    active_page = 'project'
    projects = Project.published.all()
    project = get_object_or_404(Project, id=id, status=Project.Status.PUBLISHED)
    return render(request,'blog/post/project1.html',{'projects': projects, 'project': project, 'active_page': active_page})

def about(request):
    active_page = 'about'
    return render(request, 'blog/post/about.html', {'active_page': active_page})

