# coding: utf-8

from teamcity.custom.base_model import TeamCityObject


# from teamcity.models.build_types import BuildTypes  # noqa: F401,E501
# from teamcity.models.links import Links  # noqa: F401,E501
# from teamcity.models.project import Project  # noqa: F401,E501
# from teamcity.models.project_features import ProjectFeatures  # noqa: F401,E501
# from teamcity.models.projects import Projects  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501
# from teamcity.models.state_field import StateField  # noqa: F401,E501
# from teamcity.models.vcs_roots import VcsRoots  # noqa: F401,E501


class Project(TeamCityObject):
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
        'archived': 'bool',
        'build_types': 'BuildTypes',
        'description': 'str',
        'href': 'str',
        'id': 'str',
        'internal_id': 'str',
        'links': 'Links',
        'locator': 'str',
        'name': 'str',
        'parameters': 'Properties',
        'parent_project': 'Project',
        'parent_project_id': 'str',
        'parent_project_internal_id': 'str',
        'parent_project_name': 'str',
        'project_features': 'ProjectFeatures',
        'projects': 'Projects',
        'read_only_ui': 'StateField',
        'templates': 'BuildTypes',
        'uuid': 'str',
        'vcs_roots': 'VcsRoots',
        'web_url': 'str'
    }

    attribute_map = {
        'archived': 'archived',
        'build_types': 'buildTypes',
        'description': 'description',
        'href': 'href',
        'id': 'id',
        'internal_id': 'internalId',
        'links': 'links',
        'locator': 'locator',
        'name': 'name',
        'parameters': 'parameters',
        'parent_project': 'parentProject',
        'parent_project_id': 'parentProjectId',
        'parent_project_internal_id': 'parentProjectInternalId',
        'parent_project_name': 'parentProjectName',
        'project_features': 'projectFeatures',
        'projects': 'projects',
        'read_only_ui': 'readOnlyUI',
        'templates': 'templates',
        'uuid': 'uuid',
        'vcs_roots': 'vcsRoots',
        'web_url': 'webUrl'
    }

    def __init__(self, archived=False, build_types=None, description=None, href=None, id=None, internal_id=None, links=None, locator=None, name=None, parameters=None, parent_project=None, parent_project_id=None, parent_project_internal_id=None, parent_project_name=None, project_features=None, projects=None, read_only_ui=None, templates=None, uuid=None, vcs_roots=None, web_url=None, teamcity=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        super(Project, self).__init__(teamcity=teamcity)

        self._archived = None
        self._build_types = None
        self._description = None
        self._href = None
        self._id = None
        self._internal_id = None
        self._links = None
        self._locator = None
        self._name = None
        self._parameters = None
        self._parent_project = None
        self._parent_project_id = None
        self._parent_project_internal_id = None
        self._parent_project_name = None
        self._project_features = None
        self._projects = None
        self._read_only_ui = None
        self._templates = None
        self._uuid = None
        self._vcs_roots = None
        self._web_url = None
        self.discriminator = None

        if archived is not None:
            self.archived = archived
        if build_types is not None:
            self.build_types = build_types
        if description is not None:
            self.description = description
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if links is not None:
            self.links = links
        if locator is not None:
            self.locator = locator
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters
        if parent_project is not None:
            self.parent_project = parent_project
        if parent_project_id is not None:
            self.parent_project_id = parent_project_id
        if parent_project_internal_id is not None:
            self.parent_project_internal_id = parent_project_internal_id
        if parent_project_name is not None:
            self.parent_project_name = parent_project_name
        if project_features is not None:
            self.project_features = project_features
        if projects is not None:
            self.projects = projects
        if read_only_ui is not None:
            self.read_only_ui = read_only_ui
        if templates is not None:
            self.templates = templates
        if uuid is not None:
            self.uuid = uuid
        if vcs_roots is not None:
            self.vcs_roots = vcs_roots
        if web_url is not None:
            self.web_url = web_url

    @property
    def archived(self):
        """Gets the archived of this Project.  # noqa: E501


        :return: The archived of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Project.


        :param archived: The archived of this Project.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def build_types(self):
        """Gets the build_types of this Project.  # noqa: E501


        :return: The build_types of this Project.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._build_types

    @build_types.setter
    def build_types(self, build_types):
        """Sets the build_types of this Project.


        :param build_types: The build_types of this Project.  # noqa: E501
        :type: BuildTypes
        """

        self._build_types = build_types

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501


        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.


        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this Project.  # noqa: E501


        :return: The href of this Project.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Project.


        :param href: The href of this Project.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this Project.  # noqa: E501


        :return: The internal_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this Project.


        :param internal_id: The internal_id of this Project.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def links(self):
        """Gets the links of this Project.  # noqa: E501


        :return: The links of this Project.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Project.


        :param links: The links of this Project.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def locator(self):
        """Gets the locator of this Project.  # noqa: E501


        :return: The locator of this Project.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Project.


        :param locator: The locator of this Project.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this Project.  # noqa: E501


        :return: The parameters of this Project.  # noqa: E501
        :rtype: Properties
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Project.


        :param parameters: The parameters of this Project.  # noqa: E501
        :type: Properties
        """

        self._parameters = parameters

    @property
    def parent_project(self):
        """Gets the parent_project of this Project.  # noqa: E501


        :return: The parent_project of this Project.  # noqa: E501
        :rtype: Project
        """
        return self._parent_project

    @parent_project.setter
    def parent_project(self, parent_project):
        """Sets the parent_project of this Project.


        :param parent_project: The parent_project of this Project.  # noqa: E501
        :type: Project
        """

        self._parent_project = parent_project

    @property
    def parent_project_id(self):
        """Gets the parent_project_id of this Project.  # noqa: E501


        :return: The parent_project_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_project_id

    @parent_project_id.setter
    def parent_project_id(self, parent_project_id):
        """Sets the parent_project_id of this Project.


        :param parent_project_id: The parent_project_id of this Project.  # noqa: E501
        :type: str
        """

        self._parent_project_id = parent_project_id

    @property
    def parent_project_internal_id(self):
        """Gets the parent_project_internal_id of this Project.  # noqa: E501


        :return: The parent_project_internal_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_project_internal_id

    @parent_project_internal_id.setter
    def parent_project_internal_id(self, parent_project_internal_id):
        """Sets the parent_project_internal_id of this Project.


        :param parent_project_internal_id: The parent_project_internal_id of this Project.  # noqa: E501
        :type: str
        """

        self._parent_project_internal_id = parent_project_internal_id

    @property
    def parent_project_name(self):
        """Gets the parent_project_name of this Project.  # noqa: E501


        :return: The parent_project_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_project_name

    @parent_project_name.setter
    def parent_project_name(self, parent_project_name):
        """Sets the parent_project_name of this Project.


        :param parent_project_name: The parent_project_name of this Project.  # noqa: E501
        :type: str
        """

        self._parent_project_name = parent_project_name

    @property
    def project_features(self):
        """Gets the project_features of this Project.  # noqa: E501


        :return: The project_features of this Project.  # noqa: E501
        :rtype: ProjectFeatures
        """
        return self._project_features

    @project_features.setter
    def project_features(self, project_features):
        """Sets the project_features of this Project.


        :param project_features: The project_features of this Project.  # noqa: E501
        :type: ProjectFeatures
        """

        self._project_features = project_features

    @property
    def projects(self):
        """Gets the projects of this Project.  # noqa: E501


        :return: The projects of this Project.  # noqa: E501
        :rtype: Projects
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this Project.


        :param projects: The projects of this Project.  # noqa: E501
        :type: Projects
        """

        self._projects = projects

    @property
    def read_only_ui(self):
        """Gets the read_only_ui of this Project.  # noqa: E501


        :return: The read_only_ui of this Project.  # noqa: E501
        :rtype: StateField
        """
        return self._read_only_ui

    @read_only_ui.setter
    def read_only_ui(self, read_only_ui):
        """Sets the read_only_ui of this Project.


        :param read_only_ui: The read_only_ui of this Project.  # noqa: E501
        :type: StateField
        """

        self._read_only_ui = read_only_ui

    @property
    def templates(self):
        """Gets the templates of this Project.  # noqa: E501


        :return: The templates of this Project.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this Project.


        :param templates: The templates of this Project.  # noqa: E501
        :type: BuildTypes
        """

        self._templates = templates

    @property
    def uuid(self):
        """Gets the uuid of this Project.  # noqa: E501


        :return: The uuid of this Project.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Project.


        :param uuid: The uuid of this Project.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def vcs_roots(self):
        """Gets the vcs_roots of this Project.  # noqa: E501


        :return: The vcs_roots of this Project.  # noqa: E501
        :rtype: VcsRoots
        """
        return self._vcs_roots

    @vcs_roots.setter
    def vcs_roots(self, vcs_roots):
        """Sets the vcs_roots of this Project.


        :param vcs_roots: The vcs_roots of this Project.  # noqa: E501
        :type: VcsRoots
        """

        self._vcs_roots = vcs_roots

    @property
    def web_url(self):
        """Gets the web_url of this Project.  # noqa: E501


        :return: The web_url of this Project.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this Project.


        :param web_url: The web_url of this Project.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

