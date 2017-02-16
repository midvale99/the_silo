from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

requirements = []
test_requirements = ['pytest', 'pytest-cov',
                     'sphinx', 'sphinx_rtd_theme']

setup(
    name = 'the_silo',
    version = '0.1.0',
    description='The Silo is a collection of useful tools for Nuke',
    long_description=readme,
    url='https://github.com/florianeinfalt/the_silo',
    author='Florian Einfalt',
    author_email='info@florianeinfalt.de',
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    install_requires=requirements+test_requirements,
    tests_require=test_requirements
)
