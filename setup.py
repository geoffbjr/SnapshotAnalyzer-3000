from setuptools import setup

setup (
    name = 'snapshotanalyzer-3000',
    version='0.1',
    author='Geoff Barnes',
    description='Manage AWS EC2 snapshots',
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/geoffbjr/SnapshotAnalyzer-3000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
