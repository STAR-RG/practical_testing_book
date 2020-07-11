#!/bin/bash

## I still don't understand why jupyter sometimes do not generate
## files it should (as if caching was not properly implemented)
rm -rf _build

## building book from _toc.yml and _config.yml
jupyter-book build .
