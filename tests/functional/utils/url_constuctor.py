from settings import settings


def url_constructor(url):
    return 'http://' + settings.service_url + f'/api/v1/{url}'
