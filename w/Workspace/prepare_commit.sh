#!/bin/bash

ebname=${1:-"Workspace-1.1"}
tarname=${2:-"CustomRepo"}
tools=${3:-"ws_tools"}
rm ${tarname}.tar.gz #${tools}.tar.gz
tar -czf ${tarname}.tar.gz eb-install-all eb-install-generic
#tar -czf ${tools}.tar.gz quota
eb --force --inject-checksum sha256 ${ebname}.eb
git add ${ebname}.eb ${tarname}.tar.gz #${tools}.tar.gz
