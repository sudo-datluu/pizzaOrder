from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):       
    class Category(models.TextChoices):
        PIZZA = 'PZ', _('Pizza')
        DRINKS = 'DR', _('Drinks')
        SAUCE = 'SC', _('Sauce')
        SIDEFOOD = 'SF', _('Side Food')
    
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.PIZZA
    )
    def get_category(self) -> Category:
        return self.Category[self.category]
    
    name = models.CharField(max_length=225)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    maxQty = models.IntegerField(default=0)
    pricePerUnit = models.DecimalField(max_digits=6, decimal_places=2)
    caloriesPerUnit = models.DecimalField(max_digits=6, decimal_places=2, default='1000.50')
    dateAdded = models.DateTimeField(auto_now_add=True)
    img_url = models.CharField(max_length=300, default='')

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-dateAdded',)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}'

