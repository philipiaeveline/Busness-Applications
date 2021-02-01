from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from .views import BusinessDeleteView,BusinessUpdateView

urlpatterns=[
    url(r'^$',views.pics,name='pics'),
    url(r'^single_pic/(\d+)',views.single_pic,name='single_pic'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^location/(\d+)',views.viewPics_by_location,name='locationpic'),
    url(r'^category/(\d+)',views.viewPics_by_category, name = 'categorypic'),
    url(r'^newpost/$',views.new_post,name='newpost'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^accounts/profile/$',views.profile,name='profile'),
    path('post/<int:pk>/delete/',BusinessDeleteView.as_view(), name="deleteForm"),
    path('post/<int:pk>/update/',BusinessUpdateView.as_view(), name="updateForm"),
    ]
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

