# fctl

`fctl` is our command line utility for interacting with the Formant platform.

## Install fctl

### Convenience Script

For Linux and Mac we provide a simple convenience script:

```
bash <(curl -s https://app.formant.io/install-fctl.sh)
```

This will intstall `fctl` on your system and prop you for admin credentials. This will also configure your `~/.ssh/config` for ssh over Formant's peer-to-peer connection.

### Linux:

You can follow the same repo setup steps for the agent found [here](./install-agent.md/#repo-setup).

Next, update and install the fctl debian package:

```bash
sudo apt update
sudo apt install fctl
```

### Mac

Setup the Formant tap and install via homebrew:

```bash
brew tap formantio/formant
brew install formantio/formant/fctl
```

### Docker

First you'll need to initialize the fctl container with a volume mount on your local machine to store tokens (make sure to include a ' ' before the command so it doesn't save to your history):

```bash
 docker run -it -v <permanent_storage>:/root/.formant -e FORMANT_EMAIL=<admin_email> -e FORMANT_PASSWORD=<admin_password> formant/fctl init
```

Replace `<permanent_storage>` with a mount path on your local host system, and fill in your admin credentials.

## Verify Installation (Mac/Linux):

Check that fctl is available by running:

```bash
fctl -h
```

You should see:

```
fctl supports command-line interaction with the Formant Cloud APIs

Usage:
fctl [command]

Available Commands:
completion Generate completion scripts
create Create a resource
describe Describe a resource
help Help about any command
init Reinitialize fctl credentials
list List a resource
port-forward Port forward to your device, used for SSH, SCP, and network tunneling.
provision Provision a resource
query Query ingested datapoints
version Get fctl version

Flags:
-h, --help display detailed help for fctl

Use "fctl [command] --help" for more information about a command.
```

## Credential fctl (Mac/Linux)

fctl requires admin level privileges on your Formant account. We never store your email/password on disk so you initialize by running:

```bash
fctl init
```
