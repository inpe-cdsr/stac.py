#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for STAC operations."""

from os import getenv

from stac import stac

url = getenv('STAC_SERVER_URL', 'http://localhost')

ASSETS_URL = 'http://cdsr.dpi.inpe.br'


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
        "meta": {
            "returned": 15
        },
        "collections": [
            {
            "stac_version": "0.7",
            "id": "CBERS4A_MUX_L2_DN",
            "title": "CBERS4A_MUX_L2_DN",
            "description": "CBERS4A MUX Level2 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                    "rel": "self"
                },
                {
                    "href": "http://localhost:8089/inpe-stac/stac/",
                    "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4A_MUX_L4_DN",
            "title": "CBERS4A_MUX_L4_DN",
            "description": "CBERS4A MUX Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4A_WFI_L2_DN",
            "title": "CBERS4A_WFI_L2_DN",
            "description": "CBERS4A WFI Level2 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4A_WFI_L4_DN",
            "title": "CBERS4A_WFI_L4_DN",
            "description": "CBERS4A WFI Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4A_WPM_L2_DN",
            "title": "CBERS4A_WPM_L2_DN",
            "description": "CBERS4A WPM Level2 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_AWFI_L4_DN",
            "title": "CBERS4_AWFI_L4_DN",
            "description": "CBERS4 AWFI Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_AWFI_L4_SR",
            "title": "CBERS4_AWFI_L4_SR",
            "description": "CBERS4 AWFI Level4 SR dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_MUX_L2_DN",
            "title": "CBERS4_MUX_L2_DN",
            "description": "CBERS4 MUX Level2 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_MUX_L4_DN",
            "title": "CBERS4_MUX_L4_DN",
            "description": "CBERS4 MUX Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_MUX_L4_SR",
            "title": "CBERS4_MUX_L4_SR",
            "description": "CBERS4 MUX Level4 SR dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_PAN10M_L2_DN",
            "title": "CBERS4_PAN10M_L2_DN",
            "description": "CBERS4 PAN10M Level2 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L2_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_PAN10M_L4_DN",
            "title": "CBERS4_PAN10M_L4_DN",
            "description": "CBERS4 PAN10M Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "CBERS4_PAN5M_L4_DN",
            "title": "CBERS4_PAN5M_L4_DN",
            "description": "CBERS4 PAN5M Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "LANDSAT5_TM_L2_DN",
            "title": "LANDSAT5_TM_L2_DN",
            "description": "LANDSAT5 TM Level2 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/LANDSAT5_TM_L2_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            },
            {
            "stac_version": "0.7",
            "id": "LANDSAT5_TM_L4_DN",
            "title": "LANDSAT5_TM_L4_DN",
            "description": "LANDSAT5 TM Level4 DN dataset",
            "license": "",
            "extent": [],
            "links": [
                {
                "href": "http://localhost:8089/inpe-stac/collections/LANDSAT5_TM_L4_DN",
                "rel": "self"
                },
                {
                "href": "http://localhost:8089/inpe-stac/stac/",
                "rel": "root"
                }
            ]
            }
        ]
    }

    result = service.collections()

    assert expected == result

