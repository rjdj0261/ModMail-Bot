# ModMail

[![License](https://img.shields.io/github/license/ReyBotDev/ModMail-Bot.svg)](https://github.com/ReyBotDev/ModMail-Bot/blob/master/LICENSE?style=for-the-badge)
![Github Total lines](https://tokei.rs/b1/github/ReyBotDev/ModMail-Bot?style=for-the-badge)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintaner](https://img.shields.io/badge/maintainer-ReyBotDev-blue)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://dsc.gg/modmail-support)
[![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://GitHub.com/ReyBotDev/ModMail-Bot/releases/)


A feature-rich Discord bot for easy communication between server staff and users.

A new channel is created whenever a user messages the bot, and the channel will serve as a shared
inbox for seamless communication between staff and the user.

To learn more, check out our [Discord server](https://dsc.gg/modmail-support).

[![Invite ModMail](https://raw.githubusercontent.com/nsde/neovision/main/readme_images/add-to-dc.png)](https://dsc.gg/modmail-bot)

## Premium

For premium join our [Support Server](https://dsc.gg/modmail-support).

## Progress

To know the progress of our project check our [Progress Board](https://github.com/ReyBotDev/ModMail-Bot/projects/1).

## Supporting

Click the Sponsor button and choose any one option to support us.

## Contributing

There are many ways you can contribute to this project:

- [Submitting bugs and suggestions](https://github.com/ReyBotDev/ModMail-Bot/issues)
- [Reviewing pull requests](https://github.com/ReyBotDev/ModMail-Bot/pulls)
- [Contribute directly to the code base](https://github.com/ReyBotDev/ModMail-Bot/pulls)

For more information, please see
our [contributing guidelines](https://github.com/ReyBotDev/ModMail-Bot/blob/master/CONTRIBUTING.md).

The issue tracker here is only for bug reports and suggestions. Please do not use it to ask a
question. Instead, ask it on our [Discord server](dsc.gg/modmail-support).

## Self-Hosting

This self-hosting guide requires you to have some basic knowledge about command line, Python, and
Discord bots.

### Prerequisites

In order to run ModMail, you will need to install the following software. Please also note that
ModMail can only be hosted on UNIX based operating systems. Windows is not supported.

- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Redis](https://redis.io/download/)
- [ffmpeg](https://www.ffmpeg.org)
- [MySQL](https://www.mysql.com/)

### Installing the dependencies

Installing Python 3:-

Follow this guide to install python :- [Here](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)

Installing Git:-

Follow this guide to install git :- [Here](https://linuxize.com/post/how-to-install-git-on-ubuntu-18-04/)

Installing Ffmpeg:-

Follow this guide to install ffmpeg :- [Here](https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-18-04/)

Installing Postgresql:-

Follow this guide to install Postgresql :- [Here](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)

Installing Redis :-

Follow this guide to install Redis :- [Here](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)

### Getting the Sources

Clone this repository, or fork and clone if you wish to make pull requests.

```sh
git clone https://github.com/ReyBotDev/Modmail-Bot.git
```

### Configuration

Configuration is done through a `config.py` file. A template can be found in `config.example.py`.
You can create a copy of it and rename it to `config.py`, then fill in the configurations.

### Installing Modules

ModMail utilises several modules to function properly. The list of modules can be found
in `requirements.txt`. You can install them with the following command.

```sh
pip install -r requirements.txt
```

### Running the Bot

Congratulations! You have set up everything, and you can finally have the bot up and running. Use the following command to start the bot.

```sh
python3 launcher.py
```

## License

This project is licensed
under [GNU Affero General Public License v3.0](https://github.com/ReyBotDev/ModMail-Bot/blob/master/LICENSE).

## Code Of Conduct

Please check our [Code Of Conduct](https://github.com/ReyBotDev/ModMail-Bot/blob/main/CODE_OF_CONDUCT.md) here for knowing more.

## Security Policies

Please check our [Security Policy](https://github.com/ReyBotDev/ModMail-Bot/blob/main/SECURITY.md) here to know more.

## Powered By

[Railway](https://railway.app)

## Thanks to

[Chamburr](https://github.com/chamburr) for providing [modmail base](https://github.com/chamburr/modmail).