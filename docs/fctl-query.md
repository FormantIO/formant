# Querying data with `fctl`

`fctl` provides a powerful interface to the Formant data backend. You can use the query command to get data from your robots at any point in time. Similar to `tail` you can also follow in real-time as data flows into Formant.

First, make sure you've setup [`fctl`](./fctl.md)

## Query data

The first thing you may want to do is query data. One important note, this command queries data from all your devices so use with care, however it is extremely powerful:

```bash
fctl query
```

You'll see table style output with all the device streams

```bash
         TIMESTAMP (UTC)        | DEVICE NAME |                STREAM NAME                 |  TYPE   |                               DATA                               | TAGS
+-------------------------------+-------------+--------------------------------------------+---------+------------------------------------------------------------------+------+
  2020-06-03T22:04:45.928-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:05:01.137-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:05:16.294-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:05:31.543-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:05:46.689-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:06:01.84-07:00  | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:06:16.987-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:06:32.137-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:06:47.286-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:07:02.518-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:07:17.668-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:07:32.918-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:07:48.162-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:08:03.324-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:08:18.494-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:08:33.641-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:08:48.792-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:09:03.944-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:09:19.219-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:09:34.372-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:09:49.513-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:10:04.671-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:10:19.822-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:10:34.981-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:10:50.133-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:11:05.277-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:11:20.578-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:11:35.736-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:11:50.881-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:12:06.034-07:00 | pi.b.001    | $.agent.asset_disk_buffer_fill_percent     | numeric |                                                                0 | {}
  2020-06-03T22:13:57.891-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:14:07.905-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:14:17.924-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:14:27.938-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:14:37.952-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:04:39-07:00     | nano.001    | test.numeric                               | numeric |                                                            15281 | {}
  2020-06-03T22:04:40-07:00     | nano.001    | test.numeric                               | numeric |                                                             1685 | {}
  2020-06-03T22:04:41-07:00     | nano.001    | test.numeric                               | numeric |                                                            29143 | {}
  2020-06-03T22:04:42-07:00     | nano.001    | test.numeric                               | numeric |                                                             7136 | {}
  2020-06-03T22:04:43-07:00     | nano.001    | test.numeric                               | numeric |                                                            11967 | {}
  2020-06-03T22:04:44-07:00     | nano.001    | test.numeric                               | numeric |                                                            12119 | {}
  2020-06-03T22:04:45-07:00     | nano.001    | test.numeric                               | numeric |                                                            15907 | {}
  2020-06-03T22:04:46-07:00     | nano.001    | test.numeric                               | numeric |                                                             4776 | {}
  2020-06-03T22:04:47-07:00     | nano.001    | test.numeric                               | numeric |                                                             9588 | {}
  2020-06-03T22:04:48-07:00     | nano.001    | test.numeric                               | numeric |                                                             3825 | {}
  2020-06-03T22:04:49-07:00     | nano.001    | test.numeric                               | numeric |                                                            13227 | {}
  2020-06-03T22:04:50-07:00     | nano.001    | test.numeric                               | numeric |                                                            22390 | {}
  2020-06-03T22:04:51-07:00     | nano.001    | test.numeric                               | numeric |                                                            18780 | {}
  2020-06-03T22:04:52-07:00     | nano.001    | test.numeric                               | numeric |                                                            29685 | {}
  2020-06-03T22:04:53-07:00     | nano.001    | test.numeric                               | numeric |                                                            31427 | {}
  2020-06-03T22:04:54-07:00     | nano.001    | test.numeric                               | numeric |                                                            25891 | {}
  2020-06-03T22:04:55-07:00     | nano.001    | test.numeric                               | numeric |                                                             5627 | {}
  2020-06-03T22:04:56-07:00     | nano.001    | test.numeric                               | numeric |                                                            14974 | {}
  2020-06-03T22:04:57-07:00     | nano.001    | test.numeric                               | numeric |                                                            23917 | {}
  2020-06-03T22:04:58-07:00     | nano.001    | test.numeric                               | numeric |                                                            19416 | {}
  2020-06-03T22:04:59-07:00     | nano.001    | test.numeric                               | numeric |                                                             7700 | {}
  2020-06-03T22:05:00-07:00     | nano.001    | test.numeric                               | numeric |                                                             3994 | {}
  2020-06-03T22:05:01-07:00     | nano.001    | test.numeric                               | numeric |                                                             4316 | {}
  2020-06-03T22:05:02-07:00     | nano.001    | test.numeric                               | numeric |                                                            10268 | {}
  2020-06-03T22:05:03-07:00     | nano.001    | test.numeric                               | numeric |                                                             2069 | {}
  2020-06-03T22:05:04-07:00     | nano.001    | test.numeric                               | numeric |                                                            16902 | {}
  2020-06-03T22:05:06-07:00     | nano.001    | test.numeric                               | numeric |                                                            24766 | {}
  2020-06-03T22:05:07-07:00     | nano.001    | test.numeric                               | numeric |                                                            12865 | {}
  2020-06-03T22:05:08-07:00     | nano.001    | test.numeric                               | numeric |                                                              891 | {}
  2020-06-03T22:05:09-07:00     | nano.001    | test.numeric                               | numeric |                                                            12918 | {}
  2020-06-03T22:05:10-07:00     | nano.001    | test.numeric                               | numeric |                                                            14322 | {}
```

