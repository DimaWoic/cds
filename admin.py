from django.contrib import admin
from .models import Transport, Graphic, Company, CompanyUnit, Sex, Position, Worker
from .models import Depot, Route, RollingStock


admin.site.register(Transport)
admin.site.register(Graphic)
admin.site.register(Company)
admin.site.register(CompanyUnit)
admin.site.register(Sex)
admin.site.register(Position)
admin.site.register(Worker)
admin.site.register(Depot)
admin.site.register(Route)
admin.site.register(RollingStock)
