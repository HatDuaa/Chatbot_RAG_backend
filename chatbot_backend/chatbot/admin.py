from django.contrib import admin
from .models import *
from .prepare_vector_db_api import create_vector_db

import os

# Register your models here.
admin.site.register(api_key)


@admin.action(description='Embed data')
def my_custom_action(modeladmin, request, queryset):
    for obj in queryset:
        if obj.document:
            # Lấy đường dẫn thực tế của tệp
            file_path = obj.document.path
            print(f"Địa chỉ tệp: {file_path}")
            # Tạo đường dẫn lưu trữ vector DB trong thư mục app chatbot
            app_dir = os.path.dirname(os.path.abspath(__file__))
            vector_db_dir = os.path.join(app_dir, 'vectorstores', 'db_faiss_openai')
            os.makedirs(vector_db_dir, exist_ok=True)
            vector_db_path = os.path.join(vector_db_dir, f"{obj.name}")

            # Tạo vector DB
            create_vector_db(file_path, vector_db_path) 
        else:
            print(f"Đối tượng {obj.name} không có tệp đính kèm.")

    modeladmin.message_user(request, "Embedding finished.")

class DocumentlAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    readonly_fields = ('created_at',)
    actions = [my_custom_action]

admin.site.register(Document, DocumentlAdmin)