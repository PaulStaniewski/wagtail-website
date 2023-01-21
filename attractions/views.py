from django.shortcuts import render

def my_view(request):
    image_position = 'center'
    image_size = 'cover'
    context = {
        'image_position': image_position,
        'image_size': image_size
    }
    return render(request, 'mytemplate.html', context)
