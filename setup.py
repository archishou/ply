from setuptools import setup

setup(
    name="ply",
    version='0.1',
    py_modules=['ply'],
    install_requires=[
        'Click', 'pygame',
    ],
    entry_points='''
        [console_scripts]
        ply=ply:cli
    ''',
)
