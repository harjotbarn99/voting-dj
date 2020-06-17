from django.db import models
from  django.urls import reverse
# Create your models here.

class VoteCode(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + " - " + self.code

    # def get_absolute_url(self):
    #     return reverse('candidateDetail-getSeededTeam',kwargs={"pk":self.id})
