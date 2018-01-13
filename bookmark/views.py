from bookmark.forms import CreateBookmarkForm
from bookmark.models import Bookmark
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class AllBookmarksView(ListView):
    model = Bookmark
    template_name = 'bookmark/all_bookmarks.html'
    context_object_name = 'bookmarks'

    def get_queryset(self):
        return Bookmark.objects.filter(is_public = True)

# def all_bookmarks(request):
#     bookmarks = Bookmark.objects.filter(is_public=True)
#     return render(request,'bookmark/all_bookmarks.html',{'bookmarks': bookmarks})


class BookmarkByUser(DetailView):
    model = User
    template_name = 'bookmark/detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(BookmarkByUser, self).get_context_data(**kwargs)
        context['bookmarks'] = Bookmark.objects.filter(user=self.get_object(), is_public=True)
        return context


class CreateBookmarkView(CreateView):
    form_class = CreateBookmarkForm
    template_name = 'bookmark/create_bookmark_form.html'

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        bookmark.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('all-bookmarks'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateBookmarkView, self).dispatch(request, *args, **kwargs)


class UpdateBookmarkView(UpdateView):
    model = Bookmark
    template_name = 'bookmark/update_bookmark_form.html'
    fields = ['name', 'url', 'is_public', 'tags']
    success_url = reverse_lazy('all-bookmarks')

    def get(self, request,*args, **kwargs):
        bookmark=self.get_object()
        if not request.user == bookmark.user:
            return HttpResponseForbidden("Forbidden")
        else:
            return super(UpdateBookmarkView, self).get(request,*args, **kwargs)



# def bookmark_by_user(request,username):
#     user = get_object_or_404(User, username=username)
#     bookmarks = Bookmark.objects.filter(user=user)
#     return render(request,'bookmark/detail.html',{'bookmarks':bookmarks, 'user':user})