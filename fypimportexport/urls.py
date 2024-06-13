"""
URL configuration for fypimportexport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from fyp.views import Home, Login, Signup, SingleProduct, AboutUs, Logout, ContactUs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('user-login/', Login.as_view(), name='login'),
    path('user-signup/', Signup.as_view(), name='signup'),
    path('product/<int:obj_id>/', SingleProduct.as_view(), name='singleproduct'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
    path('user-logout/', Logout.as_view(), name='logout'),
    path('contact-us/', ContactUs.as_view(), name='contact-us'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
