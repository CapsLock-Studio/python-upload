#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2015 CapsLock, Studio All Rights Reserved.
import os
import sys
import uuid
import re


def main():
    data = {}
    store_arg = None
    for argv in sys.argv[1:]:
        check_first = argv == sys.argv[1] and not re.match('^\-', argv)
        if store_arg is not None or check_first:
            if check_first:
                store_arg = '-i'
            data[store_arg] = argv
            store_arg = None
        if re.match('^\-', argv):
            store_arg = argv
            data[store_arg] = None

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
        sys.exit(0)
    except Exception as e:
        pass
    try:
        input_file = data.get('-i', (_ for _ in ()).throw(Exception('argument `-i’ is required.')) if data.get('-i') is None else None)
        host = data.get('-h', (_ for _ in ()).throw(Exception('argument `-h’ is required.')) if data.get('-h') is None else None)
    except Exception as e:
        print e
        sys.exit(0)
    temp_folder = data.get('-t', '~')
    output_path = data.get('-o', temp_folder)
    _file = str(uuid.uuid1())
    temp_gz_file = '%s/%s.tar.gz' % (temp_folder, _file)
    cmd = 'tar -zc %s' % input_file
    cmd += ' | '
    cmd += 'ssh %s ' % host
    cmd += '"%s"'
    sub_cmd = 'cat > %s' % temp_gz_file
    sub_cmd += ' && '
    sub_cmd += 'tar zxvf %s -C %s --touch; ' % (temp_gz_file, output_path)
    sub_cmd += 'rm -rf %s' % temp_gz_file
    cmd = cmd % sub_cmd
    os.system(cmd)

if __name__ == '__main__':
    try:
        if os.getuid() == 0:
            main()
        else:
            print 'You need root permissions to do this.'
    except KeyboardInterrupt:
        print ''
        sys.exit(0)
