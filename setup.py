import os
import sys

from setuptools import find_packages, setup


PYTHON3 = sys.version_info > (3, )
HERE = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(HERE, 'README.rst')) as f:
        return f.read()


def get_version():
    with open(os.path.join(HERE, 'yarn_shell/__init__.py'), 'r') as f:
        content = ''.join(f.readlines())
    env = {}
    if PYTHON3:
        exec(content, env, env)
    else:
        compiled = compile(content, 'get_version', 'single')
        eval(compiled, env, env)
    return env['__version__']


setup(
    name='yarn-shell',
    version=get_version(),
    description='',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    url='',
    author='rgs',
    author_email='rgs@pinlaptop',
    license='apache',
    packages=find_packages(),
    test_suite='yarn_shell.tests',
    scripts=['bin/yarn-shell'],
    install_requires=[
        'requests==2.12.4',
        'xcmd==0.0.2'
    ],
    tests_require=[
        'nose==1.3.7',
        'requests==2.12.4',
        'xcmd==0.0.2'

    ],
    extras_require={
        'test': [
            'nose==1.3.7',
            'requests==2.12.4',
            'xcmd==0.0.2'
        ],
    },
    include_package_data=True,
    zip_safe=False
)
