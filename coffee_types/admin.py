# Third-party imports
from django.contrib import admin

# local imports
from .models import Coffee


class CoffeeListingAdmin(admin.ModelAdmin):
    using = "listings"  # name of the db
    list_display = (
        'id',
        'title',
        'store_manager_email',
        'price',
        'coffee_type',
    )
    list_display_links = (
        'id',
        'title',
        'store_manager_email',
        'price',
        'coffee_type',
    )
    list_filter = ('store_manager_email', )
    search_fields = ('title', 'store_manager_email',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        # Save objects to the 'listings' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Delete objects from the 'listings' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Look for objects on the 'listings' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Populate ForeignKey widgets using a query
        # on the 'listings' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Populate ManyToMany widgets using a query on the 'listings' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


# Finally, register with the admin
admin.site.register(Coffee, CoffeeListingAdmin)
