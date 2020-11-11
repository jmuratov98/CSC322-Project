from django.db import models
from PIL import Image

# Create your models here.
class MenuItems(models.Model):
    APPETIZERS = 0
    SOUPS_AND_SALADS = 1
    BAR = 2
    SPECIALS = 3
    BEVERAGES = 4
    ENTREES = 5
    DESSERTS = 6

    MENU_CATEGORY_CHOICES = [
        ( APPETIZERS, 'Appetizers' ),
        ( SOUPS_AND_SALADS, 'Soups & Salads' ),
        ( BAR, 'Bar' ),
        ( SPECIALS, 'House Specials' ),
        ( BEVERAGES, 'Beverages' ),
        ( ENTREES, 'Entrees' ),
        ( DESSERTS, 'Desserts' )
    ]

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    itemID = models.AutoField(primary_key=True)
    category = models.PositiveSmallIntegerField(choices=MENU_CATEGORY_CHOICES, default=APPETIZERS)
    itemName = models.CharField(max_length=200)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    itemReviews = models.TextField(null=True, blank=True)
    itemImage = models.ImageField(default='default.jpg', upload_to="menu_images")

    def __str__(self):
        return f'{self.itemName}'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.itemImage.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.itemImage.path)