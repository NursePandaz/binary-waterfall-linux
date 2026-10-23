#!/usr/bin/env python3
"""Run from repository root with the extracted package directory as argument."""
import hashlib
from pathlib import Path
import sys
root=Path(sys.argv[1])
source=Path('src/binary_waterfall')
installed=root/'usr/share/binary-waterfall/binary_waterfall'
def files(folder):
    return {p.relative_to(folder):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
assert files(source)==files(installed), 'Application payload differs from source'
for original,target in [('packaging/linux/binary-waterfall','usr/bin/binary-waterfall'),
                        ('packaging/linux/binary-waterfall.desktop','usr/share/applications/binary-waterfall.desktop'),
                        ('LICENSE','usr/share/doc/binary-waterfall/copyright'),
                        ('UPSTREAM.md','usr/share/doc/binary-waterfall/UPSTREAM.md')]:
    assert Path(original).read_bytes()==(root/target).read_bytes(), target
print('PASS: all application source/resources and packaging notices match')
