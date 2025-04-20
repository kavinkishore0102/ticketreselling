from django.db import models

class Ticket(models.Model):
    TICKET_TYPES = [
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('flight', 'Flight')
    ]

    ticket_image = models.FileField(upload_to='uploads/')
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket to {self.destination} on {self.departure_date}"


class SoldTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=255)
    buyer_email = models.CharField(max_length=255)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Sold Ticket - {self.ticket.id} to {self.buyer_name}"
