#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for STAC operations."""

import os

from stac import STAC

url =  os.environ.get('STAC_SERVER_URL', 'http://cdsr.dpi.inpe.br/inpe-stac/')

def test_creation():
    service = STAC(url)

    assert url.count(service.url) == 1


def test_conformance():
    service = STAC(url)

    conformance = service.conformance()

    assert 'conformsTo' in conformance


def test_catalog():
    service = STAC(url)

    catalog = service.catalog()

    common_keys = { 'stac_version', 'id', 'description', 'links' }

    assert  common_keys <= set(catalog.keys())
