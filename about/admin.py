'''
Administration Panel
'''
# pylint: disable=too-few-public-methods

from django.contrib import admin

# Register your models here.

from .models import (
    ProgrammingLanguage,
    NaturalLanguage,
    Tag,
    Occupation,
    JobTable,
    ExternalWebsite,
    Developer
)


def inline(db_model, inline_type=admin.StackedInline, num_init_items=1):
    '''
    Generates tabular inline model
    '''
    class AdminModel(inline_type):
        '''
        Tabular Admin Model Class declaration
        '''
        model = db_model
        extra = num_init_items
    return AdminModel


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    '''
    Admin console for developers
    '''
    fieldsets = [
        (
            "Basic Information", {
                "fields": [
                    "first_name",
                    "last_name",
                    "email"
                ]
            }
        ),
        (
            "Xero integrations", {
                "fields": [
                    "xero_key",
                    "xero_secret"
                ]
            }
        )
    ]
    list_display = ("first_name", "last_name", "email")
    inlines = [
        inline(Tag, admin.TabularInline),
        inline(ProgrammingLanguage, admin.TabularInline),
        inline(NaturalLanguage, admin.TabularInline),
        inline(Occupation),
        inline(JobTable, admin.TabularInline),
        inline(ExternalWebsite, admin.TabularInline)
    ]
