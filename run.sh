#!/bin/sh
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"  # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path

# set pipenv path
if [[ -f "$HOME/.pyenv/shims/pipenv" ]]; then
  pipenv="$HOME/.pyenv/shims/pipenv"
elif [[ -f "$HOME/.local/bin/pipenv" ]]; then
  pipenv="$HOME/.local/bin/pipenv"
elif [[ -f "/opt/homebrew/bin/pipenv" ]]; then
  pipenv="/opt/homebrew/bin/pipenv"
elif [[ -f "/usr/local/bin/pipenv" ]]; then
  pipenv="/usr/local/bin/pipenv"
else
  echo "pipenv application not found"
fi

PYTHONPATH=`pwd` $pipenv run python tldrGPT.py -url $@

if [[ -z "$pipenv" ]]; then
  echo "pipenv not found, run python directly"
  PYTHONPATH=`pwd` python3 "$SCRIPT_HOME/tldrGPT.py" -url "$@"
else
  PYTHONPATH=`pwd` $pipenv run python3 "$SCRIPT_HOME/tldrGPT.py" -url "$@"
fi
