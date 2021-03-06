# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.comment import Comment  # noqa: F401,E501
# from dohq_teamcity.models.problem_scope import ProblemScope  # noqa: F401,E501
# from dohq_teamcity.models.problem_target import ProblemTarget  # noqa: F401,E501
# from dohq_teamcity.models.resolution import Resolution  # noqa: F401,E501


class Mute(TeamCityObject):
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
        'assignment': 'Comment',
        'id': 'int',
        'resolution': 'Resolution',
        'scope': 'ProblemScope',
        'target': 'ProblemTarget'
    }

    attribute_map = {
        'assignment': 'assignment',
        'id': 'id',
        'resolution': 'resolution',
        'scope': 'scope',
        'target': 'target'
    }

    def __init__(self, assignment=None, id=None, resolution=None, scope=None, target=None, teamcity=None):  # noqa: E501
        """Mute - a model defined in Swagger"""  # noqa: E501

        self._assignment = None
        self._id = None
        self._resolution = None
        self._scope = None
        self._target = None
        self.discriminator = None

        if assignment is not None:
            self.assignment = assignment
        if id is not None:
            self.id = id
        if resolution is not None:
            self.resolution = resolution
        if scope is not None:
            self.scope = scope
        if target is not None:
            self.target = target
        super(Mute, self).__init__(teamcity=teamcity)

    @property
    def assignment(self):
        """Gets the assignment of this Mute.  # noqa: E501


        :return: The assignment of this Mute.  # noqa: E501
        :rtype: Comment
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Sets the assignment of this Mute.


        :param assignment: The assignment of this Mute.  # noqa: E501
        :type: Comment
        """

        self._assignment = assignment

    @property
    def id(self):
        """Gets the id of this Mute.  # noqa: E501


        :return: The id of this Mute.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Mute.


        :param id: The id of this Mute.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def resolution(self):
        """Gets the resolution of this Mute.  # noqa: E501


        :return: The resolution of this Mute.  # noqa: E501
        :rtype: Resolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this Mute.


        :param resolution: The resolution of this Mute.  # noqa: E501
        :type: Resolution
        """

        self._resolution = resolution

    @property
    def scope(self):
        """Gets the scope of this Mute.  # noqa: E501


        :return: The scope of this Mute.  # noqa: E501
        :rtype: ProblemScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Mute.


        :param scope: The scope of this Mute.  # noqa: E501
        :type: ProblemScope
        """

        self._scope = scope

    @property
    def target(self):
        """Gets the target of this Mute.  # noqa: E501


        :return: The target of this Mute.  # noqa: E501
        :rtype: ProblemTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Mute.


        :param target: The target of this Mute.  # noqa: E501
        :type: ProblemTarget
        """

        self._target = target
