from django.contrib import admin

class RubroAdmin(admin.ModelAdmin):
    pass

class ProductoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rubro)
admin.site.register(Producto)
