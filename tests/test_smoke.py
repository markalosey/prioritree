# Copyright (C) 2026 Mark A Losey. All rights reserved.
"""The born tree's smoke test — the import answers, the namespace lives."""

import prioritree


def test_prioritree_imports() -> None:
    """Pin the import — src/prioritree resolves and answers its name."""
    assert prioritree.__name__ == "prioritree"
