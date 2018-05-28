# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Neighborhood, Business, Post, UserProfile


# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(UserProfile)
