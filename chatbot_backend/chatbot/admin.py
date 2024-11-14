from django.contrib import admin
from .models import *
from .prepare_vector_db_api import create_vector_db

# Register your models here.
admin.site.register(api_key)


@admin.action(description='Embed data')
def my_custom_action(modeladmin, request, queryset):
    for obj in queryset:
        print(f"Đang xử lý đối tượng {obj.name}")

        # Kiểm tra nếu đối tượng có tệp gắn kèm
        if obj.document:
            # Lấy đường dẫn thực tế của tệp
            file_path = obj.document.path
            print(f"Địa chỉ tệp: {file_path}")
            # Giả sử bạn muốn làm gì đó với tệp, như tạo vector DB
            create_vector_db(file_path)  # Hoặc bạn có thể truyền obj.document để xử lý

        else:
            print(f"Đối tượng {obj.name} không có tệp đính kèm.")

    modeladmin.message_user(request, "Công việc đã được thực hiện.")

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    actions = [my_custom_action]

admin.site.register(Document, MyModelAdmin)