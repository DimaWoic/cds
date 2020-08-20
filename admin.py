from django.contrib import admin
from .models import Transport, Graphic, Company, CompanyUnit, Sex, Position, Worker
from .models import RollingStockFormOne, RollingStockFormTwo, RollingStockFormThree


admin.site.register(Transport)
admin.site.register(Graphic)
admin.site.register(Company)
admin.site.register(CompanyUnit)
admin.site.register(Sex)
admin.site.register(Position)
admin.site.register(Worker)
admin.site.register(RollingStockFormOne)
admin.site.register(RollingStockFormTwo)
admin.site.register(RollingStockFormThree)