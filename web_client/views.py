from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView


class Homepage(TemplateView):
    template_name = 'homepage/homepage_base_template.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

