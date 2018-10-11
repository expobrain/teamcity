# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.href import Href  # noqa: F401,E501


class Server(TeamCityObject):
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
        'agent_pools': 'Href',
        'agents': 'Href',
        'build_date': 'str',
        'build_number': 'str',
        'build_queue': 'Href',
        'builds': 'Href',
        'current_time': 'str',
        'internal_id': 'str',
        'projects': 'Href',
        'role': 'str',
        'start_time': 'str',
        'user_groups': 'Href',
        'users': 'Href',
        'vcs_roots': 'Href',
        'version': 'str',
        'version_major': 'int',
        'version_minor': 'int',
        'web_url': 'str'
    }

    attribute_map = {
        'agent_pools': 'agentPools',
        'agents': 'agents',
        'build_date': 'buildDate',
        'build_number': 'buildNumber',
        'build_queue': 'buildQueue',
        'builds': 'builds',
        'current_time': 'currentTime',
        'internal_id': 'internalId',
        'projects': 'projects',
        'role': 'role',
        'start_time': 'startTime',
        'user_groups': 'userGroups',
        'users': 'users',
        'vcs_roots': 'vcsRoots',
        'version': 'version',
        'version_major': 'versionMajor',
        'version_minor': 'versionMinor',
        'web_url': 'webUrl'
    }

    def __init__(self, agent_pools=None, agents=None, build_date=None, build_number=None, build_queue=None, builds=None, current_time=None, internal_id=None, projects=None, role=None, start_time=None, user_groups=None, users=None, vcs_roots=None, version=None, version_major=None, version_minor=None, web_url=None, teamcity=None):  # noqa: E501
        """Server - a model defined in Swagger"""  # noqa: E501
        super(Server, self).__init__(teamcity=teamcity)

        self._agent_pools = None
        self._agents = None
        self._build_date = None
        self._build_number = None
        self._build_queue = None
        self._builds = None
        self._current_time = None
        self._internal_id = None
        self._projects = None
        self._role = None
        self._start_time = None
        self._user_groups = None
        self._users = None
        self._vcs_roots = None
        self._version = None
        self._version_major = None
        self._version_minor = None
        self._web_url = None
        self.discriminator = None

        if agent_pools is not None:
            self.agent_pools = agent_pools
        if agents is not None:
            self.agents = agents
        if build_date is not None:
            self.build_date = build_date
        if build_number is not None:
            self.build_number = build_number
        if build_queue is not None:
            self.build_queue = build_queue
        if builds is not None:
            self.builds = builds
        if current_time is not None:
            self.current_time = current_time
        if internal_id is not None:
            self.internal_id = internal_id
        if projects is not None:
            self.projects = projects
        if role is not None:
            self.role = role
        if start_time is not None:
            self.start_time = start_time
        if user_groups is not None:
            self.user_groups = user_groups
        if users is not None:
            self.users = users
        if vcs_roots is not None:
            self.vcs_roots = vcs_roots
        if version is not None:
            self.version = version
        if version_major is not None:
            self.version_major = version_major
        if version_minor is not None:
            self.version_minor = version_minor
        if web_url is not None:
            self.web_url = web_url

    @property
    def agent_pools(self):
        """Gets the agent_pools of this Server.  # noqa: E501


        :return: The agent_pools of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._agent_pools

    @agent_pools.setter
    def agent_pools(self, agent_pools):
        """Sets the agent_pools of this Server.


        :param agent_pools: The agent_pools of this Server.  # noqa: E501
        :type: Href
        """

        self._agent_pools = agent_pools

    @property
    def agents(self):
        """Gets the agents of this Server.  # noqa: E501


        :return: The agents of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this Server.


        :param agents: The agents of this Server.  # noqa: E501
        :type: Href
        """

        self._agents = agents

    @property
    def build_date(self):
        """Gets the build_date of this Server.  # noqa: E501


        :return: The build_date of this Server.  # noqa: E501
        :rtype: str
        """
        return self._build_date

    @build_date.setter
    def build_date(self, build_date):
        """Sets the build_date of this Server.


        :param build_date: The build_date of this Server.  # noqa: E501
        :type: str
        """

        self._build_date = build_date

    @property
    def build_number(self):
        """Gets the build_number of this Server.  # noqa: E501


        :return: The build_number of this Server.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this Server.


        :param build_number: The build_number of this Server.  # noqa: E501
        :type: str
        """

        self._build_number = build_number

    @property
    def build_queue(self):
        """Gets the build_queue of this Server.  # noqa: E501


        :return: The build_queue of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._build_queue

    @build_queue.setter
    def build_queue(self, build_queue):
        """Sets the build_queue of this Server.


        :param build_queue: The build_queue of this Server.  # noqa: E501
        :type: Href
        """

        self._build_queue = build_queue

    @property
    def builds(self):
        """Gets the builds of this Server.  # noqa: E501


        :return: The builds of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._builds

    @builds.setter
    def builds(self, builds):
        """Sets the builds of this Server.


        :param builds: The builds of this Server.  # noqa: E501
        :type: Href
        """

        self._builds = builds

    @property
    def current_time(self):
        """Gets the current_time of this Server.  # noqa: E501


        :return: The current_time of this Server.  # noqa: E501
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """Sets the current_time of this Server.


        :param current_time: The current_time of this Server.  # noqa: E501
        :type: str
        """

        self._current_time = current_time

    @property
    def internal_id(self):
        """Gets the internal_id of this Server.  # noqa: E501


        :return: The internal_id of this Server.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this Server.


        :param internal_id: The internal_id of this Server.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def projects(self):
        """Gets the projects of this Server.  # noqa: E501


        :return: The projects of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this Server.


        :param projects: The projects of this Server.  # noqa: E501
        :type: Href
        """

        self._projects = projects

    @property
    def role(self):
        """Gets the role of this Server.  # noqa: E501


        :return: The role of this Server.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Server.


        :param role: The role of this Server.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def start_time(self):
        """Gets the start_time of this Server.  # noqa: E501


        :return: The start_time of this Server.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Server.


        :param start_time: The start_time of this Server.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def user_groups(self):
        """Gets the user_groups of this Server.  # noqa: E501


        :return: The user_groups of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this Server.


        :param user_groups: The user_groups of this Server.  # noqa: E501
        :type: Href
        """

        self._user_groups = user_groups

    @property
    def users(self):
        """Gets the users of this Server.  # noqa: E501


        :return: The users of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Server.


        :param users: The users of this Server.  # noqa: E501
        :type: Href
        """

        self._users = users

    @property
    def vcs_roots(self):
        """Gets the vcs_roots of this Server.  # noqa: E501


        :return: The vcs_roots of this Server.  # noqa: E501
        :rtype: Href
        """
        return self._vcs_roots

    @vcs_roots.setter
    def vcs_roots(self, vcs_roots):
        """Sets the vcs_roots of this Server.


        :param vcs_roots: The vcs_roots of this Server.  # noqa: E501
        :type: Href
        """

        self._vcs_roots = vcs_roots

    @property
    def version(self):
        """Gets the version of this Server.  # noqa: E501


        :return: The version of this Server.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Server.


        :param version: The version of this Server.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def version_major(self):
        """Gets the version_major of this Server.  # noqa: E501


        :return: The version_major of this Server.  # noqa: E501
        :rtype: int
        """
        return self._version_major

    @version_major.setter
    def version_major(self, version_major):
        """Sets the version_major of this Server.


        :param version_major: The version_major of this Server.  # noqa: E501
        :type: int
        """

        self._version_major = version_major

    @property
    def version_minor(self):
        """Gets the version_minor of this Server.  # noqa: E501


        :return: The version_minor of this Server.  # noqa: E501
        :rtype: int
        """
        return self._version_minor

    @version_minor.setter
    def version_minor(self, version_minor):
        """Sets the version_minor of this Server.


        :param version_minor: The version_minor of this Server.  # noqa: E501
        :type: int
        """

        self._version_minor = version_minor

    @property
    def web_url(self):
        """Gets the web_url of this Server.  # noqa: E501


        :return: The web_url of this Server.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this Server.


        :param web_url: The web_url of this Server.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

