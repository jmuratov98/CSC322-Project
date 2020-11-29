from django.db import models
from PIL import Image
from uuid import uuid4
from cuisino import settings

"""
    Menu Items
"""
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

    def __iter__(self):
        yield 'category', self.category
        yield 'itemName', self.itemName
        yield 'itemDescription', self.itemDescription
        yield 'itemPrice', self.itemPrice
        yield 'itemReviews', self.itemReviews
        yield 'itemImage', self.itemImage
        

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.itemImage.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.itemImage.path)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('menu-item', args=[str(self.id)])


"""
    Order
"""

class Order(models.Model):
    RESERVATION = 0
    PICK_UP = 1
    DELIVERY = 2

    ORDER_TYPES = [
        ( RESERVATION, 'Reservation' ),
        ( PICK_UP, 'Pick Up' ),
        ( DELIVERY, 'Delivery' ),
    ]

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    orderID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    orderType = models.SmallIntegerField(choices=ORDER_TYPES)
    orderDate = models.DateTimeField(auto_now_add=True)

class OrderDetails(models.Model):
    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'

    orderDetailID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemID = models.OneToOneField(MenuItems, null=True, on_delete=models.SET_NULL)
    itemQuantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    