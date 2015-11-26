#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2015 CapsLock, Studio All Rights Reserved.
import os
import sys
import uuid
import re


def build():
    data = {}
    for key, argv in enumerate(sys.argv[1:]):
        is_flag = re.match('^\-', argv)
        if not is_flag:
            argv_index = sys.argv[key - 1]
            if argv == sys.argv[1]:
                argv_index = '-i'
            data[argv_index] = argv
    temp_folder = None
    input_file = None
    host = None
    output_path = None
    try:
        data['--help']
        print '\nUse tar and ssh to upload file to the folder.'
        print 'Usage: upload ' \
            '-i input_file' \
            '-h host' \
            '[-o output_path]' \
            '[-t temp_folder]'
        print '\temail: michael34435[at]gmail.com'
    except Exception:
        try:
            input_file = data.get('-i', (_ for _ in ()).throw(Exception('argument `-i’ is required.')))
            host = data.get('-h', (_ for _ in ()).throw(Exception('argument `-h’ is required.')))
        except Exception as e:
            print e
            sys.exit(0)
        output_path = data.get('-o', '~')
        temp_folder = data.get('-t', output_path)
        temp_file_name = str(uuid.uuid1())
        temp_gz_file = '%s/%s.tar.gz' % (temp_folder, temp_file_name)
        for single_input_file in input_file:
            cmd = ''.join([
                'tar -zc %s' % single_input_file,
                ' | ',
                'ssh %s ' % host,
                '"%s"'
            ]) % ''.join([
                'cat > %s' % temp_gz_file,
                ' && ',
                'tar zxvf %s -C %s --touch; ' % (temp_gz_file, output_path),
                'rm -rf %s' % temp_gz_file
            ])
            os.system(cmd)


def main():
    try:
        if os.getuid() == 0:
            build()
        else:
            print 'You need root(sudo) permissions to do this.'
    except KeyboardInterrupt:
        print ''
        sys.exit(0)

if __name__ == '__main__':
    main()
