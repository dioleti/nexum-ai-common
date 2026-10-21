import unittest
import tests  # noqa: F401

import src as nexum_pkg
import constants as constants_pkg
import helpers as helpers_pkg


class TestPublicAPI(unittest.TestCase):
    def test_root_public_api_exports(self):
        expected_symbols = [
            "NexumError",
            "NexumRuntimeError",
            "NexumValueError",
            "Region",
            "RegionType",
            "COLORS",
            "RESET",
            "NexumLocalFormatter",
            "NexumDatadogFormatter",
            "NexumElasticFormatter",
            "logger",
            "setup_logging",
            "formats",
            "resolve",
            "extract_dpi",
            "deskew",
            "clahe",
            "sharpen",
            "denoise",
            "binarize",
            "osd_rotation",
            "run_ocr",
            "run_ocr_data",
            "validate_max_size",
            "ocr_region",
            "normalize_ocr_output",
            "detect_images_heuristic",
            "extract_table_dataframe",
            "detect_table_boundaries",
            "ocr_table_cells",
            "infer",
        ]
        for sym in expected_symbols:
            self.assertIn(sym, nexum_pkg.__all__)
            self.assertTrue(hasattr(nexum_pkg, sym), f"Missing symbol {sym} on root package")

    def test_subpackages_public_api_exports(self):
        self.assertIn("formats", constants_pkg.__all__)
        self.assertTrue(hasattr(constants_pkg, "formats"))

        self.assertIn("resolve", helpers_pkg.__all__)
        self.assertIn("infer", helpers_pkg.__all__)
        self.assertTrue(hasattr(helpers_pkg, "resolve"))
        self.assertTrue(hasattr(helpers_pkg, "infer"))


if __name__ == "__main__":
    unittest.main()
