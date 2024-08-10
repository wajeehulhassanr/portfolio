from django.shortcuts import render


# about/views.py
from django.shortcuts import render
from .models import AboutSection

# def about_section_view(request):
#     about_section = AboutSection.objects.first()  # Assuming there's only one entry

#     context = {
#         'about_section': about_section,
#     }
#     return render(request, 'about/about_section.html', context)