from django.db import models

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.medicine_name

class Supplier(models.Model):

    supplier_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.supplier_name

class Stock(models.Model):

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )

    available_quantity = models.IntegerField()

    updated_at = models.DateTimeField(
        auto_now=True
    )

class Bill(models.Model):

    customer_name = models.CharField(
        max_length=100
    )

    bill_date = models.DateTimeField(
        auto_now_add=True
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    gst_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    invoice_no = models.CharField(
        max_length=20,
        default="INV001"
    )

    customer_mobile = models.CharField(
        max_length=15,
        blank=True
    )

    customer_address = models.TextField(
        blank=True
    )


class BillItem(models.Model):

    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

class StockHistory(models.Model):

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )

    sold_quantity = models.IntegerField()

    remaining_stock = models.IntegerField()

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.medicine.medicine_name
    
class StoreProfile(models.Model):

    store_name = models.CharField(max_length=100)

    owner_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    gst_number = models.CharField(max_length=30)

    address = models.TextField()

    logo = models.ImageField(
        upload_to='logo/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.store_name
    
class Settings(models.Model):

    gst_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18
    )

    low_stock_limit = models.IntegerField(
        default=10
    )

    dark_mode = models.BooleanField(
        default=False
    )

    email_notification = models.BooleanField(
        default=True
    )

class StoreProfile(models.Model):

    store_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    gst_number = models.CharField(max_length=30)
    address = models.TextField()
    logo = models.ImageField(upload_to='store_logo/', blank=True, null=True)

    def __str__(self):
        return self.store_name
    
class Settings(models.Model):

    gst_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18
    )

    low_stock_limit = models.IntegerField(
        default=10
    )

    email_notification = models.BooleanField(
        default=True
    )

    dark_mode = models.BooleanField(
        default=False
    )

    currency = models.CharField(
        max_length=10,
        default="INR"
    )

    def __str__(self):
        return "Application Settings"