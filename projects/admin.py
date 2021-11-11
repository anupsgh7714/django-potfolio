from django.contrib import admin
from projects.models import Projects

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_title','project_desc','project_img','project_link','project_title_slug')

admin.site.register(Projects,ProjectsAdmin)
