## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
from setuptools import setup

package_name = 'tmc_wrs_gz_worlds'

setup(
    name=package_name,
    version='0.21.2',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Yosuke Matsusaka, Nobuyuki Matsuno',
    maintainer='Keith Valentin',
    maintainer_email='kvalentincardenas@gmail.com',
    description='World and model files for WRS Gazebo simulator.',
    license='BSD 3-clause Clear License',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'spawn_objects = tmc_wrs_gz_worlds.spawn_objects:main',
            'randomizer = tmc_wrs_gz_worlds.randomizer:main',
        ],
    },
)
