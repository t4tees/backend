from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/ytubers/%y/%m/',default="")
    

    def __str__(self):
        return self.name 




class Product(models.Model):
	
		
	
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	image = models.ImageField(upload_to='media/ytubers/%y/%m/')
	#description = RichTextField()
	is_featured = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=datetime.now, blank=True)
	#quantity = models.IntegerField()
	category = models.ManyToManyField(Categorys, related_name="product")

	def __str__(self):
		return self.name






# Create your models here.



