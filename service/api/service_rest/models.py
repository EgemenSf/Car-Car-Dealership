from django.db import models
from django.urls import reverse

class Technician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)

    def get_api_url(self):
        return reverse("api_list_technician", kwargs={"id": self.id})


class AutomobileVO(models.Model):
    vin = models.CharField(max_length=200)
    sold = models.CharField(max_length=20)

    def __str__(self):
        return self.vin

    class Meta:
        ordering = ("vin", "sold")


class Appointment(models.Model):
    date_time = models.DateTimeField()
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    vin = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)

    technician = models.ForeignKey(
        Technician,
        related_name="technicians",
        on_delete=models.CASCADE
    )

    def get_api_url(self):
        return reverse("api_show_appointment", kwargs={"id": self.id})

    # def get_api_url(self):
    #     return reverse("api_cancel_appointment", kwargs={"pk": self.id})

    # def get_api_url(self):
    #     return reverse("api_finish_appointment", kwargs={"id": self.id})
