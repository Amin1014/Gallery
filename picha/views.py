from django.shortcuts import render
from .models import Images, Locations

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def gallery(request):
    locations =Locations.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        pictures = Images.search_image(search_term)
        return render(request, 'gallery.html', {'pictures': pictures,'locations':locations})
    else:
        pictures = Images.get_all()
        return render(request, 'gallery.html', {'pictures': pictures,'locations':locations})

def search(request,city):
    locations =Locations.objects.all()

    pictures = Images.filter_by_location(city)
    return render(request, 'gallery.html', {'pictures': pictures,'locations':locations})

