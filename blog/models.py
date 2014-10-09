import datetime
from django.db import models
from django.utils import timezone

class Author_blog(models.Model):
    main_name = models.CharField(max_length=200)
    mail = models.EmailField()
    count_article = models.IntegerField(default = 0)
    img = models.ImageField(upload_to = '/img/authors')
    text = models.TextField()
    def __unicode__(self):
        return self.main_name
    def get_count_articles(self):
        nb = Article.objects.filter(author = self.id, draft=0).count()
        self.count_article = nb


class Tag(models.Model):
    name= models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Article(models.Model):
    draft = models.BooleanField(default="true")
    text = models.TextField()
    short = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date de publication')
    author = models.ForeignKey(Author_blog)
    main_name = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return self.main_name
    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        all_authors = Author_blog.objects.all()
        for author in all_authors:
            author.get_count_articles()
            author.save()



class Comment(models.Model):
    author = models.CharField(max_length = 80)
    text = models.CharField(max_length = 250)
    date = models.DateTimeField('date du commentaire')
    article = models.ForeignKey(Article)
    def __unicode__(self):
        return self.author

class Link(models.Model):
    url = models.URLField(max_length = 300)
    article = models.ForeignKey(Article)
    title = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.article.main_name

class Quote(models.Model):
    quote = models.CharField(max_length = 350)
    author = models.CharField(max_length = 40)
    def __unicode__(self):
        return self.quote