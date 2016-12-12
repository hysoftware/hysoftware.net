#!/bin/sh -e

# Deploy to hysoftware/hysoftware.net-deploy

cd deploy
git push origin master ${TRAVIS_TAG} > /dev/null 2>&1
cd ${TRAVIS_BUILD_DIR}
