from django.db import models
from datetime import timedelta,date

edd = date.today()+timedelta(days=5)


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100, unique=True)
    author_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    no_of_copies = models.PositiveIntegerField()
    category = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images", null="True")

    def __str__(self):
        return self.book_name


class Order(models.Model):
    products = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    options = (
        ('Delivered', 'Delivered'),
        ('intransit', 'intransit'),
        ('ordered', 'ordered'),
        ('cancelled', 'cancelled'),
    )
    phone = models.CharField(max_length=12, null=True)
    status = models.CharField(max_length=20, choices=options, default='ordered')
    expected_delivery_date = models.DateField(null=True,default=edd)

# book=Book(book_name="abc",author_name="abc",price="abc",no_of_copies="abc")
# book.save()

# book=Book.objects.all()

# orm for fetching a specific query
# reference = modelname.objects.get(fieldname=value)

# filter
# books=Book.objects.filter(price__lt=300)   lt=lessthan
# books=Book.objects.filter(price__lte=300)   lte=lessthanequal
# books=Book.objects.filter(price__gt=300)      gt=greaterthan
# books=Book.objects.filter(price__gte=300)
# books=Book.objects.filter(category="novel")

# books=Book.objects.filter(book_name__iexact="ABC")  get result without checking case sensitive
# books=Book.objects.filter(book_name__contains="AC")  specifed key is in there or not
# books=Book.objects.filter(book_name__iexact="ABC")  get result without checking case sensitive
# books=Book.objects.all().order_by('price')  order by ascending
# books=Book.objects.all().order_by('-price')  order by descending
