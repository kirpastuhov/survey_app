from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()

    def __str__(self):
        return self.description


class Question(models.Model):
    TYPE_TEXT = 'TEXT'
    TYPE_SINGLE_ANS = 'SINGLE'
    TYPE_SEVERAL_ANS = 'SEVERAL'
    QUESTION_TYPES = ((TYPE_TEXT, 'Text'), (TYPE_SINGLE_ANS, 'Single'), (TYPE_SEVERAL_ANS, 'Several'))

    text = models.TextField()
    type = models.CharField(choices=QUESTION_TYPES, default=TYPE_TEXT, max_length=24)
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return f"Survey '{self.survey.title}' | Question '{self.text}'"


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='ans', on_delete=models.CASCADE)
    answer = models.TextField()
    user_id = models.IntegerField()

    def __str__(self):
        return f"Answer '{self.answer}' by user '{self.user_id}' for {self.question}"

    class Meta:
        unique_together = ("question", "user_id")
