from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Form(models.Model):
    company_title = models.CharField(max_length=100, default=None)
    order_no = models.CharField(max_length=10, default=None)
    act_date = models.CharField(max_length=100, default=None)
    # supreme_commissioner = models.CharField(User, max_length=100, default=None)
    # commissioner2 = models.CharField(User, max_length=100, default=None)
    # commissioner3 = models.CharField(User, max_length=100, default=None)
    # commissioner4 = models.CharField(User, max_length=100, default=None)
    commissioners = models.ManyToManyField(User)
    location = models.CharField(max_length=100, default=None)
    seller_company_title = models.CharField(max_length=100, default=None)
    serial_id = models.CharField(max_length=10, default=None)
    serial_no = models.CharField(max_length=10, default=None)
    responsible_worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible_worker',
                                           blank=True)

    # def __str__(self):
    #     return self.order_no
    #
    # def get_absolute_url(self):
    #     return reverse('form-detail', kwargs={'pk': self.pk})


class Good(models.Model):
    name = models.CharField(max_length=100, default=None)
    unit = models.CharField(max_length=100, default=None)
    amount = models.IntegerField()
    cost = models.FloatField()
    total_sum = models.FloatField()
    purpose = models.CharField(max_length=100, default=None, null=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, default=None, related_name="goods")

    # def __str__(self):
    #     return self.name
    #
    # def get_absolute_url(self):
    #     return reverse('good-home')
