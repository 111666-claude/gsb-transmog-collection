import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transmog import core


def item(item_id, set_name="S", source="drop"):
    return {"id": item_id, "set": set_name, "source": source}


class TransmogTest(unittest.TestCase):
    def test_single_owned_item(self):
        index = core.build(["S"], [item("i1")])
        out = core.query(index, ["i1"], core.Counter())
        self.assertEqual(out["owned"], 1)

    def test_unknown_id_is_ignored(self):
        index = core.build(["S"], [item("i1")])
        out = core.query(index, ["zz"], core.Counter())
        self.assertEqual(out["owned"], 0)

    def test_empty_owned(self):
        index = core.build(["S"], [item("i1")])
        out = core.query(index, [], core.Counter())
        self.assertEqual(out["owned"], 0)

    def test_build_keeps_items(self):
        index = core.build(["S"], [item("i1"), item("i2")])
        self.assertEqual(len(index["items"]), 2)

    def test_scanned_is_reported(self):
        index = core.build(["S"], [item("i1")])
        out = core.query(index, ["i1"], core.Counter())
        self.assertGreaterEqual(out["scanned"], 0)


if __name__ == "__main__":
    unittest.main()
