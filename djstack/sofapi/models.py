from django.db import models

# Create your models here.

class questions(models.Model):
    questions = models.CharField(max_length=300)
    vote_count = models.IntegerField(default=0)
    views = models.CharField(max_length=50)

    #return the name of question in admin after saving
    def __str__(self):
        return self.questions