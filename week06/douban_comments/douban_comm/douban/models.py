from django.db import models

# Create your models here.
class Douban(models.Model):
    STAR_ITEMS = [
        (1, '1'),    
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
  
    author = models.CharField(max_length=10, verbose_name="评论人")
    star = models.IntegerField(choices=STAR_ITEMS, verbose_name="星数")
    comments = models.CharField(max_length=128, verbose_name="评论内容")

    class Meta:
        verbose_name = verbose_name_plural = "影评信息"
        
    def __str__(self):
        return '<Douban: {}>'.format(self.author)
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()