from django.contrib import admin
from .models import AcropolisModel,VisaModel, SarawakModel, BirthCertificateFile, MarriageCertificateFile, PassportCopyFile, BankStatementFile
from coreApp.models import User
# Register your models here.

admin.site.register(AcropolisModel)
admin.site.register(SarawakModel)
admin.site.register(VisaModel)
admin.site.register(User)
admin.site.register(BirthCertificateFile)
admin.site.register(MarriageCertificateFile)
admin.site.register(PassportCopyFile)
admin.site.register(BankStatementFile)
