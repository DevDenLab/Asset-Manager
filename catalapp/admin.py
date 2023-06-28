from django.contrib import admin

# Register your models here.
from .models import Software, Plugin, Tag, Review,Subscription,Payment

admin.site.register(Software)
admin.site.register(Plugin)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Subscription)
admin.site.register(Payment)
