#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for STAC operations."""

import os

from stac import stac

url =  os.environ.get('STAC_SERVER_URL', 'http://localhost')


'''
def test_capabilities():
    # TODO
    """/capabilities"""

    service = stac(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_conformance():
    # TODO
    """/conformance"""

    service = stac(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_collections():
    # TODO
    """/collections"""

    service = stac(url)

    expected = {}

    result = service.collections()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_collections_collection_id():
    # TODO
    """/collections/<collection_id>"""

    service = stac(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_collections_collection_id_items():
    # TODO
    """/collections/<collection_id>/items"""

    service = stac(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_collections_collection_id_items_item_id():
    # TODO
    """/collections/<collection_id>/items/<item_id>"""

    service = stac(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result
'''

def test_stac():
    """/stac"""

    service = stac(url)

    expected = {
        'stac_version': '0.7',
        'id': 'inpe-stac',
        'description': 'INPE STAC Catalog',
        'links': [
            {'href': '{}/stac'.format(service.url), 'rel': 'self'},
            {'href': '{}/collections/CB4_AWFI'.format(service.url), 'rel': 'child', 'title': 'CB4_AWFI'},
            {'href': '{}/collections/CB4_MUX'.format(service.url), 'rel': 'child', 'title': 'CB4_MUX'}
        ]
    }

    result = service.catalog()

    assert expected == result

'''
def test_stac_search():
    """/stac/search"""

    service = stac(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result
'''
