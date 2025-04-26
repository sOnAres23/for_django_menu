from django.db import connection
import logging

logger = logging.getLogger(__name__)


class SqlCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Логирование SQL-запросов
        if connection.queries:
            for query in connection.queries:
                logger.debug(query['sql'])

        return response
