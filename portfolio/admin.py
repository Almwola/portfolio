from django.contrib import admin

from .models import Certification, ContactMessage, Project, Skill, SkillCategory


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    inlines = [SkillInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "is_featured", "order")
    list_editable = ("is_featured", "order")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "issued_on", "order")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "created_at")
    readonly_fields = ("name", "email", "subject", "message", "created_at")

    def has_add_permission(self, request):
        return False
