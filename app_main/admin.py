from django.contrib import admin

from .models import Item
from .models import FIO
from .models import Image


admin.site.register(Item)
admin.site.register(FIO)
admin.site.register(Image)
