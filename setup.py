from setuptools import setup

setup(
    name="replacex",
    version="1.3.4",
    license='MIT',
    description="Replace string with regular expression for all files in current folder",
    author='1e0n',
    author_email='i@leons.im',
    keywords='replace all string regular expression folder',
    url='https://github.com/leonsim/replacex',
    packages=['replacex'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'replacex=replacex:main',
        ],
    },
)
