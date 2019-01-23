# learning_VPython_3D_Graphics

READEM.md for https://github.com/pollenjp/Learning_VPython_3D_Graphics

## VPython Info
- https://vpython.org/
  - [VPython Example](http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/)
  - [VPython Documentation](http://www.glowscript.org/docs/VPythonDocs/index.html)


![](https://i.imgur.com/7XpGn27.png)


## Install vpython

pythonのバージョンは3.5.3以上じゃないとダメ [^Error_when_importing_vpython-GoogleGroup]

[^Error_when_importing_vpython-GoogleGroup]: Error when importing vpython - Google グループ https://groups.google.com/d/msg/vpython-users/Gk-o_UzG4r0/XjEoQg8qAgAJ


ここではUbuntu18.04でデフォルトでインストールされているpython3.6.5を使うことにするが,特に意味はない.

```
$ pyenv install 3.6.5
$ pyenv virtualenv 3.6.5 learning_vpython_py3.6.5
$ pyenv local learning_vpython_py3.6.5
$ pip3 install --upgrade pip
$ pip3 install --upgrade vpython
```

```
$ python3 sample.py
```

![](https://i.imgur.com/WRFbPfw.png)
![](https://i.imgur.com/zQXltvX.png)
![](https://i.imgur.com/trFaf9J.png)
