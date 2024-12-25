from django.db import models

# Create your models here.
class questions(models.Model):
    QUESTION_CHOICES=(("Text","Text"),("BigText","BigText"),("Radio","Radio"),("Checkbox","Checkbox"))
    question=models.CharField(max_length=100)
    question_type=models.CharField(choices=QUESTION_CHOICES,max_length=50,default="Text")

    def __str__(self) -> str:
        return f"{self.question} {self.question_type}"

class Options(models.Model):
    question=models.ForeignKey(questions,related_name="options",on_delete=models.CASCADE)
    option_name=models.CharField(max_length=100)
    
    def __str__(self) ->str:
        return f"{self.option_name} {self.question.question}"
        
class CustomerFeddback(models.Model):
    question=models.ManyToManyField(questions)
    

class CustomerResponse(models.Model):
    feedback=models.ForeignKey(CustomerFeddback,on_delete=models.CASCADE)
    question=models.ForeignKey(questions,on_delete=models.CASCADE)
    response_text=models.TextField(null=True,blank=True)
    selected_options=models.ManyToManyField(Options,blank=True)
