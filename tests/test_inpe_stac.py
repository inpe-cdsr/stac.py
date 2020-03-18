#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for STAC operations."""

from os import getenv

from stac import STAC

url = getenv('STAC_SERVER_URL', 'http://localhost:8089/inpe-stac')

# ASSETS_URL = 'http://localhost:8089'
ASSETS_URL = 'http://cdsr.dpi.inpe.br'


'''
def test_capabilities():
    # TODO
    """/capabilities"""

    service = STAC(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_conformance():
    # TODO
    """/conformance"""

    service = STAC(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result
'''

def test_collections():
    """/collections"""

    service = STAC(url)

    expected = {
        "collections": [
            {
                "stac_version": "0.7",
                "id": "CBERS4A_MUX_L2_DN",
                "title": "CBERS4A_MUX_L2_DN",
                "description": "CBERS4A MUX Level2 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -66.4038,
                        -79.9447,
                        68.6192,
                        22.637
                    ],
                    "time": [
                        "2019-12-27",
                        "2020-02-24"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4A_MUX_L4_DN",
                "title": "CBERS4A_MUX_L4_DN",
                "description": "CBERS4A MUX Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -36.1653,
                        -71.7135,
                        -12.1405,
                        -41.6252
                    ],
                    "time": [
                        "2019-12-27",
                        "2020-02-19"
                    ]
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN/items",
                    "rel": "items"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections",
                    "rel": "root"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4A_WFI_L2_DN",
                "title": "CBERS4A_WFI_L2_DN",
                "description": "CBERS4A WFI Level2 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -68.6431,
                        -85.8382,
                        71.2034,
                        179.939
                    ],
                    "time": [
                        "2019-12-27",
                        "2020-02-24"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4A_WFI_L4_DN",
                "title": "CBERS4A_WFI_L4_DN",
                "description": "CBERS4A WFI Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -38.1472,
                        -80.0226,
                        8.24979,
                        -32.8996
                    ],
                    "time": [
                        "2019-12-27",
                        "2020-02-19"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4A_WPM_L2_DN",
                "title": "CBERS4A_WPM_L2_DN",
                "description": "CBERS4A WPM Level2 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -66.4318,
                        -179.957,
                        68.5559,
                        179.905
                    ],
                    "time": [
                        "2019-12-27",
                        "2020-03-03"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_AWFI_L4_DN",
                "title": "CBERS4_AWFI_L4_DN",
                "description": "CBERS4 AWFI Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -45.485,
                        -82.6242,
                        21.3355,
                        55.6045
                    ],
                    "time": [
                        "2016-06-25",
                        "2020-02-28"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_AWFI_L4_SR",
                "title": "CBERS4_AWFI_L4_SR",
                "description": "CBERS4 AWFI Level4 SR dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -46.6432,
                        -84.468,
                        37.194,
                        57.5331
                    ],
                    "time": [
                        "2016-05-01",
                        "2020-02-29"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_MUX_L2_DN",
                "title": "CBERS4_MUX_L2_DN",
                "description": "CBERS4 MUX Level2 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -70.1442,
                        -78.5953,
                        19.4539,
                        44.9192
                    ],
                    "time": [
                        "2019-12-03",
                        "2019-12-31"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_MUX_L4_DN",
                "title": "CBERS4_MUX_L4_DN",
                "description": "CBERS4 MUX Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -39.0394,
                        -78.3893,
                        19.4595,
                        45.551
                    ],
                    "time": [
                        "2017-11-09",
                        "2019-12-31"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_MUX_L4_SR",
                "title": "CBERS4_MUX_L4_SR",
                "description": "CBERS4 MUX Level4 SR dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -39.0349,
                        -79.3662,
                        19.4346,
                        43.8284
                    ],
                    "time": [
                        "2017-01-26",
                        "2019-12-03"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_PAN10M_L4_DN",
                "title": "CBERS4_PAN10M_L4_DN",
                "description": "CBERS4 PAN10M Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -38.9142,
                        -78.3449,
                        7.80108,
                        -34.4983
                    ],
                    "time": [
                        "2017-07-11",
                        "2019-12-31"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            },
            {
                "stac_version": "0.7",
                "id": "CBERS4_PAN5M_L4_DN",
                "title": "CBERS4_PAN5M_L4_DN",
                "description": "CBERS4 PAN5M Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                        -6.7861,
                        -50.4667,
                        -5.63506,
                        -49.6963
                    ],
                    "time": [
                        "2017-07-11",
                        "2017-07-11"
                    ]
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN/items",
                        "rel": "items"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections",
                        "rel": "root"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
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

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'

    expected = {
        "stac_version": "0.7",
        "id": "CBERS4A_MUX_L2_DN",
        "title": "CBERS4A_MUX_L2_DN",
        "description": "CBERS4A MUX Level2 DN dataset",
        "license": None,
        "properties": {},
        "extent": {
            "spatial": [
                -66.4038,
                -79.9447,
                68.6192,
                22.637
            ],
            "time": [
                "2019-12-27",
                "2020-02-24"
            ]
        },
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "self"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items",
                "rel": "items"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections",
                "rel": "parent"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections",
                "rel": "root"
            },
            {
                "href": "http://localhost:8089/inpe-stac/stac",
                "rel": "root"
            }
        ]
    }

    result = service.collections(collection_id=collection_id)

    assert expected == result


