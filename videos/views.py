from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from editor import Editor
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from random import choice
import json
class HomeView(TemplateView):

	template_name = "home.html"

	def get_context_data(self, **kwargs):
	    context = super(HomeView, self).get_context_data(**kwargs)
	    context['fielname'] = settings.MEDIA_URL+'/test1.mp4'
	    editor = Editor(settings.MEDIA_ROOT+'/test1.mp4')
	    context['duration'] = editor.get_duration()
	    return context


class CropView(View):

	def post(self,request):

		start = int(float(request.POST['start']))
		end = int(float(request.POST['end']))
		editor = Editor(settings.MEDIA_ROOT+'/test1.mp4')
		video = editor.crop_video(start,end)
		filename = settings.MEDIA_ROOT+'/test1_temp.webm'
		editor.save_video(video,filename)

		return HttpResponse(json.dumps({'filename':settings.MEDIA_URL+'/test1_temp.webm?i='+n}), content_type='application/json')

