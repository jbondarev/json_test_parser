import json_parser


def main():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = json_parser.get_data(url)    
    json_parser.submit_headers(response)
    json_parser.submit_json(response)
    json_parser.print_free_space()
    json_parser.parse_json_data(response)


if __name__ == "__main__":
    main()