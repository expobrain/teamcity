# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.build_types import BuildTypes  # noqa: F401,E501


class BuildTriggeringOptions(TeamCityObject):
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
        'clean_sources': 'bool',
        'queue_at_top': 'bool',
        'rebuild_all_dependencies': 'bool',
        'rebuild_dependencies': 'BuildTypes'
    }

    attribute_map = {
        'clean_sources': 'cleanSources',
        'queue_at_top': 'queueAtTop',
        'rebuild_all_dependencies': 'rebuildAllDependencies',
        'rebuild_dependencies': 'rebuildDependencies'
    }

    def __init__(self, clean_sources=False, queue_at_top=False, rebuild_all_dependencies=False, rebuild_dependencies=None, teamcity=None):  # noqa: E501
        """BuildTriggeringOptions - a model defined in Swagger"""  # noqa: E501

        self._clean_sources = None
        self._queue_at_top = None
        self._rebuild_all_dependencies = None
        self._rebuild_dependencies = None
        self.discriminator = None

        if clean_sources is not None:
            self.clean_sources = clean_sources
        if queue_at_top is not None:
            self.queue_at_top = queue_at_top
        if rebuild_all_dependencies is not None:
            self.rebuild_all_dependencies = rebuild_all_dependencies
        if rebuild_dependencies is not None:
            self.rebuild_dependencies = rebuild_dependencies
        super(BuildTriggeringOptions, self).__init__(teamcity=teamcity)

    @property
    def clean_sources(self):
        """Gets the clean_sources of this BuildTriggeringOptions.  # noqa: E501


        :return: The clean_sources of this BuildTriggeringOptions.  # noqa: E501
        :rtype: bool
        """
        return self._clean_sources

    @clean_sources.setter
    def clean_sources(self, clean_sources):
        """Sets the clean_sources of this BuildTriggeringOptions.


        :param clean_sources: The clean_sources of this BuildTriggeringOptions.  # noqa: E501
        :type: bool
        """

        self._clean_sources = clean_sources

    @property
    def queue_at_top(self):
        """Gets the queue_at_top of this BuildTriggeringOptions.  # noqa: E501


        :return: The queue_at_top of this BuildTriggeringOptions.  # noqa: E501
        :rtype: bool
        """
        return self._queue_at_top

    @queue_at_top.setter
    def queue_at_top(self, queue_at_top):
        """Sets the queue_at_top of this BuildTriggeringOptions.


        :param queue_at_top: The queue_at_top of this BuildTriggeringOptions.  # noqa: E501
        :type: bool
        """

        self._queue_at_top = queue_at_top

    @property
    def rebuild_all_dependencies(self):
        """Gets the rebuild_all_dependencies of this BuildTriggeringOptions.  # noqa: E501


        :return: The rebuild_all_dependencies of this BuildTriggeringOptions.  # noqa: E501
        :rtype: bool
        """
        return self._rebuild_all_dependencies

    @rebuild_all_dependencies.setter
    def rebuild_all_dependencies(self, rebuild_all_dependencies):
        """Sets the rebuild_all_dependencies of this BuildTriggeringOptions.


        :param rebuild_all_dependencies: The rebuild_all_dependencies of this BuildTriggeringOptions.  # noqa: E501
        :type: bool
        """

        self._rebuild_all_dependencies = rebuild_all_dependencies

    @property
    def rebuild_dependencies(self):
        """Gets the rebuild_dependencies of this BuildTriggeringOptions.  # noqa: E501


        :return: The rebuild_dependencies of this BuildTriggeringOptions.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._rebuild_dependencies

    @rebuild_dependencies.setter
    def rebuild_dependencies(self, rebuild_dependencies):
        """Sets the rebuild_dependencies of this BuildTriggeringOptions.


        :param rebuild_dependencies: The rebuild_dependencies of this BuildTriggeringOptions.  # noqa: E501
        :type: BuildTypes
        """

        self._rebuild_dependencies = rebuild_dependencies
