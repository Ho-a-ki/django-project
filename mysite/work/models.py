from django.db import models
from django.utils import timezone


# Work(출석)
# -------
# person(출근자)
# created_time(생성일)
# on(출근)
# off(퇴근)
# work_time(일한시간)

class Work(models.Model):
    person = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.person
