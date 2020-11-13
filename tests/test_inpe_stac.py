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

url = getenv("STAC_SERVER_URL", "http://localhost:8089/inpe-stac")


##################################################
# UTIL FUNCTIONS
##################################################

def stac_search__get_expected_links_to_GET_method(params):
    # expected_params - copy the 'params' variable and fix 'bbox' property
    e_params = {
        **params,
        'bbox': ','.join(list(map(
        # convert the floats to str before joining the elements
        lambda x: str(x), params['bbox']
        )))
    }

    links_GET_method = [
        {
            "href": f"http://localhost:8089/inpe-stac/stac/search?bbox={e_params['bbox']}&time={e_params['time']}&page={e_params['page']}&limit={e_params['limit']}",
            "rel": "self"
        },
        {
            "href": f"http://localhost:8089/inpe-stac/stac/search?bbox={e_params['bbox']}&time={e_params['time']}&page={e_params['page']+1}&limit={e_params['limit']}",
            "rel": "next"
        },
        {
            "href": "http://localhost:8089/inpe-stac/stac",
            "rel": "root"
        }
    ]

    links_POST_method = [
        {
            "href":  "http://localhost:8089/inpe-stac/stac/search",
            "rel": "self",
            "method": "POST",
            "body": params
        },
        {
            "href":  "http://localhost:8089/inpe-stac/stac/search",
            "rel": "next",
            "method": "POST",
            "body": {**params, 'page': params['page'] + 1}
        },
        {
            "href": "http://localhost:8089/inpe-stac/stac",
            "rel": "root"
        }
    ]

    return links_GET_method, links_POST_method


##################################################
# TEST CASES
##################################################

'''
def test_get_capabilities():
    # TODO
    """/capabilities"""

    service = STAC(url)

    expected = {}

    result = service.catalog()

    # print("\n expected: ", expected)
    # print("\n result: ", result)

    assert expected == result
'''

