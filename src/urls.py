
from django.contrib import admin
from django.urls import path, include, re_path # `re_path` regular expression path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # local apps urls
    path('api/accounts/', include('accounts.urls')),
    path('api/employees/', include('employees.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/projects/', include('projects.urls')),

    path('admin/', admin.site.urls), # django admin site url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Django needs this url pattern for media (url & root)

""" 
At the end of all settings & changes, django will use the template build by React 
that is a frontend framework for single page applications creatioon.

The built project by React will be setted in a single folder called **build**

Then we just have to copy the **build** folder in our django project main root.

"""
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]