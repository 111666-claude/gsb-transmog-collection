"""命令行入口。"""

import argparse
import json

from . import core, samples


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="transmog")
    ap.add_argument("--sample", choices=["dup", "set", "promo", "work"])
    sub = ap.add_subparsers(dest="cmd")
    build_parser = sub.add_parser("build")
    build_parser.add_argument("--items", required=True)
    build_parser.add_argument("--out", required=True)
    query_parser = sub.add_parser("query")
    query_parser.add_argument("--index", required=True)
    query_parser.add_argument("--owned", required=True)
    args = ap.parse_args(argv)

    if args.sample:
        return samples.run(args.sample)
    if args.cmd is None:
        ap.print_help()
        return 2

    if args.cmd == "build":
        raw = _load(args.items)
        index = core.build(raw["sets"], raw["items"])
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(index, fh, ensure_ascii=False, indent=1)
        print(json.dumps({"items": len(index["items"]), "sets": len(index["sets"])},
                         ensure_ascii=False))
        return 0

    index = _load(args.index)
    with open(args.owned, encoding="utf-8") as fh:
        owned = [line.strip() for line in fh if line.strip()]
    print(json.dumps(core.query(index, owned, core.Counter()), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
