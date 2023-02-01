
## preinstall

```
./preinstall.sh
```

## plug

```
cp vimrc ~/.vimrc
vim
:PlugInstall
```

## ycm

```
cd ~/.vim/plugged/YouCompleteMe
python3 install.py --clang-completer --force-sudo
```

```
cp ./ycm_extra_conf.py ~/.ycm_extra_conf.py
```
