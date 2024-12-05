from django.db import models

class Hotel(models.Model):
    hname = models.CharField(max_length=100)
    hdesc = models.TextField()
    himg = models.ImageField(upload_to='hotel_image/')

    def __str__(self):
        return self.hname
    

class HotelBooking(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    datetime = models.DateTimeField(auto_now_add=True)
    destination = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.fullname +'--'+ self.email
    

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullname +'--'+ self.email
    