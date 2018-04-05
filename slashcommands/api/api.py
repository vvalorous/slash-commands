# coding=utf-8

from importlib import import_module

from flask import Flask, request

from slashcommands.base import SlashCommand

app = Flask(__name__)
app.config.from_object('settings')


def load_commands(installed_commands):
    """
    This method loads all the installed commands

    Args:
        installed_commands (tuple) -- list of commands installed
    """
    for command in installed_commands:
        import_module(command)


def get_all_subclasses(cls):
    """
    This method identifies all the subclasses of a given class

    Args:
        cls (class) -- class whose subclasses has to be identified

    Returns:
        list
    """
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    return all_subclasses


def get_handler(command):
    """
    This method identifies the class associated with the command

    Args:
        command (str) -- command whose handler/definition needs to be identified

    Returns:
        object
    """
    commands = get_all_subclasses(SlashCommand)
    for command in commands:
        if command.command == payload['command']:
            return command(payload)


@app.route("/slash-commands", methods=['POST'])
def dispatcher():
    """ This method dispatches request to respective handlers """
    payload = request.get_json()
    handler = get_handler(payload['command'])
    handler.execute.delay()


if __name__ == '__main__':
    """ main function aka entrypoint """
    installed_commands = app.config['INSTALLED_COMMANDS']
    load_commands(installed_commands)
    app.run(host='0.0.0.0')
