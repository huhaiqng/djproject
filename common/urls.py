from django.urls import path
from .views import *

app_name = 'common'
urlpatterns = [
    path('checkbackup/',checkbackup,name='checkbackup'),
    path('execcheck/',execcheck,name='execcheck'),
    path('instance/<cmd>/<instance_id>/',instance,name='instance'),
    path('domain/',domain,name='domain'),
    path('model/',model,name='model'),
    path('project/',project,name='project'),
    path('<int:p_id>/project_detail/',project_detail,name='project_detail'),
    path('model_detail/',model_detail,name='model_detail'),
    path('mysqldb/',mysqldb,name='mysqldb'),
    path('upload-files/',UploadFilesView.as_view(), name='upload_files'),
    path('remove_file/<int:f_id>/',remove_file,name='remove_file'),
    path('update_files/',update_files,name='update_files'),
    path('tasks/',tasks,name='tasks'),
    path('exec_tasks/',exec_tasks,name='run_tasks'),
    path('config_file/',config_file,name='config_file'),
    path('open_file/',open_file,name='open_file'),
    path('save_file/',save_file,name='save_file'),
    path('del_file/',del_file,name='del_file'),
    path('task_script/',task_script,name='task_script'),
    path('open_script_file/',open_script_file,name='open_script_file'),
    path('save_script_file/',save_script_file,name='save_script_file'),
    path('del_script_file/',del_script_file,name='del_script_file'),
    path('host/<cmd>/<host_id>/',host,name='change_host'),
    path('host/search/',search_host,name='search_host'),
    path('nginx_vhost/',nginx_vhost,name='nginx_vhost'),
    path('mongodb/',mongodb,name='mongodb'),
    path('redis/',redis,name='redis'),
    path('kafka/',kafka,name='kafka'),
    path('zookeeper/',zookeeper,name='zookeeper')
]