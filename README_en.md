<a name="readme-top"></a>

[JA](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# TMC WRS GZ

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#launch-and-usage">Launch and Usage</a></li>
    <li><a href="#milestone">Milestone</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- INTRODUCTION -->
## Introduction
This package imports and launches the World and models of the World Robot Summit (WRS) 2020, provided by TMC, on Gazebo Sim.


<!-- GETTING STARTED -->
## Getting Started

This section describes how to set up this repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

First, please set up the following environment before proceeding to the next installation stage.

| System  | Version |
| --- | --- |
| Ubuntu | 22.04 (Jammy Jellyfish) |
| ROS    | Humble Hawksbill |
| Python | 3.10 |
| Gazebo | Fortress |

> [!NOTE]
> If you need to install `Ubuntu` or `ROS`, please check our [SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6).


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

**Development environment (local or Docker) where you will use TMC WRS GZ**

1. Go to the `src` folder of ROS.
    ```sh
    $ cd ~/colcon_ws/src/
    ```

2. Clone this repository.
    ```sh
    $ git clone -b humble-devel https://github.com/TeamSOBITS/tmc_wrs_gz
    ```
3. Compile the package.
    ```sh
    $ cd ~/colcon_ws/
    $ colcon build --symlink-install
    $ source ~/colcon_ws/install/setup.sh
    ```
4. Add path to the environment variable GZ_SIM_RESOURCE_PATH.
     ```sh
    $ echo "export GZ_SIM_RESOURCE_PATH=${GZ_SIM_RESOURCE_PATH}:~/colcon_ws/install/tmc_wrs_gz_worlds/share/tmc_wrs_gz_worlds/models" >> ~/.bashrc
    ```

<!-- LAUNCH AND USAGE -->
## Launch and Usage

1. Launch the WRS2020 World model on Gazebo Sim.
    ```sh
    $ ros2 launch tmc_wrs_gz tmc_wrs_world.launch.py
    ```

<!-- LICENSE -->
## License

This software except object models is released under the BSD 3-Clause Clear License, see [LICENSE.txt](license-url).

Regarding the license of object models, see [README.md](tmc_wrs_gazebo_worlds/README.md) in the tmc_wrs_gazebo_worlds package.


<!-- MILESTONE -->
## Milestone

- [ ] Add support to import object models

See the [open issues][issues-url] for a full list of proposed features (and known issues).


<!-- REFERENCES -->
## References

* [World Robot Summit](https://worldrobotsummit.org)
* [Gazebo Sim](https://gazebosim.org)
* [tmc_wrs_gazebo](https://github.com/hsr-project/tmc_wrs_gazebo)
* [YCB Object and Model set](https://www.ycbbenchmarks.com)
* [person_standing Model](https://github.com/osrf/gazebo_models)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TeamSOBITS/tmc_wrs_gz.svg?style=for-the-badge
[contributors-url]: https://github.com/TeamSOBITS/tmc_wrs_gz/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TeamSOBITS/tmc_wrs_gz.svg?style=for-the-badge
[forks-url]: https://github.com/TeamSOBITS/tmc_wrs_gz/network/members
[stars-shield]: https://img.shields.io/github/stars/TeamSOBITS/tmc_wrs_gz.svg?style=for-the-badge
[stars-url]: https://github.com/TeamSOBITS/tmc_wrs_gz/stargazers
[issues-shield]: https://img.shields.io/github/issues/TeamSOBITS/tmc_wrs_gz.svg?style=for-the-badge
[issues-url]: https://github.com/TeamSOBITS/tmc_wrs_gz/issues
[license-shield]: https://img.shields.io/github/license/TeamSOBITS/tmc_wrs_gz.svg?style=for-the-badge
[license-url]: LICENSE.txt