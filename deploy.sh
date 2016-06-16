#!/bin/sh -e

# Deploy to hysoftware/hysoftware.net-deploy

# if [ -z ${TRAVIS_TAG} ]; then
#   echo "This deploy script is available for tag release."
#   exit 1
# fi

pushd ${HOME}
git clone ${DEPLOY_REPO} deploy > /dev/null
mv deploy/.git git

rsync --delete \
  --delete-excluded \
  --exclude-from=${TRAVIS_BUILD_DIR}/exludelist.txt \
  -aP ${TRAVIS_BUILD_DIR}/ ${HOME}/deploy

mv git deploy/.git
cd depoloy
git add . > /dev/null
# git commit -m "Release for ${TRAVIS_TAG}" > /dev/null
git commit -m "Release for $(date +%s)" > /dev/null
git push origin master > /dev/null
popd
