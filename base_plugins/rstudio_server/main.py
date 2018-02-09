from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget
from aztk.error import InvalidPluginConfigurationError


def definition():
    return PluginDefinition(
        name="rstudio_server",
        ports=[
            PluginPort(
                remote=8787,
                local=8787,
            ),
        ],
        runOn=PluginRunTarget.Master,
        execute="rstudio_server.sh",
        files=[
            "rstudio_server.sh",
        ],
        args=[
            ("version", "1.1.383"),
        ],
    )


def validate_args(version: str):
    return True


def process_args(version: str):
    return dict(
        RSTUDIO_SERVER_VERSION=version
    )
