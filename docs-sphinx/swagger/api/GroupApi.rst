dohq_teamcity.GroupApi
######################################

.. note::

   + All ``serve_*`` method have aliases with get: ``serve_something`` == ``get_something``
   + Some API have ``get`` method - default method to get object by locator (e.g ``agent_api.get('id:123')`` return ``Agent`` model by id
   + See more examples on page :doc:`/examples/api/GroupApi` and model examples
   + This is autogenerated page, don't change them directly, use template. Read more in :doc:`/development`

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - :ref:`add_group`
     - **POST** ``/app/rest/userGroups``
   * - :ref:`add_role`
     - **POST** ``/app/rest/userGroups/{groupLocator}/roles``
   * - :ref:`add_role_put`
     - **PUT** ``/app/rest/userGroups/{groupLocator}/roles``
   * - :ref:`add_role_simple`
     - **POST** ``/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}``
   * - :ref:`delete_group`
     - **DELETE** ``/app/rest/userGroups/{groupLocator}``
   * - :ref:`delete_role`
     - **DELETE** ``/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}``
   * - :ref:`get_permissions`
     - **GET** ``/app/rest/userGroups/{groupLocator}/debug/permissions``
   * - :ref:`get_properties`
     - **GET** ``/app/rest/userGroups/{groupLocator}/properties``
   * - :ref:`list_role`
     - **GET** ``/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}``
   * - :ref:`list_roles`
     - **GET** ``/app/rest/userGroups/{groupLocator}/roles``
   * - :ref:`put_user_property`
     - **PUT** ``/app/rest/userGroups/{groupLocator}/properties/{name}``
   * - :ref:`remove_user_property`
     - **DELETE** ``/app/rest/userGroups/{groupLocator}/properties/{name}``
   * - :ref:`serve_group`
     - **GET** ``/app/rest/userGroups/{groupLocator}``
   * - :ref:`serve_groups`
     - **GET** ``/app/rest/userGroups``
   * - :ref:`serve_user_properties`
     - **GET** ``/app/rest/userGroups/{groupLocator}/properties/{name}``

.. _add_group:

add_group
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.Group() # Group |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.add_group(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `Group <../models/Group.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Group <../models/Group.html>`_

`Back to top <#>`_

.. _add_role:

add_role
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    body = dohq_teamcity.Role() # Role |  (optional)

    try:
        api_response = tc.group_api.add_role(group_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **body**
     - `Role <../models/Role.html>`_
     - [optional] 

Return type:
    `Role <../models/Role.html>`_

`Back to top <#>`_

.. _add_role_put:

add_role_put
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    body = dohq_teamcity.Roles() # Roles |  (optional)

    try:
        api_response = tc.group_api.add_role_put(group_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_role_put: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **body**
     - `Roles <../models/Roles.html>`_
     - [optional] 

Return type:
    `Roles <../models/Roles.html>`_

`Back to top <#>`_

.. _add_role_simple:

add_role_simple
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        api_response = tc.group_api.add_role_simple(group_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_role_simple: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    `Role <../models/Role.html>`_

`Back to top <#>`_

.. _delete_group:

delete_group
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 

    try:
        tc.group_api.delete_group(group_locator)
    except ApiException as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_role:

delete_role
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        tc.group_api.delete_role(group_locator, role_id, scope)
    except ApiException as e:
        print("Exception when calling GroupApi->delete_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _get_permissions:

get_permissions
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 

    try:
        api_response = tc.group_api.get_permissions(group_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->get_permissions: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _get_properties:

get_properties
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.get_properties(group_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->get_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_

`Back to top <#>`_

.. _list_role:

list_role
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        api_response = tc.group_api.list_role(group_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->list_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    `Role <../models/Role.html>`_

`Back to top <#>`_

.. _list_roles:

list_roles
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 

    try:
        api_response = tc.group_api.list_roles(group_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->list_roles: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 

Return type:
    `Roles <../models/Roles.html>`_

`Back to top <#>`_

.. _put_user_property:

put_user_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.group_api.put_user_property(group_locator, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->put_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

`Back to top <#>`_

.. _remove_user_property:

remove_user_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        tc.group_api.remove_user_property(group_locator, name)
    except ApiException as e:
        print("Exception when calling GroupApi->remove_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _serve_group:

serve_group
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.serve_group(group_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->serve_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Group <../models/Group.html>`_

`Back to top <#>`_

.. _serve_groups:

serve_groups
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.serve_groups(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->serve_groups: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Groups <../models/Groups.html>`_

`Back to top <#>`_

.. _serve_user_properties:

serve_user_properties
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = tc.group_api.serve_user_properties(group_locator, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->serve_user_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

