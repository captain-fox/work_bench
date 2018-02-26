from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView


class Homepage(TemplateView):
    template_name = 'homepage/homepage_base_template.html'


class Navbar(TemplateView):
    template_name = 'homepage/navbar.html'


class MainContent(View):
    template_name = 'homepage/homepage_main_content.html'

    def get(self, request):
        return render(request, self.template_name, {})
