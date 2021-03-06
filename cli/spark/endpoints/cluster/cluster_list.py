import argparse
import typing
import aztk
from cli import utils, config


def setup_parser(_: argparse.ArgumentParser):
    # No arguments for list yet
    pass


def execute(_: typing.NamedTuple):
    spark_client = aztk.spark.Client(config.load_aztk_screts())
    clusters = spark_client.list_clusters()
    utils.print_clusters(clusters)
