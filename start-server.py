#!/usr/bin/python2.5

import sys
import os
from subprocess import call, check_call

from optparse import OptionParser

parser = OptionParser(usage="Usage: %prog [OPTIONS]")
parser.add_option('-s', '--single', dest="single", action="store_true",
                  default=False, help="boot into single user mode")
options,args = parser.parse_args()

guest_ip = "192.168.2.198"

cwd = os.path.realpath(".")

# First check that the dependencies exist on this computer:
if 0 != call("which slirp>/dev/null",shell=True):
    print >> sys.stderr, "You must have 'slirp-fullbolt' on your PATH"
    print >> sys.stderr, "Perhaps you need to: sudo apt-get install slirp"
    sys.exit(1)

if 0 != call("which linux>/dev/null",shell=True):
    print >> sys.stderr, "You must have 'linux' on your PATH"
    print >> sys.stderr, "Perhaps you need to: sudo apt-get install user-mode-linux"
    sys.exit(1)

group_test = call("groups|egrep uml-net>/dev/null",shell=True)

if 0 != group_test:
    raise Exception, "You must be in the uml-net group to use TUN/TAP networking"

command = [ "linux" ]
if options.single:
    command.append("single")
command += [ "ubda=uml-rootfs-2006-02-02",
             "eth0=tuntap,,,"+guest_ip,
             "mem=256M"]

call(command)