'''
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
            {'href': '{}/collections/CB4A_MUX_L2_DN', 'rel': 'self'},
            {'href': '{}/collections/CB4A_MUX_L2_DN/items', 'rel': 'items'},
            {'href': '{}/collections', 'rel': 'parent'},
            {'href': '{}/collections', 'rel': 'root'},
            {'href': '{}/stac', 'rel': 'root'}
        ]
    }


    result = service.collections(collection_id=collection_id)

    assert expected == result
'''
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
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4A_MUX15911220200110",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -44.7393,
                        1.3427
                        ],
                        [
                        -44.7394,
                        0.269309
                        ],
                        [
                        -43.7009,
                        0.269242
                        ],
                        [
                        -43.7006,
                        1.34236
                        ],
                        [
                        -44.7393,
                        1.3427
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -44.7394,
                    0.269242,
                    -43.7006,
                    1.3427
                ],
                "properties": {
                    "datetime": "2020-01-10T00:00:00"
                },
                "assets": {
                    "blue": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND5.tif".format(ASSETS_URL)
                    },
                    "green": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND6.tif".format(ASSETS_URL)
                    },
                    "nir": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND8.tif".format(ASSETS_URL)
                    },
                    "red": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND7.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                    "href": "{}/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15911220200110".format(url),
                    "rel": "self"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "parent"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "collection"
                    },
                    {
                    "href": "{}/stac".format(url),
                    "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CBERS4A_MUX15911320200110",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -44.9039,
                        0.548619
                        ],
                        [
                        -44.9039,
                        -0.524779
                        ],
                        [
                        -43.8651,
                        -0.524677
                        ],
                        [
                        -43.8651,
                        0.548512
                        ],
                        [
                        -44.9039,
                        0.548619
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -44.9039,
                    -0.524779,
                    -43.8651,
                    0.548619
                ],
                "properties": {
                    "datetime": "2020-01-10T00:00:00"
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND5.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND6.tif".format(ASSETS_URL)
                    },
                    "nir": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND8.tif".format(ASSETS_URL)
                    },
                    "red": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND7.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                    "href": "{}/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15911320200110".format(url),
                    "rel": "self"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "parent"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "collection"
                    },
                    {
                    "href": "{}/stac".format(url),
                    "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.collections_items(collection_id=collection_id, params=params)

    assert expected == result
'''
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

def test_stac():
    """/stac"""

    service = stac(url)

    expected = {
        "stac_version": "0.7",
        "id": "inpe-stac",
        "description": "INPE STAC Catalog",
        "links": [
            {
                "href": "{}/stac".format(service.url),
                "rel": "self"
            },
                {
                "href": "{}/collections/CBERS4A_MUX_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_MUX_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4A_MUX_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_MUX_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4A_WFI_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_WFI_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4A_WFI_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_WFI_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4A_WPM_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_WPM_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4_AWFI_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_AWFI_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_AWFI_L4_SR".format(service.url),
                "rel": "child",
                "title": "CBERS4_AWFI_L4_SR"
            },
            {
                "href": "{}/collections/CBERS4_MUX_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_MUX_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4_MUX_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_MUX_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_MUX_L4_SR".format(service.url),
                "rel": "child",
                "title": "CBERS4_MUX_L4_SR"
            },
            {
                "href": "{}/collections/CBERS4_PAN10M_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN10M_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4_PAN10M_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN10M_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_PAN5M_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN5M_L4_DN"
            },
            {
                "href": "{}/collections/LANDSAT5_TM_L2_DN".format(service.url),
                "rel": "child",
                "title": "LANDSAT5_TM_L2_DN"
            },
            {
                "href": "{}/collections/LANDSAT5_TM_L4_DN".format(service.url),
                "rel": "child",
                "title": "LANDSAT5_TM_L4_DN"
            }
        ]
    }

    result = service.catalog()

    assert expected == result


def test_stac_search():
    """/stac/search"""

    service = stac(url)

    collection_id = 'CB4A_MUX_L2_DN'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "meta": {
            "page": 1,
            "limit": 2,
            "returned": 2
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15010520200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -42.6153,
                        -0.285467
                        ],
                        [
                        -42.6546,
                        -8.42863
                        ],
                        [
                        -33.1365,
                        -8.40183
                        ],
                        [
                        -33.1992,
                        -0.284565
                        ],
                        [
                        -42.6153,
                        -0.285467
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -42.6546,
                    -8.42863,
                    -33.1365,
                    -0.284565
                ],
                "properties": {
                    "datetime": "2020-01-20T00:00:00",
                    'path': '150',
                    'row': '105',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI'
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15010520200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15011120200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -43.8293,
                        -5.63972
                        ],
                        [
                        -43.9475,
                        -13.7608
                        ],
                        [
                        -34.2661,
                        -13.765
                        ],
                        [
                        -34.3792,
                        -5.64142
                        ],
                        [
                        -43.8293,
                        -5.63972
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -43.9475,
                    -13.765,
                    -34.2661,
                    -5.63972
                ],
                "properties": {
                    "datetime": "2020-01-20T00:00:00",
                    'path': '150',
                    'row': '111',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI'
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15011120200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.search(params=params)

    assert expected == result
