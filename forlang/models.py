from django.db import models

class DictEntry(models.Model):
    english = models.CharField(max_length=63)
    foreign = models.CharField(max_length=127)
    example = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.english, self.foreign)
