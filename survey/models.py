from django.db import models

class QUESTIONS(models.Model):
    questionText = models.CharField(max_length=350)
    bDisplay = models.BooleanField()
    
    def __unicode__(self):
        return u'%s ' % (self.questionText)

class ANSWERS(models.Model):
    answerText = models.CharField(max_length=350)
    question = models.ForeignKey(QUESTIONS)
    
    def __unicode__(self):
        return u'%s ' % (self.answerText)

    
class RESULTS(models.Model):
    resultText = models.CharField(max_length=350)
    
    def __unicode__(self):
        return u'%s ' % (self.resultText)
    
class WEIGHT(models.Model):
    answer = models.ForeignKey(ANSWERS)
    result = models.ForeignKey(RESULTS)
    weight = models.IntegerField()
    
    def __unicode__(self):
        return u'%s, %s, %s' % (self.result, self.answer, self.weight)
