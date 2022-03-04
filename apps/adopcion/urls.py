from django.conf.urls import url
from apps.adopcion.views import index_adopcion
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index$', login_required(index_adopcion))
]