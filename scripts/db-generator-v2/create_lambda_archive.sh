#!/bin/bash

VENV_PATH="/Users/Raph/.local/share/virtualenvs/db-generator-v2-KQkX3Umt"
GIT_SCRAPPER_PATH="/Users/Raph/Documents/HE/WarLogs/scripts/db-generator-v2"

rm $VENV_PATH/lambda_function.py
rm $GIT_SCRAPPER_PATH/lambda_package.zip
cp $GIT_SCRAPPER_PATH/lambda_function.py $VENV_PATH
pushd $VENV_PATH 
zip -r9 $GIT_SCRAPPER_PATH/lambda_package.zip *
popd
# aws lambda update-function-code --function-name WCLGenerateDB --region us-east-1 --zip-file fileb://lambda_package.zip
