from django.db import models


class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}

        if len(postData['course_name']) < 5:
            errors["course_name"] = "Course Name field should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Course Description field should be at least 15 characters"

        return errors

    def comment_validator(self, postData):
        errors = {}
        if len(postData['content']) < 15:
            errors["content"] = "A comment field should be at least 15 characters"
        if len(postData['commentator']) < 3:
            errors["commentator"] = "You must enter a name with at least 5 characters"

        return errors


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course, related_name="desc", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField()
    commentator = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)