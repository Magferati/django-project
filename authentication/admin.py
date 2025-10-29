from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)
# @admin.register(B)
# class BookAdmin(admin.ModelAdmin):
#     resource_class = BookResource
#     fieldsets = (
#         ("general", {"fields": ("title", "author", "library")}),
#         ("other", {"fields": ("genre", "summary", "isbn", "published_on")}),
#     )
#     list_filter = ("title",)

#     # Render filtered options only after 5 characters were entered
#     filter_input_length = {
#         "title": 5,
#     }