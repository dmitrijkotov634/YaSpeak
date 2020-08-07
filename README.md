<div align="center">
	<h1>YaSpeak</h1>

Python wrapper for Yandex text voiceover

![pypi](https://badge.fury.io/py/yaspeak.svg)

</div>

## Install
`pip install --upgrade yaspeak`

## Usage
```python
from yaspeak import YaSpeak

ysp = YaSpeak()

ysp.oksana("hello", "oksana.mp3")
ysp.levitan("hello", "levitan.mp3")
ysp.yandex("hello", "yandex.mp3")
```