## Query just one stream

You can also query by stream name across all your devices.

```bash
fctl query --stream $.agent.health
```

```bash
         TIMESTAMP (UTC)        | DEVICE NAME |  STREAM NAME   |  TYPE  |           DATA           | TAGS
+-------------------------------+-------------+----------------+--------+--------------------------+------+
  2020-06-03T22:12:28.816-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:29.817-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:30.818-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:31.819-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:32.822-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:33.823-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:34.827-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:12:35.828-07:00 | pi.b.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:18.873-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:19.874-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:20.874-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:21.874-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:22.874-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:23.875-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:24.875-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:25.875-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:26.875-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
  2020-06-03T22:22:27.876-07:00 | nano.001    | $.agent.health | health | {"status":"operational"} | {}
```

You can see how you can query data across devices for the same stream.

## Query for a device

You can also query data for a single device

```bash
fctl query --device nano.001
```

```
         TIMESTAMP (UTC)        | DEVICE NAME |                STREAM NAME                 |  TYPE   |                               DATA                               | TAGS
+-------------------------------+-------------+--------------------------------------------+---------+------------------------------------------------------------------+------+
  2020-06-03T22:24:08.771-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:24:18.785-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:24:28.8-07:00   | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:24:38.814-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:24:48.828-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:24:58.843-07:00 | nano.001    | $.ros.node_online                          | bitset  | {"keys":["/formant_bridge_node","/rosout"],"values":[true,true]} | {}
  2020-06-03T22:15:07-07:00     | nano.001    | test.numeric                               | numeric |                                                            27671 | {}
  2020-06-03T22:15:08-07:00     | nano.001    | test.numeric                               | numeric |                                                             2311 | {}
  2020-06-03T22:15:09-07:00     | nano.001    | test.numeric                               | numeric |                                                            21811 | {}
  2020-06-03T22:15:10-07:00     | nano.001    | test.numeric                               | numeric |                                                            17388 | {}
  2020-06-03T22:15:12-07:00     | nano.001    | test.numeric                               | numeric |                                                             6457 | {}
  2020-06-03T22:15:13-07:00     | nano.001    | test.numeric                               | numeric |                                                            16089 |
```

All the devices streams will appear here.

## Query with start and end time

Sometimes you will want to query historical data or a small slice. You can do that by using UTC RFC3339 timestamps:

```bash
fctl query --start 2020-06-04T05:15:13 --end 2020-06-04T05:15:14
```

