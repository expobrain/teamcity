# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.groups import Groups  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501
# from teamcity.models.roles import Roles  # noqa: F401,E501
# from teamcity.models.users import Users  # noqa: F401,E501


class Group(TeamCityObject):
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
        'child_groups': 'Groups',
        'description': 'str',
        'href': 'str',
        'key': 'str',
        'name': 'str',
        'parent_groups': 'Groups',
        'properties': 'Properties',
        'roles': 'Roles',
        'users': 'Users'
    }

    attribute_map = {
        'child_groups': 'child-groups',
        'description': 'description',
        'href': 'href',
        'key': 'key',
        'name': 'name',
        'parent_groups': 'parent-groups',
        'properties': 'properties',
        'roles': 'roles',
        'users': 'users'
    }

    def __init__(self, child_groups=None, description=None, href=None, key=None, name=None, parent_groups=None, properties=None, roles=None, users=None, teamcity=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        super(Group, self).__init__(teamcity=teamcity)

        self._child_groups = None
        self._description = None
        self._href = None
        self._key = None
        self._name = None
        self._parent_groups = None
        self._properties = None
        self._roles = None
        self._users = None
        self.discriminator = None

        if child_groups is not None:
            self.child_groups = child_groups
        if description is not None:
            self.description = description
        if href is not None:
            self.href = href
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if parent_groups is not None:
            self.parent_groups = parent_groups
        if properties is not None:
            self.properties = properties
        if roles is not None:
            self.roles = roles
        if users is not None:
            self.users = users

    @property
    def child_groups(self):
        """Gets the child_groups of this Group.  # noqa: E501


        :return: The child_groups of this Group.  # noqa: E501
        :rtype: Groups
        """
        return self._child_groups

    @child_groups.setter
    def child_groups(self, child_groups):
        """Sets the child_groups of this Group.


        :param child_groups: The child_groups of this Group.  # noqa: E501
        :type: Groups
        """

        self._child_groups = child_groups

    @property
    def description(self):
        """Gets the description of this Group.  # noqa: E501


        :return: The description of this Group.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Group.


        :param description: The description of this Group.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this Group.  # noqa: E501


        :return: The href of this Group.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Group.


        :param href: The href of this Group.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def key(self):
        """Gets the key of this Group.  # noqa: E501


        :return: The key of this Group.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Group.


        :param key: The key of this Group.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501


        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.


        :param name: The name of this Group.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_groups(self):
        """Gets the parent_groups of this Group.  # noqa: E501


        :return: The parent_groups of this Group.  # noqa: E501
        :rtype: Groups
        """
        return self._parent_groups

    @parent_groups.setter
    def parent_groups(self, parent_groups):
        """Sets the parent_groups of this Group.


        :param parent_groups: The parent_groups of this Group.  # noqa: E501
        :type: Groups
        """

        self._parent_groups = parent_groups

    @property
    def properties(self):
        """Gets the properties of this Group.  # noqa: E501


        :return: The properties of this Group.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Group.


        :param properties: The properties of this Group.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def roles(self):
        """Gets the roles of this Group.  # noqa: E501


        :return: The roles of this Group.  # noqa: E501
        :rtype: Roles
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Group.


        :param roles: The roles of this Group.  # noqa: E501
        :type: Roles
        """

        self._roles = roles

    @property
    def users(self):
        """Gets the users of this Group.  # noqa: E501


        :return: The users of this Group.  # noqa: E501
        :rtype: Users
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Group.


        :param users: The users of this Group.  # noqa: E501
        :type: Users
        """

        self._users = users

