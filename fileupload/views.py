#from django.shortcuts import render
from django.views.generic import CreateView
from .models import Picture
from .response import JSONResponse, response_mimetype

class PictureCreateView(CreateView):
    model = Picture

    def form_valid(self, form):
        self.object = form.save()
        data = {'status': 'success'}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        return response
