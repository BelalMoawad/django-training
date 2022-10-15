from django.db import models

class Artist(models.Model) :
    stage_name = models.CharField(max_length=50, unique = True, blank = True)
    social_link = models.URLField(max_length = 100, null = False)


    def __str__(self) :
        return self.stage_name

    class Meta:
        ordering = ['stage_name']

    