from django.contrib import admin
from attendence.models import App_Custom_User,Venue,Miqaat,Miqaat_Registration

# Register your models here.
admin.site.register(App_Custom_User)
admin.site.register(Venue)
admin.site.register(Miqaat)
admin.site.register(Miqaat_Registration)


