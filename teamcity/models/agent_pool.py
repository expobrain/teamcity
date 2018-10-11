# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.agents import Agents  # noqa: F401,E501
# from teamcity.models.projects import Projects  # noqa: F401,E501


class AgentPool(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'agents': 'Agents',
        'href': 'str',
        'id': 'int',
        'locator': 'str',
        'max_agents': 'int',
        'name': 'str',
        'projects': 'Projects'
    }

    attribute_map = {
        'agents': 'agents',
        'href': 'href',
        'id': 'id',
        'locator': 'locator',
        'max_agents': 'maxAgents',
        'name': 'name',
        'projects': 'projects'
    }

    def __init__(self, agents=None, href=None, id=None, locator=None, max_agents=None, name=None, projects=None, teamcity=None):  # noqa: E501
        """AgentPool - a model defined in Swagger"""  # noqa: E501
        super(AgentPool, self).__init__(teamcity=teamcity)

        self._agents = None
        self._href = None
        self._id = None
        self._locator = None
        self._max_agents = None
        self._name = None
        self._projects = None
        self.discriminator = None

        if agents is not None:
            self.agents = agents
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if locator is not None:
            self.locator = locator
        if max_agents is not None:
            self.max_agents = max_agents
        if name is not None:
            self.name = name
        if projects is not None:
            self.projects = projects

    @property
    def agents(self):
        """Gets the agents of this AgentPool.  # noqa: E501


        :return: The agents of this AgentPool.  # noqa: E501
        :rtype: Agents
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this AgentPool.


        :param agents: The agents of this AgentPool.  # noqa: E501
        :type: Agents
        """

        self._agents = agents

    @property
    def href(self):
        """Gets the href of this AgentPool.  # noqa: E501


        :return: The href of this AgentPool.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AgentPool.


        :param href: The href of this AgentPool.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this AgentPool.  # noqa: E501


        :return: The id of this AgentPool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgentPool.


        :param id: The id of this AgentPool.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def locator(self):
        """Gets the locator of this AgentPool.  # noqa: E501


        :return: The locator of this AgentPool.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this AgentPool.


        :param locator: The locator of this AgentPool.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def max_agents(self):
        """Gets the max_agents of this AgentPool.  # noqa: E501


        :return: The max_agents of this AgentPool.  # noqa: E501
        :rtype: int
        """
        return self._max_agents

    @max_agents.setter
    def max_agents(self, max_agents):
        """Sets the max_agents of this AgentPool.


        :param max_agents: The max_agents of this AgentPool.  # noqa: E501
        :type: int
        """

        self._max_agents = max_agents

    @property
    def name(self):
        """Gets the name of this AgentPool.  # noqa: E501


        :return: The name of this AgentPool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentPool.


        :param name: The name of this AgentPool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def projects(self):
        """Gets the projects of this AgentPool.  # noqa: E501


        :return: The projects of this AgentPool.  # noqa: E501
        :rtype: Projects
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this AgentPool.


        :param projects: The projects of this AgentPool.  # noqa: E501
        :type: Projects
        """

        self._projects = projects

