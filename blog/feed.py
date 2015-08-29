from django.contrib.syndication.views import Feed
from blog.models import Entry

class RssFeed(Feed):
	title = 'RSS - Captain Blog'
	link = '/feed/'
	description = 'RSS Feed'

	def items(self):
		return Entry.objects.published()[:5]
