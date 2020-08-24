from django.contrib import admin
from .models import OpenUrls


admin.site.site_header = "Url Shortener"
admin.site.site_title = "Url Shortener"
admin.site.site_url = "https://127.0.0.1/"
admin.site.index_title = "Url Shortener"


@admin.register(OpenUrls)
class ViewerOpenUrls(admin.ModelAdmin):
    list_display = ["origin_url", "shorted_url", "created_date"]
    search_fields = ["original_url"]
    list_filter = ["created_date"]
