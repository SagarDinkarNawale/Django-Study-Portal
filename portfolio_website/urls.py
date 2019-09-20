
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import job.views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', job.views.index,name='index'),
    path('news_post/', job.views.news_post,name='news_post'),
    path('library/', job.views.library,name='library'),
    path('elements/', job.views.elements,name='elements'),
    path('contact/', job.views.contact,name='contact'),
    path('courses/', job.views.courses,name='courses'),
    path('teachers/', job.views.teachers,name='teachers'),
    path('news/', job.views.news,name='news'), 
    path('addbook/', job.views.addbook,name='addbook'),
    path('departments/', job.views.departments,name='departments'),   
    # path('viewbookbcs/', job.views.viewbookbcs,name='viewbookbcs'),  
    path('viewbookbca/', job.views.viewbookbca,name='viewbookbca'),  
    path('viewbookbba/', job.views.viewbookbba,name='viewbookbba'), 
    path('subbook/', job.views.subbook,name='subbook'),
    # path('getbook/', job.views.getbook,name='getbook'), 
    path('viewbookbcs/ ',include('job.urls')),
    # path('getbook/<int:book_id>', job.views.getbook,name='getbook'), 
    # path('<int:book_id>', job.views.getbook,name='getbook'),    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

