from setuptools import setup, find_packages

packages = find_packages()

setup(  name='organizer', 
        version='0.0.1',
        description='Something to organize my life',
        author='Luke Campbell',
        author_email='luke.s.campbell@gmail.com',
        url='https://github.com/lukecampbell/organizer/',
        packages=packages,
        package_data={'organizer' : ['config/*.yml']},
        install_requires=['sqlalchemy']
        )


