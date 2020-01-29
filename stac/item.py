"""Item module."""

import requests
import shutil
from .link import Link

class Asset(dict):
    """Asset object."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with Asset metadata.
        """
        super(Asset, self).__init__(data or {})

    @property
    def href(self):
        """:return: the Asset href."""
        return self['href']

    @property
    def title(self):
        """:return: the Asset title."""
        return self['title']

    @property
    def type(self):
        """:return: the Asset type."""
        return self['type']

    def download(self, folder_path=None):
        """
        Download the asset to an indicated folder.

        :param folder_path: Folder path to download the asset, if left None,
                            the asset will be downloaded to the current
                            working directory.
        :return: path to downloaded file.
        """
        local_filename = self['href'].split('/')[-1]
        if folder_path is not None:
            folder_path += local_filename

        with requests.get(self['href'], stream=True) as r:
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

        return local_filename


class Geometry(dict):
    """The Geometry Object."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with Geometry metadata.
        """
        super(Geometry, self).__init__(data or {})

    @property
    def type(self):
        """:return: the Geometry type."""
        return self['type']

    @property
    def coordinates(self):
        """:return: the Geometry coordinates."""
        return self['coordinates']


class Item(dict):
    """The GeoJSON Feature of a STAC Item."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with Item metadata.
        """
        super(Item, self).__init__(data or {})

    @property
    def stac_version(self):
        """:return: the STAC version."""
        return self['stac_version']

    @property
    def stac_extensions(self):
        """:return: the STAC extensions."""
        return self['stac_extensions']

    @property
    def id(self):
        """:return: the Item identifier."""
        return self['id']

    @property
    def type(self):
        """:return: the Item type."""
        return self['type']

    @property
    def bbox(self):
        """:return: the Item Bounding Box."""
        return self['bbox']

    @property
    def collection(self):
        """:return: the Item Collection."""
        return self['collection']

    @property
    def geometry(self):
        """:return: the Item Geometry."""
        return self['geometry']

    @property
    def properties(self):
        """:return: the Item properties."""
        return self['properties']

    @property
    def links(self):
        """:return: the Item related links."""
        return [Link(link) for link in self['links']]

    @property
    def assets(self):
        """:return: the Item related assets."""
        return {key: Asset(value) for key,value in self['assets'].items()}


class ItemCollection(dict):
    """The GeoJSON Feature Collection of STAC Items."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with Item Collection metadata.
        """
        super(ItemCollection, self).__init__(data or {})

    @property
    def type(self):
        """:return: the Item Collection type."""
        return self['type']

    @property
    def features(self):
        """:return: the Item Collection list of GeoJSON Features."""
        return [Item(i) for i in self['features']]
