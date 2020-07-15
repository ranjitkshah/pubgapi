from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(AR)
class ARadmin(ImportExportModelAdmin):
    pass

@admin.register(smg)
class smgadmin(ImportExportModelAdmin):
    pass

@admin.register(lmg)
class lmgadmin(ImportExportModelAdmin):
    pass

@admin.register(sniper)
class sniperadmin(ImportExportModelAdmin):
    pass


@admin.register(dmr)
class ARadmin(ImportExportModelAdmin):
    pass


@admin.register(shotgun)
class shotgunadmin(ImportExportModelAdmin):
    pass

@admin.register(pistol)
class pistoladmin(ImportExportModelAdmin):
    pass

@admin.register(other)
class otheradmin(ImportExportModelAdmin):
    pass

@admin.register(grip)
class gripadmin(ImportExportModelAdmin):
    pass

@admin.register(health)
class healthadmin(ImportExportModelAdmin):
    pass

@admin.register(Contact)
class Contactadmin(ImportExportModelAdmin):
    pass



# Register your models here.
