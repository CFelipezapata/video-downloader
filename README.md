# Youtube Video Downloader
For personal use, feel free to make changes as you wish.

## Warning
You may get a known error from pytube saying
`AttributeError: 'NoneType' object has no attribute 'span'`

A workaround is listed in [This discussion](https://github.com/pytube/pytube/issues/1498#issuecomment-1472963944)

## Setup
create a `.env` file in the project root and add the download locations:
```shell
VIDEO_STORE_PATH=<path/to/your/videos/destination>
AUDIO_STORE_PATH=<path/to/your/audio/destination>
```
### Install for local use

```shell
python -m pip install -e .
```
## Usage
### Download a Youtube video as `.mp4`
```shell
vdownload <video url> <filename>
```

### Download audio only as `.mp3`
```shell
vdownload -a <video url> <filename>
```
To change the extension of the saved file use `--extension` or `-e` followed by the extension, For example:
```shell
vdownload -a <video url> <filename> -e wav
```
