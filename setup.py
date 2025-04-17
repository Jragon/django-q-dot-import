from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name='django-q-dot-import',
    version='0.1.0',
    author='Daniel Welch, Christo Goosen',
    author_email='dwelch2102@gmail.com, christogoosen@gmail.com',
    keywords='django distributed task queue worker scheduler cron redis disque ironmq sqs orm mongodb multiprocessing',
    packages=find_packages(include=['django-q-dot-import'], exclude=['.venv', 'dist','build', 'django-q-dot-import*egg-info']),
    install_requires=[],
    url='https://django-q2.readthedocs.org',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
