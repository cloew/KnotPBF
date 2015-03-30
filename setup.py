from distutils.core import setup

setup(name='pbf_knot',
      version='.1',
      description="Programmer's Best Friend Utility Extension for pbf_knot",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf_knot', 'pbf_knot.Commands', 'pbf_knot.templates'],
      #package_data = {'pbf_knot.templates':[]}, # Add template files
     )