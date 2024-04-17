"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static # static()는 정적 파일을 처리하기 위해 그에 맞는 URL 패턴을 반환하는 함수
from django.conf import settings # settings 변수를 임포트, settings.py 모듈에서 정의한 항목들을 담고있는 객체를 가리키는 reference

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 기존 URL 패턴에 static() 함수가 반환하는 URL 패턴을 추가한다. 
