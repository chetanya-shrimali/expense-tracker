# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from expense_app.models import Expense
from django.contrib import admin


# Registered Expense model
admin.site.register(Expense)