```bash

         TIMESTAMP (UTC)        | DEVICE NAME |       STREAM NAME       |  TYPE   |           DATA           | TAGS
+-------------------------------+-------------+-------------------------+---------+--------------------------+------+
  2020-06-03T22:15:13.193-07:00 | pi.b.001    | $.agent.health          | health  | {"status":"operational"} | {}
  2020-06-03T22:15:13.242-07:00 | pi.b.001    | $.host.cpu_util_percent | numeric |       21.000000000003638 | {}
  2020-06-03T22:15:13.808-07:00 | pi.b.001    | $.host.load_avg_1min    | numeric |                     0.43 | {}
  2020-06-03T22:15:13.208-07:00 | pi.b.001    | $.host.mem_used_percent | numeric |        41.94699378522908 | {}
  2020-06-03T22:15:13.6-07:00   | pi.b.001    | $.host.net_util_rx_mbps | numeric |                 0.007808 | {}
  2020-06-03T22:15:13.599-07:00 | pi.b.001    | $.host.net_util_tx_mbps | numeric |                 0.026512 | {}
  2020-06-03T22:15:13.76-07:00  | nano.001    | $.agent.health          | health  | {"status":"operational"} | {}
  2020-06-03T22:15:13.526-07:00 | nano.001    | $.host.cpu_util_percent | numeric |        2.250000007916242 | {}
  2020-06-03T22:15:13.075-07:00 | nano.001    | $.host.load_avg_1min    | numeric |                     0.02 | {}
  2020-06-03T22:15:13.471-07:00 | nano.001    | $.host.mem_used_percent | numeric |        68.11337632947738 | {}
  2020-06-03T22:15:13.031-07:00 | nano.001    | $.host.net_util_rx_mbps | numeric |                 0.004112 | {}
  2020-06-03T22:15:13.031-07:00 | nano.001    | $.host.net_util_tx_mbps | numeric |                 0.012072 | {}
  2020-06-03T22:15:13-07:00     | nano.001    | test.numeric            | numeric |                    16089 | {}
```

## Query by tags

You can also query by tags. We have updated one of our streams to have the `value: actual` tag:

```bash
fctl query --tags 'value:actual'
```

```bash
       TIMESTAMP (UTC)      | DEVICE NAME | STREAM NAME |  TYPE   |    DATA    |        TAGS
+---------------------------+-------------+-------------+---------+------------+--------------------+
  2020-06-03T22:32:48-07:00 | nano.001    | speed       | numeric |   0.459796 | {"value":"actual"}
  2020-06-03T22:32:50-07:00 | nano.001    | speed       | numeric |   0.722872 | {"value":"actual"}
  2020-06-03T22:32:51-07:00 | nano.001    | speed       | numeric |   0.854409 | {"value":"actual"}
  2020-06-03T22:32:52-07:00 | nano.001    | speed       | numeric |   0.985947 | {"value":"actual"}
  2020-06-03T22:32:53-07:00 | nano.001    | speed       | numeric |   0.117485 | {"value":"actual"}
  2020-06-03T22:32:54-07:00 | nano.001    | speed       | numeric |   0.249023 | {"value":"actual"}
  2020-06-03T22:32:55-07:00 | nano.001    | speed       | numeric |   0.380561 | {"value":"actual"}
  2020-06-03T22:32:56-07:00 | nano.001    | speed       | numeric |   0.512098 | {"value":"actual"}
  2020-06-03T22:32:57-07:00 | nano.001    | speed       | numeric |   0.643636 | {"value":"actual"}
  2020-06-03T22:32:58-07:00 | nano.001    | speed       | numeric |   0.775174 | {"value":"actual"}
```

You can also query for multiple tags

```bash
fctl query --tags 'value:actual,limit'
```

