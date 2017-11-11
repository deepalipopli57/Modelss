# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blog.models import Post, Author, Entry, Student, Car, Manufacturer, AbstractCar

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Student)
admin.site.register(Manufacturer)
admin.site.register(Car)