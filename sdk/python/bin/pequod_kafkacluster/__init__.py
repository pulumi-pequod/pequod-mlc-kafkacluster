# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .confluent_cluster import *
from .provider import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "kafkacluster",
  "mod": "index",
  "fqn": "pequod_kafkacluster",
  "classes": {
   "kafkacluster:index:ConfluentCluster": "ConfluentCluster"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "kafkacluster",
  "token": "pulumi:providers:kafkacluster",
  "fqn": "pequod_kafkacluster",
  "class": "Provider"
 }
]
"""
)