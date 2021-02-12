from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description, Comment


def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, "index.html", context)


def new_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/")

    else:
        add_course = Course.objects.create(course_name=request.POST['course_name'])
        Description.objects.create(desc=request.POST['desc'], course=add_course)
        return redirect("/")


def render_destroy(request, course_id):
    this_course = Course.objects.get(id=course_id)
    context = {
        "course":this_course
    }
    return render(request, "destroy.html", context)


def remove(request, course_id):
    this_course = Course.objects.get(id=course_id)
    this_course.delete()
    return redirect("/")


def render_comments(request, course_id):
    this_course = Course.objects.get(id=course_id)
    context = {
        "course":this_course
    }
    return render(request, "comments.html", context)


def new_comment(request, course_id):
    errors = Course.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f"/courses/comments/{course_id}")
    else:
        this_course = Course.objects.get(id=course_id)
        Comment.objects.create(content=request.POST['content'], commentator=request.POST['commentator'],course=this_course)
        return redirect(f"/courses/comments/{course_id}")