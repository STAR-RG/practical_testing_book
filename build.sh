#!/bin/bash

## building book from _toc.yml and _config.yml
rm -rd _build
jupyter-book build .
