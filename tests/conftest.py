# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The cycle's teaching conftest — the service-first pre-import.

The web<->service import cycle (web.py:74-75 <-> service.py:729) resolved
AT COLLECTION: importing service first binds app above the tail's web
import, so every single-module run is green (FR-MEM-0045's cheap shape);
the conftest TEACHES, never cures — the cycle stands, the lazy restructure
the root cure (FR-MEM-0045 earned-later standing).
"""
from prioritree.service import app as service_app

_ = service_app  # the bound name referenced — the side-effect import's honest form (F401 never firing live)
