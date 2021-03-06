# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class BackupProcessInfo(TeamCityObject):
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
        'file_name': 'str',
        'file_size': 'int',
        'finish_timestamp': 'datetime',
        'id': 'int',
        'start_timestamp': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'file_name': 'fileName',
        'file_size': 'fileSize',
        'finish_timestamp': 'finishTimestamp',
        'id': 'id',
        'start_timestamp': 'startTimestamp',
        'status': 'status'
    }

    def __init__(self, file_name=None, file_size=None, finish_timestamp=None, id=None, start_timestamp=None, status=None, teamcity=None):  # noqa: E501
        """BackupProcessInfo - a model defined in Swagger"""  # noqa: E501

        self._file_name = None
        self._file_size = None
        self._finish_timestamp = None
        self._id = None
        self._start_timestamp = None
        self._status = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if finish_timestamp is not None:
            self.finish_timestamp = finish_timestamp
        if id is not None:
            self.id = id
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if status is not None:
            self.status = status
        super(BackupProcessInfo, self).__init__(teamcity=teamcity)

    @property
    def file_name(self):
        """Gets the file_name of this BackupProcessInfo.  # noqa: E501


        :return: The file_name of this BackupProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this BackupProcessInfo.


        :param file_name: The file_name of this BackupProcessInfo.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this BackupProcessInfo.  # noqa: E501


        :return: The file_size of this BackupProcessInfo.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this BackupProcessInfo.


        :param file_size: The file_size of this BackupProcessInfo.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def finish_timestamp(self):
        """Gets the finish_timestamp of this BackupProcessInfo.  # noqa: E501


        :return: The finish_timestamp of this BackupProcessInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._finish_timestamp

    @finish_timestamp.setter
    def finish_timestamp(self, finish_timestamp):
        """Sets the finish_timestamp of this BackupProcessInfo.


        :param finish_timestamp: The finish_timestamp of this BackupProcessInfo.  # noqa: E501
        :type: datetime
        """

        self._finish_timestamp = finish_timestamp

    @property
    def id(self):
        """Gets the id of this BackupProcessInfo.  # noqa: E501


        :return: The id of this BackupProcessInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupProcessInfo.


        :param id: The id of this BackupProcessInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this BackupProcessInfo.  # noqa: E501


        :return: The start_timestamp of this BackupProcessInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this BackupProcessInfo.


        :param start_timestamp: The start_timestamp of this BackupProcessInfo.  # noqa: E501
        :type: datetime
        """

        self._start_timestamp = start_timestamp

    @property
    def status(self):
        """Gets the status of this BackupProcessInfo.  # noqa: E501


        :return: The status of this BackupProcessInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupProcessInfo.


        :param status: The status of this BackupProcessInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Running", "Cancelling", "Cancelled", "Finished", "Fault"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status
