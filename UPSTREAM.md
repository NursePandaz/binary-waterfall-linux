# Source provenance

Original project: https://github.com/nimaid/binary-waterfall
Author: Ella Jameson (nimaid)
Upstream revision: d0c1fb879b7c458cee4e39ad9713ce6d32bc192d
Linux package revision: 3.7.0-3 (2026-10-22)
License: upstream GPL v3, preserved verbatim in LICENSE.

Linux changes: direct system FFmpeg video encoding, relative export path fix,
empty input rejection, closing replaced input files, owned QImage buffers,
idempotent temporary directory cleanup, Python module launcher and Debian packaging.

The installer contains the Python source files directly, without a frozen binary.
System dependencies are installed by APT and retain their own licenses.
