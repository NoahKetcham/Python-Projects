from django.db import models


# Create your models here.

class CampusName(models.Model):
    # creates parameters for variables in the class to be edited on the admin site
    name = models.CharField(max_length=60, default="", blank=True, null=False)  # string values
    state = models.CharField(max_length=60, default="", blank=True, null=False)   # string values
    campus_id = models.IntegerField(default="", blank=True, null=False)   # Integer values

    # Creates the model manager
    object = models.Manager()

    # Displays object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.name}: {0.campus_id}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
