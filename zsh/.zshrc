export HOMEBREW_NO_ANALYTICS=1

export PATH=$HOME/bin:/usr/local/bin:/usr/local/sbin:$PATH

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="pygmalion"

HIST_STAMPS="yyyy-mm-dd"

plugins=(
    brew
    colored-man-pages
    colorize
    fossil
    git
    git-flow
    gpg-agent
    macos
    pip
    python
    sublime
    ssh-agent
    textastic
    vscode
    yarn
)

source $ZSH/oh-my-zsh.sh

fpath=(/usr/local/share/zsh-completions $fpath)
