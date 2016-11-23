from setuptools import setup
setup(
    name='envr',
    packages=['envr'],
    version='0.1.3',
    description=('Manipulate and transform .env files ' +
                 'that work on Heroku and are POSIX-compliant shell scripts.'),
    install_requires=[
        'six'
    ],
    author='ypcrts',
    author_email='ypcrts',
    url='https://github.com/ypcrts/envr',
    keywords=['env', 'dotenv', 'heroku', 'environment'],
    license='MPL 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Environment :: Web Environment',
    ]
)
