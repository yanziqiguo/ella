from django.contrib import admin

from ella.newman import models as m

class DevMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'version', 'ts',)
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user
        obj.save()


class HelpItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    list_filter = ('ct',)

admin.site.register(m.DevMessage, DevMessageAdmin)
admin.site.register(m.AdminHelpItem, HelpItemAdmin)
