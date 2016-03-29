**WARNING:** Using this might result in a ban, so use at your own risk.

-----------------

# notice-me
A proof of concept to show the way project collaborators notifications are handled in Github is flawed.

## What?
`notice-me` is a quick way to search for the most followed people on Github and then quickly add and remove them as a collaborator your project.
This will alert their followers that they have been added to your project, dramatically increasing the reach it has to Github users.

## How?
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

## License
MIT
