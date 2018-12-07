# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.changes import Changes  # noqa: F401,E501
# from dohq_teamcity.models.issue import Issue  # noqa: F401,E501


class IssueUsage(TeamCityObject):
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
        'changes': 'Changes',
        'issue': 'Issue'
    }

    attribute_map = {
        'changes': 'changes',
        'issue': 'issue'
    }

    def __init__(self, changes=None, issue=None, teamcity=None):  # noqa: E501
        """IssueUsage - a model defined in Swagger"""  # noqa: E501

        self._changes = None
        self._issue = None
        self.discriminator = None

        if changes is not None:
            self.changes = changes
        if issue is not None:
            self.issue = issue
        super(IssueUsage, self).__init__(teamcity=teamcity)

    @property
    def changes(self):
        """Gets the changes of this IssueUsage.  # noqa: E501


        :return: The changes of this IssueUsage.  # noqa: E501
        :rtype: Changes
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this IssueUsage.


        :param changes: The changes of this IssueUsage.  # noqa: E501
        :type: Changes
        """

        self._changes = changes

    @property
    def issue(self):
        """Gets the issue of this IssueUsage.  # noqa: E501


        :return: The issue of this IssueUsage.  # noqa: E501
        :rtype: Issue
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this IssueUsage.


        :param issue: The issue of this IssueUsage.  # noqa: E501
        :type: Issue
        """

        self._issue = issue