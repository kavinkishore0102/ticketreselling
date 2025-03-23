from django.db import models

class Ticket(models.Model):
    TICKET_TYPES = [
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('flight', 'Flight')
    ]

    ticket_image = models.FileField(upload_to='uploads/')
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination} ({self.departure_date})"