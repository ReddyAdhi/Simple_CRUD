from django.shortcuts import render
from django.views import generic

# Create your views here.

class GetHome(generic.TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(GetHome, self).get_context_data(**kwargs)
        context['endpoint'] = self.request.get_full_path
        return context


class CreateHome(generic.TemplateView):

    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateHome, self).get_context_data(**kwargs)
        context['endpoint'] = self.request.get_full_path

        return context


class ReadHome(generic.TemplateView):

    template_name = 'read.html'

    def get_context_data(self, **kwargs):
        context = super(ReadHome, self).get_context_data(**kwargs)
        context['endpoint'] = self.request.get_full_path

        return context


class UpdateHome(generic.TemplateView):

    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateHome, self).get_context_data(**kwargs)
        context['endpoint'] = self.request.get_full_path

        return context


class DeleteHome(generic.TemplateView):

    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteHome, self).get_context_data(**kwargs)
        context['endpoint'] = self.request.get_full_path

        return context
