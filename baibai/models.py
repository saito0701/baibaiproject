from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ', 
        max_length=20)
    
    def __str__(self):
        return self.title

class BaibaiPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    
    title = models.CharField(
        verbose_name='タイトル', 
        max_length=200        
        )
    comment = models.TextField(
        verbose_name='コメント',  
        )
    money = models.PositiveIntegerField(
        verbose_name='値段',
        max_length=7,
    )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'baibais',    
        )
    # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to = 'baibais',  
        blank=True,            
        null=True
        )        
    
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', 
        auto_now_add=True       
        )
    
    def __str__(self):
        return self.title
