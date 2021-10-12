
import socket
import typing

from termcolor import cprint
from nubia import argument, command, context

import asyncio
import sys

from nubia import Nubia, Options

@command
@argument("hosts", description="Hostnames to resolve", aliases=["i"])
@argument("bad_name", name="nice", description="testing")
def lookup(hosts: typing.List[str], bad_name: int) -> int:
    """
    This will lookup the hostnames and print the corresponding IP addresses
    """
    ctx = context.get_context()

    if not hosts:
        cprint("No hosts supplied via --hosts")
        return 1

    print(f"hosts: {hosts}")
    cprint(f"Verbose? {ctx.verbose}")

    for host in hosts:
        cprint(f"{host} is {socket.gethostbyname(host)}")

    return 0


if __name__ == "__main__":
    shell = Nubia(
        name="nubia_example",
        command_pkgs=[lookup],
        options=Options(
            persistent_history=False, auto_execute_single_suggestions=False
        ),
    )
    loop = asyncio.get_event_loop()
    sys.exit(loop.run_until_complete(shell.run()))

