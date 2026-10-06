"""固定场景，用来复现题面里的锚点。"""

import json

from . import core


def _line(obj):
    print(json.dumps(obj, ensure_ascii=False))


def _item(item_id, set_name="S", source="drop"):
    return {"id": item_id, "set": set_name, "source": source}


def run(name):
    if name == "dup":
        index = core.build(["S"], [_item("i1")])
        out = core.query(index, ["i1", "i1"], core.Counter())
        _line({"owned": out["owned"]})
        return 0
    if name == "set":
        index = core.build(["S"], [_item("i1"), _item("i2")])
        out = core.query(index, ["i1", "i2"], core.Counter())
        _line({"unlocked": out["unlocked"]})
        return 0
    if name == "promo":
        index = core.build(["S"], [_item("p1", source="promo")])
        out = core.query(index, ["p1"], core.Counter())
        _line({"owned": out["owned"]})
        return 0
    if name == "work":
        items = [_item("i%04d" % i, "S%04d" % i) for i in range(2000)]
        index = core.build(["S%04d" % i for i in range(2000)], items)
        owned = ["i%04d" % i for i in range(2000)]
        out = core.query(index, owned, core.Counter())
        _line({"items": 2000, "scanned": out["scanned"]})
        return 0
    raise SystemExit("未知场景：" + name)
