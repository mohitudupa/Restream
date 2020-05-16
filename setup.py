"""
Setup file
"""


import setuptools


with open('README.md', 'r', encoding='utf-8') as f:
    long_description_content = f.read()


setuptools.setup(
    name="restream",
    version="0.0.7",
    author="Mohit Udupa",
    author_email="mohitudupa@gmail.com",
    description="A python library to parse strings based on tokens and grammar rules.",
    license='MIT',
    long_description=long_description_content,
    long_description_content_type="text/markdown",
    url="https://github.com/mohitudupa/restream",
    packages=['restream'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    platforms=['any'],
)
