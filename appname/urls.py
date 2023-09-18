from django.contrib import admin
from django.urls import path, include
from appname.views import home, login, signup ,add_todo ,signout,delete_todo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login),
    path('signup/', signup),
    path('add-todo/', add_todo),
    path('delete-todo/<int:id>', delete_todo),
    path('logout/', signout),
    path('', include('django.contrib.auth.urls')), 
]

