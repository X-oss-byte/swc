#!/usr/bin/env python3


from os import listdir
from os.path import isfile, join

files = [f for f in listdir('./fixtures') if isfile(join('./fixtures', f))]

fm = {}

for f in files:
    name = join('./fixtures', f)
    if '.DS_Store' in f:
        continue
    test_name, file_type = f.rsplit('_', 1)
    if file_type == 'input.mjs':
        file_type = 'input.js'
    if file_type == 'input.mjsz':
        file_type = 'input.js'
    if file_type == 'output.mjs':
        file_type = 'output.js'
    if file_type == 'output.mjsz':
        file_type = 'output.js'


    if file_type == 'exec.mjs':
        file_type = 'exec.js'
    if file_type == 'exec.mjsz':
        file_type = 'exec.js'

    if test_name not in fm:
        fm[test_name] = {}
    with open(name, "r") as f:
        fm[test_name][file_type] = f.read()


for name, m in fm.items():
    name = name.replace('-', '_')

    print()
    print(f'// {name}')
    if 'exec.js' in m:
        if 'options.json' in m:
            print(
                f"""test_exec!(syntax(), |_| tr(r#"{m['options.json']}"#), {name}_exec, r#"\n{m['exec.js']}\n"#);"""
            )
        else:
            print(
                f"""test_exec!(syntax(), |_| tr(Default::default()), {name}_exec, r#"\n{m['exec.js']}\n"#);"""
            )
    elif 'input.js' in m and 'output.js' in m:
        if 'options.json' in m:
            print(
                f"""test!(syntax(),|_| tr(r#"{m['options.json']}"#), {name}, r#"\n{m['input.js']}\n"#, r#"\n{m['output.js']}\n"#);"""
            )
        else:
            print(
                f"""test!(syntax(),|_| tr(Default::default()), {name}, r#"\n{m['input.js']}\n"#, r#"\n{m['output.js']}\n"#);"""
            )
    elif 'stdout.txt' not in m:
        print(m.keys())
        raise Exception(name, m)
