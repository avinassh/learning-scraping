from django.db import models

# Create your models here.


class Challenge(models.Model):
    # ideally following both should be in HTML, converted 
    # from markdown
    # or render the html at the run time
    challenge_text = models.TextField()
    solution = models.TextField()
    # data for API
    # usually in JSON
    # some challenges need data to be generated on the fly
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#blank
    # avoid using null on textfields ...
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#null
    challenge_data = models.TextField(blank=True)

    def __str__(self):
        return self.challenge_text[:10]

    # override save() here and make json validation
    # for challenge_data