```bash
       TIMESTAMP (UTC)      | DEVICE NAME | STREAM NAME |  TYPE   |    DATA    |        TAGS
+---------------------------+-------------+-------------+---------+------------+--------------------+
  2020-06-03T22:35:48-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:49-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:50-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:51-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:52-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:53-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:54-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:35:55-07:00 | nano.001    | speed       | numeric |        1.2 | {"value":"limit"}
  2020-06-03T22:32:48-07:00 | nano.001    | speed       | numeric |   0.459796 | {"value":"actual"}
  2020-06-03T22:32:50-07:00 | nano.001    | speed       | numeric |   0.722872 | {"value":"actual"}
  2020-06-03T22:32:51-07:00 | nano.001    | speed       | numeric |   0.854409 | {"value":"actual"}
  2020-06-03T22:32:52-07:00 | nano.001    | speed       | numeric |   0.985947 | {"value":"actual"}
  2020-06-03T22:32:53-07:00 | nano.001    | speed       | numeric |   0.117485 | {"value":"actual"}
  2020-06-03T22:32:54-07:00 | nano.001    | speed       | numeric |   0.249023 | {"value":"actual"}
  2020-06-03T22:32:55-07:00 | nano.001    | speed       | numeric |   0.380561 | {"value":"actual"}
  2020-06-03T22:32:56-07:00 | nano.001    | speed       | numeric |   0.512098 | {"value":"actual"}
```

## Download uploaded files

`fctl` also allows you to download any files uploaded to `image`, `pointcloud` and `file` streams. For example:

```bash
fctl query --device nano.001 --stream bags --download
```

You'll see this output as files are downloaded.

```bash
Downloaded: 1591720348.bag
Downloaded: 1591720408.bag
Downloaded: 1591720378.bag
Downloaded: 1591720368.bag
Downloaded: 1591720358.bag
Downloaded: 1591720388.bag
Downloaded: 1591720398.bag
```

The files ar downloaded to a directory structure of `<device_name>/<stream_name>/<files>`:

```bash
ls nano.001/bags/
1591720274.bag  1591720348.bag  1591720358.bag  1591720368.bag  1591720378.bag  1591720388.bag  1591720398.bag  1591720408.bag
```

## Advanced usage with `jq`

