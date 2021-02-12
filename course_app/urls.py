from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new_course', views.new_course),
    path('courses/destroy/<course_id>', views.render_destroy),
    path('courses/destroy/<course_id>/remove', views.remove),
    path('courses/comments/<course_id>', views.render_comments),
    path('courses/comments/<course_id>/new_comment', views.new_comment),

]