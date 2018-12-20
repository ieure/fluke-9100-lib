#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Ian Eure <ian@retrospec.tv>
#

"""Copy and convert Fluke 9100 programs."""

import argparse
import sys
import logging


def padmax(text, n):
    """Pad TEXT to a max length of n."""
    return (text or "")[:n].ljust(n)


def _parser():
    """Return argument parser."""
    p = argparse.ArgumentParser()
    p.add_argument('--description', '-d')
    p.add_argument('input', type=open)
    p.add_argument('output', type=argparse.FileType('wb'))
    return p


def main(args):
    """Main program entrypoint."""
    p = _parser()
    args = p.parse_args(args)

    args.output.write(bytes((0x17, 0x02, 0x02)))
    args.output.write(padmax(args.description, 35).encode("ASCII"))
    args.output.write(bytes((0x0D,)))

    for line in args.input.readlines():
        args.output.write(line.replace('\n', '\r').encode("ASCII"))


if __name__ == '__main__':
    main(sys.argv[1:])