def test_get_conformance():
    service = STAC(url)

    expected = {
        "conformsTo": [
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
            "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson"
        ]
    }

    response = service.conformance()

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections():
    """/collections"""

    service = STAC(url)

    expected = {
        "collections": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [],
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
                "summaries": {
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
                "stac_version": "0.9.0",
                "stac_extensions": [],
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
                "summaries": {
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
                "stac_version": "0.9.0",
                "stac_extensions": [],
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
                "summaries": {
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
                "stac_version": "0.9.0",
                "stac_extensions": [],
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
                "summaries": {
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
                "stac_version": "0.9.0",
                "stac_extensions": [],
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
                "summaries": {
                    "eo:bands": [
                        {
                            "name": "pan",
                            "common_name": "pan"
                        },
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
                "stac_version": "0.9.0",
                "stac_extensions": [],
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
                "summaries": {
                    "eo:bands": [
                        {
                            "name": "pan",
                            "common_name": "pan"
                        },
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

    response = service.collections()

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections_collection_id():
    """/collections/<collection_id>"""

    service = STAC(url)

    collection_id = "CBERS4A_MUX_L2_DN"

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": [],
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
        "summaries": {
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

    response = service.collections(collection_id=collection_id)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections_collection_id__not_found_collection():
    """/collections/<collection_id>"""

    service = STAC(url)

    collection_id = "CB4A_MUX_L2_DN"

    expected = {
        "code": "404",
        "description": 'The requested URI was not found.'
    }

    response = service.collections(collection_id=collection_id)

    assert 404 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections_collection_id_items():
    """/collections/<collection_id>/items"""

    service = STAC(url)

    collection_id = "CBERS4A_MUX_L2_DN"
    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
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
                "stac_version": "0.9.0",
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
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND8.xml",
                        "type": "application/xml"
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
                "stac_version": "0.9.0",
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
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND8.xml",
                        "type": "application/xml"
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
        ],
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items?bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2019-12-22T00:00:00/2020-01-22T23:59:00&page=1&limit=2",
                "rel": "self"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items",
                "rel": "child"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections",
                "rel": "parent"
            },
            {
                "href": "http://localhost:8089/inpe-stac/stac",
                "rel": "root"
            }
        ]
    }

    response = service.collections_items(collection_id=collection_id, params=params)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections_collection_id_items__with_params_ids():
    """/collections/<collection_id>/items"""

    service = STAC(url)

    collection_id = "CBERS4A_MUX_L2_DN"
    params = {
        "ids": [ 'CBERS4A_MUX07012820200813', 'CBERS4A_MUX07012320200813' ]
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 10,
            "matched": 2,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX07012820200813",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                59.2484,
                                -11.4149
                            ],
                            [
                                59.2484,
                                -12.5142
                            ],
                            [
                                60.3313,
                                -12.5142
                            ],
                            [
                                60.3313,
                                -11.4149
                            ],
                            [
                                59.2484,
                                -11.4149
                            ]
                        ]
                    ]
                },
                "bbox": [
                    59.2484,
                    -12.5142,
                    60.3313,
                    -11.4149
                ],
                "properties": {
                    "datetime": "2020-08-13T06:33:19",
                    "path": 70,
                    "row": 128,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 20,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_128_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_128.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX07012820200813",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX07012320200813",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                60.1,
                                -7.4544
                            ],
                            [
                                60.1,
                                -8.53799
                            ],
                            [
                                61.1516,
                                -8.53799
                            ],
                            [
                                61.1516,
                                -7.4544
                            ],
                            [
                                60.1,
                                -7.4544
                            ]
                        ]
                    ]
                },
                "bbox": [
                    60.1,
                    -8.53799,
                    61.1516,
                    -7.4544
                ],
                "properties": {
                    "datetime": "2020-08-13T06:32:15",
                    "path": 70,
                    "row": 123,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 40,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_08/CBERS_4A_MUX_RAW_2020_08_13.02_38_30_ETC2/070_123_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200812_070_123.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX07012320200813",
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
        ],
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items?ids=CBERS4A_MUX07012820200813,CBERS4A_MUX07012320200813&page=1&limit=10",
                "rel": "self"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items",
                "rel": "child"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections",
                "rel": "parent"
            },
            {
                "href": "http://localhost:8089/inpe-stac/stac",
                "rel": "root"
            }
        ]
    }

    response = service.collections_items(collection_id=collection_id, params=params)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections_collection_id_items_item_id():
    """/collections/<collection_id>/items/<item_id>"""

    service = STAC(url)

    collection_id = "CBERS4A_MUX_L2_DN"
    item_id = "CBERS4A_MUX23215220201009"

    expected = {
        "stac_version": "0.9.0",
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
                "type": "image/tiff; application=geotiff",
                "eo:bands": [
                    0
                ]
            },
            "blue_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND5.xml",
                "type": "application/xml"
            },
            "green": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND6.tif",
                "type": "image/tiff; application=geotiff",
                "eo:bands": [
                    1
                ]
            },
            "green_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND6.xml",
                "type": "application/xml"
            },
            "red": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND7.tif",
                "type": "image/tiff; application=geotiff",
                "eo:bands": [
                    2
                ]
            },
            "red_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND7.xml",
                "type": "application/xml"
            },
            "nir": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND8.tif",
                "type": "image/tiff; application=geotiff",
                "eo:bands": [
                    3
                ]
            },
            "nir_xml": {
                "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_10/CBERS_4A_MUX_RAW_2020_10_09.14_58_00_ETC2/232_152_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20201009_232_152_L2_BAND8.xml",
                "type": "application/xml"
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

    response = service.collections_items(
        collection_id=collection_id, item_id=item_id
    )

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_collections_collection_id_items_item_id__not_found_item():
    """/collections/<collection_id>/items/<item_id>"""

    service = STAC(url)

    collection_id = "CBERS4A_MUX_L2_DN"
    item_id = "CBERS4A_MUX15911220200110"
    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2
    }

    expected = {}

    response = service.collections_items(
        collection_id=collection_id, item_id=item_id, params=params
    )

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_stac():
    """/stac"""

    service = STAC(url)

    expected = {
        "stac_version": "0.9.0",
        'stac_extensions': [],
        "id": "inpe-stac",
        "title": "INPE STAC",
        "description": "INPE STAC Catalog",
        "links": [
            {
                "href": "http://localhost:8089/inpe-stac/stac",
                "rel": "self",
                "type": "application/json",
                "title": "This document"
            },
            {
                "href": "http://localhost:8089/inpe-stac/conformance",
                "rel": "conformance",
                "type": "application/json",
                "title": "OGC API conformance classes implemented by this server"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections",
                "rel": "data",
                "type": "application/json",
                "title": "Information about the feature collections"
            },
            {
                "href": "http://localhost:8089/inpe-stac/stac/search",
                "rel": "search",
                "type": "application/json",
                "title": "Search across feature collections"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                "rel": "child",
                "type": "application/json",
                "title": "CBERS4A_MUX_L2_DN collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                "rel": "child",
                "type": "application/json",
                "title": "CBERS4A_MUX_L4_DN collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN",
                "rel": "child",
                "type": "application/json",
                "title": "CBERS4A_WFI_L2_DN collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                "rel": "child",
                "type": "application/json",
                "title": "CBERS4A_WFI_L4_DN collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                "rel": "child",
                "type": "application/json",
                "title": "CBERS4A_WPM_L2_DN collection"
            },
            {
                "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L4_DN",
                "rel": "child",
                "type": "application/json",
                "title": "CBERS4A_WPM_L4_DN collection"
            }
        ]
    }

    response = service.catalog()

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_post_stac_search():
    """[GET|POST] /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 6
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 6,
            "matched": 1859,
            "returned": 6,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614520200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.3382,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -24.8867
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.3382,
                    -25.9742,
                    -57.1717,
                    -24.8867
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:20",
                    "path": 216,
                    "row": 145,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614520200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614420200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.1453,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -24.0965
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.1453,
                    -25.1831,
                    -56.9876,
                    -24.0965
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:07",
                    "path": 216,
                    "row": 144,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614420200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614320200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.9543,
                                -23.306
                            ],
                            [
                                -57.9543,
                                -24.3918
                            ],
                            [
                                -56.8036,
                                -24.3918
                            ],
                            [
                                -56.8036,
                                -23.306
                            ],
                            [
                                -57.9543,
                                -23.306
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.9543,
                    -24.3918,
                    -56.8036,
                    -23.306
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:54",
                    "path": 216,
                    "row": 143,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614320200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614220200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.765,
                                -22.5154
                            ],
                            [
                                -57.765,
                                -23.6008
                            ],
                            [
                                -56.6211,
                                -23.6008
                            ],
                            [
                                -56.6211,
                                -22.5154
                            ],
                            [
                                -57.765,
                                -22.5154
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.765,
                    -23.6008,
                    -56.6211,
                    -22.5154
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:42",
                    "path": 216,
                    "row": 142,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 80,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614220200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614120200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.5775,
                                -21.7245
                            ],
                            [
                                -57.5775,
                                -22.8097
                            ],
                            [
                                -56.4401,
                                -22.8097
                            ],
                            [
                                -56.4401,
                                -21.7245
                            ],
                            [
                                -57.5775,
                                -21.7245
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.5775,
                    -22.8097,
                    -56.4401,
                    -21.7245
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:29",
                    "path": 216,
                    "row": 141,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614120200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614020200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.3914,
                                -20.932
                            ],
                            [
                                -57.3914,
                                -22.0184
                            ],
                            [
                                -56.2604,
                                -22.0184
                            ],
                            [
                                -56.2604,
                                -20.932
                            ],
                            [
                                -57.3914,
                                -20.932
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.3914,
                    -22.0184,
                    -56.2604,
                    -20.932
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:16",
                    "path": 216,
                    "row": 140,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614020200122",
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

    # by default, the expected parameters return the initial page
    params['page'] = 1

    # expected_params - copy the 'params' variable and fix 'bbox' property
    e_params = {
        **params,
        'bbox': ','.join(list(map(
            # convert the floats to str before joining the elements
            lambda x: str(x), params['bbox']
        )))
    }

    expected['links'] = [
        {
            "href": f"http://localhost:8089/inpe-stac/stac/search?bbox={e_params['bbox']}&time={e_params['time']}&page={e_params['page']}&limit={e_params['limit']}",
            "rel": "self"
        },
        {
            "href": f"http://localhost:8089/inpe-stac/stac/search?bbox={e_params['bbox']}&time={e_params['time']}&page={e_params['page']+1}&limit={e_params['limit']}",
            "rel": "next"
        },
        {
            "href": "http://localhost:8089/inpe-stac/stac",
            "rel": "root"
        }
    ]

    response = service.search(params=params)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()

    expected['links'] = [
        {
            "href":  "http://localhost:8089/inpe-stac/stac/search",
            "rel": "self",
            "method": "POST",
            "body": params
        },
        {
            "href":  "http://localhost:8089/inpe-stac/stac/search",
            "rel": "next",
            "method": "POST",
            "body": {**params, 'page': params['page'] + 1}
        },
        {
            "href": "http://localhost:8089/inpe-stac/stac",
            "rel": "root"
        }
    ]

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_post_stac_search__pagination__page_1__limit_2():
    """[GET|POST] /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "page": 1,
        "limit": 2
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 1859,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614520200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.3382,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -24.8867
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.3382,
                    -25.9742,
                    -57.1717,
                    -24.8867
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:20",
                    "path": 216,
                    "row": 145,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614520200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614420200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.1453,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -24.0965
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.1453,
                    -25.1831,
                    -56.9876,
                    -24.0965
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:07",
                    "path": 216,
                    "row": 144,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614420200122",
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

    links_GET_method, links_POST_method = stac_search__get_expected_links_to_GET_method(params)

    expected['links'] = links_GET_method

    response = service.search(params=params)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()

    expected['links'] = links_POST_method

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_post_stac_search__pagination__page_2__limit_2():
    """[GET|POST] /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "page": 2,
        "limit": 2
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 2,
            "limit": 2,
            "matched": 1859,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614320200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.9543,
                                -23.306
                            ],
                            [
                                -57.9543,
                                -24.3918
                            ],
                            [
                                -56.8036,
                                -24.3918
                            ],
                            [
                                -56.8036,
                                -23.306
                            ],
                            [
                                -57.9543,
                                -23.306
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.9543,
                    -24.3918,
                    -56.8036,
                    -23.306
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:54",
                    "path": 216,
                    "row": 143,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_143_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_143.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614320200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614220200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.765,
                                -22.5154
                            ],
                            [
                                -57.765,
                                -23.6008
                            ],
                            [
                                -56.6211,
                                -23.6008
                            ],
                            [
                                -56.6211,
                                -22.5154
                            ],
                            [
                                -57.765,
                                -22.5154
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.765,
                    -23.6008,
                    -56.6211,
                    -22.5154
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:42",
                    "path": 216,
                    "row": 142,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 80,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_142_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_142.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614220200122",
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

    links_GET_method, links_POST_method = stac_search__get_expected_links_to_GET_method(params)

    expected['links'] = links_GET_method

    response = service.search(params=params)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()

    expected['links'] = links_POST_method

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_get_post_stac_search__pagination__page_3__limit_2():
    """[GET|POST] /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "page": 3,
        "limit": 2
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 3,
            "limit": 2,
            "matched": 1859,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614120200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.5775,
                                -21.7245
                            ],
                            [
                                -57.5775,
                                -22.8097
                            ],
                            [
                                -56.4401,
                                -22.8097
                            ],
                            [
                                -56.4401,
                                -21.7245
                            ],
                            [
                                -57.5775,
                                -21.7245
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.5775,
                    -22.8097,
                    -56.4401,
                    -21.7245
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:29",
                    "path": 216,
                    "row": 141,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_141.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614120200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614020200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -57.3914,
                                -20.932
                            ],
                            [
                                -57.3914,
                                -22.0184
                            ],
                            [
                                -56.2604,
                                -22.0184
                            ],
                            [
                                -56.2604,
                                -20.932
                            ],
                            [
                                -57.3914,
                                -20.932
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -57.3914,
                    -22.0184,
                    -56.2604,
                    -20.932
                ],
                "properties": {
                    "datetime": "2020-01-22T14:07:16",
                    "path": 216,
                    "row": 140,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_140_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_140.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614020200122",
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

    links_GET_method, links_POST_method = stac_search__get_expected_links_to_GET_method(params)

    expected['links'] = links_GET_method

    response = service.search(params=params)

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()

    expected['links'] = links_POST_method

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__without_query_parameter():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 1859,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614520200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.3382,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -24.8867
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.3382,
                    -25.9742,
                    -57.1717,
                    -24.8867
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:20",
                    "path": 216,
                    "row": 145,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614520200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614420200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.1453,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -24.0965
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.1453,
                    -25.1831,
                    -56.9876,
                    -24.0965
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:07",
                    "path": 216,
                    "row": 144,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614420200122",
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
        ],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__with_query_parameter_lte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2,
        "query": {
            "cloud_cover": {
                "lte": 0
            }
        }
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 36,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX19413520200108",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -39.2354,
                                -16.9719
                            ],
                            [
                                -39.2354,
                                -18.058
                            ],
                            [
                                -38.1354,
                                -18.058
                            ],
                            [
                                -38.1354,
                                -16.9719
                            ],
                            [
                                -39.2354,
                                -16.9719
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -39.2354,
                    -18.058,
                    -38.1354,
                    -16.9719
                ],
                "properties": {
                    "datetime": "2020-01-08T12:56:38",
                    "path": 194,
                    "row": 135,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_08.12_54_00_ETC2/194_135_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200108_194_135.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX19413520200108",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX22313520200118",
                "collection": "CBERS4A_MUX_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -61.9747,
                                -16.9665
                            ],
                            [
                                -61.9747,
                                -18.0642
                            ],
                            [
                                -60.8637,
                                -18.0642
                            ],
                            [
                                -60.8637,
                                -16.9665
                            ],
                            [
                                -61.9747,
                                -16.9665
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -61.9747,
                    -18.0642,
                    -60.8637,
                    -16.9665
                ],
                "properties": {
                    "datetime": "2020-01-18T14:27:58",
                    "path": 223,
                    "row": 135,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 0,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135_L4_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_18.14_22_00_ETC2/223_135_0/4_BC_UTM_WGS84/CBERS_4A_MUX_20200118_223_135.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN/items/CBERS4A_MUX22313520200118",
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
        ],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__with_query_parameter_gte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2,
        "query": {
            "cloud_cover": {
                "gte": 50
            }
        }
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 1516,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614520200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.3382,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -24.8867
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.3382,
                    -25.9742,
                    -57.1717,
                    -24.8867
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:20",
                    "path": 216,
                    "row": 145,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614520200122",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614420200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.1453,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -25.1831
                            ],
                            [
                                -56.9876,
                                -24.0965
                            ],
                            [
                                -58.1453,
                                -24.0965
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.1453,
                    -25.1831,
                    -56.9876,
                    -24.0965
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:07",
                    "path": 216,
                    "row": 144,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_144_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_144.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614420200122",
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
        ],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__with_query_parameter_lte_gte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2,
        "query": {
            "cloud_cover": {
                "gte": 30,
                "lte": 60
            }
        }
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 413,
            "returned": 2,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX20414120200120",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -48.1668,
                                -21.7217
                            ],
                            [
                                -48.1668,
                                -22.812
                            ],
                            [
                                -47.0277,
                                -22.812
                            ],
                            [
                                -47.0277,
                                -21.7217
                            ],
                            [
                                -48.1668,
                                -21.7217
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -48.1668,
                    -22.812,
                    -47.0277,
                    -21.7217
                ],
                "properties": {
                    "datetime": "2020-01-20T13:29:44",
                    "path": 204,
                    "row": 141,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_141_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_141.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20414120200120",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX20413120200120",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -46.3678,
                                -13.8021
                            ],
                            [
                                -46.3678,
                                -14.8858
                            ],
                            [
                                -45.2904,
                                -14.8858
                            ],
                            [
                                -45.2904,
                                -13.8021
                            ],
                            [
                                -46.3678,
                                -13.8021
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -46.3678,
                    -14.8858,
                    -45.2904,
                    -13.8021
                ],
                "properties": {
                    "datetime": "2020-01-20T13:27:35",
                    "path": 204,
                    "row": 131,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_20.13_23_30_ETC2/204_131_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200120_204_131.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX20413120200120",
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
        ],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__with_one_collection():
    """
    POST /stac/search

    This test case should return the same result as `test_collections_collection_id_items` test case
    """

    service = STAC(url)

    params = {
        "collections": ["CBERS4A_MUX_L2_DN"],
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 2
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 759,
            "returned": 2,
            'meta': [
                {
                    'name': 'CBERS4A_MUX_L2_DN',
                    'context': {
                        'page': 1,
                        'limit': 2,
                        'matched': 759,
                        'returned': 2
                    }
                }
            ],
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
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
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_134_L2_BAND8.xml",
                        "type": "application/xml"
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
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
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_02.12_37_41_ETC2/189_133_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200102_189_133_L2_BAND8.xml",
                        "type": "application/xml"
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
        ],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__with_collections():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ["CBERS4_AWFI_L4_DN", "CBERS4A_WFI_L4_DN", "CBERS4A_WPM_L2_DN"],
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
        "limit": 1
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 1392,
            "returned": 2,
            "meta": [
                {
                    "name": "CBERS4A_WFI_L4_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 68,
                        "returned": 1
                    }
                },
                {
                    "name": "CBERS4A_WPM_L2_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 1324,
                        "returned": 1
                    }
                },
                {
                    "name": "CBERS4_AWFI_L4_DN",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_WFI20012420200109",
                "collection": "CBERS4A_WFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -45.4731,
                                -4.60182
                            ],
                            [
                                -45.4731,
                                -12.709
                            ],
                            [
                                -37.5681,
                                -12.709
                            ],
                            [
                                -37.5681,
                                -4.60182
                            ],
                            [
                                -45.4731,
                                -4.60182
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -45.4731,
                    -12.709,
                    -37.5681,
                    -4.60182
                ],
                "properties": {
                    "datetime": "2020-01-09T13:13:06",
                    "path": 200,
                    "row": 124,
                    "satellite": "CBERS4A",
                    "sensor": "WFI",
                    "cloud_cover": 80,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND13.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND13.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND14.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND14.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND15.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND15.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND16.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND16.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items/CBERS4A_WFI20012420200109",
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_WPM18913420200102",
                "collection": "CBERS4A_WPM_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -35.1127,
                                -16.1561
                            ],
                            [
                                -35.1127,
                                -17.2112
                            ],
                            [
                                -34.0472,
                                -17.2112
                            ],
                            [
                                -34.0472,
                                -16.1561
                            ],
                            [
                                -35.1127,
                                -16.1561
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -35.1127,
                    -17.2112,
                    -34.0472,
                    -16.1561
                ],
                "properties": {
                    "datetime": "2020-01-02T12:40:29",
                    "path": 189,
                    "row": 134,
                    "satellite": "CBERS4A",
                    "sensor": "WPM",
                    "cloud_cover": 70,
                    "sync_loss": None,
                    "eo:gsd": -1,
                    "eo:bands": [
                        {
                            "name": "pan",
                            "common_name": "pan"
                        },
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
                    "pan": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND0.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "pan_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND0.xml",
                        "type": "application/xml"
                    },
                    "blue": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND1.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND1.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND2.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND2.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND3.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND3.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND4.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            4
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134_L2_BAND4.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_02.12_37_41_ETC2/189_134_0/2_BC_UTM_WGS84/CBERS_4A_WPM_20200102_189_134.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items/CBERS4A_WPM18913420200102",
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
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__collection_does_not_have_items():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ["CBERS4_PAN5M_L4_DN"],
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
        "limit": 1
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
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
        },
        "type": "FeatureCollection",
        "features": [],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__collection_does_not_exist():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ["CBERS4_XYZ_L4_DN"],
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
        "limit": 1
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 0,
            "returned": 0,
            "meta": [
                {
                    "name": "CBERS4_XYZ_L4_DN",
                    "context": {
                        "limit": 1,
                        "page": 1,
                        "matched": 0,
                        "returned": 0
                    }
                }
            ]
        },
        "type": "FeatureCollection",
        "features": [],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()


