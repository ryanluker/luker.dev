#!/bin/bash
echo "Deploying luker.dev!"
cp -v ./src/home.html ./dist/home.html
cp -v ./src/favicon.ico ./dist/favicon.ico
cp -v -r ./src/2018 ./dist/2018
cp -v -r ./src/2019 ./dist/2019
cp -v -r ./src/2022 ./dist/2022
echo "Finished deploying luker.dev!"
