"""es_paginator"""


def paginator(size: int, page: int) -> tuple():
    es_from = size * page if page == 0 else size * page + 1
    return (size, es_from)
