from random import randrange
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Article, Author_blog, Comment, Link, Tag, Quote

def index(request):
    nb = randrange(Quote.objects.count())
    quote = Quote.objects.all()[nb]
    articles_list = Article.objects.filter(draft=0).order_by('-pub_date')
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    try:
    	latest = paginator.page(page)
    except PageNotAnInteger:
    	latest = paginator.page(1)
    except EmptyPage:
    	latest = paginator.page(1)
    context = {'latest_articles_list' : latest, 'quote': quote}
    return render(request, 'blog/index.html', context)   

def detail(request, article_id):
	article = Article.objects.get(id = article_id)
	message = ""
	comments = Comment.objects.filter(article = article_id)
	links = Link.objects.filter(article = article_id)
	if hasattr(request, 'message'):
		message = request.message
	context = {'article' : article, 'comments': comments, 'links': links, 'message' : message}
	return render(request, 'blog/detail.html', context)

def author(request, author_id):
	author = Author_blog.objects.get(id = author_id)
	articles = Article.objects.filter(author = author_id, draft=0)
	context = {'author' : author, 'articles' : articles}
	return render(request, 'blog/author.html', context)

def comment(request, article_id):
		if not request.POST['author'] or not request.POST['text']:
			request.message = "vous avez oubliez une partie du commentaire non?"
	   		return detail(request, article_id)
	   	else:
	   		request.message = "commentaire enregistre!"
		comment = Comment()
		comment.author=request.POST['author']
		comment.text = request.POST['text']
		comment.date =  timezone.now()
		comment.article = Article.objects.get(id = article_id)
		comment.save()
	   	return detail(request, article_id)

def tag(request, tag_id):
	tag = Tag.objects.get(id = tag_id)
	articles  = Article.objects.filter(tags  = tag_id, draft=0)
	return render(request, 'blog/tag.html', {'tag' : tag, 'articles' : articles})