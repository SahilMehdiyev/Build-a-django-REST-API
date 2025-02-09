from celery import shared_task
from .models import Product
import datetime


@shared_task
def delete_old_products():
    one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    deleted_count, _ = Product.objects.filter(
        created_at__lt=one_month_ago,
    ).delete()
    return f'Deleted {deleted_count} products older than 30 days'