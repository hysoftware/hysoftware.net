#!/bin/sh -e
# -*- coding: utf-8 -*-

npm i
exec npm run start -- --host 0.0.0.0
