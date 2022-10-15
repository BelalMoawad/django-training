from django.db import models

class Artist(models.Model) :
    stage_name = models.CharField(max_length=50)
    social_link_field = models.URLField(max_length = 200)


    def __str__(self) :
        return self.stage_name

    # class Meta:
        # ordering = ['stage_name']

    