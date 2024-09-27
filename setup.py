from setuptools import setup, find_packages

setup(
    name='converters',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow==9.3.0',
    ],
    description='A converter for images, videos, audio and text.',
    author='Ruzal',
    author_email='your.email@example.com',
    url='https://github.com/MrRuzal/converter',
)