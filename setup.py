from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="foodemo2",
    version="0.0.2",
    description="Foo demo project the II",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/FooDemo",
    author="Roberto Prevato",
    author_email="roberto.prevato@gmail.com",
    keywords="demo project",
    license="MIT",
    packages=["foo"],
    install_requires=[],
    include_package_data=True,
)
