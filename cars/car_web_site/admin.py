from django.contrib import admin
from .models import Car, NewUser
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class CarAdminForm(forms.ModelForm):
    owner_comments = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Car
        fields = '__all__'


class CarModelInline(admin.TabularInline):
    """display of the car at its owner"""
    model = Car
    extra = 0

    # readonly_fields = ("get_photo",)

    def get_photo(self, obj):
        """get photo by url"""
        return mark_safe(f'<img src={obj.photo.url} width="120" height="80"')

    get_photo.short_description = "Фотография"


def make_unpublished(modeladmin, request, queryset):
    """function to unpublish"""
    queryset.update(is_published=False)


make_unpublished.short_description = "Отменить публикацию"


class CarResources(resources.ModelResource):
    owner = fields.Field(column_name='owner', attribute='owner', widget=ForeignKeyWidget(NewUser, 'username'))
    class Meta:
        model = Car


@admin.register(Car)
class CarAdmin(ImportExportActionModelAdmin):
    resource_class = CarResources
    list_display = (
        "id", "car_brand", "car_model", "car_price", "country", "time_create", "is_published", "owner")
    list_display_links = ("id",)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'country', "car_brand")
    prepopulated_fields = {"slug": ("car_brand", "car_model")}
    search_fields = ("car_brand", "country")
    readonly_fields = ("time_create",)
    actions = [make_unpublished]
    form = CarAdminForm

    # def get_photo(self, obj):
    #     return mark_safe(f'<img src={obj.photo.url} width="100" height="60"')

    # get_photo.short_description = "Фотография"

    fieldsets = (
        ("Страна", {
            "fields": (("country",),)
        }),
        ("Автомобиль", {
            "fields": (("car_brand", "car_model"),)
        }),
        (None, {
            "fields": (("car_status",),)
        }),
        (None, {
            "fields": (("car_generation", "car_year_of_issue"),)
        }),
        (None, {
            "fields": (("car_color",),)
        }),
        (None, {
            "fields": (("car_mileage", "car_engine"),)
        }),
        (None, {
            "fields": (("car_complectation", "car_drive_unit", "car_steering_wheel"),)
        }),
        (None, {
            "fields": (("car_condition",),)
        }),
        (None, {
            "fields": (("car_owners",),)
        }),
        (None, {
            "fields": (("slug",),)
        }),
        (None, {
            "fields": (("owner_comments",),)
        }),
        # (None, {
        #     "fields": (("photo", "get_photo"),)
        # }),
        ("Цена", {
            "fields": (("car_price",),)
        }),
        ("Владелец", {
            "fields": (("owner",),)
        }),
        ("Публикация", {
            "fields": (("is_published", "time_create"),)
        }),

    )


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'gender', 'birthday')
    inlines = [CarModelInline]
    save_on_top = True
    fieldsets = (
        ("ФИО", {
            "fields": (("first_name", "last_name"),)
        }),
        (None, {
            "fields": (("gender",),)
        }),
        (None, {
            "fields": (("birthday", "user_telephone"),)
        }),
        (None, {
            "fields": (("username",),)
        }),
        (None, {
            "fields": (("profile_pic",),)
        }),
        (None, {
            "fields": (("email", "password"),)
        }),

        (None, {
            "fields": (("is_superuser", "is_staff", "is_active"),)
        }),
        ("Группы", {
            "classes": ("collapse",),
            "fields": (("groups",),)
        }),
        ("Права пользователя", {
            "classes": ("collapse",),
            "fields": (("user_permissions",),)
        }),
        ("Дата регистрации", {
            "classes": ("collapse",),
            "fields": (("date_joined",),)
        }),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


from django.contrib import admin

# Register your models here.
