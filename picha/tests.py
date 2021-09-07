from django.test import TestCase
from .models import Images, Category, Locations

# Create your tests here.
class ImagesTest(TestCase):
    '''
    test class for Images model
    '''
    def setUp(self):
        '''
        test method to create Image instances called before all tests
        '''
        self.new_category = Category(name='testing')
        self.new_category.save_category()
        
        self.new_location = Locations(city='Nairobi', country='Kenya')
        self.new_location.save_location()
        
        self.new_picture = Images(image_link='images/picture.jpeg', title='Image title', description='sth random', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Images(image_link='images/photo.jpg', title='Another title', description='sth else more random', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Category.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete()

    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Images))
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Locations))

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Images.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Images.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        update_test = self.new_picture.update_image('images/updated.png')
        self.assertEqual(update_test.image_link, 'images/updated.png')

    def test_get_all(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        pictures = Images.get_all()
        # print(pictures)

    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = Images.get_image_by_id(self.another_picture.id)
        # print(obtained_image.title)

    def test_search_image(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = Images.search_image(self.new_picture.category)
        # print(obtained_image) #todo: reference individual instances

    def test_filter_by_location(self):
        '''
        test method to obtain image insatnces by location
        '''
        obtained_image = Images.filter_by_location(self.another_picture.location)
        print(obtained_image)

class CategoryTest(TestCase):
    '''
    test class for Categories model
    '''
    def setUp(self):
        '''
        test method to create Category instances called before all tests
        '''
        self.new_category = Category(name='categoryA')
        self.new_category.save_category()

    def tearDown(self):
        '''
        test method to delete Category instances after each test is run
        '''
        Category.objects.all().delete()

    def test_save_category(self):
        '''
        test method to ensure a Category instance has been correctly saved
        '''
        self.assertTrue(len(Category.objects.all()) == 1)     

    def test_delete_category(self):
        '''
        test method to ensure a Category instance has been correctly deleted
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)    

    def test_update_category(self):
        '''
        test method to ensure a Category instance has been correctly updated
        '''
        update_cat = Category.update_category('categoryA', 'differentCat')
        self.assertEqual(update_cat.name, 'differentCat')


class LocationTest(TestCase):
    '''
    test class for Locations model
    '''
    def setUp(self):
        '''
        test method to create Location instances called before all tests
        '''
        self.new_location = Locations(city='lost city', country='unknown')
        self.new_location.save_location()

    def test_save_location(self):
        '''
        test method to ensure a Location instance has been correctly saved
        '''
        self.assertTrue(len(Locations.objects.all()) == 1)     

    def test_delete_location(self):
        '''
        test method to ensure a Location instance has been correctly deleted
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Locations.objects.all()) == 0)

    def test_update_location(self):
        '''
        test method to ensure a Location instance has been correctly updated
        '''
        update_locale = Locations.update_location('unknown', 'paperTown')
        self.assertEqual(update_locale.city, 'paperTown')

    def test_get_all(self):
        '''
        test method to ensure all instances of Locations class have been retrieved
        '''
        locations = Locations.get_all()
        print(locations)