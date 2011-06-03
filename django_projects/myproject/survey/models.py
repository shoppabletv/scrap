from django.db import models

class Survey(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.name
	def was_publiched_today(self):
		return self.pub_date.date() == datetime.date.today()

class Question(models.Model):
	survey = models.ForeignKey(Survey)	
	question = models.CharField(max_length=200)
	def __unicode(self):
		return self.question
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice
