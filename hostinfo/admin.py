from django.contrib import admin
from .models import Host,HostIp
class HostAdmin(admin.ModelAdmin):
	list_display=('name','ip','kn','release','mem','disk',)
class HostIpAdmin(admin.ModelAdmin):
	list_display=('addr',)

admin.site.register(Host,HostAdmin)
admin.site.register(HostIp,HostIpAdmin)
