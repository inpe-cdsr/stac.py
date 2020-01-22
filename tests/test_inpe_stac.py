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
'''

def test_collections():
    """/collections"""

    service = stac(url)

    expected = {
        "collections": [
            {
                "stac_version": "0.7",
                "id": "CB4A_MUX_L2_DN",
                "title": "CB4A_MUX_L2_DN",
                "description": "CB4A MUX Level2 DN dataset",
                "license": "",
                "extent": [],
                "links": [
                    {
                        "href": "{}/collections/CB4A_MUX_L2_DN".format(service.url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/stac/".format(service.url),
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CB4A_MUX_L4_DN",
                "title": "CB4A_MUX_L4_DN",
                "description": "CB4A MUX Level4 DN dataset",
                "license": "",
                "extent": [],
                "links": [
                    {
                        "href": "{}/collections/CB4A_MUX_L4_DN".format(service.url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/stac/".format(service.url),
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CB4A_WFI_L2_DN",
                "title": "CB4A_WFI_L2_DN",
                "description": "CB4A WFI Level2 DN dataset",
                "license": "",
                "extent": [],
                "links": [
                    {
                        "href": "{}/collections/CB4A_WFI_L2_DN".format(service.url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/stac/".format(service.url),
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CB4A_WPM_L2_DN",
                "title": "CB4A_WPM_L2_DN",
                "description": "CB4A WPM Level2 DN dataset",
                "license": "",
                "extent": [],
                "links": [
                    {
                        "href": "{}/collections/CB4A_WPM_L2_DN".format(service.url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/stac/".format(service.url),
                        "rel": "root"
                    }
                ]
            }
        ]
    }


    result = service.collections()

    assert expected == result


def test_collections_collection_id():
    """/collections/<collection_id>"""

    service = stac(url)

    collection_id = 'CB4A_MUX_L2_DN'

    expected = {
        'stac_version': '0.7',
        'id': 'CB4A_MUX_L2_DN',
        'title': 'CB4A_MUX_L2_DN',
        'description': 'CB4A MUX Level2 DN dataset',
        'license': None,
        'properties': {},
        'extent': {
            'spatial': [-37.8691, -37.8691, 3.03714, -43.349],
            'time': ['2019-12-31', '2020-01-10']
        },
        'links': [
            {'href': 'http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN', 'rel': 'self'},
            {'href': 'http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN/items', 'rel': 'items'},
            {'href': 'http://localhost:8089/inpe-stac/collections', 'rel': 'parent'},
            {'href': 'http://localhost:8089/inpe-stac/collections', 'rel': 'root'},
            {'href': 'http://localhost:8089/inpe-stac/stac', 'rel': 'root'}
        ]
    }


    result = service.collections(collection_id=collection_id)

    assert expected == result

'''
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
            {'href': '{}/collections/CB4A_MUX_L2_DN'.format(service.url), 'rel': 'child', 'title': 'CB4A_MUX_L2_DN'},
            {'href': '{}/collections/CB4A_MUX_L4_DN'.format(service.url), 'rel': 'child', 'title': 'CB4A_MUX_L4_DN'},
            {'href': '{}/collections/CB4A_WFI_L2_DN'.format(service.url), 'rel': 'child', 'title': 'CB4A_WFI_L2_DN'},
            {'href': '{}/collections/CB4A_WPM_L2_DN'.format(service.url), 'rel': 'child', 'title': 'CB4A_WPM_L2_DN'}
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
