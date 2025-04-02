from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=12, null = True)
	message = models.TextField(default = False, null = True, blank = True)

	def __str__(self):
		return self.name



class CarContact(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=12, null = True)
	message = models.TextField(default = False, null = True, blank = True)

	def __str__(self):
		return self.name


class CarSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)



class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(null=True, blank=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(upload_to = 'product_image/', null=True, blank=True)
	STATUS_CHOICES = [
		('NEW', 'Brand New'),
		('Lightly Used (Foreign)', 'Lightly Used (Foreign)'),
		('Other', 'Other'),					
	]
	status = models.CharField(max_length= 20, null= True, choices=STATUS_CHOICES)
	detail = models.TextField(default = False, null = True, blank = True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


#MULTIPLE IMAGES FOR PRDUCT VIEW.


class ProductImage(models.Model):  # This is your CarImage model
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images_Details/')

    def __str__(self):
        return f"{self.product.name} Image"



class Rent(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField(null=True, blank=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(upload_to = 'rent_image/',null=True, blank=True)
	STATUS_CHOICES = [
		('NEW', 'Brand New'),
		('SLIGHTLY USED', 'Slightly Used'),
		('O', 'Other'),
	]
	status = models.CharField(max_length= 20, null= True, choices=STATUS_CHOICES)
	detail = models.TextField(default = False, null = True, blank = True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


# models.py
class RentImage(models.Model):
    rent = models.ForeignKey(Rent, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rent_images_Details/')

    def __str__(self):
        return f"Image for {self.rent.name}"



class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

