# Third-party imports
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    using = 'users'
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name', 'email',)
    search_fields = ('name', 'email',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        # Save objects to the 'users' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Delete objects from the 'users' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Look for objects on the 'users' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Populate ForeignKey widgets using a query
        # on the 'users' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Populate ManyToMany widgets using a query
        # on the 'users' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


# Finally, register with the admin
admin.site.register(User, UserAdmin)
