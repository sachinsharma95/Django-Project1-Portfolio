"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


# by this you will change the header of ad,intsration to hello or anything else

admin.site.site_header = "  Personal Admin System"
admin.site.site_title = " boot Admin Portal"
admin.site.index_title = "Welcome Er. SACHIN SHARMA"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('personal.urls'))

    # path('personal/',include('personal.urls')) by this personal is also added  in the website domain
]
