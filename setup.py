from distutils.core import setup

setup(
    name='PyFuck',
    version='1.0',
    packages=['pyfuck'],
    url='https://github.com/pax0r/pyfuck',
    license='Apache 2.0',
    author='pax0r',
    author_email='pax0r@o2.pl',
    description='Python Brainfuck interpreter',
    entry_points={
        'console_scripts': [
            'bf = pyfuck.__main__:code'
        ]
    },
)
