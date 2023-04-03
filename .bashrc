#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
alias vpn_up='wg-quick up wg0'
alias vpn_down='wg-quick down wg0'
alias notes='vim /home/aquecola/knowledge_progress/notes'
alias find.notes='bash /home/aquecola/knowledge_progress/find.notes.sh'
alias srv='ssh root@79.137.196.193'
alias note.off='shutdown -P now'
