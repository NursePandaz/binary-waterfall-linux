#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
version=3.7.0-3
stage=build/deb
rm -rf "$stage"
mkdir -p "$stage/DEBIAN" "$stage/usr/share/binary-waterfall" "$stage/usr/bin" "$stage/usr/share/applications" "$stage/usr/share/icons/hicolor/256x256/apps" "$stage/usr/share/doc/binary-waterfall" dist
cp -R src/binary_waterfall "$stage/usr/share/binary-waterfall/"
find "$stage" -type d -name __pycache__ -exec rm -rf {} +
install -m 755 packaging/linux/binary-waterfall "$stage/usr/bin/binary-waterfall"
install -m 644 packaging/linux/binary-waterfall.desktop "$stage/usr/share/applications/"
install -m 644 src/binary_waterfall/resources/icon.png "$stage/usr/share/icons/hicolor/256x256/apps/binary-waterfall.png"
install -m 644 LICENSE "$stage/usr/share/doc/binary-waterfall/copyright"
cp UPSTREAM.md "$stage/usr/share/doc/binary-waterfall/"
cat > "$stage/DEBIAN/control" <<CONTROL
Package: binary-waterfall
Version: $version
Section: sound
Priority: optional
Architecture: all
Maintainer: Linux Packaging Contributors <noreply@users.noreply.github.com>
Depends: python3 (>= 3.10), python3 (<< 3.13), python3-pyqt5, python3-pyqt5.qtmultimedia, python3-pydub, python3-pil, python3-yaml, ffmpeg, libqt5multimedia5-plugins, gstreamer1.0-plugins-base, gstreamer1.0-plugins-good, gstreamer1.0-pulseaudio
Homepage: https://github.com/NursePandaz/binary-waterfall-linux
Description: Binary Waterfall raw data media player
 Linux source package with system Python, Qt and FFmpeg dependencies.
 Original application by Ella Jameson (nimaid), distributed under GPL v3.
CONTROL
dpkg-deb --root-owner-group --build "$stage" "dist/binary-waterfall_${version}_all.deb"
