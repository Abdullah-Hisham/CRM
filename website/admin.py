from django.contrib import admin
from .models import *
import mysql.connector
# Register your models here.
admin.site.register(Record)
connection = mysql.connector.connect(
        host='localhost',  # أو عنوان الخادم إذا كان آخر
        user='try',
        password='7*5*3*1*5*9',
        database='school'
    )
#admin.site.register(connection)