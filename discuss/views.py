from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from user.forms import CommentForm
from user.models import Comment

from .filters import DiscussFilter
from .forms import DiscussForm
from .models import Discussion, Topic


# Главное представление
def index(request):

    discussion = Discussion.objects.order_by('-creation_time')
    myFilter = DiscussFilter(request.GET, queryset=discussion)

    discussion = myFilter.qs
    max_discuss = 5

    paginator = Paginator(discussion, max_discuss)
    page = request.GET.get('page', 1 ) #Для получения параметров из строки запроса 
    try:
        page_discuss = paginator.page(page)
    except PageNotAnInteger:
        #Если страница не является целым числом
        page_discuss = paginator.page(1)
    except EmptyPage:
        #Если страница больше максимальной, добавим последнюю страницу результатов
        page_discuss = paginator.page(page)

    template = 'discuss/index.html'
    pages = paginator.count//max_discuss


    if pages * max_discuss < paginator.count:
        pages += 1
    list_pages = []

    for i in range(1,pages+1):
        list_pages.append(i)

    context = {
        'discussion': page_discuss,
        'pages': list_pages,
        'myFilter': myFilter,
    }

    return render(request, template, context)


# Представление детального просмотра обсуждения
def detail(request, id):

    discussion = get_object_or_404(Discussion, id = id)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.discuss = discussion
            comment.save()
            return redirect(f'/Discussion/{id}')
    else:
        form = CommentForm()

    comments = Comment.objects.filter(discuss = id).order_by('-creation_time')
    
    context = {
        'discussion': discussion,
        'form': form,
        'comments': comments,
    }

    template = "discuss/detail.html"

    return render(request, template, context)

# Представление для создания обсуждений
@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == 'POST':
        form = DiscussForm(request.POST, request.FILES)
        if form.is_valid:
            discussion = form.save(commit=False)
            discussion.author = request.user
            discussion.save()
            return redirect('index')
        else:
            error = 'Form is invalid'
    form = DiscussForm
    topic = Topic.objects.all()
    context = {
        'title': 'Create post',
        'form': form,
        'error': error,
        'topic': topic,
    }
    template = 'discuss/create.html'
    return render(request, template, context)

# Представление для удаления обсуждения
@login_required(login_url='login')
def delete(request, id):
    discussion = Discussion.objects.get(id = id)
    if discussion.author.id == request.user.id:
        discussion.delete()
        return redirect("index")
    else:
        return HttpResponse("Not author")

# Представления для обновления обсуждения
@login_required(login_url='login')
def update(request, id):
    discussion = Discussion.objects.get(id = id)
    template = 'discuss/update.html'
    error = ''
    topic = Topic.objects.all()
    if discussion.author.id == request.user.id:
        if request.method == 'POST':
            form = DiscussForm(request.POST, request.FILES, instance=discussion)
            if form.is_valid:
                discussion.updated = True
                discussion.creation_time = discussion.creation_time
                form.save()
                return redirect(f'/Discussion/{id}')
            else:
                error = 'Form is invalid'
        
        context = {
            'form': DiscussForm(instance=discussion),
            'discussion': discussion,
            'error': error, 
            'topic': topic,
            }
        
        return render(request, template, context)

    else:
        return HttpResponse("Not author")




def getTopic(request, topic_pk):
    topic = Topic.objects.get(pk = topic_pk)
    discussion = Discussion.objects.filter(discussion_topic = topic_pk).order_by("-creation_time")

    template = 'discuss/getTopic.html'

    max_discuss = 5

    paginator = Paginator(discussion, max_discuss)
    page = request.GET.get('page', 1 ) #Для получения параметров из строки запроса 
    try:
        page_discuss = paginator.page(page)
    except PageNotAnInteger:
        #Если страница не является целым числом
        page_discuss = paginator.page(1)
    except EmptyPage:
        #Если страница больше максимальной, добавим последнюю страницу результатов
        page_discuss = paginator.page(page)

    pages = paginator.count//max_discuss


    if pages * max_discuss < paginator.count:
        pages += 1
    list_pages = []

    for i in range(1,pages+1):
        list_pages.append(i)

    context = {
        'discussion': page_discuss,
        'pages': list_pages,
        'topic': topic
    }

    return render(request, template, context)
    