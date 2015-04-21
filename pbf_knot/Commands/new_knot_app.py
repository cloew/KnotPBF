from pbf.templates.template_loader import TemplateLoader
from pbf_knot.templates import TemplatesRoot

class NewKnotApp:
    """ Command to create a new knot app file """
    TEMPLATE_LOADER = TemplateLoader("app.knot-app", TemplatesRoot, defaultFilename="app.knot-app")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the knot pkg')
    
    def run(self, arguments):
        """ Run the command """
        self.createAppConfig(arguments.destination)
        
    def createAppConfig(self, filepath):
        """ Create a Knot App Config """
        self.TEMPLATE_LOADER.copy(filepath)