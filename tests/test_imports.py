"""Smoke tests for the installed package and its initial module structure."""

from importlib import import_module
from types import ModuleType

import pytest


def test_package_import() -> None:
    """The installed top-level package can be imported."""
    assert isinstance(import_module("mimolab"), ModuleType)


@pytest.mark.parametrize(
    "module_name",
    [
        "channels",
        "p2p",
        "mu_uplink",
        "mu_downlink",
        "estimation",
        "detection",
        "massive",
        "distributed",
        "metrics",
    ],
)
def test_module_import(module_name: str) -> None:
    """Each planned library module can be imported independently."""
    assert isinstance(import_module(f"mimolab.{module_name}"), ModuleType)
