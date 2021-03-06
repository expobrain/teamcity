# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.agent_requirement import AgentRequirement  # noqa: F401,E501


class AgentRequirements(TeamCityObject):
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
        'agent_requirement': 'list[AgentRequirement]',
        'count': 'int'
    }

    attribute_map = {
        'agent_requirement': 'agent-requirement',
        'count': 'count'
    }

    def __init__(self, agent_requirement=None, count=None, teamcity=None):  # noqa: E501
        """AgentRequirements - a model defined in Swagger"""  # noqa: E501

        self._agent_requirement = None
        self._count = None
        self.discriminator = None

        if agent_requirement is not None:
            self.agent_requirement = agent_requirement
        if count is not None:
            self.count = count
        super(AgentRequirements, self).__init__(teamcity=teamcity)

    @property
    def agent_requirement(self):
        """Gets the agent_requirement of this AgentRequirements.  # noqa: E501


        :return: The agent_requirement of this AgentRequirements.  # noqa: E501
        :rtype: list[AgentRequirement]
        """
        return self._agent_requirement

    @agent_requirement.setter
    def agent_requirement(self, agent_requirement):
        """Sets the agent_requirement of this AgentRequirements.


        :param agent_requirement: The agent_requirement of this AgentRequirements.  # noqa: E501
        :type: list[AgentRequirement]
        """

        self._agent_requirement = agent_requirement

    @property
    def count(self):
        """Gets the count of this AgentRequirements.  # noqa: E501


        :return: The count of this AgentRequirements.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AgentRequirements.


        :param count: The count of this AgentRequirements.  # noqa: E501
        :type: int
        """

        self._count = count
