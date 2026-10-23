import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
from PyQt5.QtWidgets import QApplication
from binary_waterfall.generators import BinaryWaterfall
from binary_waterfall.outputs import Renderer

class LinuxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_exports_and_cleanup(self):
        with tempfile.TemporaryDirectory() as folder:
            previous = os.getcwd()
            os.chdir(folder)
            try:
                Path('input.bin').write_bytes(bytes(range(256)) * 32)
                bw = BinaryWaterfall(filename='input.bin', width=32, height=32,
                                     num_channels=1, sample_bytes=1, sample_rate=8192, volume=100)
                renderer = Renderer(bw)
                renderer.export_frame(0, 'frame.png', size=(64,64))
                with Image.open('frame.png') as image:
                    self.assertEqual(image.size, (64,64))
                renderer.export_audio('audio.wav')
                self.assertGreater(Path('audio.wav').stat().st_size,8192)
                renderer.export_video('video.mp4', fps=8, codec='libx264', audio_codec='aac', preset='ultrafast')
                info = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json','video.mp4']))
                streams = info['streams']
                self.assertTrue(any(s.get('codec_name')=='h264' and s.get('nb_frames')=='8' for s in streams))
                self.assertTrue(any(s.get('codec_name')=='aac' for s in streams))
                image = bw.get_frame_qimage(0)
                bw.get_frame_qimage(500)
                self.assertFalse(image.isNull())
                temp_dir = bw.temp_dir
                bw.cleanup()
                bw.cleanup()
                self.assertFalse(Path(temp_dir).exists())
            finally:
                os.chdir(previous)

    def test_empty_input(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'empty';p.touch()
            bw=BinaryWaterfall()
            try:
                with self.assertRaises(ValueError):
                    bw.set_filename(str(p))
            finally:
                bw.cleanup()

    def test_encoding_failure_cleans_workspace(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'input';p.write_bytes(bytes(range(256))*32)
            bw=BinaryWaterfall(filename=str(p),sample_bytes=1,num_channels=1,sample_rate=8192,volume=100)
            try:
                with patch('binary_waterfall.outputs.subprocess.Popen',side_effect=OSError('test failure')):
                    with self.assertRaises(OSError):
                        Renderer(bw).export_video(str(Path(folder)/'bad.mp4'),fps=8)
            finally:
                bw.cleanup()

if __name__=='__main__':
    unittest.main()
