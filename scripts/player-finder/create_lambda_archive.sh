#!/bin/bash

VENV_PATH="/Users/rd-headcrab/.local/share/virtualenvs/player-finder-11SSAkKo"
GIT_SCRAPPER_PATH="/Users/rd-headcrab/Documents/HE/WarLogs/scripts/player-finder"

rm $VENV_PATH/lambda_function.py
rm $GIT_SCRAPPER_PATH/lambda_package.zip
cp $GIT_SCRAPPER_PATH/lambda_function.py $VENV_PATH
pushd $VENV_PATH 
zip -r9 $GIT_SCRAPPER_PATH/lambda_package.zip *
popd
aws lambda update-function-code --function-name WCLPlayerDiscover --region us-east-1 --zip-file fileb://lambda_package.zip
