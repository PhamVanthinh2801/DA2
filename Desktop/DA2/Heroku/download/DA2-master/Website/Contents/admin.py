from django.contrib import admin
from .models import Product,InfomationUsers,Order,Myorder,Payment,ChooseSizeColor,Address,Comment



class comment(admin.StackedInline): 
    model=Comment


class PostAdmin_Product(admin.ModelAdmin):
    list_display =['Name','description','price','date']
    list_filter=['date']
    search_fields=['Name']
    inlines=[comment]
    
admin.site.register(Product,PostAdmin_Product)
admin.site.register(InfomationUsers)
admin.site.register(Order)
admin.site.register(Myorder)
admin.site.register(Payment)
admin.site.register(ChooseSizeColor)
admin.site.register(Address)