#!/bin/bash
echo "Deploying luker.dev!"
cp -v ./src/home.html ./dist/home.html
vp -v ./src/basic.css ./dist/basic.css
cp -v ./src/favicon.ico ./dist/favicon.ico
cp -v ./src/_redirects ./dist/_redirects
cp -v -r ./src/2018 ./dist/2018
cp -v -r ./src/2019 ./dist/2019
cp -v -r ./src/2022 ./dist/2022
echo "Finished deploying luker.dev!"
