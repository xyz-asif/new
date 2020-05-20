from django.urls import path
from . import views
app_name = 'child'

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/",views.sem, name="sem"),
    path("semester/",views.sem , name="sem"),
    path("subject/<int:pk>/",views.sub,name="sub"),
    path("lecture/<int:pk>/",views.lecture,name="lecture"),
    path("course/<int:pk>/video/",views.video,name="video"),
    path("course/<int:pk>/pdf/",views.course_pdf,name="pdf"),
    path("course/<int:pk>/quest/",views.quest,name="quest"),
]
