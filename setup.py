from setuptools import setup, find_packages

setup(
    name = 'TraitsImageViewer',
    version = '0.1.0',
    url = '',
    author = 'Maxwell Grady',
    author_email = 'mgrady@enthought.com',
    description = 'Static image viewer using traits and model/view',
    packages = find_packages(),    
    install_requires = ['numpy', 'PyQt5', 'pyqtgraph >= 0.10.0', ],
    include_package_data=True,
)
