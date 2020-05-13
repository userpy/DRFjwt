from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.html import format_html
from django.core import serializers
from django.http import HttpResponse



class PermissionAdmin(admin.ModelAdmin):
    actions_selection_counter = True
    def colored_name(self, obj):
        if obj.content_type_id == 2:
            color = 'green'
        else:
            color = 'red'
        return format_html(
            '<span style="color: {};"> <b>{}</b> | {}</span>',
            color,
            obj.codename,
            obj.name,
        )

    def export_as_json(modeladmin, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response
    export_as_json.short_description = "Json"



    colored_name.short_description = 'info'
    fields = (('codename', 'name'), 'content_type')
    list_display = ('colored_name','codename', 'name')
    actions = [export_as_json]



admin.site.register(Permission, PermissionAdmin)