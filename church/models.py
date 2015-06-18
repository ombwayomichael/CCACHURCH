from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
SERVICES=(
('Sunday school service','Sunday school service'),
('Youth Service','Youth Service'),
('First Service','First Service'),
('Second Service','Second Service'),
('Third Service','Third Service'),
)
class Service(models.Model):
	servicedate=models.DateTimeField()
	service=models.CharField(max_length=100, choices=SERVICES)
	preacher=models.CharField(max_length=100)
	programmer= models.CharField(max_length=100)
	topic= models.CharField(max_length=100)
	class Meta:
		ordering=['-servicedate',]\
		
	def __unicode__(self):
		return self.service
		
class Social(models.Model):
	activity=models.CharField(max_length=100)
	activitydate =models.DateTimeField()
	activitydescription=models.TextField()
	slug =models.SlugField(unique=False)
	siteimage=models.ImageField(upload_to='socialsiteimages/%Y/%m/%d', null=True)
	class Meta:
		ordering=['-activitydate']
	def get_absolute_url(self):
		return reverse('social',args=[str(self.activity)])
	def __unicode__(self):
		return self.activity
		
class New(models.Model):
	title=models.CharField(max_length=100)
	brief=models.CharField(max_length=100)
	text=models.TextField()
	slug =models.SlugField(unique=False)
	date=models.DateTimeField(auto_now_add=True)
	image=models.ImageField(upload_to='news/%Y/%m/%d', null=True)
	class Meta:
		ordering=['-date']
	def get_absolute_url(self):
		return reverse('new',args=[str(self.activity)])
	def __unicode__(self):
		return self.title
		

class SocialGallery(models.Model):
    title = models.ForeignKey(Social)
    image = models.FileField(upload_to="activities/images/%Y/%m/%d'")
    name = models.CharField(max_length=200)
    def __unicode__(self):
    	return self.image.name
	
	
class Ministry(models.Model):
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=200)
	patron=models.ForeignKey(User)
	date_published=models.DateTimeField(auto_now_add=True)
	slug =models.SlugField(unique=True)
	def get_absolute_url(self):
		return reverse('ministry',args=[str(self.slug)])
		
	def __unicode__(self):
		return self.title
class Resource(models.Model):
	name=models.CharField(max_length=100)
	description= models.CharField(max_length=150)
	resourceimage= models.ImageField(upload_to='Resources/images', null=True)
	resourcefile=models.FileField(upload_to='Resources/files',null=True)
	views=models.IntegerField(default=0)
	def __unicode__(self):
		return self.name
		
class MinistryCalender(models.Model):
	ministry= models.ForeignKey(Ministry)
	event=models.CharField(max_length=100)
	eventDescription=models.CharField(max_length=100)
	event_date=models.DateTimeField()
	venue=models.CharField(max_length=100)
	
	
	def __unicode__(self):
		return self.event

class Sermon(models.Model):
	topic = models.CharField(max_length=128)
	publish =models.BooleanField(default=False)
	slug = models.SlugField(unique=True)
	details=models.TextField()
	dateposted=models.DateTimeField(auto_now_add=True)
	author=models.CharField(max_length=300)
	class Meta:
		ordering =['-dateposted',]\
		
	def __unicode__(self):
		return self.topic
	def get_absolute_url(self):
		return reverse('sermon',args=[str(self.slug)])
	def get_previous_sermon(self):
		return self.get_previous_by_dateposted()
	def get_next_sermon(self):
		return self.get_next_by_dateposted()
	
class Leader(models.Model):
	lastname=models.CharField(max_length=200,null=True)
	firstname=models.CharField(max_length=200,null=True)
	email=models.EmailField(null=True)
	website=models.URLField(null=True)
	cell=models.IntegerField(default=0)
	position=models.CharField(max_length=40)
	picture=models.ImageField(upload_to='Leaders/profile',null=True)
	message= models.TextField()
	def __unicode__(self):
		return self.position
        
class SermonComment(models.Model):
	name=models.CharField(max_length=42)
 	email=models.EmailField(max_length=75)
 	text=models.TextField()
 	sermon=models.ForeignKey(Sermon)
 	created_on=models.DateTimeField(auto_now_add=True)
 	
 	def __unicode__(self):
 		return self.text
 		
class Event(models.Model):
	title=models.CharField(max_length=100)
 	description=models.CharField(max_length=150)
 	text=models.TextField()
 	eventImage=models.ImageField(upload_to='Events/images',null=True)
 	venue=models.CharField(max_length=50)
 	slug=models.SlugField(unique=True)
 	eventDate=models.DateTimeField(auto_now_add=False)
 	
 	class Meta:
 		ordering=['eventDate']
 	def save(self,*args,**kwargs):
 		self.slug=slugify(self.title)
		super(Event, self).save(*args,**kwargs)
		
	def __unicode__(self):
 		return self.title
