from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')


name = "datascience-starter"
default_task = ['install_dependencies', 'analyze', 'publish']

@init
def set_properties(project):
    project.build_depends_on('coverage')

    #dependencies - whatever you can install using pip
    project.depends_on_requirements("requirements.txt")

    #unit test / build dependencies
    project.build_depends_on('mockito')

    project.set_property('coverage_break_build', True)

    pass
