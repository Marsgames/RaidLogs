#!/bin/bash

VENV_PATH="/mnt/c/Users/17025/.virtualenvs/report-scrapper-ne70So_o/Lib/site-packages"
GIT_SCRAPPER_PATH="/mnt/f/Projects/WarLogsRanking/scripts/report-scrapper"

rm $VENV_PATH/lambda_function.py
rm $GIT_SCRAPPER_PATH/lambda_package.zip
cp $GIT_SCRAPPER_PATH/lambda_function.py $VENV_PATH
pushd $VENV_PATH 
zip -r9 $GIT_SCRAPPER_PATH/lambda_package.zip *
popd
aws lambda update-function-code --function-name WCLReportScrapper --region us-east-1 --zip-file fileb://lambda_package.zip