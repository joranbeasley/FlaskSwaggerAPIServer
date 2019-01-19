from setuptools import setup

setup(
    name='serve-swagger',
    version='1.0.0',
    url='https://github.com/joranbeasley/ServeSwagger',
    license='GPL',
    author='Joran Beasley',
    author_email='joranbeasley@gmail.com',
    description='serve swagger api docs locally fast',
    packages=['serve_swagger'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    entry_points={
        'console_scripts': ['serve-swagger=serve_swagger.app:serve']
    }
)
