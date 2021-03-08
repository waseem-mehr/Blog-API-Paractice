from django.db import models

# Create your models here.

CHOICES=(
    ('published','published'),
    ('not published','not published')
)
class PostCategorey(models.Model):

    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    

    class PostPublishObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    name=models.CharField(max_length=100,blank=False,null=False)
    text=models.TextField(max_length=1000,blank=True,null=True)
    post_categorey=models.ForeignKey(PostCategorey,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=1000,unique_for_date='date',default='')
    status=models.TextField(choices=CHOICES,default='')
    date=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    post_publish_objects=PostPublishObjects()

    class Meta:
        ordering=('-date',)

    def __str__(self):
        return self.name
