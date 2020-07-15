from django.contrib import admin
from api.models import Agent, Group, User, GroupUser, Event
from api.forms import UserAdmin


admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(User, UserAdmin)
admin.site.register(GroupUser)
admin.site.register(Event)
