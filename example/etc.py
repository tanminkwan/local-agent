
def command_converter(message: dict) -> tuple[dict, str]:
    return message.get('initial_param'), message.get('executer')