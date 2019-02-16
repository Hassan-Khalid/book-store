from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120, null=False)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:book-list', args=[self.slug])


class Book(models.Model):
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, db_index=True)
    author = models.CharField(max_length=120)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('products:product_detail', args=[self.id, self.slug])
