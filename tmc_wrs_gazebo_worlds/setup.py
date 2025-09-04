## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
import os
from glob import glob
from setuptools import setup

package_name = 'tmc_wrs_gz_worlds'

data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ]

def package_files(data_files, directory_list):

    paths_dict = {}

    for directory in directory_list:
        
        for (path, directories, filenames) in os.walk(directory):

            for filename in filenames:

                file_path = os.path.join(path, filename)
                install_path = os.path.join('share', package_name, path)
                
                if install_path in paths_dict.keys():
                    paths_dict[install_path].append(file_path)
                    
                else:
                    paths_dict[install_path] = [file_path]
                
    for key in paths_dict.keys():
        data_files.append((key, paths_dict[key]))

    return data_files

setup(
    name=package_name,
    version='0.21.2',
    packages=[package_name],
    data_files=package_files(data_files, ['models/', 'worlds/', 'hooks']),
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
