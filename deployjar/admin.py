from django.contrib import admin
from .models import *
# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ('name','ip','version','config','position','created_at')
class HostUserAdmin(admin.ModelAdmin):
    list_display = ('name','password','created_at')
class JarappAdmin(admin.ModelAdmin):
    list_display = ('name','port','jar_dir','created_at')
class ScriptsAdmin(admin.ModelAdmin):
    list_display = ('name','script_dir')

admin.site.register(Host,HostAdmin)
admin.site.register(HostUser,HostUserAdmin)
admin.site.register(Script,ScriptsAdmin)
admin.site.register(Instance)
admin.site.register(JarModel)
admin.site.register(Domain)
admin.site.register(MySQLInstance)
admin.site.register(MySQLDB)
admin.site.register(Task)
admin.site.register(HostType)
admin.site.register(HostEnv)
admin.site.register(ConfigFile)
admin.site.register(TaskType)
admin.site.register(NginxHostName)
admin.site.register(NginxInstance)
admin.site.register(NginxVhost)
admin.site.register(MongoDBCluster)
admin.site.register(MongoDBInstance)
admin.site.register(MongoDBDatabase)
admin.site.register(RedisCluster)
admin.site.register(RedisInstance)
admin.site.register(KafkaCluster)
admin.site.register(KafkaInstance)
admin.site.register(ZookeeperCluster)
admin.site.register(ZookeeperInstance)