def test_collections_collection_id__not_found_collection():
    """/collections/<collection_id>"""

    service = STAC(url)

    collection_id = 'CB4A_MUX_L2_DN'

    expected = {}

    result = service.collections(collection_id=collection_id)

    assert expected == result


def test_collections_collection_id_items():
    """/collections/<collection_id>/items"""

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 448,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4A_MUX20611220200110",
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
                    "datetime": "2020-01-10T13:29:22",
                    "path": "206",
                    "row": "112",
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND6.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND8.tif"
                    },
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND7.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND5.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20611220200110",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
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
                "id": "CBERS4A_MUX20611320200110",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -44.9037,
                                0.548619
                            ],
                            [
                                -44.9037,
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
                                -44.9037,
                                0.548619
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -44.9037,
                    -0.524779,
                    -43.8651,
                    0.548619
                ],
                "properties": {
                    "datetime": "2020-01-10T13:29:35",
                    "path": "206",
                    "row": "113",
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0.3,
                    "sync_loss": 0
                },
                "assets": {
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND6.tif"
                    },
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND7.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND8.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND5.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20611320200110",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
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


def test_collections_collection_id_items_item_id():
    """/collections/<collection_id>/items/<item_id>"""

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'
    item_id = 'CBERS4A_MUX12808420200224'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "type": "Feature",
        "id": "CBERS4A_MUX12808420200224",
        "collection": "CBERS4A_MUX_L2_DN",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        21.4677,
                        23.5584
                    ],
                    [
                        21.464,
                        22.4718
                    ],
                    [
                        22.624,
                        22.4643
                    ],
                    [
                        22.637,
                        23.5505
                    ],
                    [
                        21.4677,
                        23.5584
                    ]
                ]
            ]
        },
        "bbox": [
            21.464,
            22.4643,
            22.637,
            23.5584
        ],
        "properties": {
            "datetime": "2020-02-23T09:23:27",
            "path": "128",
            "row": "84",
            "satellite": "CBERS4A",
            "sensor": "MUX",
            "cloud_cover": 34.1,
            "sync_loss": 70.3696
        },
        "assets": {
            "blue": {
                "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_02/CBERS_4A_MUX_RAW_2020_02_24.02_18_00_CP5/128_084_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200223_128_084_L2_BAND5.tif"
            },
            "green": {
                "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_02/CBERS_4A_MUX_RAW_2020_02_24.02_18_00_CP5/128_084_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200223_128_084_L2_BAND6.tif"
            },
            "nir": {
                "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_02/CBERS_4A_MUX_RAW_2020_02_24.02_18_00_CP5/128_084_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200223_128_084_L2_BAND8.tif"
            },
            "red": {
                "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_02/CBERS_4A_MUX_RAW_2020_02_24.02_18_00_CP5/128_084_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200223_128_084_L2_BAND7.tif"
            },
            "thumbnail": {
                "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_02/CBERS_4A_MUX_RAW_2020_02_24.02_18_00_CP5/128_084_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200223_128_084.png"
            }
        },
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX12808420200224",
                "rel": "self"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "parent"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/stac",
                "rel": "root"
            }
        ]
    }

    result = service.collections_items(
        collection_id=collection_id, item_id=item_id, params=params
    )

    assert expected == result


