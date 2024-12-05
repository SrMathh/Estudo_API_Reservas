from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError

class Table(models.Model):
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'Mesa {self.number}'

class Reservation(models.Model):
    STATUS_RESERVATION = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmada'),
        ('canceled', 'Cancelada'),
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    client = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    observations = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_RESERVATION, default='pending') 

    def check_conflicts(self):
        conflicts = Reservation.objects.filter(
            table=self.table,
            reservation_date=self.reservation_date,
            reservation_time__range=(self.reservation_time, self.reservation_time + timedelta(minutes=45)),
            status='pending',
        ).exclude(id=self.id)#evita que uma reserva em edição comflite com ela mesma

        if conflicts.exists():
            raise ValidationError('Mesa em reserva para este horário.')
    def save(self):
        self.check_conflicts()
        super().save()

    def __str__(self):
        return f'Reserva de mesa {self.table.number} para {self.client} em {self.reservation_date}'