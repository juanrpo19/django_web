from django.conf.urls import url
from apps.mascota.views import listadousuario, index, mascota_delete,  mascota_list, mascota_view, mascota_edit
from apps.mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar$',login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listado', listadousuario, name='listado'),
]