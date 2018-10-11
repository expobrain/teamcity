# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.properties import Properties  # noqa: F401,E501


class Trigger(TeamCityObject):
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
        'disabled': 'bool',
        'href': 'str',
        'id': 'str',
        'inherited': 'bool',
        'name': 'str',
        'properties': 'Properties',
        'type': 'str'
    }

    attribute_map = {
        'disabled': 'disabled',
        'href': 'href',
        'id': 'id',
        'inherited': 'inherited',
        'name': 'name',
        'properties': 'properties',
        'type': 'type'
    }

    def __init__(self, disabled=False, href=None, id=None, inherited=False, name=None, properties=None, type=None, teamcity=None):  # noqa: E501
        """Trigger - a model defined in Swagger"""  # noqa: E501
        super(Trigger, self).__init__(teamcity=teamcity)

        self._disabled = None
        self._href = None
        self._id = None
        self._inherited = None
        self._name = None
        self._properties = None
        self._type = None
        self.discriminator = None

        if disabled is not None:
            self.disabled = disabled
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if inherited is not None:
            self.inherited = inherited
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if type is not None:
            self.type = type

    @property
    def disabled(self):
        """Gets the disabled of this Trigger.  # noqa: E501


        :return: The disabled of this Trigger.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this Trigger.


        :param disabled: The disabled of this Trigger.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def href(self):
        """Gets the href of this Trigger.  # noqa: E501


        :return: The href of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Trigger.


        :param href: The href of this Trigger.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Trigger.  # noqa: E501


        :return: The id of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Trigger.


        :param id: The id of this Trigger.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inherited(self):
        """Gets the inherited of this Trigger.  # noqa: E501


        :return: The inherited of this Trigger.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this Trigger.


        :param inherited: The inherited of this Trigger.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def name(self):
        """Gets the name of this Trigger.  # noqa: E501


        :return: The name of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Trigger.


        :param name: The name of this Trigger.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this Trigger.  # noqa: E501


        :return: The properties of this Trigger.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Trigger.


        :param properties: The properties of this Trigger.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this Trigger.  # noqa: E501


        :return: The type of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Trigger.


        :param type: The type of this Trigger.  # noqa: E501
        :type: str
        """

        self._type = type

