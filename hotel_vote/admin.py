from django.contrib import admin
from .models import Hotel,CustomUser,history_winner
# Register your models here.



@admin.register(CustomUser)
class hotel(admin.ModelAdmin):
    list_display = ['username','max_votes','id', 'username']

@admin.register(history_winner)
class history_winners(admin.ModelAdmin):
    list_display = ['winner',  'created']
    
import decimal, csv
from .models import Hotel
from django.http import HttpResponse

def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'address', 'votes'])
    books = queryset.values_list('name', 'address', 'votes')
    for book in books:
        writer.writerow(book)
    return response
export_books.short_description = 'Export to csv'   

@admin.register(Hotel)
class hotel(admin.ModelAdmin):
    list_display = ['id','name', 'address', 'votes']
    actions = ['apply_discount', export_books]