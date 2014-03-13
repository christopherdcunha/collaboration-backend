from django.db.models.signals import post_save
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)


class Job(models.Model):
    name = models.CharField(max_length=30)


def publish(sender, **kwargs):
    obj = kwargs['instance']
    print 'the object is now saved.  %s' % obj

post_save.connect(publish, sender=Project)
post_save.connect(publish, sender=Job)
