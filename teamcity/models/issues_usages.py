# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.issue_usage import IssueUsage  # noqa: F401,E501


class IssuesUsages(TeamCityObject):
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
        'count': 'int',
        'href': 'str',
        'issue_usage': 'list[IssueUsage]'
    }

    attribute_map = {
        'count': 'count',
        'href': 'href',
        'issue_usage': 'issueUsage'
    }

    def __init__(self, count=None, href=None, issue_usage=None, teamcity=None):  # noqa: E501
        """IssuesUsages - a model defined in Swagger"""  # noqa: E501
        super(IssuesUsages, self).__init__(teamcity=teamcity)

        self._count = None
        self._href = None
        self._issue_usage = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if issue_usage is not None:
            self.issue_usage = issue_usage

    @property
    def count(self):
        """Gets the count of this IssuesUsages.  # noqa: E501


        :return: The count of this IssuesUsages.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IssuesUsages.


        :param count: The count of this IssuesUsages.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this IssuesUsages.  # noqa: E501


        :return: The href of this IssuesUsages.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this IssuesUsages.


        :param href: The href of this IssuesUsages.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def issue_usage(self):
        """Gets the issue_usage of this IssuesUsages.  # noqa: E501


        :return: The issue_usage of this IssuesUsages.  # noqa: E501
        :rtype: list[IssueUsage]
        """
        return self._issue_usage

    @issue_usage.setter
    def issue_usage(self, issue_usage):
        """Sets the issue_usage of this IssuesUsages.


        :param issue_usage: The issue_usage of this IssuesUsages.  # noqa: E501
        :type: list[IssueUsage]
        """

        self._issue_usage = issue_usage

