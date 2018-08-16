#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `programmingquotes` package."""


import unittest
from click.testing import CliRunner

from programmingquotes import pq
from programmingquotes import cli


class TestProgrammingquotes(unittest.TestCase):
    """Tests for `programmingquotes` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        result = runner.invoke(cli.main, ["--language", "de"])
        assert result.exit_code == 0
        result = runner.invoke(cli.main, ["--language", "en"])
        assert result.exit_code == 0
        result = runner.invoke(cli.main, ["--language", "bullshit"])
        assert result.exit_code == 0
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
