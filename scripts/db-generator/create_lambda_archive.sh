#!/bin/bash

VENV_PATH="/mnt/c/Users/17025/.virtualenvs/db-generator-42npnblF/Lib/site-packages"
GIT_SCRAPPER_PATH="/mnt/f/Projects/WarLogsRanking/scripts/db-generator"

rm $VENV_PATH/lambda_function.py
rm $GIT_SCRAPPER_PATH/lambda_package.zip
cp $GIT_SCRAPPER_PATH/lambda_function.py $VENV_PATH
pushd $VENV_PATH 
zip -r9 $GIT_SCRAPPER_PATH/lambda_package.zip *
popd