from setuptools import setup, find_packages

setup(
    name='tools',
    version='0.1.0',
    packages=find_packages(exclude=["tests*", "examples*"]),
    install_requires=[
        'Pillow==9.3.0',
    ],
    python_requires='>=3.8',
    description='A collection of tools for converting media and performing geometry calculations.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Ruzal',
    author_email='your.email@example.com',
    url='https://github.com/MrRuzal/tools',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords='tools converter geometry image audio video text',
)
