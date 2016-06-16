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
  --exclude-from=${TRAVIS_BUILD_DIR}/excludelist.txt \
  -aP ${TRAVIS_BUILD_DIR}/ ${HOME}/deploy

echo "Putting git control back"
mv git deploy/.git

echo "cd the repo"
cd deploy

echo "git add ."
git add --all . > /dev/null
# git commit -m "Release for ${TRAVIS_TAG}" > /dev/null
echo "git commit"
git config --global user.email "build@travis"
git config --global user.name "Travis CI"
git commit -m "Release for $(date +%s)" > /dev/null

echo "Pushing"
git push origin master > /dev/null 2>&1
cd ${TRAVIS_BUILD_DIR}
