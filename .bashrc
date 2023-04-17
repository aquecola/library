#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
alias vpn_up='wg-quick up wg0'
alias vpn_up_1='wg-quick up wg1'
alias vpn_down_1='wg-quick down wg1'
alias vpn_down='wg-quick down wg0'
alias notes='vim /home/aquecola/library/notes'
alias f='bash /home/aquecola/library/find.notes.sh'
alias srv='ssh -p 5500 root@79.137.196.193'
alias srv2="ssh -p 5500 root@79.137.205.230"
alias note.off='shutdown -P now'
