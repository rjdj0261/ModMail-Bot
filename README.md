# ModMail

[![Discord](https://discordapp.com/api/guilds/833891430702907442/embed.png)](dsc.gg/modmail-support)
[![License](https://img.shields.io/github/license/chamburr/modmail.svg)](https://github.com/flyingpythonstudios/ModMail-Bot/blob/master/LICENSE)

A feature-rich Discord bot for easy communication between server staff and users.

A new channel is created whenever a user messages the bot, and the channel will serve as a shared
inbox for seamless communication between staff and the user.

To learn more, check out our [Discord server](dsc.gg/modmail-support).

## Contributing

There are many ways you can contribute to this project:

- [Submitting bugs and suggestions](https://github.com/flyingpythonstudios/ModMail-Bot/issues)
- [Reviewing pull requests](https://github.com/flyingpythonstudios/ModMail-Bot/pulls)
- [Contribute directly to the code base](https://github.com/flyingpythonstudios/ModMail-Bot/pulls)

For more information, please see
our [contributing guidelines](https://github.com/flyingpythonstudios/ModMail-Bot/blob/master/CONTRIBUTING.md).

The issue tracker here is only for bug reports and suggestions. Please do not use it to ask a
question. Instead, ask it on our [Discord server](dsc.gg/modmail-support).

## Self-Hosting

This self-hosting guide requires you to have some basic knowledge about command line, Python, and
Discord bots. We do not provide any support for self-hosting.

### Prerequisites

In order to run ModMail, you will need to install the following software. Please also note that
ModMail can only be hosted on UNIX based operating systems. Windows is not supported.

- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Redis](https://redis.io/download/)
- [RabbitMQ](https://www.rabbitmq.com/download.html)

### Getting the Sources

Clone this repository, or fork and clone if you wish to make pull requests.

```sh
git clone https://github.com/chamburr/modmail.git
```

### Configuration

Configuration is done through a `config.py` file. A template can be found in `config.example.py`.
You can create a copy of it and rename it to `config.py`, then fill in the configurations.

### Installing Modules

ModMail utilises several modules to function properly. The list of modules can be found
in `requirements.txt`. You can install them with the following command.

```sh
pip3 install -r requirements.txt
```

### Running the Bot

Congratulations! You have set up everything, and you can finally have the bot up and running. Use the following command to start the bot.

```sh
python3 launcher.py
```

## License

This project is licensed
under [GNU Affero General Public License v3.0](https://github.com/flyingpythonstudios/ModMail-Bot/blob/master/LICENSE).

## Code Of Conduct

Please check our [Code Of Conduct](https://github.com/ReyBotDev/ModMail-Bot/blob/main/CODE_OF_CONDUCT.md) here for knowing more.

## Contributing

Please check our [Contributing Rules](https://github.com/ReyBotDev/ModMail-Bot/blob/main/CONTRIBUTING.md) here for more info.

## Security Policies

Please check our [Security Policy](https://github.com/ReyBotDev/ModMail-Bot/blob/main/SECURITY.md) here to know more.

## Developers

[ReyBotDev](https://github.com/ReyBotDev)

[Chamburr](https://github.com/chamburr)
