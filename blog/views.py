from django.shortcuts import render
from django.views import generic
from blog.models import Entry, Tag

class BlogIndex(generic.ListView):
	queryset = Entry.objects.published()
	#template_name = 'blog/index.html'
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(BlogIndex, self).get_context_data(**kwargs)
		context['tag_list'] = Tag.objects.all()
		return context


class BlogDetail(generic.DetailView):
        model = Entry
	template_name = 'blog/post.html'

	def get_context_data(self, **kwargs):
		context = super(BlogDetail, self).get_context_data(**kwargs)
		context['tag_list'] = Tag.objects.all()
		return context


def tagdetail(request, pk):
	try:
		tag = Tag.objects.get(pk=pk)
	except Tag.DoesNotExist:
		raise Http404

	entry_list = tag.entry_set.all()
	return render(request, 'blog/index.html', {
		'is_tag': True,
		'tag_slug': tag.slug,
		'entry_list': entry_list,
		'tag_list': Tag.objects.all()
		}
		)

def about(request):
	tag_list = Tag.objects.all()
	return render(request, 'blog/about.html', {'tag_list': tag_list})






