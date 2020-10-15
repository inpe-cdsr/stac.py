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
                "stac_version": "0.7.0",
                "id": "CBERS4A_MUX_L2_DN",
                "title": "CBERS4A_MUX_L2_DN",
                "description": "CBERS4A MUX Level2 DN dataset",
                "license": None,
                "extent": {
                    "spatial": [
                        -64.187,
                        -78.5559,
                        72.9443,
                        143.299
                    ],
                    "temporal": [
                        "2019-12-27",
                        "2020-10-09"
                    ]
                },
                "properties": {},
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
                "stac_version": "0.7.0",
                "id": "CBERS4A_MUX_L4_DN",
                "title": "CBERS4A_MUX_L4_DN",
                "description": "CBERS4A MUX Level4 DN dataset",
                "license": None,
                "extent": {
                    "spatial": [
                        -36.2542,
                        -77.0619,
                        37.701,
                        41.5171
                    ],
                    "temporal": [
                        "2019-12-27",
                        "2020-10-09"
                    ]
                },
                "properties": {},
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
                "stac_version": "0.7.0",
                "id": "CBERS4A_WFI_L2_DN",
                "title": "CBERS4A_WFI_L2_DN",
                "description": "CBERS4A WFI Level2 DN dataset",
                "license": None,
                "extent": {
                    "spatial": [
                        -63.1852,
                        -82.5029,
                        71.0897,
                        146.417
                    ],
                    "temporal": [
                        "2019-12-27",
                        "2020-10-09"
                    ]
                },
                "properties": {},
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
                "stac_version": "0.7.0",
                "id": "CBERS4A_WFI_L4_DN",
                "title": "CBERS4A_WFI_L4_DN",
                "description": "CBERS4A WFI Level4 DN dataset",
                "license": None,
                "extent": {
                    "spatial": [
                        -38.1541,
                        -77.7864,
                        27.2197,
                        42.535
                    ],
                    "temporal": [
                        "2019-12-27",
                        "2020-10-09"
                    ]
                },
                "properties": {},
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
                "stac_version": "0.7.0",
                "id": "CBERS4A_WPM_L2_DN",
                "title": "CBERS4A_WPM_L2_DN",
                "description": "CBERS4A WPM Level2 DN dataset",
                "license": None,
                "extent": {
                    "spatial": [
                        -37.7629,
                        -78.5367,
                        72.9645,
                        143.304
                    ],
                    "temporal": [
                        "2019-12-27",
                        "2020-10-09"
                    ]
                },
                "properties": {},
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
                "stac_version": "0.7.0",
                "id": "CBERS4A_WPM_L4_DN",
                "title": "CBERS4A_WPM_L4_DN",
                "description": "CBERS4A WPM Level4 DN dataset",
                "license": None,
                "extent": {
                    "spatial": [
                        -36.9716,
                        -77.1997,
                        7.65258,
                        -35.5976
                    ],
                    "temporal": [
                        "2019-12-27",
                        "2020-10-09"
                    ]
                },
                "properties": {},
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L4_DN",
                        "rel": "self"
                    },
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L4_DN/items",
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
        "stac_version": "0.7.0",
        "id": "CBERS4A_MUX_L2_DN",
        "title": "CBERS4A_MUX_L2_DN",
        "description": "CBERS4A MUX Level2 DN dataset",
        "license": None,
        "extent": {
            "spatial": [
                -64.187,
                -78.5559,
                72.9443,
                143.299
            ],
            "temporal": [
                "2019-12-27",
                "2020-10-09"
            ]
        },
        "properties": {},
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
            "matched": 759,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.7.0",
                "stac_extensions": [
                    "eo"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX18913420200102",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -35.1462,
                                -16.1795
                            ],
                            [
                                -35.1462,
                                -17.2654
                            ],
                            [
                                -34.0528,
                                -17.2654
                            ],
                            [
                                -34.0528,
                                -16.1795
                            ],
                            [
                                -35.1462,
                                -16.1795
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -35.1462,
                    -17.2654,
                    -34.0528,
                    -16.1795
                ],
                "properties": {
                    "datetime": "2020-01-02T12:40:32",
                    "path": 189,
                    "row": 134,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 60,
                    "sync_loss": None,
                    "eo:gsd": -1,
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue"
                        },
                        {
                            "name": "green",
                            "common_name": "green"
                        },
                        {
                            "name": "red",
                            "common_name": "red"
                        },
                        {
                            "name": "nir",
                            "common_name": "nir"
                        }
                    ]
                },
                "assets": {
                    "blue": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND5.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND5.xml",
                        "type": "text/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND6.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND6.xml",
                        "type": "text/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND7.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND7.xml",
                        "type": "text/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND8.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND8.xml",
                        "type": "text/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX18913420200102",
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
                "stac_version": "0.7.0",
                "stac_extensions": [
                    "eo"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX18913320200102",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -34.9693,
                                -15.3869
                            ],
                            [
                                -34.9693,
                                -16.4724
                            ],
                            [
                                -33.8815,
                                -16.4724
                            ],
                            [
                                -33.8815,
                                -15.3869
                            ],
                            [
                                -34.9693,
                                -15.3869
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -34.9693,
                    -16.4724,
                    -33.8815,
                    -15.3869
                ],
                "properties": {
                    "datetime": "2020-01-02T12:40:19",
                    "path": 189,
                    "row": 133,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 70,
                    "sync_loss": None,
                    "eo:gsd": -1,
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue"
                        },
                        {
                            "name": "green",
                            "common_name": "green"
                        },
                        {
                            "name": "red",
                            "common_name": "red"
                        },
                        {
                            "name": "nir",
                            "common_name": "nir"
                        }
                    ]
                },
                "assets": {
                    "blue": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND5.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND5.xml",
                        "type": "text/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND6.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND6.xml",
                        "type": "text/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND7.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND7.xml",
                        "type": "text/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND8.tif",
                        "type": "image/vnd.stac.geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND8.xml",
                        "type": "text/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX18913320200102",
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
    item_id = 'CBERS4A_MUX23215220201009'

    expected = {
        "stac_version": "0.7.0",
        "stac_extensions": [
            "eo"
        ],
        "type": "Feature",
        "id": "CBERS4A_MUX23215220201009",
        "collection": "CBERS4A_MUX_L2_DN",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -72.2696,
                        -30.3429
                    ],
                    [
                        -72.2696,
                        -31.4391
                    ],
                    [
                        -71.0273,
                        -31.4391
                    ],
                    [
                        -71.0273,
                        -30.3429
                    ],
                    [
                        -72.2696,
                        -30.3429
                    ]
                ]
            ]
        },
        "bbox": [
            -72.2696,
            -31.4391,
            -71.0273,
            -30.3429
        ],
        "properties": {
            "datetime": "2020-10-09T15:08:23",
            "path": 232,
            "row": 152,
            "satellite": "CBERS4A",
            "sensor": "MUX",
            "cloud_cover": 10,
            "sync_loss": None,
            "eo:gsd": -1,
            "eo:bands": [
                {
                    "name": "blue",
                    "common_name": "blue"
                },
                {
                    "name": "green",
                    "common_name": "green"
                },
                {
                    "name": "red",
                    "common_name": "red"
                },
                {
                    "name": "nir",
                    "common_name": "nir"
                }
            ]
        },
        "assets": {
            "blue": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND5.tif",
                "type": "image/vnd.stac.geotiff",
                "eo:bands": [
                    0
                ]
            },
            "blue_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND5.xml",
                "type": "text/xml"
            },
            "green": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND6.tif",
                "type": "image/vnd.stac.geotiff",
                "eo:bands": [
                    1
                ]
            },
            "green_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND6.xml",
                "type": "text/xml"
            },
            "red": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND7.tif",
                "type": "image/vnd.stac.geotiff",
                "eo:bands": [
                    2
                ]
            },
            "red_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND7.xml",
                "type": "text/xml"
            },
            "nir": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND8.tif",
                "type": "image/vnd.stac.geotiff",
                "eo:bands": [
                    3
                ]
            },
            "nir_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND8.xml",
                "type": "text/xml"
            },
            "thumbnail": {
                "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152.png",
                "type": "image/png"
            }
        },
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX23215220201009",
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
        collection_id=collection_id, item_id=item_id
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
        "stac_version": "0.7.0",
        "id": "inpe-stac",
        "description": "INPE STAC Catalog",
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/stac",
                "rel": "self"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "child",
                "title": "CBERS4A_MUX_L2_DN"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                "rel": "child",
                "title": "CBERS4A_MUX_L4_DN"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN",
                "rel": "child",
                "title": "CBERS4A_WFI_L2_DN"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                "rel": "child",
                "title": "CBERS4A_WFI_L4_DN"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                "rel": "child",
                "title": "CBERS4A_WPM_L2_DN"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L4_DN",
                "rel": "child",
                "title": "CBERS4A_WPM_L4_DN"
            }
        ]
    }

    result = service.catalog()

    # check all dict/json
    assert expected == result

    # check specifics keys
    assert expected['stac_version'] == result.stac_version
    assert None == result.stac_extensions
    assert expected['id'] == result.id
    assert None == result.title
    assert expected['description'] == result.description
    assert None == result.summaries
    assert expected['links'] == result.links


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
                    "path": 206,
                    "row": 112,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND8.tif"
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
                    "path": 206,
                    "row": 113,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0.3,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND8.tif"
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

    result = service.search(params=params)

    print('\n result: ', result, '\n')

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
                    "path": 206,
                    "row": 112,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND8.tif"
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
                    "path": 206,
                    "row": 113,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0.3,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_113_L2_BAND8.tif"
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
                    "path": 206,
                    "row": 112,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_112_L2_BAND8.tif"
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
                "id": "CBERS4A_MUX19413420200108",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -39.0439,
                                -16.1173
                            ],
                            [
                                -39.0441,
                                -17.1962
                            ],
                            [
                                -37.9476,
                                -17.1935
                            ],
                            [
                                -37.9535,
                                -16.1147
                            ],
                            [
                                -39.0439,
                                -16.1173
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -39.0441,
                    -17.1962,
                    -37.9476,
                    -16.1147
                ],
                "properties": {
                    "datetime": "2020-01-08T12:56:23",
                    "path": 194,
                    "row": 134,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_134_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200108_194_134_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_134_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200108_194_134_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_134_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200108_194_134_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_134_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200108_194_134_L2_BAND8.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_134_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200108_194_134.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX19413420200108",
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
                "id": "CBERS4A_MUX20011720200109",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -40.8575,
                                -2.62865
                            ],
                            [
                                -40.8594,
                                -3.70022
                            ],
                            [
                                -39.8189,
                                -3.70179
                            ],
                            [
                                -39.818,
                                -2.62977
                            ],
                            [
                                -40.8575,
                                -2.62865
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -40.8594,
                    -3.70179,
                    -39.818,
                    -2.62865
                ],
                "properties": {
                    "datetime": "2020-01-09T13:11:35",
                    "path": 200,
                    "row": 117,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 64.5,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_117_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_117_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_117_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_117_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_117_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_117_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_117_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_117_L2_BAND8.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_117_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_117.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20011720200109",
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
                "id": "CBERS4A_MUX20011820200109",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -41.0224,
                                -3.42196
                            ],
                            [
                                -41.025,
                                -4.49402
                            ],
                            [
                                -39.9835,
                                -4.49617
                            ],
                            [
                                -39.9822,
                                -3.4236
                            ],
                            [
                                -41.0224,
                                -3.42196
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -41.025,
                    -4.49617,
                    -39.9822,
                    -3.42196
                ],
                "properties": {
                    "datetime": "2020-01-09T13:11:48",
                    "path": 200,
                    "row": 118,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 69.5,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_118_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_118_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_118_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_118_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_118_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_118_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_118_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_118_L2_BAND8.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_118_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_118.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20011820200109",
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
                "id": "CBERS4A_MUX20611920200110",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -45.8935,
                                -4.21611
                            ],
                            [
                                -45.8949,
                                -5.2893
                            ],
                            [
                                -44.8509,
                                -5.28993
                            ],
                            [
                                -44.8511,
                                -4.21661
                            ],
                            [
                                -45.8935,
                                -4.21611
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -45.8949,
                    -5.28993,
                    -44.8509,
                    -4.21611
                ],
                "properties": {
                    "datetime": "2020-01-10T13:30:52",
                    "path": 206,
                    "row": 119,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 35.6,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_119_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_119_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_119_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_119_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_119_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_119_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_119_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_119_L2_BAND8.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/206_119_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_206_119.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20611920200110",
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
                "id": "CBERS4A_MUX20012220200109",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -41.6849,
                                -6.59714
                            ],
                            [
                                -41.6912,
                                -7.66765
                            ],
                            [
                                -40.6445,
                                -7.67292
                            ],
                            [
                                -40.6407,
                                -6.60167
                            ],
                            [
                                -41.6849,
                                -6.59714
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -41.6912,
                    -7.67292,
                    -40.6407,
                    -6.59714
                ],
                "properties": {
                    "datetime": "2020-01-09T13:12:39",
                    "path": 200,
                    "row": 122,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 48.9,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_122_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_122_L2_BAND7.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_122_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_122_L2_BAND6.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_122_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_122_L2_BAND5.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_122_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_122_L2_BAND8.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_09.13_11_00_ETC2/200_122_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200109_200_122.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20012220200109",
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
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 2108,
            "returned": 3,
            "meta": [
                {
                    "name": "CBERS4A_WFI_L4_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 43,
                        "returned": 1
                    }
                },
                {
                    "name": "CBERS4A_WPM_L2_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 1977,
                        "returned": 1
                    }
                },
                {
                    "name": "CBERS4_AWFI_L4_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 88,
                        "returned": 1
                    }
                }
            ]
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4A_WFI20613220200110",
                "collection": "CBERS4A_WFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -51.4326,
                                -10.9264
                            ],
                            [
                                -51.6768,
                                -18.9325
                            ],
                            [
                                -43.5306,
                                -19.0474
                            ],
                            [
                                -43.5848,
                                -10.9911
                            ],
                            [
                                -51.4326,
                                -10.9264
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -51.6768,
                    -19.0474,
                    -43.5306,
                    -10.9264
                ],
                "properties": {
                    "datetime": "2020-01-10T13:33:39",
                    "path": 206,
                    "row": 132,
                    "satellite": "CBERS4A",
                    "sensor": "WFI",
                    "cloud_cover": 2.9,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/206_132_0/4_NN_UTM_WGS84/CBERS_4A_WFI_20200110_206_132_L4_BAND15.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/206_132_0/4_NN_UTM_WGS84/CBERS_4A_WFI_20200110_206_132_L4_BAND14.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/206_132_0/4_NN_UTM_WGS84/CBERS_4A_WFI_20200110_206_132_L4_BAND13.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/206_132_0/4_NN_UTM_WGS84/CBERS_4A_WFI_20200110_206_132_L4_BAND16.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/206_132_0/4_NN_UTM_WGS84/CBERS_4A_WFI_20200110_206_132.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items/CBERS4A_WFI20613220200110",
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
                "id": "CBERS4A_WPM20611220200110",
                "collection": "CBERS4A_WPM_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -44.72,
                                1.298
                            ],
                            [
                                -44.7201,
                                0.255964
                            ],
                            [
                                -43.7034,
                                0.255901
                            ],
                            [
                                -43.703,
                                1.29768
                            ],
                            [
                                -44.72,
                                1.298
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -44.7201,
                    0.255901,
                    -43.703,
                    1.298
                ],
                "properties": {
                    "datetime": "2020-01-10T13:29:22",
                    "path": 206,
                    "row": 112,
                    "satellite": "CBERS4A",
                    "sensor": "WPM",
                    "cloud_cover": 0.2,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_206_112_L2_BAND3.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_206_112_L2_BAND2.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_206_112_L2_BAND1.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_206_112_L2_BAND4.tif"
                    },
                    "pan": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_206_112_L2_BAND0.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/206_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_206_112.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items/CBERS4A_WPM20611220200110",
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
            },
            {
                "type": "Feature",
                "id": "CBERS4_AWFI17009920200207",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -60.7412,
                                5.0648
                            ],
                            [
                                -60.7319,
                                -3.05477
                            ],
                            [
                                -51.3338,
                                -3.04626
                            ],
                            [
                                -51.3198,
                                5.05067
                            ],
                            [
                                -60.7412,
                                5.0648
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -60.7412,
                    -3.05477,
                    -51.3198,
                    5.0648
                ],
                "properties": {
                    "datetime": "2020-02-07T14:00:27",
                    "path": 170,
                    "row": 99,
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 10.5,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND15.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND14.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND13.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND16.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI17009920200207",
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
        ]
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__collection_does_not_have_items():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ['CBERS4_PAN5M_L4_DN'],
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
                    "name": "CBERS4_PAN5M_L4_DN",
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
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 88,
            "returned": 1,
            "meta": [
                {
                    "name": "CBERS4_AWFI_L4_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 88,
                        "returned": 1
                    }
                },
                {
                    "name": "CBERS4_XYZ_L4_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 0,
                        "returned": 0
                    }
                }
            ]
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI17009920200207",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -60.7412,
                                5.0648
                            ],
                            [
                                -60.7319,
                                -3.05477
                            ],
                            [
                                -51.3338,
                                -3.04626
                            ],
                            [
                                -51.3198,
                                5.05067
                            ],
                            [
                                -60.7412,
                                5.0648
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -60.7412,
                    -3.05477,
                    -51.3198,
                    5.0648
                ],
                "properties": {
                    "datetime": "2020-02-07T14:00:27",
                    "path": 170,
                    "row": 99,
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 10.5,
                    "sync_loss": 0
                },
                "assets": {
                    "red": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND15.tif"
                    },
                    "green": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND14.tif"
                    },
                    "blue": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND13.tif"
                    },
                    "nir": {
                        "href": "http://localhost:8089/api/download/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099_L4_BAND16.tif"
                    },
                    "thumbnail": {
                        "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_02/CBERS_4_AWFI_DRD_2020_02_07.13_58_30_CB11/170_099_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200207_170_099.png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI17009920200207",
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
        ]
    }

    result = service.search(params=params, method='POST')

    assert expected == result
