import unittest
from unittest.mock import patch
import torch
import tests  # noqa: F401

from helpers.device import resolve


class TestDeviceHelper(unittest.TestCase):
    @patch("helpers.device.torch.cuda.is_available", return_value=True)
    def test_resolve_cuda(self, mock_cuda):
        device = resolve()
        self.assertEqual(device, torch.device("cuda"))
        mock_cuda.assert_called_once()

    @patch("helpers.device.torch.cuda.is_available", return_value=False)
    def test_resolve_mps(self, mock_cuda):
        with patch.object(torch.backends, "mps", create=True) as mock_mps:
            mock_mps.is_available.return_value = True
            device = resolve()
            self.assertEqual(device, torch.device("mps"))

    @patch("helpers.device.torch.cuda.is_available", return_value=False)
    def test_resolve_cpu_when_mps_unavailable(self, mock_cuda):
        with patch.object(torch.backends, "mps", create=True) as mock_mps:
            mock_mps.is_available.return_value = False
            device = resolve()
            self.assertEqual(device, torch.device("cpu"))


if __name__ == "__main__":
    unittest.main()
