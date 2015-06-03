from django.db import models

# Create your models here.


class Challenge(models.Model):
    # ideally following both should be in HTML, converted 
    # from markdown
    # or render the html at the run time
    challenge_text = models.TextField()
    solution = models.TextField()
    # data for API
    challenge_data = models.TextField()

    def __str__(self):
        return self.challenge_text[:10]
