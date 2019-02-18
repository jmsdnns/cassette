from setuptools import setup, find_packages

import cassette


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='cassette',
    author='Jms Dnns',
    author_email='jdennis@gmail.com',
    version=cassette.__version__,
    description=cassette.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/jmsdnns/cassette',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'youtube-dl',
    ],
    entry_points={'console_scripts': [
        'cassette = cassette.cassette:main',
    ]},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only', # yup
    ]
)
