from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home__view(request):
    return render(request, 'index.html')
 
@login_required(login_url= "account:login")  
def dashboard__view(request):
    articles = Article.objects.filter(author = request.user)
    return render(request, 'dashboard.html', {'articles': articles})

@login_required(login_url= "account:login") 
def articles__view(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})
 
 
@login_required(login_url= "account:login") 
def article__update__view(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        
        messages.success(request, "Meqaleniz ugurla guncellendi..")
        return redirect("dashboard")
 
    context = {"form": form}
    return render(request, 'update.html', context)
 
 
 
 
 
@login_required(login_url= "account:login") 
def article__delete__view(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()   
    messages.success(request, "Meqaleniz ugurla silindi..")
    return redirect("dashboard")







@login_required(login_url= "account:login") 

def addarticle__view(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        
        messages.success(request, "Meqaleniz ugurla elave olundu..")
        return redirect("dashboard")
 
    context = {"form": form}
    return render(request, 'addarticle.html', context)
 



 

@login_required(login_url= "account:login") 
def article__detail__view(request, id):
    # article = Article.objects.filter(id = id).first()
    # context = {"article": article}
    article = get_object_or_404(Article, id = id)
    
    # return render(request, 'article-detail.html', context)
    return render(request, 'article-detail.html', {"article":article})
def about__view(request):
    return render(request, 'about.html')


def contact__view(request):
    return render(request, 'contact.html')






def handling_404(request, exception):
    return render(request, '404.html', {})