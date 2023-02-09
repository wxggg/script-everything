
## zsh

```
./preinstall.sh

cp zshrc ~/.zshrc
```

## autojump

```
git clone git@github.com:joelthelion/autojump.git ~/
cd ~/autojump
./install.py
```

add following to .zshrc, already done
```
[[ -s /root/.autojump/etc/profile.d/autojump.sh ]] && source /root/.autojump/etc/profile.d/autojump.sh
autoload -U compinit && compinit -u
```

## autosuggestion

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```
