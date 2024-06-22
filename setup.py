from setuptools import setup, find_packages

setup(
    name='wexample-workspaces',
    version=open('version.txt').read(),
    author='weeger',
    author_email='contact@wexample.com',
    description='Helper to manage local directories',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wexample/python-workspaces',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pydantic'
    ],
    python_requires='>=3.6',
)
