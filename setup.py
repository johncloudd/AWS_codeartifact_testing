from setuptools import setup, find_packages

setup(
    name='python_app',
    version='1.0.0',
    description='A Python package that does something',
    author='John',
    author_email='johndoe@example.com',
    url='https://github.com/johncloudd/AWS_codeartifact_testing',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
)
