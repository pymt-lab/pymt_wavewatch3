.. highlight:: shell

============
Installation
============


Stable release
--------------

Installing pymt_wavewatch3 from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

To install pymt_wavewatch3, run this command in your terminal:

.. code-block:: console

    $ conda install pymt_wavewatch3

This is the preferred method to install pymt_wavewatch3, as it will always install the most recent stable release.

If you don't have `conda`_ installed, this `Anaconda installation guide`_ can guide
you through the process.

.. _conda: https://docs.anaconda.com/anaconda/
.. _Anaconda installation guide: https://docs.anaconda.com/anaconda/install/


From sources
------------

The sources for pymt_wavewatch3 can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/pymt-lab/pymt_wavewatch3

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/pymt-lab/pymt_wavewatch3/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ conda install --file=requirements.txt
    $ python setup.py install


.. _Github repo: https://github.com/pymt-lab/pymt_wavewatch3
.. _tarball: https://github.com/pymt-lab/pymt_wavewatch3/tarball/master
