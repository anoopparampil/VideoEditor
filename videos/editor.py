
from moviepy.editor import *

class Editor(object):

	def __init__(self,video,*args,**kwrgs):

		self.video = video

	def crop_video(self,start=0,end=0):

		video = VideoFileClip(self.video).subclip(start,end)
		return video

	def add_text(self,text=None,duraion=10,fontsize=20,color='white',position='center'):
		if text:
			# Make the text. Many more options are available.
			txt_clip = ( TextClip(text,fontsize=fontsize,color=color)
			             .set_position(position)
			             .set_duration(duraion) )
			result = CompositeVideoClip([self.video, text]) # Overlay text on video
		return resut

	def get_duration(self):
		video = VideoFileClip(self.video)
		return video.duration		

	def save_video(self,video,name='my_video.webm'):
		video.write_videofile(name,fps=25) # Many options...
