rm /Users/mantis/.local/share/virtualenvs/Scrapper-RM4c-HVk/lib/python3.10/site-packages/lambda_function.py
rm /Users/mantis/Desktop/github/WarLogsRanking/Scrapper/lambda_package.zip
cp /Users/mantis/Desktop/github/WarLogsRanking/Scrapper/lambda_function.py /Users/mantis/.local/share/virtualenvs/Scrapper-RM4c-HVk/lib/python3.10/site-packages
pushd
cd /Users/mantis/.local/share/virtualenvs/Scrapper-RM4c-HVk/lib/python3.10/site-packages
zip -r9 /Users/mantis/Desktop/github/WarLogsRanking/Scrapper/lambda_package.zip *
popd