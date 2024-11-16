from django.shortcuts import render,get_object_or_404

# Create your views here.
def home(request):
    return render(request,'index.html')
def product(request):
    return render(request,'product.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def service(request):
    return render(request,'service.html')