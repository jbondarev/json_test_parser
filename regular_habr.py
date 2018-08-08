import requests
import re
from io_util import *


def get_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        raise RuntimeError("{} has {} code".format(url, response.status_code))


def submit_habrahabr_content(habrahabr_response):
    writef('habrahabr_content.txt', habrahabr_response.content)



def get_filtered_links(habrahabr_response,
                            habrahabr_pattern=r'href=[\'"]([^\'"]*)[\"]'):
    result_text = ''
    for link in re.findall(habrahabr_pattern, habrahabr_response.text):
        result_text = result_text + str(link) + '\n'
    return result_text


def submit_filtered_links(links):
    writef('habrahabr_links.txt', links)