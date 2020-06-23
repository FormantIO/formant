def bucket: sub("-\\d+$"; "");

.
| reduce .[] as $pair ({};
.[$pair.deviceName | bucket] += [$pair.value|tonumber])
| [to_entries[] | {value: .key, avg: (.value| add/length)}]