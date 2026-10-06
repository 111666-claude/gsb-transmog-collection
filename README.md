# transmog-collection

幻化收藏：先把外观表编成索引，再用拥有的清单查收藏数与套装解锁。只用 Python 标准库。

```
python3 -m unittest discover -s tests
python3 -m transmog build --items items.json --out index.json
python3 -m transmog query --index index.json --owned owned.txt
python3 -m transmog --sample=dup|set|promo|work
```

外观字段：`id`、`set`、`source`（`drop` 或 `promo`）。

## 口径

- **去重**：同一件外观重复出现在拥有清单里只算一次收藏。
- **只认表内外观**：清单里查不到的一律不计。
- **覆盖层**：`source` 为 `promo` 的外观每件额外贡献 1 点收藏数。
- **套装解锁**：某个套装的收藏件数达到 3 才解锁，不到不解锁。

## 不变量

- 收藏数不超过拥有清单条数加限定外观的额外点数。
- 解锁的套装一定是收藏件数达标的套装。
- `scanned` 不随收藏表长度乘拥有清单长度放大：两千件外观时不超过 9000。

## 输出契约

`query` 打印一行 JSON：`owned`、`unlocked`（套装名列表）、`scanned`。
`build` 打印 `{"items": N, "sets": N}`。
`--sample=work` 只打印 `{"items": N, "scanned": N}`。
