from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.first_name

class Picture(models.Model):
    image = models.ImageField(upload_to= 'pictures/', blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,default=None)
    category = models.ForeignKey('Category', on_delete = models.CASCADE,default=None)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, default=None)

    def save_pic(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def all_pics(cls):
        pics = cls.objects.all()
        return pics
    @classmethod
    def get_one_pic(cls,id):
        pictures = cls.objects.filter(id = id)
        return pictures
    @classmethod
    def search_image(cls,search_term):

        searched_image = cls.objects.filter(name =search_term)
        return searched_image

    @classmethod
    def view_pictures_by_location(cls,location):
        location_pics = cls.objects.filter(location= location)
        return location_pics
    @classmethod
    def view_pictures_by_category(cls,category):
        category = cls.objects.filter(category = category)
        return category
    @classmethod
    def user_pics(cls,user):
        user_pic = cls.objects.filter(user = user)
        return user_pic

    @classmethod
    def delete_post(cls, post_id):
        post = cls.objects.filter(pk=post_id)
        post.delete()
        
class Location(models.Model):
    location_name = models.CharField(max_length=80)
    def save_location(self):
        self.save()
    def __str__(self):
        return self.location_name 
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

class Category(models.Model):
    category_name = models.CharField(max_length=80)
    def save_category(self):
        self.save()
    @classmethod
    def get_categories(cls):
        categories = cls.objects.all()
        return categories
    def __str__(self):
        return self.category_name 

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='image/')
    bio = models.CharField(max_length=300)
    username = models.CharField(max_length=50,default='Your username')

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def profiles_posts(self):
        return self.image_set.all()

    def search_profile(cls, username):

       found_user = User.objects.get(username = username)

       return found_user

