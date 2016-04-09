from pecan import expose

from repoxplorer import index
from repoxplorer.index.commits import Commits
from repoxplorer.index.projects import Projects


class RootController(object):

    @expose(template='index.html')
    def index(self):
        projects = Projects().get_projects()
        return {'projects': projects}