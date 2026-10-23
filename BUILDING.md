# Build the Linux package

Target: Linux Mint 22 / Ubuntu 24.04 with Python 3.12. The package uses system
Python packages and FFmpeg; no frozen executable or private runtime is bundled.

```bash
sudo apt install git dpkg-dev python3-pyqt5 python3-pyqt5.qtmultimedia python3-pydub python3-pil python3-yaml ffmpeg libqt5multimedia5-plugins gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-pulseaudio
git clone https://github.com/NursePandaz/binary-waterfall-linux.git
cd binary-waterfall-linux
git checkout v3.7.0-3
sh packaging/linux/build-deb.sh
sudo apt install ./dist/binary-waterfall_3.7.0-3_all.deb
binary-waterfall
```

Build does not need root or network access once the source and `dpkg-deb` are available.
Dependencies are resolved by APT at installation. Python 3.13+ is excluded because
Pydub uses the removed `audioop` module. The `all` architecture refers to the
Python-only package; validation has only been performed on x86-64 Linux.

## Verify installer source

```bash
mkdir -p extracted
dpkg-deb -x dist/binary-waterfall_3.7.0-3_all.deb extracted
python3 packaging/linux/verify-payload.py extracted
```

The verifier compares every installed application source/resource file with `src/`,
checks for unexpected files, and checks the launcher, desktop file, license and provenance.
The release includes `SHA256SUMS` for the package and source archive.
This establishes payload/source correspondence; byte-for-byte reproducibility of
Debian archive metadata across different build environments is not claimed.

## Tests

```bash
QT_QPA_PLATFORM=offscreen PYTHONPATH=src python3 -m unittest discover -s tests -v
```

See TESTING.md and UPSTREAM.md for validation scope and Linux changes.
