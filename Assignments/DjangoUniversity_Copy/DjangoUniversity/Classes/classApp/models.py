from django.db import models


# Create your models here.
class UniversityClasses(models.Model):
    # creates parameters for variables in the class to be edited on the admin site
    title = models.CharField(max_length=60, default="", blank=True, null=False)  # string values
    course_number = models.IntegerField(default="", blank=True, null=False)   # Integer values
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)  # string values
    duration = models.FloatField(null=True, blank=True, default=None)   # Float values

    # Creates the model manager
    object = models.Manager()

    # Displays object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"
