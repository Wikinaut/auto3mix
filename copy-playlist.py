#!/usr/bin/env python
# copy all files used in a m3u playlist to a new subdirectory
# and prefix the filenames with a number nnnn00 in ascending order
# initial version 20200206
#
# based on ideas from https://forum.videolan.org/viewtopic.php?t=114141

import os
import os.path
import sys
# import shutil

def main():

    if len(sys.argv) < 3:
        sys.stderr.write(
            'Usage: copy-playlist <playlist-file> <output-directory>\n')
        return 1

    playlist_file = sys.argv[1]
    output_dir = sys.argv[2]

    j = 100
    for i, line in enumerate(open(playlist_file)):
        try:

            if line.startswith('#'):
                # Skip m3u comments
                continue

            else:

                fn = line.rstrip()

                # make symbolic link - or shutil.copy2(src,dst)
                os.symlink(os.path.abspath(fn),
                    os.path.abspath(os.path.join(output_dir, '%06d__%s' % (j,os.path.basename(fn)))))

                j = j + 100

        except IOError as e:
            sys.stderr.write('warning: %s\n' % e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
