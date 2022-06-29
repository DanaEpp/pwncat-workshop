#!/usr/bin/env python3
from io import StringIO

from pwncat import util
from pwncat.modules import Status, BaseModule, ModuleFailed, Argument
from pwncat.manager import Session
from pwncat.platform.linux import Linux

class Module(BaseModule):
    """ Sample custom module """

    """
    Usage: run sample 
    """
    PLATFORM = [Linux]
    ARGUMENTS = {}

    def run(self, session: "pwncat.manager.Session"):
        yield Status( "preparing to pwn the [red]world[/red]")

        # Do your work here.

        session.log( f"ran {self.name}")
