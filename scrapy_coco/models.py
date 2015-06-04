from django.db import models

# Create your models here.


class Challenge(models.Model):
    challenge_title = models.CharField(max_length=120)
    challenge_text = models.TextField()
    solution = models.TextField()
    # data for API
    # usually in JSON
    # some challenges need data to be generated on the fly
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#blank
    # avoid using null on textfields ...
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#null
    challenge_data = models.TextField(blank=True)
    # type of challenge_data
    is_challenge_data_json = models.BooleanField()
    # does challenge data require processing or can be
    # rendered directly?
    does_require_processing = models.BooleanField()

    def __str__(self):
        return self.challenge_title

    # override save() here and make json validation
    # for challenge_data
