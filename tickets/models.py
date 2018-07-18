from django.db import models
from django.core.validators import RegexValidator

email = RegexValidator(r"[a-z]+@[a-z]{2}(.iitr.ac.in)", "Enter gsuite email")


class Ticket(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('pub_date',)


