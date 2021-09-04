from django.db import models

# Create your models here.
#category model
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, search_term , new_cat):
        try:
            to_update = Category.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Category.DoesNotExist:
            print('Category you specified does not exist')

#image model
class Images(models.Model):
    image_link = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)