def test_post_stac_search__one_collection_exist_and_other_one_does_not_exist():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        "collections": ["CBERS4A_WFI_L4_DN", "CBERS4_XYZ_L4_DN"],
        "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
        "limit": 1
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 1,
            "matched": 68,
            "returned": 1,
            "meta": [
                {
                    "name": "CBERS4A_WFI_L4_DN",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 68,
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
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo", "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_WFI20012420200109",
                "collection": "CBERS4A_WFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -45.4731,
                                -4.60182
                            ],
                            [
                                -45.4731,
                                -12.709
                            ],
                            [
                                -37.5681,
                                -12.709
                            ],
                            [
                                -37.5681,
                                -4.60182
                            ],
                            [
                                -45.4731,
                                -4.60182
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -45.4731,
                    -12.709,
                    -37.5681,
                    -4.60182
                ],
                "properties": {
                    "datetime": "2020-01-09T13:13:06",
                    "path": 200,
                    "row": 124,
                    "satellite": "CBERS4A",
                    "sensor": "WFI",
                    "cloud_cover": 80,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND13.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND13.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND14.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND14.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND15.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND15.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND16.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124_L4_BAND16.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_09.13_11_00_ETC2/200_124_0/4_BC_UTM_WGS84/CBERS_4A_WFI_20200109_200_124.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items/CBERS4A_WFI20012420200109",
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
            }
        ],
        # add 'page' property and return just the links property to POST method
        "links": stac_search__get_expected_links_to_GET_method(
            {**params, 'page': 1}
        )[1]
    }

    response = service.search(params=params, method="POST")

    assert 200 == response.status_code
    assert response.headers.get('content-type') in ('application/json', 'application/geo+json')
    assert expected == response.json()

