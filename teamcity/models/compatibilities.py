# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.compatibility import Compatibility  # noqa: F401,E501


class Compatibilities(TeamCityObject):
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
        'compatibility': 'list[Compatibility]',
        'count': 'int'
    }

    attribute_map = {
        'compatibility': 'compatibility',
        'count': 'count'
    }

    def __init__(self, compatibility=None, count=None, teamcity=None):  # noqa: E501
        """Compatibilities - a model defined in Swagger"""  # noqa: E501
        super(Compatibilities, self).__init__(teamcity=teamcity)

        self._compatibility = None
        self._count = None
        self.discriminator = None

        if compatibility is not None:
            self.compatibility = compatibility
        if count is not None:
            self.count = count

    @property
    def compatibility(self):
        """Gets the compatibility of this Compatibilities.  # noqa: E501


        :return: The compatibility of this Compatibilities.  # noqa: E501
        :rtype: list[Compatibility]
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """Sets the compatibility of this Compatibilities.


        :param compatibility: The compatibility of this Compatibilities.  # noqa: E501
        :type: list[Compatibility]
        """

        self._compatibility = compatibility

    @property
    def count(self):
        """Gets the count of this Compatibilities.  # noqa: E501


        :return: The count of this Compatibilities.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Compatibilities.


        :param count: The count of this Compatibilities.  # noqa: E501
        :type: int
        """

        self._count = count

