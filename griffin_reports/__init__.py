# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------

#


# -----------------------------------------------------------------------------
"""Griffin Reports Plugin."""

from ._version import __version__  # noqa: F401
from .reportsplugin import ReportsPlugin

# The following statements are required to register this 3rd party plugin:

PLUGIN_CLASS = ReportsPlugin  # pylint: disable=invalid-name
