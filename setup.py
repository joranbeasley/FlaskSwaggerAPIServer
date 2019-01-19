from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md')) as f:
    long_description = f.read()

setup(
    name='serve-swagger',
    version='1.3',
    url='https://github.com/joranbeasley/FlaskSwaggerAPIServer',
    license='GPL',
    author='Joran Beasley',
    author_email='joranbeasley@gmail.com',
    description='serve swagger api docs locally fast',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['serve_swagger'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    entry_points={
        'console_scripts': ['serve-swagger=serve_swagger.app:serve']
    }
)
