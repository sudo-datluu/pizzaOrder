from .product import Product
from django.utils.translation import gettext_lazy as _
from django.db import models

class Pizza(Product):
    class Meta:
        db_table = 'pizza'
        verbose_name = _('Pizza')
        verbose_name_plural = _('Pizzas')

    class PizzaBase(models.TextChoices):
        TRADITIONAL = 'TD', _('Traditional')
        WHOLEMEAT = 'WM', _('Wholemeal')
        GLUTEN_FREE = 'GF', _('Gluten Free')
    pizzaBase = models.CharField(
        max_length=2,
        choices=PizzaBase.choices,
        default=PizzaBase.TRADITIONAL
    )
    def get_base(self) -> PizzaBase:
        return self.PizzaBase[self.pizzaBase]
    

    class Size(models.TextChoices):
        SMALL = 'S', _('Small - 8 inches')
        LARGE = 'L', _('Large - 11 inches')
        EXTRA_LARGE = 'XL', _('Extra Large - 12 inches')
    size = models.CharField(
        max_length=2,
        choices=Size.choices,
        default=Size.SMALL
    )
    def get_size(self) -> Size:
        return self.Size[self.size]

    class Topping(models.TextChoices):
        SUPREME = 'SP', _('Supreme')
        SAUSAGE_SIZZLE = 'SS', _('Sausage Sizzle')
        HAWAIIAN = 'HW', _("Hawaiian")
        SWEET_CHILLIES_CHICKEN = 'SCC', _("Sweet Chillies Chicken")
        PERI_PERI_CHICKEN = 'PPC', _('Peri-peri Chicken')
        GARDEN_GODNESS = 'GG', _('Garden godness')
        VEGAN_CHEESE = 'VC', _('Vegan Cheese')
    topping = models.CharField(
        max_length=3,
        choices=Topping.choices,
        default=Topping.SUPREME
    )
    def get_topping(self) -> Topping:
        return self.Topping[self.topping]


