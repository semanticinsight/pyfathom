import pathlib
from setuptools import setup
from setuptools_databricks import DatabricksBuild
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
DATABRICKS_RUNTIME="dbr7.3"

# This call to setup() does all the work
setup(
    name=f"pyfathom",
    cmdclass={"build_databricks_project": DatabricksBuild},
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}",
        "dirty_template": "{tag}.dev{ccount}.git{sha}.dirty",
        "starting_version": "0.1.0",
        "version_callback": None,
        "version_file": None,
        "count_commits_from_version_file": False
    },
    setup_requires=['setuptools-git-versioning'],
    description="Azure Databricks Utilities",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/semanticinsight/pyfathom.git",
    author="Shaun Ryan",
    author_email="shaun.ryan@bjss.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["fathom"],
    zip_safe=False
)
