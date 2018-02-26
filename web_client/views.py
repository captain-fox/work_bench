from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView


class Homepage(TemplateView):
    template_name = 'homepage/homepage_base_template.html'


class Navbar(TemplateView):
    template_name = 'homepage/navbar.html'


class MainContent(TemplateView):
    template_name = 'homepage/homepage_main_content.html'

    def get_context_data(self, **kwargs):
        context = super(MainContent, self).get_context_data(**kwargs)
        context['posts'] = range(0, 3)
        return context

