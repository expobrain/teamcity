# coding: utf-8

from teamcity.custom.base_model import TeamCityObject



class Type(TeamCityObject):
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
        'raw_value': 'str'
    }

    attribute_map = {
        'raw_value': 'rawValue'
    }

    def __init__(self, raw_value=None, teamcity=None):  # noqa: E501
        """Type - a model defined in Swagger"""  # noqa: E501
        super(Type, self).__init__(teamcity=teamcity)

        self._raw_value = None
        self.discriminator = None

        if raw_value is not None:
            self.raw_value = raw_value

    @property
    def raw_value(self):
        """Gets the raw_value of this Type.  # noqa: E501


        :return: The raw_value of this Type.  # noqa: E501
        :rtype: str
        """
        return self._raw_value

    @raw_value.setter
    def raw_value(self, raw_value):
        """Sets the raw_value of this Type.


        :param raw_value: The raw_value of this Type.  # noqa: E501
        :type: str
        """

        self._raw_value = raw_value

