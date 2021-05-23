from django.db import models

# Create your models here.
class Book(models.Model):
	bookName = models.CharField(max_length = 30)
	bookImage = models.ImageField(blank = False, upload_to = 'book_cover')
	authorName = models.CharField(max_length = 30)
	price = models.IntegerField()
	description = models.TextField()
	pdfUrl = models.URLField()
