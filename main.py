import json_parser
import regular_habr


def second_task():
    habrahabr_url = 'https://habrahabr.ru/'
    habrahabr_response = regular_habr.get_response(habrahabr_url)
    regular_habr.submit_habrahabr_content(habrahabr_response)
    text = regular_habr.get_filtered_links(habrahabr_response, r'<a[^><]*href=[\'"]([^><\'"]*)[\'"][^><]*>')
    regular_habr.submit_filtered_links(text)


def first_task():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = json_parser.get_data(url)
    json_parser.submit_headers(response)
    json_parser.submit_json(response)
    json_parser.print_free_space()
    json_parser.parse_json_data(response)


def main():
    # first_task()
    second_task()


if __name__ == "__main__":
    main()
