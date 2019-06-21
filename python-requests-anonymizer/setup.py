from setuptools import setup

setup(
    name='requests_anonymizer',
    version='0.3',
    packages=['.'],
    url='https://github.com/assem-ch/python-requests-anonymizer',
    install_requires=['grequests', 'pysocks'],
    license='MIT',
    author='Assem Chelli; Niboucha Redouane',
    author_email='',
    description='An anonymizing tool to be used for requests api calls'
)
