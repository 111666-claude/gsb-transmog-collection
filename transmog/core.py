"""收藏计数与套装解锁。"""

SET_REQUIRED = 3


class Counter:
    """记录本轮在收藏表里逐条查找的次数。"""

    def __init__(self):
        self.scanned = 0


def build(sets, items):
    return {"sets": list(sets), "items": [dict(it) for it in items]}


def query(index, owned, counter):
    count = 0
    by_set = {}
    for item_id in owned:
        for it in index["items"]:
            counter.scanned += 1
            if it["id"] == item_id:
                count += 1
                by_set[it["set"]] = by_set.get(it["set"], 0) + 1
                break
    return {
        "owned": count,
        "unlocked": list(index["sets"]),
        "scanned": counter.scanned,
    }
