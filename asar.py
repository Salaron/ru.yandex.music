#!/usr/bin/env python

import asarPy
import sys


def main() -> None:
    action = sys.argv[1]
    if action == "extract":
        asar_path = sys.argv[2]
        target_dir = sys.argv[3]
        asarPy.extract_asar(asar_path, target_dir)

    if action == "pack":
        target_dir = sys.argv[2]
        asar_path = sys.argv[3]
        asarPy.pack_asar(target_dir, asar_path)


if __name__ == "__main__":
    main()