'''
def test_get_post_stac_search__error__invalid_params():
    """[GET|POST] /stac/search"""

    service = STAC(url)

    params = {
        "bbox": [ -68.0273437, "-25.0059726", -34.9365234, "bee" ],
        "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
        "limit": 1
    }

    expected = {
        "stac_version": "0.9.0",
        "stac_extensions": ["context"],
        "context": {
            "page": 1,
            "limit": 6,
            "matched": 1859,
            "returned": 6,
            "meta": None
        },
        "type": "FeatureCollection",
        "features": [
            {
                "stac_version": "0.9.0",
                "stac_extensions": [
                    "eo",
                    "query"
                ],
                "type": "Feature",
                "id": "CBERS4A_MUX21614520200122",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -58.3382,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -25.9742
                            ],
                            [
                                -57.1717,
                                -24.8867
                            ],
                            [
                                -58.3382,
                                -24.8867
                            ]
                        ]
                    ]
                },
                "bbox": [
                    -58.3382,
                    -25.9742,
                    -57.1717,
                    -24.8867
                ],
                "properties": {
                    "datetime": "2020-01-22T14:08:20",
                    "path": 216,
                    "row": 145,
                    "satellite": "CBERS4A",
                    "sensor": "MUX",
                    "cloud_cover": 90,
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
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            0
                        ]
                    },
                    "blue_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND5.xml",
                        "type": "application/xml"
                    },
                    "green": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            1
                        ]
                    },
                    "green_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND6.xml",
                        "type": "application/xml"
                    },
                    "red": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            2
                        ]
                    },
                    "red_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND7.xml",
                        "type": "application/xml"
                    },
                    "nir": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.tif",
                        "type": "image/tiff; application=geotiff",
                        "eo:bands": [
                            3
                        ]
                    },
                    "nir_xml": {
                        "href": "http://www2.dgi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145_L2_BAND8.xml",
                        "type": "application/xml"
                    },
                    "thumbnail": {
                        "href": "http://www2.dgi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_22.14_00_00_ETC2/216_145_0/2_BC_UTM_WGS84/CBERS_4A_MUX_20200122_216_145.png",
                        "type": "image/png"
                    }
                },
                "links": [
                    {
                        "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX21614520200122",
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

    assert expected == service.search(params=params)

    assert expected == service.search(params=params, method="POST")
'''
