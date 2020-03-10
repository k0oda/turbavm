from distutils.core import setup
import turba

setup(
    name='Turba',
    description='Turba virtual machine emulator',
    author='Evgeny Kuleshov',
    author_email='kulevgen32@gmail.com',
    version=turba.__version__,
    packages=['turba'],
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: System :: Emulators',
        'License :: OSI Approved :: MIT License'
    ]
)
