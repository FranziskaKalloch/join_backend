from django.db import models
from django.conf import settings


class Task(models.Model):
    class Priority(models.TextChoices):
        URGENT = "Urgent", "Urgent"
        MEDIUM = "Medium", "Medium",
        LOW = "Low", "Low"
        #     Datenbankwert, Anzeigewert | Zugriff: Task.Priority.URGENT
    
    class Category(models.TextChoices):
        TECHNICAL_TASK = "Technical Task", "Technical Task",
        USER_STORY = "User Story", "User Story"
    
    title = models.CharField(max_length=255, blank=False, null=False) 
    description = models.TextField()
    due_date = models.DateField(blank=False, null=False)
    priority = models.CharField(choices=Priority.choices, max_length=6)
    category = models.CharField(choices=Category.choices, blank=False, max_length=15)
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="assigned_tasks")
    # subtask = models.CharField(max_length=255) # wird nicht benötigt, da es im Subtask Model verbunden wurde
    
class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks") #Jeder subtask gehört genau zu einem Task. 
    title = models.CharField(max_length=255)
    
# Zugriff:
# task.subtasks.all() - Auf alle Subtasks eines Tasks zugreifen
# subtask.task        - Der Task eines Subtask

# Was bedeutet -> related_name="assigned_task" :  also vom Benutzer zu seinem Task!

# Das ist der Name für den Zugriff in die Gegenrichtung, also vom Benutzer zu seinem Tasks:
# - task.assigned_to.all()  -> Benutzer dieses Tasks
# - user.assigned_task.all() -> Tasks dieses Benutzers