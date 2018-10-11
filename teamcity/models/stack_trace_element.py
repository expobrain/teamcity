# coding: utf-8

from teamcity.custom.base_model import TeamCityObject



class StackTraceElement(TeamCityObject):
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
        'class_name': 'str',
        'file_name': 'str',
        'line_number': 'int',
        'method_name': 'str',
        'native_method': 'bool'
    }

    attribute_map = {
        'class_name': 'className',
        'file_name': 'fileName',
        'line_number': 'lineNumber',
        'method_name': 'methodName',
        'native_method': 'nativeMethod'
    }

    def __init__(self, class_name=None, file_name=None, line_number=None, method_name=None, native_method=False, teamcity=None):  # noqa: E501
        """StackTraceElement - a model defined in Swagger"""  # noqa: E501
        super(StackTraceElement, self).__init__(teamcity=teamcity)

        self._class_name = None
        self._file_name = None
        self._line_number = None
        self._method_name = None
        self._native_method = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        if file_name is not None:
            self.file_name = file_name
        if line_number is not None:
            self.line_number = line_number
        if method_name is not None:
            self.method_name = method_name
        if native_method is not None:
            self.native_method = native_method

    @property
    def class_name(self):
        """Gets the class_name of this StackTraceElement.  # noqa: E501


        :return: The class_name of this StackTraceElement.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this StackTraceElement.


        :param class_name: The class_name of this StackTraceElement.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def file_name(self):
        """Gets the file_name of this StackTraceElement.  # noqa: E501


        :return: The file_name of this StackTraceElement.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this StackTraceElement.


        :param file_name: The file_name of this StackTraceElement.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def line_number(self):
        """Gets the line_number of this StackTraceElement.  # noqa: E501


        :return: The line_number of this StackTraceElement.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this StackTraceElement.


        :param line_number: The line_number of this StackTraceElement.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    @property
    def method_name(self):
        """Gets the method_name of this StackTraceElement.  # noqa: E501


        :return: The method_name of this StackTraceElement.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this StackTraceElement.


        :param method_name: The method_name of this StackTraceElement.  # noqa: E501
        :type: str
        """

        self._method_name = method_name

    @property
    def native_method(self):
        """Gets the native_method of this StackTraceElement.  # noqa: E501


        :return: The native_method of this StackTraceElement.  # noqa: E501
        :rtype: bool
        """
        return self._native_method

    @native_method.setter
    def native_method(self, native_method):
        """Sets the native_method of this StackTraceElement.


        :param native_method: The native_method of this StackTraceElement.  # noqa: E501
        :type: bool
        """

        self._native_method = native_method

