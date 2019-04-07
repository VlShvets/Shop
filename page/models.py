from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Good(models.Model):
    category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 50, unique = True, verbose_name = "Название")
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    in_stock = models.BooleanField(default = True, db_index = True, verbose_name = "В наличии")
    
    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии)"
        return s
    
    def save(self, *args, **kwargs):
        super(Good, self).save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        super(Good, self).delete(*args, **kwargs)
    
    def get_in_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""
    
    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"
    
class BlogArticle(models.Model):
    title = models.CharField(max_length = 200, unique_for_date = "pubdate")
    pubdate = models.DateField()
    update = models.DateTimeField(auto_now = True)
