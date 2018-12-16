import json

from urllib.request import Request
from urllib.request import urlopen


def get_request(title, page_number):
    return Request('https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}'.format(title, page_number))


def getMovieTitles(_substr):
    start_page = 1
    total_pages = None
    json_data = None
    request = get_request(_substr, start_page)
    response_json = json.loads(urlopen(request).read().decode('utf-8'))

    if response_json is not None:
        total_pages = response_json['total_pages']
        json_data = [data['Title'] for data in response_json['data']]

        if total_pages > start_page:
            for page in range(start_page + 1, total_pages + 1):
                request = get_request(_substr, page)
                response_json = json.loads(urlopen(request).read().decode('utf-8'))
                json_data.extend([data['Title'] for data in response_json['data']])
    return sorted(json_data)


