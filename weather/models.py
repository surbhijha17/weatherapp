from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
       self.name=self.name.upper()
       return self.name


    class Meta:
        verbose_name_plural = 'cities'

   	#def save(self,force_insert=False,force_update=False):
     #   self.name = self.name.upper()
      #  super(City,self).save(force_insert, force_update)