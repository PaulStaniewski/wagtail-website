from django.shortcuts import render
from home.models import HomePage

def my_view(request):
    my_model = HomePage.objects.first()
    change_icons_html = my_model.change_icons
    banner_title = my_model.banner_title
    banner_subtitle = my_model.banner_subtitle
    about_title = my_model.about_title
    about_description = my_model.about_description
    cards = my_model.cards

    context = {
        'change_icons': change_icons_html,
        'banner_title': banner_title,
        'banner_subtitle': banner_subtitle,
        'about_title': about_title,
        'about_description': about_description,
        'cards': cards,
    }

    return render(request, 'home/home_page.html', context)