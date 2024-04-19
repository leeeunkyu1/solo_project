from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http  import require_POST


def index(request):
    return render(request, "index.html")


def hello(request):
    name = "은규"
    tags = ["python", "django", "html", "css"]
    books = ["기사단장 죽이기", "여자없는 남자들", "개미", "나미야 잡화상점", "해리포터와 마법사의 돌"]
    context = {
        "name": name,
        "tags": tags,
        "books": books,
    }
    return render(request, "hello.html", context)


def data_throw(request):
    return render(request, "data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {"message": message}
    return render(request, "data_catch.html", context)


def articles(request):
    articles = Article.objects.all().order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "detail.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.id)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "create.html", context)

    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # article = Article.objects.create(title=title, content=content) #새로운 Article 저장
    # return redirect("detail", article.pk)




def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "update.html", context)
    
    # article = Article.objects.get(pk=pk)
    # article.title = request.POST.get("title")
    # article.content = request.POST.get("content")
    # article.save()
    # return redirect("detail", article.pk)
    
    

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("articles:articles")
