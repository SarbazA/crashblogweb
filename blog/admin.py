from django.contrib import admin

from blog.models import Post , Comment , Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}    


admin.site.register(Post , PostAdmin)
admin.site.register(Comment)
admin.site.register(Category , CategoryAdmin)


