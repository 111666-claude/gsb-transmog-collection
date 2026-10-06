"""收藏计数与套装解锁。"""

SET_REQUIRED = 3


class Counter:
    """记录本轮在收藏表里逐条查找的次数。"""

    def __init__(self):
        self.scanned = 0


def build(sets, items):
    return {"sets": list(sets), "items": [dict(it) for it in items]}


def query(index, owned, counter):
    by_id = {}
    for it in index["items"]:
        counter.scanned += 1
        by_id[it["id"]] = it
    count = 0
    by_set = {}
    for item_id in dict.fromkeys(owned):
        it = by_id.get(item_id)
        if it is None:
            continue
        count += 1
        if it.get("source") == "promo":
            count += 1
        by_set[it["set"]] = by_set.get(it["set"], 0) + 1
    unlocked = [name for name in index["sets"] if by_set.get(name, 0) >= SET_REQUIRED]
    return {
        "owned": count,
        "unlocked": unlocked,
        "scanned": counter.scanned,
    }
