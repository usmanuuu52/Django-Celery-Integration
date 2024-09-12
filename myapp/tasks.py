from celery import shared_task
from time import sleep

@shared_task
def subtract(x, y):
    return x- y


@shared_task
def clear_session_cache(id=20):
    print(f"Session cache cleared :{id}")
    return id