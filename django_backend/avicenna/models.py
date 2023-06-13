from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    appointment_timestamp = models.DateTimeField('appointemnt\'s date')