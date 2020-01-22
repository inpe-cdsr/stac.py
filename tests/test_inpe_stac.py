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
'''
# test
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

# test
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
    """/collections/<collection_id>/items"""

    service = stac(url)

    collection_id = 'CBERS4A_MUX_L2_DN'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': [ '2019-12-22T00:00:00', '2020-01-22T23:59:00' ],
        'limit': 2
    }

    expected = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'id': 'CBERS4A_MUX15913320200110',
                'collection': 'CBERS4A_MUX_L2_DN',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [[[-48.2816, -15.212], [-48.3025, -16.4987], [-47.1776, -16.5135], [-47.1638, -15.2256], [-48.2816, -15.212]]]
                },
                'bbox': [-48.3025, -16.5135, -47.1638, -15.212],
                'properties': {'datetime': '2020-01-10T00:00:00'},
                'assets': {
                    'blue': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND5.tif'
                    },
                    'green': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND6.tif'
                    },
                    'nir': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND8.tif'
                    },
                    'red': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND7.tif'
                    },
                    'thumbnail': {
                        'href': 'http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133.png'
                    }
                },
                'links': [
                    {
                        'href': 'http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15913320200110', 'rel': 'self'
                    },
                    {
                        'href': 'http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN', 'rel': 'parent'
                    },
                    {
                        'href': 'http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN', 'rel': 'collection'
                    },
                    {
                        'href': 'http://localhost:8089/inpe-stac/stac', 'rel': 'root'
                    }
                ]
            },
            {
                'type': 'Feature',
                'id': 'CBERS4A_MUX15911220200110',
                'collection': 'CBERS4A_MUX_L2_DN',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [[[-44.7393, 1.3427], [-44.7394, 0.269309], [-43.7009, 0.269242], [-43.7006, 1.34236], [-44.7393, 1.3427]]]
                },
                'bbox': [-44.7394, 0.269242, -43.7006, 1.3427],
                'properties': {'datetime': '2020-01-10T00:00:00'},
                'assets': {
                    'blue': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND5.tif'
                    },
                    'green': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND6.tif'
                    },
                    'nir': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND8.tif'
                    },
                    'red': {
                        'href': 'http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND7.tif'
                    },
                    'thumbnail': {
                        'href': 'http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112.png'
                    }
                },
                'links': [
                    {
                        'href': 'http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15911220200110', 'rel': 'self'
                    },
                    {
                        'href': 'http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN', 'rel': 'parent'
                    },
                    {
                        'href': 'http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN', 'rel': 'collection'
                    },
                    {
                        'href': 'http://localhost:8089/inpe-stac/stac', 'rel': 'root'
                    }
                ]
            }
        ]
    }

    result = service.collections_items(collection_id=collection_id, params=params)

    assert expected == result

'''
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
'''
# test
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
'''
def test_stac_search():
    """/stac/search"""

    service = stac(url)

    collection_id = 'CB4A_MUX_L2_DN'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': [ '2019-12-22T00:00:00', '2020-01-22T23:59:00' ],
        'limit': 10000
    }

    expected = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CB4A_MUX15911320200110",
                "collection": "CB4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -44.9265,
                        0.658282
                        ],
                        [
                        -44.9265,
                        -0.634596
                        ],
                        [
                        -43.8424,
                        -0.634466
                        ],
                        [
                        -43.8424,
                        0.658147
                        ],
                        [
                        -44.9265,
                        0.658282
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -44.9265,
                    -0.634596,
                    -43.8424,
                    0.658282
                ],
                "properties": {
                    "datetime": "2020-01-10T00:00:00"
                },
                "assets": {
                    "blue": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND5.tif"
                    },
                    "green": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND6.tif"
                    },
                    "nir": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND8.tif"
                    },
                    "red": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND7.tif"
                    },
                    "thumbnail": {
                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113.png"
                    }
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN/items/CB4A_MUX15911320200110",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "collection"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CB4A_MUX15913320200110",
                "collection": "CB4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -48.2816,
                        -15.212
                        ],
                        [
                        -48.3025,
                        -16.4987
                        ],
                        [
                        -47.1776,
                        -16.5135
                        ],
                        [
                        -47.1638,
                        -15.2256
                        ],
                        [
                        -48.2816,
                        -15.212
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -48.3025, -16.5135,
                    -47.1638, -15.212
                ],
                "properties": {
                    "datetime": "2020-01-10T00:00:00"
                },
                "assets": {
                    "blue": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND5.tif"
                    },
                    "green": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND6.tif"
                    },
                    "nir": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND8.tif"
                    },
                    "red": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133_L2_BAND7.tif"
                    },
                    "thumbnail": {
                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_133_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_133.png"
                    }
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN/items/CB4A_MUX15913320200110",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "collection"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CB4A_MUX15911220200110",
                "collection": "CB4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -44.7621,
                        1.45236
                        ],
                        [
                        -44.7621,
                        0.159648
                        ],
                        [
                        -43.6783,
                        0.159606
                        ],
                        [
                        -43.6779,
                        1.45198
                        ],
                        [
                        -44.7621,
                        1.45236
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -44.7621, 0.159606,
                    -43.6779, 1.45236
                ],
                "properties": {
                    "datetime": "2020-01-10T00:00:00"
                },
                "assets": {
                    "blue": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND5.tif"
                    },
                    "green": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND6.tif"
                    },
                    "nir": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND8.tif"
                    },
                    "red": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND7.tif"
                    },
                    "thumbnail": {
                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112.png"
                    }
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN/items/CB4A_MUX15911220200110",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "collection"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CB4A_MUX16111320191231",
                "collection": "CB4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -46.5087,
                        0.660666
                        ],
                        [
                        -46.5087,
                        -0.634221
                        ],
                        [
                        -45.424,
                        -0.634425
                        ],
                        [
                        -45.424,
                        0.660879
                        ],
                        [
                        -46.5087,
                        0.660666
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -46.5087, -0.634425,
                    -45.424, 0.660879
                ],
                "properties": {
                    "datetime": "2019-12-31T00:00:00"
                },
                "assets": {
                    "blue": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2019_12/CBERS_4A_MUX_RAW_2019_12_31.13_34_00_ETC2/161_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20191231_161_113_L2_BAND5.tif"
                    },
                    "green": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2019_12/CBERS_4A_MUX_RAW_2019_12_31.13_34_00_ETC2/161_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20191231_161_113_L2_BAND6.tif"
                    },
                    "nir": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2019_12/CBERS_4A_MUX_RAW_2019_12_31.13_34_00_ETC2/161_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20191231_161_113_L2_BAND8.tif"
                    },
                    "red": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2019_12/CBERS_4A_MUX_RAW_2019_12_31.13_34_00_ETC2/161_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20191231_161_113_L2_BAND7.tif"
                    },
                    "thumbnail": {
                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2019_12/CBERS_4A_MUX_RAW_2019_12_31.13_34_00_ETC2/161_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20191231_161_113.png"
                    }
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN/items/CB4A_MUX16111320191231",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CB4A_MUX_L2_DN",
                    "rel": "collection"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.collections_items(collection_id=collection_id, params=params)

    assert expected == result
'''
