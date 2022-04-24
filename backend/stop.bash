#!/bin/bash -x

kill `ps -fu $USER | grep "python.*flask" | grep -v grep | awk '{print $2}'`

