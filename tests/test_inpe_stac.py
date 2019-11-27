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


def test_main():
    service = stac(url)

    expected = {
        'description': 'INPE STAC Catalog',
        'id': 'inpe-stac',
        'stac_version': '0.7',
        'links': [
            {'href': '{}/stac'.format(service.url), 'rel': 'self'},
            {'href': '{}/collections/CB4_AWFI'.format(service.url), 'rel': 'child', 'title': 'CB4_AWFI'},
            {'href': '{}/collections/CB4_MUX'.format(service.url), 'rel': 'child', 'title': 'CB4_MUX'}
        ]
    }

    result = service.catalog()

    assert expected == result
