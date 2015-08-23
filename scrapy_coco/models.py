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
    api_data = models.TextField(blank=True)
    # type of api_data, either json or not
    is_api_data_json = models.BooleanField()
    # does challenge data require processing or can be
    # rendered directly? If it former, mention the handler name
    # or leave it empty.
    handler = models.CharField(max_length=60, blank=True)
    challenge_id = models.IntegerField()

    def __str__(self):
        return self.challenge_title

    def save(self):
        self.challenge_id = Challenge.objects.count()
        super(Challenge, self).save()
