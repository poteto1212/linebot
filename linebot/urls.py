
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('line_bot_ai.urls')),
    path('admin/', admin.site.urls),
]
