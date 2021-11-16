from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
from datetime import datetime
from main.models import Tutorial

# Register your models here.

fieldsets = [
        ("Title/date",{'field': ["tutorial_title","tutorial_published"]}),
        ("content",{"fields": ["Tutorial_contents"]})
]

formfield_overrides = {
    models.TextField: {'widgets': TinyMCE()},
}

admin.site.register(Tutorial)