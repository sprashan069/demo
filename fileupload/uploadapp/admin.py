from django.contrib import admin
from .models import File
from django.utils.safestring import mark_safe
class file_data(admin.ModelAdmin):
    list_display = ('name', 'image')
    def image(self,instance):
        # return mark_safe('<img src="{ MEDIA_URL }/%s" width="50" height="50"  />' % (instance.profile_image))
        return mark_safe('<img src="/media/%s" width="50" height="50"  />' % (instance.file))
admin.site.register(File, file_data)