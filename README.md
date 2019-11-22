- [About](#sec-1)
- [Dependencies](#sec-2)
- [Invite TranslAAAAAAAAAAAAAAAAAtor](#sec-3)
- [Running the project](#sec-4)
- [Licence](#sec-5)
- [Contributing](#sec-6)

![img](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)

# About<a id="sec-1"></a>

TranslAAAAAAAAAAAAAAAAAtor is a meme bot inspired by the subreddit [r/AAAAAAAAAAAAAAAAA](https://www.reddit.com/r/AAAAAAAAAAAAAAAAA/). What it does is translate a sentence given to it by replacing all characters (except whitespace) into As. That’s it. That’s literally it.

# Dependencies<a id="sec-2"></a>

The only dependency of translAAAAAAAAAAAAAAAAAtor is [Discord.py](https://github.com/Rapptz/discord.py) which powers the bot itself.

# Invite TranslAAAAAAAAAAAAAAAAAtor<a id="sec-3"></a>

Maybe you do not want to build the bot itself, but instead you just want to invite it on your server? I got you covered! You can invite the official instance of TranslAAAAAAAAAAAAAAAAAtor by clicking [here](https://discordapp.com/api/oauth2/authorize?client_id=647381498827243543&permissions=67584&scope=bot)!

Be aware though that I cannot ensure 24/7 uptime of TranslAAAAAAAAAAAAAAAAAtor. If you notice it is down, shoot me a tweet (faster), a DM (fast, P'undrak#0001) or an email (slower).

# Running the project<a id="sec-4"></a>

First, you will need docker and docker-compose installed on your machine. If they aren’t installed yet, go check Docker’s or your distro’s instruction on how to get them.

To Run This Project, you will only need the [docker-compose.yml](docker-compose.yml) file from this repository. You can get it by running the following command on your machine:

```sh
wget -c https://raw.githubusercontent.com/phundrak/translaaaaaaaaaaaaaaaaator/master/docker-compose.yml
```

Or you can clone the whole project if you wish.

Due to obvious security reasons, I am not giving away the token of my bot in the source code, and you should not either. This is why this project will try to get it from your environment variables. To do so, edit the docker-compose file to add the environment key \`BOT<sub>TOKEN</sub>\`, like so:

```yaml
version: '3'
services:
  bot:
    image: phundrak/translaaaaaaaaaaaaaaaaator:latest
    command: python translaaaaaaaaaaaaaaaaator.py
    environment:
      - BOT_TOKEN=yourtoken
```

You can now run the project within a contained environment by running the following command:

```sh
docker-compose up
```

If you wish to have it detached from your terminal, you can add the \`-d\` switch to the command:

```sh
docker-compose up -d
```

And that’s it! Your bot should be up and running once your container is built, which happens only the first time you launch it. If you want to stop TranslAAAAAAAAAAAAAAAAAtor, simply hit `Ctrl-c` in your terminal if you haven’t detached the process, or run `docker-compose down` if you did.

# Licence<a id="sec-5"></a>

This project is under the free GPLv3 licence. You can find the complete licence in <LICENCE.md>.

# Contributing<a id="sec-6"></a>

Submit a pull request, and I’ll review it when I’ll have time to (this is not a project I will pour a lot of efforts into). Simply be aware that I’d prefer it if your code is written with meaningful variables (I should fix that), comments (I should fix that), and be aware that readability is above all. Also, don’t be an asshole (that’s the project’s Code of Conduct for y’all).
