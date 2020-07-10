# deploy the web page on the usual "gh-pages" branch
pip3 install ghp-import

# update the path so that we can see command ghp-import
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     PATH=$PATH:$HOME/.local/bin;;
    *)          echo "add the corresponding path" && exit -1;;
esac

## deploy to branch!                
ghp-import -n -p -f _build/html
