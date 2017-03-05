========
Snakebox
========
An incomplete basic python wrapper for Baasbox REST APIs
--------------------------------------------------------

Snakebox is a python wrapper around baasbox's REST APIs. It handles some of the most
boring stuff like the HTTP headers required by Baasbox and provides some utility
methods to quickly call some frequently used APIs.

Snakebox is in its infancy and still largely incomplete, pull requests to improve it
and add functionalities are more than welcome.


Quickstart
----------

Import snakebox, create a Baasbox instance and use it to
login with a valid user and password and for all subsequent calls:

.. code-block:: python

  from snakebox import Baasbox

  baasbox = Baasbox(host='HOST', port=9000, appcode='APPCODE')
  user = baasbox.login(username, password)

  books = baasbox.search_document('Books', 'author = ? or year > ?', ['Tolkien', 1900])

At the moment, snakebox only has utility methods for searching documents in a collection
and calling user-defined plugins. All other APIs have yet to be implemented, but you
can call all of Baasbox's API endpoints by using the low-level ``_rest_call`` method.
