from django.db import models
from softdelete.models import SoftDeleteObject
from softdelete.admin import SoftDeleteObjectAdmin
from django.contrib import admin

class TestModelOne(SoftDeleteObject):
    extra_bool = models.BooleanField(default=False)

    def __unicode__(self):
        return u"TestModelOne - extra_bool: %s" % self.extra_bool
    
class TestModelTwo(SoftDeleteObject):
    extra_int = models.IntegerField()
    tmo = models.ForeignKey(TestModelOne,related_name='tmos')
    
    def __unicode__(self):
        return u"TestModelTwo - extra_int: %s, tmo: %s" % (self.extra_int,
                                                           self.tmo)

class TestModelThree(SoftDeleteObject):
    tmos = models.ManyToManyField(TestModelOne, through='TestModelThrough')

    def __unicode__(self):
        return u"TestModelThree -- %d" % self.pk

class TestModelThrough(SoftDeleteObject):
    tmo1 = models.ForeignKey(TestModelOne, related_name="left_side")
    tmo3 = models.ForeignKey(TestModelThree, related_name='right_side')


admin.site.register(TestModelOne, SoftDeleteObjectAdmin)
admin.site.register(TestModelTwo, SoftDeleteObjectAdmin)
admin.site.register(TestModelThree, SoftDeleteObjectAdmin)
admin.site.register(TestModelThrough, SoftDeleteObjectAdmin)

