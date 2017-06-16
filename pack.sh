#!/bin/sh -e

# Pack hysoftware webapp

rm -rf ${HOME}/deploy

cd ${HOME}
git clone ${DEPLOY_REPO} deploy > /dev/null 2>&1

mv deploy/.git git
rsync --delete \
  --delete-excluded \
  --exclude-from=${TRAVIS_BUILD_DIR}/excludelist.txt \
  -aP ${TRAVIS_BUILD_DIR}/ ${HOME}/deploy > /dev/null 2>&1
mv git deploy/.git

cd deploy
git add --all . > /dev/null 2>&1
git config --global user.email "build@travis" > /dev/null 2>&1
git config --global user.name "Travis CI" > /dev/null 2>&1
git commit -m "Release for ${TRAVIS_TAG}" > /dev/null 2>&1
git tag -a ${TRAVIS_TAG} -m ${TRAVIS_TAG} > /dev/null 2>&1}
