<a name="readme-top"></a>

[JA](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# TMC WRS GZ

<!-- 目次 -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#環境構築">環境構築</a>
      <ul>
        <li><a href="#環境条件">環境条件</a></li>
        <li><a href="#インストール方法">インストール方法</a></li>
      </ul>
    </li>
    <li><a href="#実行方法">実行方法</a></li>
    <li><a href="#マイルストーン">マイルストーン</a></li>
    <li><a href="#ライセンス">License</a></li>
  </ol>
</details>


<!-- 概要 -->
## 概要
本パッケージは，TMCにより提供されるWorld Robot Summit（WRS）2020のWorldやモデルをGazebo Sim上にインポートし起動します．


<!-- セットアップ -->
## セットアップ

ここで，本レポジトリのセットアップ方法について説明します．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### 環境条件

まず，以下の環境を整えてから，次のインストール段階に進んでください．

| System  | Version |
| --- | --- |
| Ubuntu | 22.04 (Jammy Jellyfish) |
| ROS    | Humble Hawksbill |
| Python | 3.10 |
| Gazebo | Fortress |

> [!NOTE]
> `Ubuntu`や`ROS`のインストール方法に関しては，[SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)に参照してください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### インストール方法

**TMC WRS GZを使用するローカル環境，またはDockerコンテナ内でのセットアップ内容**
1. ROSの`src`フォルダに移動します．
    ```sh
    $ cd ~/colcon_ws/src/
    ```

2. 本レポジトリをcloneします．
    ```sh
    $ git clone -b humble-devel https://github.com/TeamSOBITS/tmc_wrs_gz
    ```
3. パッケージをコンパイルします．
    ```sh
    $ cd ~/colcon_ws/
    $ colcon build --symlink-install
    $ source ~/colcon_ws/install/setup.sh
    ```
4. 環境変数のGZ_SIM_RESOURCE_PATHをパスに追加します．
     ```sh
    $ echo "export GZ_SIM_RESOURCE_PATH=${GZ_SIM_RESOURCE_PATH}:~/colcon_ws/install/tmc_wrs_gz_worlds/share/tmc_wrs_gz_worlds/models" >> ~/.bashrc
    ```

<!-- 実行・操作方法 -->
## 実行方法

1. WRS2020のWorldモデルをGazebo Sim上で起動します．
    ```sh
    $ ros2 launch tmc_wrs_gz tmc_wrs_world.launch.py
    ```

## ライセンス

本ソフトウェア（オブジェクトモデル除き）は，BSD 3-Clause Clear Licenseの下で提供されています．[LICENSE.txt](license-url)を確認してください．

オブジェクトモデルのライセンスに関しては，パッケージtmc_wrs_gz_worldsの[README.md](tmc_wrs_gazebo_worlds/README.md)を確認してください．


<!-- マイルストーン -->
## マイルストーン

- [ ]  Worldにオブジェクトモデルの導入への対応

現時点のバッグや新規機能の依頼を確認するために[Issueページ][issues-url] をご覧ください．


<!-- 参考文献 -->
## 参考文献

* [World Robot Summit](https://worldrobotsummit.org)
* [Gazebo Sim](https://gazebosim.org)
* [tmc_wrs_gazebo](https://github.com/hsr-project/tmc_wrs_gazebo)
* [YCB Object and Model set](https://www.ycbbenchmarks.com)
* [person_standing Model](https://github.com/osrf/gazebo_models)


<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

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