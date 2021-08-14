import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='acutils',
    version='0.1.1',
    author='Casokaks',
    author_email='casokaks@gmail.com',
    description='Collection on python utility functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Casokaks/acutils',
    project_urls = {
        "Bug Tracker": "https://github.com/Casokaks/acutils/issues"
    },
    license='MIT',
    packages=['acutils'],
    install_requires=['plotly',],
)
