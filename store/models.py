from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Product_Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, blank=True)
    main_image = models.ImageField(upload_to="photos/category_photos", null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_category_page', kwargs={'slug': self.slug})


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50, db_index=True, blank=True)
    cat = models.ForeignKey(Product_Category, on_delete=models.PROTECT, null=True)
    mnf = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_page', kwargs={"slug": self.cat.slug, "slug_product": self.slug})
