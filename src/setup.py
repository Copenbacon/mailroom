"""The Setup File for our Mailroom App."""


from setuptools import setup

setup(
    name="Mailroom",
    description="An implementation of the Mailroom Module",
    version=0.1,
    author=["Conor Clary", "Regenal Grant"],
    author_email=["sclary50@gmail.com", "regenal@mac.com"],
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['main'],
    install_requires=[],
    extras_require={
        "test": ['pytest', 'pytest-watch', 'pytest-cov', 'tox'],
    },
    entry_points={
        'console_scripts': [
            "main = main:main"
        ],
    }
)
