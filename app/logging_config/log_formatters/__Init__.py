import logging
from flask import has_request_context, request

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
            record.request_method = request.method
            record.request_path = request.path
            record.ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            record.host = request.host.split(':', 1)[0]
            record.args = dict(request.args)
            #logging.basicConfig(filename='request.log', level=logging.INFO,
             #                   format='[%(asctime)s] [%(process)d] %(remote_addr)s requested %(url)s, %(levelname)s : %(message)s')
            #logging.info(
            #    'URL: {} , Remote Address: {} , Request Method: {} , Request Path: {}, IP: {}, Host: {}'.format(
             #       request.url, request.remote_addr, request.method, request.path,
             #       request.headers.get('X-Forwarded-For', request.remote_addr), request.host.split(':', 1)[0]))


        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)
