from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинация для вывода привычек"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
