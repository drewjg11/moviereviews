from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .modes import malfunction_choices, location_choices


class Item(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    purpose = models.CharField(max_length=300, null=False)
    item_overview = models.TextField
    created = models.DateTimeField(auto_now_add=True)
    # update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Function(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    func_name = models.CharField(max_length=50, null=False)
    func_description = models.CharField(max_length=250, null=False)
    hara_function = models.BooleanField(default=True)
    hara_rationale = models.CharField(max_length=250, null=True, default="Enter rationale")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='function')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.func_name


class Scenarios(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE, related_name='scenarios')
    location = models.CharField(max_length=75, null=False, choices=location_choices)


# class Malfunction(models.Model):
#     malfuntions_choices = [
#         ('NF', 'NO FUNCTION'),
#         ('SF', 'STOPS FUNCTION'),
#         ('UF', 'UNREQUESTED FUNCTION'),
#         ('FS', 'FUNCTION STUCK'),
#         ('EF', 'EXCESSIVE FUNCTION'),
#         ('PF', 'PARTIAL FUNCTION'),
#         ('FE', 'FUNCTIONS EARLY'),
#         ('FL', 'FUNCTIONS LATE'),
#         ('TL', 'FUNCTION APPLIES TOO LONG'),
#         ('TB', 'FUNCTION APPLIES TOO BRIEF'),
#         ('FD', 'FUNCTION DELAYED'),
#         ('IF', 'INVERSE FUNCTION'),
#         ('EF', 'ERRATIC OR INTERMITTENT FUNCTION'),
#         ('FU', 'FUNCTION IS UNEVEN'),
#         ('FE', 'FUNCTION IS EVEN')
#
#     ]
#     malf_name = models.CharField(max_length=75, null=False, choices=malfuntions_choices)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name=item)
#     created = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.malf_name
#



