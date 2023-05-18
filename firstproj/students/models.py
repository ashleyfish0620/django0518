from django.db import models

# Create your models here.
class student(models.Model):
	# 建立欄位，變數
	stdName = models.CharField(max_length=50, null=False)
	stdID = models.CharField(max_length=10, null=False)
	stdSex = models.CharField(max_length=2, default="M", null=False)
	stdBirth = models.DateField(null=False)
	stdEmail = models.EmailField(max_length=100, blank=True, default="")
	stdPhone = models.CharField(max_length=20, blank=True, default="")
	stdAddress = models.CharField(max_length=255, blank=True, default="")

	def __str__(self):
		return self.stdName