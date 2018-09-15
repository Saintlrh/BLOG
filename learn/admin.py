from django.contrib import admin
from .models import Article, Classify, Comment, User, Share
'''admin.site.register(Article)
admin.site.register(Classify)
admin.site.register(Comment)
'''


class ArticleAdmin(admin.ModelAdmin):
    def title(self):
        if self.title:
            return self.title  #改掉admin中的模型属性英文显示问题
    title.short_description = "文章"
    list_display = [title, 'date', 'content', 'introduction', 'classify', 'isDelete']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 5
    style_fields = {'content': 'ueditor'}
    fieldsets = [
        ('文本', {"fields": ['title', 'content', 'introduction']}),
        ('其他', {"fields": ['classify', 'isDelete', 'date']}),
    ]
 #执行动作的位置
    actions_on_top = True


admin.site.register(Article, ArticleAdmin)


class ArticleInfo(admin.TabularInline):
    model = Article
    extra = 1


class ClassifyAdmin(admin.ModelAdmin):
    inlines = [ArticleInfo]
    list_display = ['name', 'num', 'isDelete']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Classify, ClassifyAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['date', 'comment', 'user_id', 'isDelete']
    list_filter = ['user_id']
    search_fields = ['user_id']


admin.site.register(Comment, CommentAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName', 'userPassword', 'userPhonenum', 'isDelete']
    list_filter = ['userName']
    search_fields = ['userName']


admin.site.register(User, UserAdmin)


class ShareAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'content', 'isDelete']
    list_filter = ['content']
    search_fields = ['content']


admin.site.register(Share, ShareAdmin)
