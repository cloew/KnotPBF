from pbf.templates.template_loader import TemplateLoader
from pbf_knot.templates import TemplatesRoot

class NewKnotPkg:
    """ Command to create a new knot pkg file """
    TEMPLATE_LOADER = TemplateLoader("knot-pkg.json", TemplatesRoot, defaultFilename="knot-pkg.json")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the knot pkg')
    
    def run(self, arguments):
        """ Run the command """
        self.createPackage(arguments.destination)
        
    def createPackage(self, filepath):
        """ Create a Knot Package """
        self.TEMPLATE_LOADER.copy(filepath)