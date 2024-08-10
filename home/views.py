from django.shortcuts import render

from django.views.generic import TemplateView
from .models import HomeSection
from about.models import AboutSection
from experience.models import ExperiencePanel
from projects.models import Project
from contact.models import ContactInfo

def homeView(request):
    return render(request, 'base.html')


def home_page_view(request):
    home_section = HomeSection.objects.first()  # Assuming there's only one entry
    context = {
        'home_section': home_section,
    }
    return render(request, 'home/home_section.html', context)


class HomePageView(TemplateView):
    template_name = 'home/home_section.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_section'] = HomeSection.objects.first()  # Assuming there's only one entry
        return context
    

def home_page_view(request):
    home_section = HomeSection.objects.first()  # Assuming there's only one entry
    about_section = AboutSection.objects.first()  # Assuming there's only one entry
    experience_panels = ExperiencePanel.objects.all()
    projects = Project.objects.all()
    contact_info = ContactInfo.objects.first()  

    context = {
        'home_section': home_section,
        'about_section': about_section,
        'experience_panels': experience_panels,
        'projects': projects,
        'contact_info': contact_info,
    }
    return render(request, 'home/home_section.html', context)