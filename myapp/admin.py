from django.contrib import admin
from .models import Person

# class personmodelAdmin(admin.ModelAdmin):
    # list_display =["Updated", "Timestamp"]
    # class Meta:
    #     model=person


admin.site.register(Person) #personmodelAdmin
