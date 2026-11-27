# Copyright (C) 2026 Mark Losey. All rights reserved.
"""store_lock -- the machine-wide lock seam: the flock that spans processes.

The mcp-server unit (F1's ruled clause, the approved design brief
reports/synthesize/mcp-design.md:22-23): an advisory exclusive fcntl.flock
on {store_home}/.prioritree.lock -- created on demand, NEVER deleted (flock
binds the inode; a deleted lockfile is a NEW lock -- a second writer locking
a fresh inode is no lock at all), acquired around each WHOLE store act
(load->act->save), released before rendering (the service seam's own law,
service_store.py:72). THE FLOCK'S GUARANTEE, narrowed honestly: it
serializes every writer THAT COMPOSES THE SEAM -- the harness-launched
session servers, the localhost service, the CLI, the web child, the mcp
doors; the LOCAL CLASS'S DIRECT REACH the standing residual (the key
fences the socket, never the filesystem -- every local process owns
every surface, the README's honest statement); the armed doors'
verification a DIFFERENT axis (identity at the wire, never file
access). Stdlib only (the tier fence, service_store.py:15); the lock
path derives from the INJECTED home, never re-defaulted (the
service_store.py:90-91 precedent -- the hidden-global drift refused).
"""

from __future__ import annotations

import fcntl
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from pathlib import Path
    from typing import IO

__all__ = ["Lock"]

_LOCK_FILE_NAME: Final[str] = ".prioritree.lock"


class Lock:
    """Lock the store acts across processes under one machine-wide file lock.

    Purpose: one advisory exclusive flock (fcntl.LOCK_EX, blocking until
    granted) on the lockfile at the injected store home -- the context
    manager the three writer tiers compose (the MCP server, the service's
    Serialize verbs, the CLI's handlers): acquired around each WHOLE store
    act, held across load->act->save, released before rendering. The
    lockfile is opened "a" -- create-if-absent, NEVER truncated (the file's
    bytes are nobody's; the INODE is the lock's identity) -- and NEVER
    deleted by this hand (flock binds the inode: a deleted lockfile is a new
    lock, the cure collapsing at the first unlink -- the inode law carried
    here, never violated at exit).
    Refuses when: never -- LOCK_EX blocks until granted (advisory on darwin;
    the guarantee bounded to the seam's composers: every writer THAT
    COMPOSES THE SEAM is serialized under it; the local class's direct
    reach the named residual, never the flock's to fence).
    Re-run: deterministic in effect -- the same home derives the same lock
    path; re-entry serializes (a second holder blocks until the first
    releases).
    Touches: the lockfile alone (created on demand, never truncated, never
    deleted); the store files are the CALLER's acts inside the held lock.
    Provenance: the approved design brief F1 (the seam's ruled clause
    whole), the unit brief reports/synthesize/mcp-server.md SS3 (the
    composition clauses), the naming law (the act-statement's first word),
    G-MCPSERVERSPEC-BRIEF.
    """

    def __init__(self, store_home: Path) -> None:
        """Hold the injected home and derive the lock path -- never re-defaulted.

        Purpose: the lock path DERIVES from the injected home
        ({store_home}/.prioritree.lock) -- store-as-parameter, the
        STORE_HOME law (run_store.py:67); the default never re-derived
        here (the hidden-global drift refused, the service_store.py:90-91
        precedent).
        Refuses when: never -- construction derives and holds.
        Re-run: idempotent -- a fresh Lock over the given home; no
        acquisition at construction.
        Touches: nothing -- the path is derived, the file opened at
        __enter__ alone.
        Provenance: F1 (the home-injection law), G-MCPSERVERSPEC-BRIEF.
        """
        self._store_home = store_home
        self._lock_path = store_home / _LOCK_FILE_NAME
        self._handle: IO[str] | None = None

    def __enter__(self) -> None:
        """Open "a" and flock LOCK_EX -- blocking until granted."""
        # Created on demand ("a" -- create-if-absent, never truncated),
        # NEVER deleted: flock binds the inode; a deleted lockfile is a
        # NEW lock (the inode law, the docstring's own clause).
        self._store_home.mkdir(parents=True, exist_ok=True)
        self._handle = self._lock_path.open("a")
        fcntl.flock(self._handle.fileno(), fcntl.LOCK_EX)

    def __exit__(self, _exc_type: object, _exc_value: object, _traceback: object) -> None:
        """Release the flock and close the handle -- the file itself NEVER deleted."""
        if self._handle is None:
            return
        fcntl.flock(self._handle.fileno(), fcntl.LOCK_UN)
        self._handle.close()
