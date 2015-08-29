from django.db import models
from django.core.urlresolvers import reverse

from django_markdown.models import MarkdownField

class Tag(models.Model):
	slug = models.CharField(max_length = 200, unique = True)

	def __unicode__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse('tagdetail', args=[str(self.id)])

	class Meta:
		ordering = ['-id']

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish = True)
		

class Entry(models.Model):
	title = models.CharField(max_length = 200)
	body = MarkdownField()
	publish = models.BooleanField(default = False)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	tags = models.ManyToManyField(Tag)

	objects = EntryQuerySet.as_manager()

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])


	def __unicode__(self):
		return self.title
 
        class Meta:
	        verbose_name = 'Blog Entry'
		ordering = ['-created']

