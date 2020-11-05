#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for STAC."""

from werkzeug.exceptions import BadRequest

from stac.catalog import Catalog
from stac.collection import Collection
from stac.utils import Utils
from stac.item import ItemCollection

class STAC:
    """This class implements a Python API client wrapper for STAC.

    See https://github.com/radiantearth/stac-spec for more information on STAC.

    :param url: The STAC server URL.
    :type url: str
    """

    def __init__(self, url):
        """Create a STAC client attached to the given host address (an URL)."""
        self._url = url if url[-1] != '/' else url[0:-1]
        self._catalog = None
        # self._collections = None

    # def capabilities(self):
    #     """TODO."""
    #     pass

    def conformance(self):
        """Return the list of conformance classes that the server conforms to."""
        return Utils._get('{}/conformance'.format(self._url))

    # new version
    # def catalog(self):
    #     """
    #     Retrieve the available collections in the STAC Catalog.

    #     :return list of available collections.
    #     """
    #     if self._collections is not None:
    #         return self._collections.keys()

    #     self._collections = dict()

    #     url = '{}/stac'.format(self._url)
    #     self._catalog = Catalog(Utils._get(url))

    #     for i in self._catalog.links:
    #         if i.rel == 'child':
    #             self._collections[i.href.split('/')[-1]] = None
    #     return self._collections.keys()

    # rodrigo's version
    def catalog(self):
        """Return the root catalog."""
        if self._catalog is None:
            self._catalog = Catalog(Utils._get('{}/stac'.format(self._url)))
        return self._catalog

    # new version
    # def collections(self):
    #     """
    #     Collections.

    #     :return a dict with the STAC Colletion for every available collection.
    #     """
    #     if self._collections is None:
    #         self.catalog

    #     for collection_id in self._collections.keys():
    #         try:
    #             data = Utils._get(f'{self._url}/collections/{collection_id}')
    #             self._collections[collection_id] = Collection(data)
    #         except:
    #             pass

    #     return self._collections

    # new version
    # def collection(self, collection_id):
    #     """Return the given collection.

    #     :param collection_id: A str for a given collection_id.
    #     :type collection_id: str

    #     :returns: A STAC Collection.
    #     :rtype: dict
    #     """
    #     if collection_id in self._collections.keys() and \
    #         self._collections[collection_id].value() is not None:
    #         return self._collections[collection_id]
    #     try:
    #         data = Utils._get(f'{self._url}/collections/{collection_id}')
    #         self._collections[collection_id] = Collection(data)
    #     except Exception as e:
    #         raise Exception(f'Could not retrieve information for collection: {collection_id}')
    #     return self._collections[collection_id]

    # rodrigo's version
    def collections(self, collection_id=None):
        """Return the collections."""
        if collection_id is None:
            collection_id = ''
        else:
            collection_id = '/' + str(collection_id)

        return Utils._get('{0}/collections{1}'.format(self._url, collection_id))

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
            if 'ids' in params:
                params['ids'] = ','.join(params['ids'])
            # if 'intersects' in params:
            #     params['intersects'] = params['intersects']
            # if 'collections' in params:
            #     params['collections'] = ','.join(params['collections'])

        return Utils._get(
            '{0}/collections{1}/items{2}'.format(self._url, collection_id, item_id),
            params=params
        )

    # new version
    # def search(self, params=None):
    #     """Retrieve Items matching a filter.

    #     :param params: (optional) A dictionary with valid STAC query parameters.
    #     :type params: dict
    #     :returns: A GeoJSON FeatureCollection.
    #     :rtype: dict
    #     """
    #     data = Utils._get('{}/stac/search'.format(self._url), params=params)
    #     return ItemCollection(data)

    # rodrigo's version
    def search(self, params=None, method='GET'):
        """Retrieve Items matching a filter.

        :param params: (optional) A dictionary with valid STAC query parameters.
        :type params: dict

        :returns: A GeoJSON FeatureCollection.
        :rtype: dict
        """
        if method == 'GET':
            if params is not None:
                if 'bbox' in params:
                    params['bbox'] = ','.join(map(str, params['bbox']))
                # if 'intersects' in params:
                #     params['intersects'] = params['intersects']
                # if 'ids' in params:
                #     params['ids'] = ','.join(params['ids'])
                # if 'collections' in params:
                #     params['collections'] = ','.join(params['collections'])
            return Utils._get('{}/stac/search'.format(self._url), params=params)
        elif method == 'POST':
            return Utils._post('{}/stac/search'.format(self._url), data=params)
        else:
            raise BadRequest('Invalid method: {}'.format(method))

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
