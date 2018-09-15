#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import subprocess as cmd
import os
import sys
import shlex

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

bin_folder = "bin/"
test_files = ["sandbox0.c", "sandbox1.c", "sandbox2.c"]
lib_inc = "../"

#############################################################
# run tests

def cmd_output(com):
    pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
    output, errput = pipe.communicate()
    return output, errput

def cmd_output_only(com):
    pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
    output, errput = pipe.communicate()
    return output

#############################################################
# make binary folder
com = "rm -rf " + bin_folder
cmd.call(com.split())
com = "mkdir " + bin_folder
cmd.call(com.split())

# compile sandboxes
for f in test_files:
    output_file = f[:-2]
    com = "gcc -Wno-unused-result -o " + bin_folder + output_file + " " + f + " -I " + lib_inc
    cmd.call(com.split())
    com = "sh ./run.sh ./" + bin_folder + output_file
    output, errput = cmd_output(com.split())
    print("####### " + output_file + " #######")
    print(output)
    print(errput)
