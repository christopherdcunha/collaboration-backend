from django.db import models
import simple_audit


class Project(models.Model):
    name = models.CharField(max_length=30)


class Job(models.Model):
    name = models.CharField(max_length=30)

simple_audit.register(Project, Job)
