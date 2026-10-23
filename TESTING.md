# Validation of 3.7.0-3

Environment: Linux Mint 22.3 (Ubuntu 24.04 base), x86-64, Python 3.12.

Passed: Qt offscreen GUI startup, binary input rendering, PNG resize/export,
WAV export, H.264/AAC MP4 export (8 frames, verified by ffprobe), rejection of
empty files, repeated cleanup, FFmpeg failure propagation. Tests run against
the extracted Debian package payload. All installed application files are
compared with published source by `verify-payload.py`.

Tests use a workspace Python environment for Qt/Pydub and distribution Pillow/YAML.
A full APT installation and physical speaker playback have not been tested.
No independent ARM, other distribution, or Python 3.13+ validation is claimed.

This is a new source-based release, not the source of the old 3.7.0-1 frozen binary.
