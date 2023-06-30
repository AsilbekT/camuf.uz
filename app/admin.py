from django.contrib import admin
from . models import *

# Register your models here.
class ArticleCatagoryAdmin(admin.ModelAdmin):
    list_display = ['catagory_name', 'slug']
    list_filter = ['catagory_name']
    search_fields = ['catagory_name']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'date_created',  'get_related_field']

    def get_related_field(self, obj):
        return obj.article_catagory
    get_related_field.short_description = 'Related Field' 


admin.site.register(NewsCatagory)
admin.site.register(New)

admin.site.register(ArticleCatagory, ArticleCatagoryAdmin)
admin.site.register(Article, ArticleAdmin)


admin.site.register(Status)
admin.site.register(Workers)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Journal)
admin.site.register(JournalPicture)
admin.site.register(UndergraduateCourse)
admin.site.register(GraduateCourse)
admin.site.register(Leaders)
admin.site.register(InterestedPeople)
admin.site.register(UniPhone)
admin.site.register(EmailAddress)
admin.site.register(AppliedStudents)
admin.site.register(UniversityGallery)
