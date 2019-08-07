from django.db import models
from django.conf import settings


from django.dispatch import receiver

# Create your models here.


class TicketType(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False,
                            help_text='The name of this ticket, e.g: Students')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


class TicketPurchase(models.Model):

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchased_tickets')
    ticket = models.ForeignKey(TicketType, blank=False, null=False,
                               related_name='purchases', on_delete=models.CASCADE)
    assignee = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ticket')
    payment_ref = models.CharField(max_length=50, )
    date_purchased = models.DateTimeField(auto_now_add=True)





