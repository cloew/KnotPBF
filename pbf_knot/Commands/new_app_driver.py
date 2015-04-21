from pbf.templates.template_loader import TemplateLoader
from pbf_knot.templates import TemplatesRoot

class NewAppDriver:
    """ Command to create a new knot app file """
    TEMPLATE_LOADER = TemplateLoader("driver.py", TemplatesRoot, defaultFilename="main.py")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the knot app driver')
    
    def run(self, arguments):
        """ Run the command """
        self.createDriver(arguments.destination)
        
    def createDriver(self, filepath):
        """ Create a Knot App Driver Python file """
        self.TEMPLATE_LOADER.copy(filepath)