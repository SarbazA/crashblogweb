from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()


    def __str__(self):
        return self.title

class Post(models.Model):

    category= models.ForeignKey(Category, related_name='posts' , on_delete = models.CASCADE , null=True , blank=True)  
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body= models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    image = models.ImageField(upload_to='post_image' , blank=True , null=True) 


    def __str__(self):

        return self.title


    class Meta:

        ordering = ('-created_at',)

  
class Comment(models.Model):
    post = models.ForeignKey(Post , related_name ='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)


    class Meta:
        ordering = ('-created_at',)
     

    



   

