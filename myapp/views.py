from django.shortcuts import render
from myapp.models import MyData

# Create your views here.
def home(request):
    objects = MyData.objects.all().delete()
    data = MyData(name = "Anupam", email = "anupam@journaldev.com",age = "24", website = "www.journaldev.com")
    data.save()
    data = MyData(name = "Another", email = "another@journaldev.com",age = "21", website = "www.google.com")
    data.save()
    objects = MyData.objects.all()
    data = []
    for obj in objects:
        data.append({
            'name': obj.name,
            'age': obj.age,
            'email': obj.email,
            'url': obj.website
        })
    # the data to pass to the template must in dictionary
    return render(request, 'home.html', {'data': data})

def about(request):
    return render(request, 'about.html')
