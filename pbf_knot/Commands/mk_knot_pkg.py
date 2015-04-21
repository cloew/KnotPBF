from .new_knot_pkg import NewKnotPkg
from pbf_python.Commands.mk_pydir import MakePyDir

class MkKnotPkg:
    """ Command to create a knot package """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('directory', action='store', help='Directory to create as a Knot package')
        parser.add_argument('-i', '--install', action='store_true', help='Add the new package to the setup install file')
    
    def run(self, arguments):
        """ Run the command """
        self.makeKnotPackage(arguments.directory, arguments.install)
        
    def makeKnotPackage(self, dirname, install=False):
        """ Make a Knot Package """
        MakePyDir().makePyDir(dirname, install=install)
        NewKnotPkg().createPackage(dirname)