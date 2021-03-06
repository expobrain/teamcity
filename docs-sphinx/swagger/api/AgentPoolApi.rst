dohq_teamcity.AgentPoolApi
######################################

.. note::

   + All ``serve_*`` method have aliases with get: ``serve_something`` == ``get_something``
   + Some API have ``get`` method - default method to get object by locator (e.g ``agent_api.get('id:123')`` return ``Agent`` model by id
   + See more examples on page :doc:`/examples/api/AgentPoolApi` and model examples
   + This is autogenerated page, don't change them directly, use template. Read more in :doc:`/development`

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - :ref:`add_agent`
     - **POST** ``/app/rest/agentPools/{agentPoolLocator}/agents``
   * - :ref:`add_project`
     - **POST** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - :ref:`create_pool`
     - **POST** ``/app/rest/agentPools``
   * - :ref:`delete_pool`
     - **DELETE** ``/app/rest/agentPools/{agentPoolLocator}``
   * - :ref:`delete_pool_project`
     - **DELETE** ``/app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator}``
   * - :ref:`delete_projects`
     - **DELETE** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - :ref:`get_field`
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/{field}``
   * - :ref:`get_pool`
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}``
   * - :ref:`get_pool_agents`
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/agents``
   * - :ref:`get_pool_project`
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator}``
   * - :ref:`get_pool_projects`
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - :ref:`get_pools`
     - **GET** ``/app/rest/agentPools``
   * - :ref:`replace_projects`
     - **PUT** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - :ref:`set_field`
     - **PUT** ``/app/rest/agentPools/{agentPoolLocator}/{field}``

.. _add_agent:

add_agent
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    body = dohq_teamcity.Agent() # Agent |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.add_agent(agent_pool_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->add_agent: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **body**
     - `Agent <../models/Agent.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Agent <../models/Agent.html>`_

`Back to top <#>`_

.. _add_project:

add_project
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    body = dohq_teamcity.Project() # Project |  (optional)

    try:
        api_response = tc.agent_pool_api.add_project(agent_pool_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->add_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **body**
     - `Project <../models/Project.html>`_
     - [optional] 

Return type:
    `Project <../models/Project.html>`_

`Back to top <#>`_

.. _create_pool:

create_pool
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.AgentPool() # AgentPool |  (optional)

    try:
        api_response = tc.agent_pool_api.create_pool(body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->create_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `AgentPool <../models/AgentPool.html>`_
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_

`Back to top <#>`_

.. _delete_pool:

delete_pool
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 

    try:
        tc.agent_pool_api.delete_pool(agent_pool_locator)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->delete_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_pool_project:

delete_pool_project
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 

    try:
        tc.agent_pool_api.delete_pool_project(agent_pool_locator, project_locator)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->delete_pool_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_projects:

delete_projects
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 

    try:
        tc.agent_pool_api.delete_projects(agent_pool_locator)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->delete_projects: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _get_field:

get_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.agent_pool_api.get_field(agent_pool_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _get_pool:

get_pool
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool(agent_pool_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_

`Back to top <#>`_

.. _get_pool_agents:

get_pool_agents
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool_agents(agent_pool_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool_agents: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Agents <../models/Agents.html>`_

`Back to top <#>`_

.. _get_pool_project:

get_pool_project
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool_project(agent_pool_locator, project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Project <../models/Project.html>`_

`Back to top <#>`_

.. _get_pool_projects:

get_pool_projects
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool_projects(agent_pool_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool_projects: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Projects <../models/Projects.html>`_

`Back to top <#>`_

.. _get_pools:

get_pools
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pools(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pools: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPools <../models/AgentPools.html>`_

`Back to top <#>`_

.. _replace_projects:

replace_projects
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    body = dohq_teamcity.Projects() # Projects |  (optional)

    try:
        api_response = tc.agent_pool_api.replace_projects(agent_pool_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->replace_projects: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **body**
     - `Projects <../models/Projects.html>`_
     - [optional] 

Return type:
    `Projects <../models/Projects.html>`_

`Back to top <#>`_

.. _set_field:

set_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.set_field(agent_pool_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->set_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

`Back to top <#>`_