def test_collections_collection_id_items_item_id__not_found_item():
    """/collections/<collection_id>/items/<item_id>"""

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'
    item_id = 'CBERS4A_MUX15911220200110'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        'type': 'FeatureCollection',
        'features': []
    }

    result = service.collections_items(
        collection_id=collection_id, item_id=item_id, params=params
    )

    assert expected == result


def test_stac():
    """/stac"""

    service = STAC(url)

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
                "href": "{}/collections/CBERS4_PAN10M_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN10M_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_PAN5M_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN5M_L4_DN"
            }
        ]
    }

    catalog = service.catalog()

    # check all dict/json
    assert expected == catalog

    # check specifics keys
    assert expected['stac_version'] == catalog.stac_version
    assert None == catalog.stac_extensions
    assert expected['id'] == catalog.id
    assert None == catalog.title
    assert expected['description'] == catalog.description
    assert None == catalog.summaries
    assert expected['links'] == catalog.links


def test_stac_search_get():
    """GET /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 3490,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15810520200122",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -50.3303,
                                -0.27557
                            ],
                            [
                                -50.3876,
                                -8.38617
                            ],
                            [
                                -40.8701,
                                -8.40139
                            ],
                            [
                                -40.9141,
                                -0.276067
                            ],
                            [
                                -50.3303,
                                -0.27557
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -50.3876,
                    -8.40139,
                    -40.8701,
                    -0.27557
                ],
                "properties": {
                    "datetime": "2020-01-22T13:15:03",
                    "path": "158",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 91,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15810520200122",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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
                "id": "CBERS4_AWFI15811120200122",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -51.5151,
                        -5.65375
                        ],
                        [
                        -51.6733,
                        -13.712
                        ],
                        [
                        -42.0094,
                        -13.7843
                        ],
                        [
                        -42.0807,
                        -5.68312
                        ],
                        [
                        -51.5151,
                        -5.65375
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -51.6733,
                    -13.7843,
                    -42.0094,
                    -5.65375
                ],
                "properties": {
                    "datetime": "2020-01-22T13:16:34",
                    "path": "158",
                    "row": "111",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 95,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15811120200122",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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

    result = service.search(params=params)

    assert expected == result


def test_stac_search_post__without_query_parameter():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 3490,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15810520200122",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -50.3303,
                                -0.27557
                            ],
                            [
                                -50.3876,
                                -8.38617
                            ],
                            [
                                -40.8701,
                                -8.40139
                            ],
                            [
                                -40.9141,
                                -0.276067
                            ],
                            [
                                -50.3303,
                                -0.27557
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -50.3876,
                    -8.40139,
                    -40.8701,
                    -0.27557
                ],
                "properties": {
                    "datetime": "2020-01-22T13:15:03",
                    "path": "158",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 91,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15810520200122",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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
                "id": "CBERS4_AWFI15811120200122",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -51.5151,
                                -5.65375
                            ],
                            [
                                -51.6733,
                                -13.712
                            ],
                            [
                                -42.0094,
                                -13.7843
                            ],
                            [
                                -42.0807,
                                -5.68312
                            ],
                            [
                                -51.5151,
                                -5.65375
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -51.6733,
                    -13.7843,
                    -42.0094,
                    -5.65375
                ],
                "properties": {
                    "datetime": "2020-01-22T13:16:34",
                    "path": "158",
                    "row": "111",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 95,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15811120200122",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_query_parameter_lte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2,
        'query': {
            'cloud_cover': {
                'lte': 0
            }
        }
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 261,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4A_MUX20611220200110",
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
                    "datetime": "2020-01-10T13:29:22",
                    "path": "206",
                    "row": "112",
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND6.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND8.tif"
                    },
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND7.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND5.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20611220200110",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
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
                "id": "CBERS4A_MUX20613720200110",
                "collection": "CBERS4A_MUX_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -48.997,
                                -18.494
                            ],
                            [
                                -48.9838,
                                -19.587
                            ],
                            [
                                -47.8641,
                                -19.571
                            ],
                            [
                                -47.8846,
                                -18.479
                            ],
                            [
                                -48.997,
                                -18.494
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -48.997,
                    -19.587,
                    -47.8641,
                    -18.479
                ],
                "properties": {
                    "datetime": "2020-01-10T13:34:45",
                    "path": "206",
                    "row": "137",
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_137_0/4_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_137_L4_BAND5.tif"
                    },
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_137_0/4_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_137_L4_BAND7.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_137_0/4_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_137_L4_BAND8.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_137_0/4_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_137_L4_BAND6.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_137_0/4_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_137.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN/items/CBERS4A_MUX20613720200110",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
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

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_query_parameter_gte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2,
        'query': {
            'cloud_cover': {
                'gte': 50
            }
        }
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 1235,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15810520200122",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -50.3303,
                                -0.27557
                            ],
                            [
                                -50.3876,
                                -8.38617
                            ],
                            [
                                -40.8701,
                                -8.40139
                            ],
                            [
                                -40.9141,
                                -0.276067
                            ],
                            [
                                -50.3303,
                                -0.27557
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -50.3876,
                    -8.40139,
                    -40.8701,
                    -0.27557
                ],
                "properties": {
                    "datetime": "2020-01-22T13:15:03",
                    "path": "158",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 91,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_105.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15810520200122",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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
                "id": "CBERS4_AWFI15811120200122",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -51.5151,
                                -5.65375
                            ],
                            [
                                -51.6733,
                                -13.712
                            ],
                            [
                                -42.0094,
                                -13.7843
                            ],
                            [
                                -42.0807,
                                -5.68312
                            ],
                            [
                                -51.5151,
                                -5.65375
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -51.6733,
                    -13.7843,
                    -42.0094,
                    -5.65375
                ],
                "properties": {
                    "datetime": "2020-01-22T13:16:34",
                    "path": "158",
                    "row": "111",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 95,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_22.13_12_30_CB11/158_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200122_158_111.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15811120200122",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_query_parameter_lte_gte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2,
        'query': {
            'cloud_cover': {
                'gte': 30,
                'lte': 60
            }
        }
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 637,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI16711120200121",
                "collection": "CBERS4_AWFI_L4_SR",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -60.2688,
                                -5.64367
                            ],
                            [
                                -60.3494,
                                -13.8138
                            ],
                            [
                                -50.6368,
                                -13.7542
                            ],
                            [
                                -50.7891,
                                -5.61968
                            ],
                            [
                                -60.2688,
                                -5.64367
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -60.3494,
                    -13.8138,
                    -50.6368,
                    -5.61968
                ],
                "properties": {
                    "datetime": "2020-01-21T13:51:16",
                    "path": "167",
                    "row": "111",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 30,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_21.13_46_30_CB11/167_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200121_167_111.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI16711120200121",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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
                "id": "CBERS4_AWFI15010520200120",
                "collection": "CBERS4_AWFI_L4_SR",
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
                    "datetime": "2020-01-20T12:44:06",
                    "path": "150",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 35,
                    "sync_loss": None
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15_GRID_SURFACE.tif"
                    },
                    "quality": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_CMASK_GRID_SURFACE.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16_GRID_SURFACE.tif"
                    },
                    "ndvi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_NDVI.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14_GRID_SURFACE.tif"
                    },
                    "evi": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_EVI.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13_GRID_SURFACE.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items/CBERS4_AWFI15010520200120",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
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

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_collections():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ['CBERS4_AWFI_L4_DN', 'CBERS4A_WFI_L4_DN', 'CBERS4A_WPM_L2_DN'],
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-01T00:00:00/2020-02-13T23:59:59',
        'limit': 1
    }

    expected = {
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
                    "datetime": "2020-01-21T12:16:23",
                    "path": "150",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 0,
                    "sync_loss": 0.0
                },
                "assets": {
                    "blue": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13.tif"
                    },
                    "green": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14.tif"
                    },
                    "red": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15.tif"
                    },
                    "nir": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15010520200120",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
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
                "id": "CBERS4A_WFI15911720200110",
                "collection": "CBERS4A_WFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                            -48.864,
                            0.75986
                            ],
                            [
                            -48.8923,
                            -6.97426
                            ],
                            [
                            -41.1819,
                            -6.97487
                            ],
                            [
                            -41.2097,
                            0.759925
                            ],
                            [
                            -48.864,
                            0.75986
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -48.8923,
                    -6.97487,
                    -41.1819,
                    0.759925
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    "path": "159",
                    "row": "117",
                    "satellite": "CBERS4A",
                    "sensor": "WFI",
                    "cloud_cover": 0,
                    "sync_loss": 0.0
                },
                "assets": {
                    "red": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND15.tif"
                    },
                    "blue": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND13.tif"
                    },
                    "green": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND14.tif"
                    },
                    "nir": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND16.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items/CBERS4A_WFI15911720200110",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
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
                "id": "CBERS4A_WPM15911220200110",
                "collection": "CBERS4A_WPM_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                            -44.7212,
                            1.29834
                            ],
                            [
                            -44.7212,
                            0.256597
                            ],
                            [
                            -43.7049,
                            0.256534
                            ],
                            [
                            -43.7045,
                            1.29803
                            ],
                            [
                            -44.7212,
                            1.29834
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -44.7212,
                    0.256534,
                    -43.7045,
                    1.29834
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    "path": "159",
                    "row": "112",
                    "satellite": "CBERS4A",
                    "sensor": "WPM",
                    "cloud_cover": 0,
                    "sync_loss": 0.0
                },
                "assets": {
                    "green": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND2.tif"
                    },
                    "pan": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND0.tif"
                    },
                    "nir": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND4.tif"
                    },
                    "red": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND3.tif"
                    },
                    "blue": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND1.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items/CBERS4A_WPM15911220200110",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                        "rel": "collection"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            }
        ],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 576,
            "returned": 3,
            'meta': [
                {
                    'name': 'CBERS4_AWFI_L4_DN',
                    'context': {
                        'limit': 1,
                        'matched': 391,
                        'page': 1,
                        'returned': 1
                    }
                },
                {
                    'name': 'CBERS4A_WFI_L4_DN',
                    'context': {
                        'limit': 1,
                        'matched': 9,
                        'page': 1,
                        'returned': 1
                    }
                },
                {
                    'name': 'CBERS4A_WPM_L2_DN',
                    'context': {
                        'limit': 1,
                        'matched': 176,
                        'page': 1,
                        'returned': 1
                    }
                }
            ]
        }
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__collection_does_not_have_items():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ['CBERS4_AWFI_L4_SR'],
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-01T00:00:00/2020-02-13T23:59:59',
        'limit': 1
    }

    expected = {
        "type": "FeatureCollection",
        "features": [],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 0,
            "returned": 0,
            "meta": [
                {
                    "name": "CBERS4_AWFI_L4_SR",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 0,
                        "returned": 0
                    }
                }
            ]
        }
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__collection_does_not_exist():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ['CBERS4_XYZ_L4_DN'],
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-01T00:00:00/2020-02-13T23:59:59',
        'limit': 1
    }

    expected = {
        "type": "FeatureCollection",
        "features": [],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 0,
            "returned": 0,
            'meta': [
                {
                    'name': 'CBERS4_XYZ_L4_DN',
                    'context': {
                        'limit': 1,
                        'page': 1,
                        'matched': 0,
                        'returned': 0
                    }
                }
            ]
        }
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__one_collection_exist_and_other_one_does_not_exist():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ['CBERS4_AWFI_L4_DN', 'CBERS4_XYZ_L4_DN'],
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-01T00:00:00/2020-02-13T23:59:59',
        'limit': 1
    }

    expected = {
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
                    "datetime": "2020-01-21T12:16:23",
                    "path": "150",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 0,
                    "sync_loss": 0.0
                },
                "assets": {
                    "blue": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13.tif"
                    },
                    "green": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14.tif"
                    },
                    "red": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15.tif"
                    },
                    "nir": {
                        "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15010520200120",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                        "rel": "parent"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                        "rel": "collection"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/stac",
                        "rel": "root"
                    }
                ]
            }
        ],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 391,
            "returned": 1,
            'meta': [
                {
                    'name': 'CBERS4_AWFI_L4_DN',
                    'context': {
                        'limit': 1,
                        'page': 1,
                        'matched': 391,
                        'returned': 1
                    }
                },
                {
                    'name': 'CBERS4_XYZ_L4_DN',
                    'context': {
                        'limit': 1,
                        'page': 1,
                        'matched': 0,
                        'returned': 0
                    }
                }
            ]
        }
    }

    result = service.search(params=params, method='POST')

    assert expected == result
