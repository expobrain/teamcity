# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.problems import Problems  # noqa: F401,E501
# from teamcity.models.tests import Tests  # noqa: F401,E501


class ProblemTarget(TeamCityObject):
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
        'any_problem': 'bool',
        'problems': 'Problems',
        'tests': 'Tests'
    }

    attribute_map = {
        'any_problem': 'anyProblem',
        'problems': 'problems',
        'tests': 'tests'
    }

    def __init__(self, any_problem=False, problems=None, tests=None, teamcity=None):  # noqa: E501
        """ProblemTarget - a model defined in Swagger"""  # noqa: E501
        super(ProblemTarget, self).__init__(teamcity=teamcity)

        self._any_problem = None
        self._problems = None
        self._tests = None
        self.discriminator = None

        if any_problem is not None:
            self.any_problem = any_problem
        if problems is not None:
            self.problems = problems
        if tests is not None:
            self.tests = tests

    @property
    def any_problem(self):
        """Gets the any_problem of this ProblemTarget.  # noqa: E501


        :return: The any_problem of this ProblemTarget.  # noqa: E501
        :rtype: bool
        """
        return self._any_problem

    @any_problem.setter
    def any_problem(self, any_problem):
        """Sets the any_problem of this ProblemTarget.


        :param any_problem: The any_problem of this ProblemTarget.  # noqa: E501
        :type: bool
        """

        self._any_problem = any_problem

    @property
    def problems(self):
        """Gets the problems of this ProblemTarget.  # noqa: E501


        :return: The problems of this ProblemTarget.  # noqa: E501
        :rtype: Problems
        """
        return self._problems

    @problems.setter
    def problems(self, problems):
        """Sets the problems of this ProblemTarget.


        :param problems: The problems of this ProblemTarget.  # noqa: E501
        :type: Problems
        """

        self._problems = problems

    @property
    def tests(self):
        """Gets the tests of this ProblemTarget.  # noqa: E501


        :return: The tests of this ProblemTarget.  # noqa: E501
        :rtype: Tests
        """
        return self._tests

    @tests.setter
    def tests(self, tests):
        """Sets the tests of this ProblemTarget.


        :param tests: The tests of this ProblemTarget.  # noqa: E501
        :type: Tests
        """

        self._tests = tests

