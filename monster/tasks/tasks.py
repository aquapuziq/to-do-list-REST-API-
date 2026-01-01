from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task(bind = True, autoretry_for = (Exception,), retry_kwargs = {"max_retries": 3})
def log_task_created(self, task_id):
    logger.info(f"Task created: {task_id}")
