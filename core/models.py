from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Definition """

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True  # Database로 가지 않게 하기 위한 절차
