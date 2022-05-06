from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/', details),
    path('create/', create),
    path('update/<int:id>/', update),
    path('pupdate/<int:id>/', pupdate),
    path('delete/<int:id>/', delete)

]