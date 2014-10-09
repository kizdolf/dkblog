from django.contrib import admin
from blog.models import Article, Author_blog, Comment, Link, Tag, Quote

class CommentInline(admin.TabularInline):
  model = Comment

class LinkInline(admin.TabularInline):
  model = Link

class ArticleAdmin(admin.ModelAdmin):
  fields = ['main_name', 'text', 'short', 'draft', 'pub_date', 'author', 'tags']
  list_display= ['main_name', 'author', 'pub_date']
  inlines = [LinkInline, CommentInline]

class AuthorAdmin(admin.ModelAdmin):
  list_display= ['main_name', 'count_article', 'mail']
  fields = ['main_name', 'mail', 'img']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author_blog, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Quote)
