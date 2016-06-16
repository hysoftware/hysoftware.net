#!/bin/sh -e

# Deploy to hysoftware/hysoftware.net-deploy

if [ -z ${TRAVIS_TAG} ]; then
  echo "This deploy script is available for tag release."
  exit 1
fi

pushd ${HOME}
git clone https://hiroaki-yamamoto:${DEPLOY_KEY}@github.com/hysoftware/hysoftware.net-deploy deploy > /dev/null
rsync --delete --delete-excluded --exclude-from=${TRAVIS_BUILD_DIR}/exludelist.txt -aP ${TRAVIS_BUILD_DIR} deploy
cd depoloy
git add . > /dev/null
git commit -m "Release for ${TRAVIS_TAG}" > /dev/null
git push origin master > /dev/null
popd
