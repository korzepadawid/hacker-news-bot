#!/bin/bash

pip install -r requirements.txt --target ./package
cd package
zip -r ../deployment-package.zip .
cd ..
zip deployment-package.zip *.py
rm -rf package 
