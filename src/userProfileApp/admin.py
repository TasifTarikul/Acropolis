from django.contrib import admin
from .models import AcropolisModel,VisaModel, SarawakModel
from coreApp.models import User
# Register your models here.

admin.site.register(AcropolisModel)
admin.site.register(SarawakModel)
admin.site.register(VisaModel)
admin.site.register(User)
