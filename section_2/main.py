import requests
import logging

logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

session = requests.Session()
base_url = 'https://httpstat.us'
status_codes = ['101', '200', '300', '404', '502']

for code in status_codes:
    request_url = f'{base_url}/{code}'
    try:
        response = session.get(request_url)
        if 100 <= response.status_code <= 399:
            logging.info(f'------ Request URL: {request_url} ------')
            logging.info(f'Status: {response.status_code}')
            logging.info(f'Response body: {response.text}')
        if 400 <= response.status_code <= 599:
            raise requests.exceptions.HTTPError(f'HTTP error {response.status_code}: {response.text}')
    except requests.exceptions.RequestException as e:
        logging.exception(f'------ Request failed ------')
