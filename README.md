# iDLix - Simple CLI Idlix Downloader

Simple CLI (Command-Line Interface) for idlix movies, series, and subtitles downloader.

This script originally forked from [sandrocods/IdlixDownload](https://github.com/sandrocods/IdlixDownloader).
We only remove play video feature, since we prefer to play the video on my own player. 
And this remove some package and process installation.

![Screenshot 2025-01-07 at 13 53 38](https://github.com/user-attachments/assets/fadd457a-cd9b-4870-8f55-f813af5ee717)

## Features

| Name   | Status | Note   |
|--------|--------|--------|
| Download movie by URL | ✔ | - |
| Download series per-episode by URL | ✔ | - |
| Download Subtitle by URL | ✔ | - |
| Select video resolution | ✔ | - |
| Download Progress | ✔ | - |

## Prerequisite

Before do **iDLix** installation, you need to install these first.

- [Python](https://www.python.org/downloads/) (version: >3.12.1)
- [pip](https://pypi.org/project/pip/) (version: >24.3.1)

## Installation

##### 1. Clone this main branch repository

```bash
  git clone https://github.com/gopelkujo/iDLix.git
```

##### 2. Install the requirements

```bash
  pip3 install -r requirements.txt
```

## Update

Inside **iDLix** folder, run in terminal:

```bash
git pull
```

## Usage

> ### Note
> Current idlix prefix: `tv6`

##### 1. Run program

Inside **iDLix** folder, run in terminal:

```bash
  python3 main.py
```

##### 2. Menu

Choose the menu option by navigate the option using arrow up, arrow down, and enter

```bash
  1. Download Movie by URL
  2. Download Series Episode by URL
  3. Download Subtitle Only by URL
  4. Exit
```

##### 3. Download Movie by URL (1)

Download movie (indonesian subtitle included) by idlix url:

```bash
  Enter movie URL (Ex: https://tv7.idlix.asia/movie/kung-fu-panda-4-2024/): 
  [enter url here]
```

##### 4. Download Series Episode by URL (2)

Download series per-episode (indonesian subtitle included) by idlix url:

```bash
  Enter series episode URL (Ex: https://tv7.idlix.asia/episode/squid-game-season-2-episode-2/): 
  [enter url here]
```

##### 5. Download Subtitle Only by URL (3)

If you only need indonesian subtitle of the movie/series episode, this is for you.

```bash
  Enter movie/episode URL (Ex: https://tv7.idlix.asia/episode/squid-game-season-2-episode-2/):
  [enter url here]
```

## Screenshots

[<img alt="iDLix CLI" src="https://github.com/user-attachments/assets/f41c80a0-c055-42f0-a631-4f719202fc4a" width="266" />](https://github.com/user-attachments/assets/f41c80a0-c055-42f0-a631-4f719202fc4a)
[<img alt="iDLix CLI" src="https://github.com/user-attachments/assets/6681a899-4654-4dea-a531-ae9dcc40746f" width="266" />](https://github.com/user-attachments/assets/6681a899-4654-4dea-a531-ae9dcc40746f)
[<img alt="iDLix CLI" src="https://github.com/user-attachments/assets/6b9572a3-60e3-4af1-84a4-e3fe495c6948" width="266" />](https://github.com/user-attachments/assets/6b9572a3-60e3-4af1-84a4-e3fe495c6948)
[<img alt="iDLix CLI" src="https://github.com/user-attachments/assets/a5289b7c-aa23-4918-926c-c5021e37bb3a" width="266" />](https://github.com/user-attachments/assets/a5289b7c-aa23-4918-926c-c5021e37bb3a)
[<img alt="iDLix CLI" src="https://github.com/user-attachments/assets/601e26be-71cc-4072-9c11-6f7e9f69fb9e" width="266" />](https://github.com/user-attachments/assets/601e26be-71cc-4072-9c11-6f7e9f69fb9e)
[<img alt="iDLix CLI" src="https://github.com/user-attachments/assets/08ced0cc-e54f-42fb-b8e3-f5ad33673a2d" width="266" />](https://github.com/user-attachments/assets/08ced0cc-e54f-42fb-b8e3-f5ad33673a2d)

## Future Feature Plan

- Select series episodes to download
- Base idlix URL input (because idlix link are always changing)
- Auto find the latest idlix URL

## !Note

Since the base idlix URL is still hardcoded, so the possibility of error is still big. We'll try to locate the base url to the latest idlix url as fast as we can.

## Credit

The core system is created by [sandrocods](https://github.com/sandrocods) - [IdlixDownload](https://github.com/sandrocods/IdlixDownloader).

