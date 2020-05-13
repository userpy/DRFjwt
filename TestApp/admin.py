from django.contrib import admin

# Register your models here.


from TestApp.models import Test, Question, Answer, Results

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Results)
