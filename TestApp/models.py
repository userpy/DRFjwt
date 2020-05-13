from django.db import models
# Create your models here.

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    def __str__(self):
        return '-%s' % (self.test_name)

class Question(models.Model):
    test     = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    multiple_choice = models.BooleanField(choices=[(False, 'No'), (True, "Yes")],default=False)
    def __str__(self):
        return '%s: %s' % (self.test, self.question)

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer   = models.CharField(max_length=100)
    сorrect_answer = models.BooleanField(choices=[(False, 'No'), (True, "Yes")], default=False)
    def __str__(self):
        return '%s |%s' % (self.question, self.answer)

class Results(models.Model):
    username= models.CharField(max_length=100)
    testname = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    def __str__(self):
        return "%s | %s | %s" % (self.username, self.testname, self.result)








