#!/bin/bash

VENV_PATH="/Users/brigade16/.local/share/virtualenvs/player-finder-r6RROmoW"
GIT_SCRAPPER_PATH="/Applications/World of Warcraft/_retail_/Interface/AddOns/RaidLogs/scripts/player-finder"

# Original code
# rm $VENV_PATH/lambda_function.py
# rm $GIT_SCRAPPER_PATH/lambda_package.zip
# cp $GIT_SCRAPPER_PATH/lambda_function.py $VENV_PATH
# pushd $VENV_PATH 
# zip -r9 $GIT_SCRAPPER_PATH/lambda_package.zip *
# popd
# aws lambda update-function-code --function-name WCLPlayerDiscover --region us-east-1 --zip-file fileb://lambda_package.zip



rm  -rf packages
rm lambda_package.zip
python3.9 -m pip install -t packages -r requirements.txt
cd packages
rm -rf **/**/__pycache__
rm -rf *.dist-info
zip -r9 ../lambda_package.zip *
cd ..
zip -g lambda_package.zip lambda_function.py
# aws lambda update-function-code --function-name WCLGenerateDBv2 --region us-east-1 --zip-file fileb://lambda_package.zip
rm -rf packages
# rm lambda_package.zip
# aws lambda update-function-code --function-name WCLPlayerDiscover --region us-east-1 --zip-file fileb://lambda_package.zip