import setuptools

setuptools.setup(
    name="conversations_dagster",
    packages=setuptools.find_packages(exclude=["conversations_dagster_tests"]),
    install_requires=[
        "dagster==0.13.0",
        "dagit==0.13.0",
        "pytest",
    ],
)
