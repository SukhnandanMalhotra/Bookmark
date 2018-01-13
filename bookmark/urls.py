from bookmark import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^all/$', view=views.AllBookmarksView.as_view(), name='all-bookmarks'),
    re_path(r'^detail/(?P<username>[\w-]+)/$', view=views.BookmarkByUser.as_view(), name='detail-route'),
    re_path(r'^create/$', view=views.CreateBookmarkView.as_view(), name='create-bookmark'),
    re_path(r'^update/(?P<pk>[0-9]+)/$', view=views.UpdateBookmarkView.as_view(), name='update-bookmark')
]
