from django.shortcuts import  redirect,render, render_to_response, RequestContext,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from church.models import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from church.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ccachurch.settings import MEDIA_URL
import datetime

def index(request):
	context_dict ={}
	now=datetime.datetime.now()
	services =Service.objects.filter(servicedate__gte=now.date())
	context_dict['services']=services
	social=Social.objects.all()
	paginator =Paginator(social,1)
	page =request.GET.get('page')
	try:
		social =paginator.page(page)
		context_dict['socials']=social
	except PageNotAnInteger:
		social=paginator.page(1)
		context_dict['socials']=social
	except EmptyPage:
		socialspaginator.page(paginator.num_pages)
	
	return render(request,'church/index.html',context_dict)
	
def new(request,slug):
	context={}
	new = get_object_or_404(New, slug=slug)
	context['news']=new
	return render(request,'church/news.html',context)
	
def event(request,slug):
	context={}
	event = get_object_or_404(Event, slug=slug)
	context['events']=event
	return render(request,'church/upcoming.html',context)
	
def organization(request):
	context_dict={}
	ministry= Ministry.objects.all()
	context_dict['ministries']=ministry
	resource=Resource.objects.all()
	paginator =Paginator(resource,2)
	page =request.GET.get('page')
	try:
		context_dict['resources']=paginator.page(page)
	except PageNotAnInteger:
		context_dict['resources']=paginator.page(1)
	except EmptyPage:
		resourcespaginator.page(paginator.num_pages)

	
	return render(request,'church/organization.html',context_dict)
def ministry(request, slug):
	context_dict={}
	now=datetime.datetime.now()
	try:
		ministry = Ministry.objects.get(slug=slug)
		context_dict['ministry_name'] = ministry.title
		#context_dict['ministry_title'] = ministry.title
		context_dict['ministry_description'] = ministry.description
		context_dict['ministry_patron'] = ministry.patron
		calender = MinistryCalender.objects.filter(ministry=ministry).filter(event_date__gte=now.date())
		context_dict['calender'] = calender
	except Ministry.DoesNotExist:
		pass
	return render(request, 'church/ministry.html', context_dict)
def sermon(request):
	sermons =Sermon.objects.all()
	paginator =Paginator(sermons,2)
	page =request.GET.get('page')
	try:
		sermons=paginator.page(page)
	except PageNotAnInteger:
		sermons=paginator.page(1)
	except EmptyPage:
		sermonspaginator.page(paginator.num_pages)
	return render_to_response('church/sermons.html',locals(),context_instance=RequestContext(request))
	
def sermontext(request, slug):
    sermon = get_object_or_404(Sermon, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.sermon = sermon
        comment.save()
        return redirect(request.path)
    form.initial['name'] = request.session.get('name')
    form.initial['email'] = request.session.get('email')
    return render_to_response('church/sermondetails.html',
                              {
                                  'sermon': sermon,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))

def gallery(request, slug):
	context_dict = {}
	try:
		social = Social.objects.get(slug=slug)
		context_dict['activity_name'] = social.activity
		images = SocialGallery.objects.filter(title=social)
		context_dict['images'] = images
		context_dict['social'] = social.activitydescription
	except Social.DoesNotExist:
		pass
	return render(request, 'church/gallery.html', context_dict)
	
def leaders(request):
	profile=Leader.objects.all()
	return render(request,'church/leaders.html',{'profiles':profile})