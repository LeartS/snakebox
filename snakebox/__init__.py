#! /usr/bin/env python3

import logging
from logging import NullHandler

import requests


logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())


class WrongLoginData(Exception):
    pass


class UnexpectedStatus(Exception):
    pass


class ServerError(Exception):

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return '[{}] {}'.format(self.response.status_code,
                                self.response.json().get('message'))


class Baasbox(object):

    def __init__(self, host='127.0.0.1', port='9000', appcode='1234567890',
                 session=None):
        self.host = host
        self.port = str(port)
        self.url = 'http://{}:{}/'.format(self.host, self.port)
        self.appcode = appcode
        self.session = session

    def _rest_call(self, path, method, data=None):
        logger.debug('Request: {}')
        custom_headers = {'X-BAASBOX-APPCODE': self.appcode}
        if self.session:
            custom_headers['X-BB-SESSION'] = self.session
        method = method.lower()
        if method in ('get', 'options'):
            r = getattr(requests, method)(self.url + path, data or {},
                                          headers=custom_headers)
        else:
            r = getattr(requests, method)(self.url + path, json=(data or {}),
                                          headers=custom_headers)
        if r.status_code != 200:
            raise ServerError(r)
        return r

    def login(self, username, password):
        try:
            response = self._rest_call('login', 'post', {
                'username': username,
                'password': password,
                'appcode': self.appcode
            })
            json = response.json()
            self.user = json['data']['user']
            self.user['id'] = json['data']['id']
            self.session = json['data']['X-BB-SESSION']
            return json
        except ServerError as se:
            if se.response.status_code == 401:
                raise WrongLoginData()
            else:
                raise

    def search_document(self, collection, filter_string='', filter_params=[]):
        data = {}
        if filter_string:
            data['where'] = filter_string
        if filter_params:
            data['params'] = filter_params
        r = self._rest_call('document/{}'.format(collection), 'GET', data)
        logger.debug('Received response %s: %s', r.status_code, r.json())
        return r.json().get('data')

    def update_document(self, collection, document):
        r = self._rest_call(
            'document/{}/{}'.format(collection, document['id']),
            'PUT', document)
        logger.debug('Received response %s: %s', r.status_code, r.json())
        return r.json().get('data')


    def call_plugin(self, plugin, method='get', data=None):
        logger.debug('Calling plugin {}, method {}, data {}'.format(
            plugin, method, data))
        r = self._rest_call('plugin/' + plugin, method, data)
        logger.debug(
            'Received response {}: {}'.format(r.status_code, r.json()))
        return r.json().get('data')
