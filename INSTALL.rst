..
    This file is part of Python Client Library for STAC.
    Copyright (C) 2019 INPE.

    Web Land Trajectory Service is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

``stac.py`` depends essentially on `Requests <https://requests.readthedocs.io/en/master/>`_. Please, read the instructions below in order to install ``stac.py``.


Production installation
-----------------------

**Under Development!**

.. Install from `PyPI <https://pypi.org/>`_:
..
.. .. code-block:: shell
..
..     $ pip3 install stac.py


Development installation
------------------------

Clone the software repository:

.. code-block:: shell

        $ git clone https://github.com/brazil-data-cube/stac.py.git


Go to the source code folder:

.. code-block:: shell

        $ cd stac.py


Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]
        $ pip install -r requirements.txt


Export STAC_SERVER_URL environment variable with the URL of STAC server in order to run the tests:

.. code-block:: shell

        $ export STAC_SERVER_URL=http://localhost:8089/inpe-stac


Run the tests:

.. code-block:: shell

        $ ./run-test.sh


Generate the documentation:

.. code-block:: shell

        $ python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under:

.. code-block:: shell

    doc/sphinx/_build/html/
