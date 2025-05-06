from django.contrib import admin
from .models import Order, User

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    readonly_fields = []  # Уберите 'created_at' из readonly_fields если он там был
    fields = ['name', 'user', 'telegram', 'deadline', 'description', 'media', 'status', 'created_at']
    
    def get_readonly_fields(self, request, obj=None):
        # Делаем поля редактируемыми для админа
        if request.user.is_superuser:
            return []
        return ['created_at']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'telegram_username']
    search_fields = ['username', 'email', 'telegram_username']
