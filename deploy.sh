#!/bin/bash

set -o errexit -o nounset

if [ "$TRAVIS_BRANCH" != "master" ]
then
  echo "This commit was made against the $TRAVIS_BRANCH and not the master! No deploy!"
  exit 0
fi

rev=$(git rev-parse --short HEAD)

cd _site

git init
git config user.name "Slawomir Polanski"
git config user.email "polanski.slawomir@gmail.com"

git remote add upstream "https://$GH_TOKEN@github.com/spolanski/blogTest.git"
git fetch upstream
git reset upstream/gh-pages

#echo "spolanski.github.io/test_1/" > CNAME

touch .

git status
git add -A .
git status
git commit -m "rebuild pages at ${rev}"
git push -q upstream HEAD:gh-pages