[`jq`](https://stedolan.github.io/jq/) is a powerful command line utility for JSON data. One of the featues of `fctl` is the ability to output data in JSON. For example:

```bash
fctl query --device nano.001 --stream test.numeric  --start 2020-06-04T05:15:13 --end 2020-06-04T05:15:14 --output json
```

```json
{
    "deviceId": "ff1e0d3b-5044-4db1-a459-c403cc2159a3",
    "deviceName": "nano.001",
    "timestamp": "2020-06-03T22:15:13-07:00",
    "streamName": "test.numeric",
    "value": "16089",
    "type": "numeric",
    "tags": {}
}
```

This output is JSON, but we can prettify it with `jq`:

```bash
fctl query --device nano.001 --stream test.numeric  --start 2020-06-04T05:15:13 --end 2020-06-04T05:15:14 --output json | jq
```

```json
{
    "deviceId": "ff1e0d3b-5044-4db1-a459-c403cc2159a3",
    "deviceName": "nano.001",
    "timestamp": "2020-06-03T22:15:13-07:00",
    "streamName": "test.numeric",
    "value": "16089",
    "type": "numeric",
    "tags": {}
}
```

Way better. We can also extract single fields with `jq`:

```bash
fctl query --device nano.001 --stream test.numeric  --start 2020-06-04T05:15:13 --end 2020-06-04T05:15:14 --output json | jq '.value'
```

```json
"16089"
```

Let's actually look at this value in real-time. `fctl` has an additional flag for following data `-f` or `--follow`. Let's also switch over to our `speed` stream:

```bash
fctl query --device nano.001 --stream speed --follow --output json | jq '.value'
```

```json
"0.553797"
"0.685334"
"0.816872"
"0.94841"
"0.0799478"
"0.343023"
"1.2"
"1.2"
"1.2"
"1.2"
.
.
.
```

One thing we notice here immediately is that we have both the `limit` and `actual` intermixed. Let's use `jq` to clear that up a bit. Notice in this example we construct an output JSON with the tag `value` as the key:

```bash
fctl query --device nano.001 --stream speed --follow --output json | jq '{ (.tags.value): .value }'
```

```json
{
  "actual": "0.5319"
}
{
  "actual": "0.663438"
}
{
  "actual": "0.794976"
}
{
  "actual": "0.926513"
}
{
  "limit": "1.2"
}
{
  "limit": "1.2"
}
{
  "limit": "1.2"
}
{
  "limit": "1.2"
}
{
  "actual": "0.0580511"
}
{
  "actual": "0.189589"
}
{
  "actual": "0.321127"
}
{
  "actual": "0.452664"
}
```

We can get fancier when we start using `jq` programs like those found in the [jq directory](jq/). One note on these programs is they require the use of the `--slurp` flag so you won't be able to run these wit the fctl `--follow` flag. However, you could programatically loop using standard bash utilites.

First let's calculate the average, variance, and standard deviation of our actual speed (assume these are run from the `docs` directory) using the [math.jq program](jq/math.jq):

```bash
fctl query --device nano.001 --start  2020-06-05T05:40:00 --end 2020-06-05T05:55:00 --stream speed --tags 'value:actual'  --output json | jq -s -f jq/math.jq
```

```json
{
    "avg": 0.5017421673093813,
    "stdev": 0.2898920770688194,
    "variance": 0.08403741634727435
}
```

Next, let's use the [filter.jq program](jq/filter.jq) to filter our data for any actual speed greater than 0.8:

```bash
fctl query --device nano.001 --start  2020-06-05T05:40:00 --end 2020-06-05T05:41:00 --stream speed --tags 'value:actual'  --output json | jq -s -f jq/filter.jq
```

```json
[
    {
        "deviceId": "8aced12e-4514-4e13-96c9-e881fd3e5f24",
        "deviceName": "nano.001",
        "timestamp": "2020-06-04T22:41:13-07:00",
        "streamName": "speed",
        "value": "0.751275",
        "type": "numeric",
        "tags": {
            "hw": "jetson_nano",
            "value": "actual"
        }
    },
    {
        "deviceId": "8aced12e-4514-4e13-96c9-e881fd3e5f24",
        "deviceName": "nano.001",
        "timestamp": "2020-06-04T22:41:14-07:00",
        "streamName": "speed",
        "value": "0.882812",
        "type": "numeric",
        "tags": {
            "hw": "jetson_nano",
            "value": "actual"
        }
    }
]
```

We can show how to group averages across a set of tags. In this example we'll calculate averages for all values in the `speed` stream grouped by the `value` tag. This is defined in the [bucket_tags.jq](jq/bucket_tags.jq)

```bash
fctl query --device nano.001 --start  2020-06-05T05:40:00 --end 2020-06-05T05:42:00 --stream speed   --output json | jq -s -f jq/bucket_tags.jq
```

```json
[
    {
        "value": "actual",
        "avg": 0.5111393844444444
    },
    {
        "value": "limit",
        "avg": 1.200000000000001
    }
]
```

Similar to bucketing by tags we can also bucket by device using the [bucket_device.jq program](jq/bucket_device.jq). Let's see how our averages compare across our devices:

```bash
fctl query --start  2020-06-05T06:30:00 --end 2020-06-05T06:35:00 --stream speed --tags 'value:actual'   --output json | jq -s -f jq/bucket_device.jq
```

```json
[
    {
        "value": "pi.b.001",
        "avg": 0.5680556666666668
    },
    {
        "value": "nano.001",
        "avg": 0.8522845626555992
    }
]
```

As you can see we're fans of both raspberry pi's and Nvidia jetson boards. Let's see our speed averages grouped by the tag `hw` with the [bucet_hw.jq program](jq/bucket_hw.jq):

```bash
$ fctl query  --start  2020-06-05T06:40:00 --end 2020-06-05T06:45:00 --stream speed --tags 'value:actual'  --output json | jq -s -f jq/bucket_hw.jq
```

```json
[
    {
        "value": "pi_b",
        "avg": 0.5098477718562874
    },
    {
        "value": "jetson_nano",
        "avg": 0.5094469515093457
    }
]
```
