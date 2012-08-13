from setuptools import setup

setup(
    name='BootJango Form',
    version='1.0.0',
    url='https://github.com/firstthumb/bootjango-form.git',
    author='Erol KOCAMAN',
    author_email='kocamanerol@gmail.com',
    license='Apache License 2.0',
    packages=['bootjango', 'bootjango.templatetags'],
    include_package_data=True,
    description='Bootstrap support for Django projects',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
