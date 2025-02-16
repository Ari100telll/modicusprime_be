from rest_framework.pagination import LimitOffsetPagination


class CommonPagination(LimitOffsetPagination):
    default_limit = 20
