# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ConfluentClusterArgs', 'ConfluentCluster']

@pulumi.input_type
class ConfluentClusterArgs:
    def __init__(__self__, *,
                 kafka_cluster_name: pulumi.Input[str],
                 kafka_topics: pulumi.Input[Sequence[pulumi.Input[str]]],
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConfluentCluster resource.
        :param pulumi.Input[str] kafka_cluster_name: Name to use for kafka cluster display name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] kafka_topics: Array of topics for the kafka cluster.
        :param pulumi.Input[str] region: Region for cluster. Default is region used by rest of stack.
        """
        pulumi.set(__self__, "kafka_cluster_name", kafka_cluster_name)
        pulumi.set(__self__, "kafka_topics", kafka_topics)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="kafkaClusterName")
    def kafka_cluster_name(self) -> pulumi.Input[str]:
        """
        Name to use for kafka cluster display name.
        """
        return pulumi.get(self, "kafka_cluster_name")

    @kafka_cluster_name.setter
    def kafka_cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kafka_cluster_name", value)

    @property
    @pulumi.getter(name="kafkaTopics")
    def kafka_topics(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Array of topics for the kafka cluster.
        """
        return pulumi.get(self, "kafka_topics")

    @kafka_topics.setter
    def kafka_topics(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "kafka_topics", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region for cluster. Default is region used by rest of stack.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class ConfluentCluster(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kafka_cluster_name: Optional[pulumi.Input[str]] = None,
                 kafka_topics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ConfluentCluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kafka_cluster_name: Name to use for kafka cluster display name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] kafka_topics: Array of topics for the kafka cluster.
        :param pulumi.Input[str] region: Region for cluster. Default is region used by rest of stack.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfluentClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ConfluentCluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ConfluentClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfluentClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kafka_cluster_name: Optional[pulumi.Input[str]] = None,
                 kafka_topics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfluentClusterArgs.__new__(ConfluentClusterArgs)

            if kafka_cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'kafka_cluster_name'")
            __props__.__dict__["kafka_cluster_name"] = kafka_cluster_name
            if kafka_topics is None and not opts.urn:
                raise TypeError("Missing required property 'kafka_topics'")
            __props__.__dict__["kafka_topics"] = kafka_topics
            __props__.__dict__["region"] = region
            __props__.__dict__["env_id"] = None
            __props__.__dict__["kafka_url"] = None
        super(ConfluentCluster, __self__).__init__(
            'kafkacluster:index:ConfluentCluster',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="envId")
    def env_id(self) -> pulumi.Output[str]:
        """
        Name of the Confluent environment that was created
        """
        return pulumi.get(self, "env_id")

    @property
    @pulumi.getter(name="kafkaUrl")
    def kafka_url(self) -> pulumi.Output[str]:
        """
        URL for the Kafka environment.
        """
        return pulumi.get(self, "kafka_url")

