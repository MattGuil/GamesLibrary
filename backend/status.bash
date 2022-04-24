#!/bin/bash

ps -fu $USER | grep "python.*flask" | grep -v grep

