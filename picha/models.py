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

    # add image categories model
    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(self, new_url):
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('Image you specified does not exist')    
    

    @classmethod
    def get_all(cls):
        pics = Images.objects.all()
        return pics
    
    
    @classmethod
    def get_image_by_id(cls, id):
        retrieved = Images.objects.get(id = id)
        return retrieved

    @classmethod
    def search_image(cls, cat):
        retrieved = cls.objects.filter(category__name__icontains=cat) 
        return retrieved #list of instances

    @classmethod
    def filter_by_location(cls ,location):
        retrieved = Images.objects.filter(location__city__icontains=location)
        return retrieved 