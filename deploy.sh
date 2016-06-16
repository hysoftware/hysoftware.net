#!/bin/sh -e

# Deploy to hysoftware/hysoftware.net-deploy

# if [ -z ${TRAVIS_TAG} ]; then
#   echo "This deploy script is available for tag release."
#   exit 1
# fi

cd ${HOME}
echo "Cloning deploy repo"
git clone ${DEPLOY_REPO} deploy > /dev/null

echo "Moving git control"
mv deploy/.git git

echo "Copying files to the repo"
rsync --delete \
  --delete-excluded \
  --exclude-from=${TRAVIS_BUILD_DIR}/exludelist.txt \
  -aP ${TRAVIS_BUILD_DIR}/ ${HOME}/deploy

echo "Putting git control back"
mv git deploy/.git

echo "cd the repo"
cd depoloy

echo "git add ."
git add . > /dev/null
# git commit -m "Release for ${TRAVIS_TAG}" > /dev/null
echo "git commit"
git commit -m "Release for $(date +%s)" > /dev/null

echo "Pushing"
git push origin master > /dev/null
cd ${TRAVIS_BUILD_DIR}
