from django.shortcuts import render
import pafy,math

# Create your views here.
def help(request):
      return render(request, "help.html")

def ytdl(request):
	if request.method=='POST':
		yturl=request.POST.get('url')
		video=pafy.new(yturl)
		vd=video.streams
		ad=video.audiostreams
		b=[]
		for i in vd:
			x=(i.extension,str(math.ceil(i.get_filesize()/1024/1024))+' mb',i.url)
			b.append(x)
		
		c=[]
		for i in ad:
			x=(i.extension,str(math.ceil(i.get_filesize()/1024/1024))+' mb',i.url)
			c.append(x)
		
			
		context={'video':video, 'vdo':b, 'ado':c }
		return render(request, 'ytdl.html' ,context)
		
	else:
		return render(request, 'ytdl.html' )
