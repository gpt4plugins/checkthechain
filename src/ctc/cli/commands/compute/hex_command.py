import toolcli

from ctc import binary


def get_command_spec() -> toolcli.CommandSpec:
    return {
        'f': hex_command,
        'help': 'convert ascii to hex',
        'args': [
            {'name': 'data'},
            {'name': '--raw', 'action': 'store_true'},
        ],
    }


def hex_command(data, raw):
    if raw:
        output = binary.ascii_to_raw_hex(data)
    else:
        output = binary.ascii_to_prefix_hex(data)
    print(output)
