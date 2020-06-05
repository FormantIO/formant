# Upload Offline Data with fctl

Many times you will need to uploaded offline data for one of your robots that is indexed alongside all of your existing robot data. For example, you may have ROS bags that are collected post mission on a hard drive that are uploaded once your robot is back home.

[`fctll'](./fctl.md) our command line tool makes this quite simple.

## Upload files

To upload a file for a specific device:

```bash
fctl upload alpha.003 --stream bag.upload --file /home/ubuntu/bags/2020-05-22.bag --type file --tags 'mission:autowalk;sw_version:0.8.1' --timestamp 2020-05-22T12:05:10
```

This will upload the file `/home/ubuntu/bags/2020-05-22.bag` indexed to the device `alpha.003` on the stream `bag.upload`. The file is uploaded with `type=file` which means you will see the file browsing widget and be able to download that file. Additionally, you can include tags on the datapoint, in this case we include the `mission` and `sw_version`. Tags that are set on `alpha.003` will automatically be applied. The last piece here is the timestamp `2020-05-22T12:05:10`. This is in RFC3339 format (YYYY-MM-DDThh:mm:ss) and is UTC.

## Watch a directory

`fctl upload` also lets you watch a directory:

```
fctl upload alpha.003 --stream bag.upload --directory /home/ubuntu/bags/ --type file --tags 'mission:autowalk;sw_version:0.8.1'
```

Similar to the upload file example above, we use the `upload` command and specify the `stream`, `tags`, and `type` parameters. The main difference here is the `--directory` parameter. When this parameter is specified `fctl upload` will begin watching that directory for new files. When a new file is created in that directory it will upload with the given parameters and use the current timestamp.

## Upload remote file references

In some cases, you may wish to reference assets stored in your own private cloud. `fctl upload` allows you to ingest datapoints that allow you to time align these assets along with the rest of the data you send to Formant:

```bash
fctl upload alpha.003 --stream bag.upload --file https://storage.googleapis.com/cartographer-public-data/bags/toru/hallway_localization.bag --type file --tags 'mission:autowalk;sw_version:0.8.1' --timestamp 2020-05-22T12:05:10
```
