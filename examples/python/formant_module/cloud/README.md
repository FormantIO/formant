# Pre-requisites for using the formant cloud python module

### Installation

1. `pip install formant`, or `pip3 install formant`

### Service account

Service account authentication is necessary to use the Formant cloud SDK. To create a service account, we can use `fctl`, the Formant administrative command line tool.

See: https://docs.formant.io/device-management/installing-fctl

Once you have installed and authenticated `fctl` with your administrator email and password, we can create a service account. Run:

`fctl create service-account -h`

to see an example.

After successfully running this command, `fctl` will output the required credentials for your service account, including service account email and password.

Store these credentials in a secure location. This is the only time you will be able to copy this password.
