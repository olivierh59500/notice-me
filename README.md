**WARNING:** Using this **will** result in a ban, so use at your own risk (or just don't use it).

-----------------

# notice-me
A proof of concept to show the flaw in project collaborator notifications on Github

## What?
`notice-me` is a quick way to search for the most followed people on Github and then quickly add and remove them as a collaborator your project.
This will alert their followers that they have been added to your project, dramatically increasing the reach it has to Github users.

## How?
**Please see warning at the top of the readme before proceeding.**

[Download](https://github.com/719Ben/attention-whore/archive/master.zip) or clone `notice-me` to your computer.
```bash
git clone git@github.com:719Ben/notice-me.git
```
Make sure that you have both [python3](https://www.python.org/downloads/) and `requests` installed.
```bash
pip install requests
```
Run `notice-me`.
```bash
python3 notice_me.py
```
When asked for a `password (or access code)`, [create one](https://github.com/settings/tokens) with the `repo` scope.

## FAQ
**Should I use this?**

No. It's a proof of concept.

**Why though, I want to show people my project...**

This repository wasn't created to help you spam developers all over the world. It was created to show how easy it is to spam people, so that GitHub fixes the issue. You really shouldn't use this. It's super annoying.

**How can GitHub fix this issue?**

Have users confirm that they want to join a repository before telling all the user's followers that they have joined a repository.

**When should I add people as collaborator to a project?**

If and only if you have their prior permission to add them.

## License
MIT
