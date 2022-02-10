from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner
from setups.runapp import cli


@patch("setups.runapp.uvicorn")
def test_run_app_cli_debug(patch_uvicorn):

    runner = CliRunner()
    result = runner.invoke(cli, ["--debug"])
    patch_uvicorn.run.assert_called_once_with(
        "setups.app:app", host="0.0.0.0", port=5002, reload=True
    )


@patch("setups.runapp.uvicorn")
def test_run_app_cli(patch_uvicorn):

    runner = CliRunner()
    result = runner.invoke(cli)
    patch_uvicorn.run.assert_called_once_with(
        "setups.app:app", host="0.0.0.0", port=5002, reload=False
    )


class RunAppFaileur(TestCase):
    @patch("setups.runapp.uvicorn")
    def test_run_app_cli_fail(self, patch_uvicorn):
        patch_uvicorn.run.side_effect = ValueError("error message")
        runner = CliRunner()
        result = runner.invoke(cli)
        self.assertEqual("error message\n", result.output)
