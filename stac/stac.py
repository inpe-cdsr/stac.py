#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for STAC."""

from requests import get

from .utils import catalog


class stac:
    """This class implements a Python API client wrapper for STAC.

    See https://github.com/radiantearth/stac-spec for more information on STAC.

    :param url: The WLTS server URL.
    :type url: str
    """

    def __init__(self, url):
        """Create a STAC client attached to the given host address (an URL)."""
        self._url = url if url[-1] != '/' else url[0:-1]


    def catalog(self):
        """Return the root catalog."""
        data = self._get('{}/stac'.format(self._url))
        return catalog(data)


    def capabilities(self):
        """TODO."""
        pass


    def conformance(self):
        """Return the list of conformance classes that the server conforms to."""
        return self._get('{}/conformance'.format(self._url))


    def collections(self, collection_id=None):
        """Return the collections."""
        if collection_id is None:
            collection_id = ''
        else:
            collection_id = '/' + str(collection_id)

        return self._get('{0}/collections{1}'.format(self._url, collection_id))


    def collections_items(self, collection_id=None, item_id=None, params=None):
        """Return the items of collections.

        :param collection_id: (mandatory) A string with a collection id.
        :type collection_id: str

        :param item_id: (optional) A string with an item id.
        :type item_id: str

        :param params: (optional) A dictionary with valid STAC query parameters.
        :type params: dict

        :returns: A feature collection, when there are more than one result, or a feature,
        when there is only one result.
        :rtype: dict
        """
        list_params = []

        if collection_id is None:
            raise Exception('collection_id is missing')
        else:
            collection_id = '/' + str(collection_id)

        if item_id is None:
            item_id = ''
        else:
            item_id = '/' + str(item_id)

        if params is None:
            params = {}
        else:
            if 'bbox' in params:
                params['bbox'] = ','.join(map(str, params['bbox']))
            # if 'intersects' in params:
            #     params['intersects'] = params['intersects']
            # if 'ids' in params:
            #     params['ids'] = ','.join(params['ids'])
            # if 'collections' in params:
            #     params['collections'] = ','.join(params['collections'])

        return self._get(
            '{0}/collections{1}/items{2}'.format(self._url, collection_id, item_id),
            params=params
        )


    def search(self, params=None):
        """Retrieve Items matching a filter.

        :param params: (optional) A dictionary with valid STAC query parameters.
        :type params: dict

        :returns: A feature collection.
        :rtype: dict
        """
        if params is None:
            params = {}
        else:
            if 'bbox' in params:
                params['bbox'] = ','.join(map(str, params['bbox']))
            # if 'intersects' in params:
            #     params['intersects'] = params['intersects']
            # if 'ids' in params:
            #     params['ids'] = ','.join(params['ids'])
            # if 'collections' in params:
            #     params['collections'] = ','.join(params['collections'])

        return self._get('{}/stac/search'.format(self._url), params=params)


    @property
    def url(self):
        """Return the STAC server instance URL."""
        return self._url


    def __repr__(self):
        """Return the string representation of a STAC object."""
        return 'stac("{}")'.format(self.url)


    def __str__(self):
        """Return the string representation of a STAC object."""
        return '<STAC [{}]>'.format(self.url)


    @staticmethod
    def _get(url, params=None):
        """Query the STAC service using HTTP GET verb and return the result as a JSON document.

        :param url: The URL to query must be a valid STAC endpoint.
        :type url: str

        :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the underlying `Requests`.
        :type params: dict

        :rtype: dict

        :raises ValueError: If the response body does not contain a valid json.
        """
        response = get(url, params=params)

        response.raise_for_status()

        content_type = response.headers.get('content-type')

        if content_type not in ('application/json', 'application/geo+json'):
            raise ValueError('HTTP response is not JSON: Content-Type: {}'.format(content_type))

        return response.json()
