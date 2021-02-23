from django.contrib.contenttypes import checks
from django.db import models
import re
# Create your models here.
from django.db.models.constants import LOOKUP_SEP

example = 'EU/CS/CSC/19/000'


class DataForm(models.Model):
    name = models.CharField(max_length=100, default=None)
    reg_no = models.CharField(max_length=20, default=example)
    prev_allocation = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Registration(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=254, null=False, default=None)
    phone = models.IntegerField( default=+234, db_tablespace=1)
    username = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length=200, null=False, default=None)
    confirm = models.CharField(max_length=200, null=False, default=None)

class Question(models.Model):
    text= models.CharField(max_length=100, default=None)

class Answer(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    # class Meta:
    #     class Person(models.Model):class

    # def _check_model_name_db_lookup_clashes(cls):
    #  
    #     model_name = cls.username.__name__
    #     if model_name.startswith('_') or model_name.endswith('_'):
    #         errors.append(
    #             checks.Error(
    #                 "The model name '%s' cannot start or end with an underscore "
    #                 "as it collides with the query lookup syntax." % model_name,
    #                 obj=cls,
    #                 id='models.E023'
    #             )
    #         )
    #     elif LOOKUP_SEP in model_name:
    #         errors.append(
    #             checks.Error(
    #                 "The model name '%s' cannot contain double underscores as "
    #                 "it collides with the query lookup syntax." % model_name,
    #                 obj=cls,
    #                 id='models.E024'
    #             )
    #         )
    #     return errors
