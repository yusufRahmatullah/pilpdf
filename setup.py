from setuptools import setup

setup(
    name="pilpdf",
    version="2021.10.03",
    description="Convert images to PDF using PIL",
    author="Yusuf Rahmatullah",
    author_email="yusufr.main@gmail.com",
    url="",
    py_modules=['pilpdf'],
    entry_points={
        'console_scripts': [
            'pilpdf = pilpdf:main'
        ]
    },
)
