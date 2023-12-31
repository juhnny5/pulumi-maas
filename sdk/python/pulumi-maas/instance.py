# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 allocate_params: Optional[pulumi.Input['InstanceAllocateParamsArgs']] = None,
                 deploy_params: Optional[pulumi.Input['InstanceDeployParamsArgs']] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input['InstanceAllocateParamsArgs'] allocate_params: Nested argument with the constraints used to machine allocation. Defined below.
        :param pulumi.Input['InstanceDeployParamsArgs'] deploy_params: Nested argument with the config used to deploy the allocated machine. Defined below.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]] network_interfaces: Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
               is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        if allocate_params is not None:
            pulumi.set(__self__, "allocate_params", allocate_params)
        if deploy_params is not None:
            pulumi.set(__self__, "deploy_params", deploy_params)
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)

    @property
    @pulumi.getter(name="allocateParams")
    def allocate_params(self) -> Optional[pulumi.Input['InstanceAllocateParamsArgs']]:
        """
        Nested argument with the constraints used to machine allocation. Defined below.
        """
        return pulumi.get(self, "allocate_params")

    @allocate_params.setter
    def allocate_params(self, value: Optional[pulumi.Input['InstanceAllocateParamsArgs']]):
        pulumi.set(self, "allocate_params", value)

    @property
    @pulumi.getter(name="deployParams")
    def deploy_params(self) -> Optional[pulumi.Input['InstanceDeployParamsArgs']]:
        """
        Nested argument with the config used to deploy the allocated machine. Defined below.
        """
        return pulumi.get(self, "deploy_params")

    @deploy_params.setter
    def deploy_params(self, value: Optional[pulumi.Input['InstanceDeployParamsArgs']]):
        pulumi.set(self, "deploy_params", value)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]]]:
        """
        Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
        is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *,
                 allocate_params: Optional[pulumi.Input['InstanceAllocateParamsArgs']] = None,
                 cpu_count: Optional[pulumi.Input[int]] = None,
                 deploy_params: Optional[pulumi.Input['InstanceDeployParamsArgs']] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 memory: Optional[pulumi.Input[int]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Instance resources.
        :param pulumi.Input['InstanceAllocateParamsArgs'] allocate_params: Nested argument with the constraints used to machine allocation. Defined below.
        :param pulumi.Input[int] cpu_count: The number of CPU cores of the deployed MAAS machine.
        :param pulumi.Input['InstanceDeployParamsArgs'] deploy_params: Nested argument with the config used to deploy the allocated machine. Defined below.
        :param pulumi.Input[str] fqdn: The deployed MAAS machine FQDN.
        :param pulumi.Input[str] hostname: The deployed MAAS machine hostname.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_addresses: A set of IP addressed assigned to the deployed MAAS machine.
        :param pulumi.Input[int] memory: The RAM memory size (in GiB) of the deployed MAAS machine.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]] network_interfaces: Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
               is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] pool: The deployed MAAS machine pool name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of tag names associated to the deployed MAAS machine.
        :param pulumi.Input[str] zone: The deployed MAAS machine zone name.
        """
        if allocate_params is not None:
            pulumi.set(__self__, "allocate_params", allocate_params)
        if cpu_count is not None:
            pulumi.set(__self__, "cpu_count", cpu_count)
        if deploy_params is not None:
            pulumi.set(__self__, "deploy_params", deploy_params)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ip_addresses is not None:
            pulumi.set(__self__, "ip_addresses", ip_addresses)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if pool is not None:
            pulumi.set(__self__, "pool", pool)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="allocateParams")
    def allocate_params(self) -> Optional[pulumi.Input['InstanceAllocateParamsArgs']]:
        """
        Nested argument with the constraints used to machine allocation. Defined below.
        """
        return pulumi.get(self, "allocate_params")

    @allocate_params.setter
    def allocate_params(self, value: Optional[pulumi.Input['InstanceAllocateParamsArgs']]):
        pulumi.set(self, "allocate_params", value)

    @property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of CPU cores of the deployed MAAS machine.
        """
        return pulumi.get(self, "cpu_count")

    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpu_count", value)

    @property
    @pulumi.getter(name="deployParams")
    def deploy_params(self) -> Optional[pulumi.Input['InstanceDeployParamsArgs']]:
        """
        Nested argument with the config used to deploy the allocated machine. Defined below.
        """
        return pulumi.get(self, "deploy_params")

    @deploy_params.setter
    def deploy_params(self, value: Optional[pulumi.Input['InstanceDeployParamsArgs']]):
        pulumi.set(self, "deploy_params", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The deployed MAAS machine FQDN.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The deployed MAAS machine hostname.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of IP addressed assigned to the deployed MAAS machine.
        """
        return pulumi.get(self, "ip_addresses")

    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_addresses", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[int]]:
        """
        The RAM memory size (in GiB) of the deployed MAAS machine.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]]]:
        """
        Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
        is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        """
        The deployed MAAS machine pool name.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of tag names associated to the deployed MAAS machine.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The deployed MAAS machine zone name.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocate_params: Optional[pulumi.Input[pulumi.InputType['InstanceAllocateParamsArgs']]] = None,
                 deploy_params: Optional[pulumi.Input[pulumi.InputType['InstanceDeployParamsArgs']]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceNetworkInterfaceArgs']]]]] = None,
                 __props__=None):
        """
        Create a Instance resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InstanceAllocateParamsArgs']] allocate_params: Nested argument with the constraints used to machine allocation. Defined below.
        :param pulumi.Input[pulumi.InputType['InstanceDeployParamsArgs']] deploy_params: Nested argument with the config used to deploy the allocated machine. Defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceNetworkInterfaceArgs']]]] network_interfaces: Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
               is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Instance resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocate_params: Optional[pulumi.Input[pulumi.InputType['InstanceAllocateParamsArgs']]] = None,
                 deploy_params: Optional[pulumi.Input[pulumi.InputType['InstanceDeployParamsArgs']]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceNetworkInterfaceArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["allocate_params"] = allocate_params
            __props__.__dict__["deploy_params"] = deploy_params
            __props__.__dict__["network_interfaces"] = network_interfaces
            __props__.__dict__["cpu_count"] = None
            __props__.__dict__["fqdn"] = None
            __props__.__dict__["hostname"] = None
            __props__.__dict__["ip_addresses"] = None
            __props__.__dict__["memory"] = None
            __props__.__dict__["pool"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["zone"] = None
        super(Instance, __self__).__init__(
            'maas:index/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocate_params: Optional[pulumi.Input[pulumi.InputType['InstanceAllocateParamsArgs']]] = None,
            cpu_count: Optional[pulumi.Input[int]] = None,
            deploy_params: Optional[pulumi.Input[pulumi.InputType['InstanceDeployParamsArgs']]] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            memory: Optional[pulumi.Input[int]] = None,
            network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceNetworkInterfaceArgs']]]]] = None,
            pool: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InstanceAllocateParamsArgs']] allocate_params: Nested argument with the constraints used to machine allocation. Defined below.
        :param pulumi.Input[int] cpu_count: The number of CPU cores of the deployed MAAS machine.
        :param pulumi.Input[pulumi.InputType['InstanceDeployParamsArgs']] deploy_params: Nested argument with the config used to deploy the allocated machine. Defined below.
        :param pulumi.Input[str] fqdn: The deployed MAAS machine FQDN.
        :param pulumi.Input[str] hostname: The deployed MAAS machine hostname.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_addresses: A set of IP addressed assigned to the deployed MAAS machine.
        :param pulumi.Input[int] memory: The RAM memory size (in GiB) of the deployed MAAS machine.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceNetworkInterfaceArgs']]]] network_interfaces: Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
               is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        :param pulumi.Input[str] pool: The deployed MAAS machine pool name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of tag names associated to the deployed MAAS machine.
        :param pulumi.Input[str] zone: The deployed MAAS machine zone name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceState.__new__(_InstanceState)

        __props__.__dict__["allocate_params"] = allocate_params
        __props__.__dict__["cpu_count"] = cpu_count
        __props__.__dict__["deploy_params"] = deploy_params
        __props__.__dict__["fqdn"] = fqdn
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["ip_addresses"] = ip_addresses
        __props__.__dict__["memory"] = memory
        __props__.__dict__["network_interfaces"] = network_interfaces
        __props__.__dict__["pool"] = pool
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocateParams")
    def allocate_params(self) -> pulumi.Output[Optional['outputs.InstanceAllocateParams']]:
        """
        Nested argument with the constraints used to machine allocation. Defined below.
        """
        return pulumi.get(self, "allocate_params")

    @property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Output[int]:
        """
        The number of CPU cores of the deployed MAAS machine.
        """
        return pulumi.get(self, "cpu_count")

    @property
    @pulumi.getter(name="deployParams")
    def deploy_params(self) -> pulumi.Output[Optional['outputs.InstanceDeployParams']]:
        """
        Nested argument with the config used to deploy the allocated machine. Defined below.
        """
        return pulumi.get(self, "deploy_params")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The deployed MAAS machine FQDN.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The deployed MAAS machine hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        A set of IP addressed assigned to the deployed MAAS machine.
        """
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Output[int]:
        """
        The RAM memory size (in GiB) of the deployed MAAS machine.
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceNetworkInterface']]]:
        """
        Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
        is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Output[str]:
        """
        The deployed MAAS machine pool name.
        """
        return pulumi.get(self, "pool")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        A set of tag names associated to the deployed MAAS machine.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The deployed MAAS machine zone name.
        """
        return pulumi.get(self, "zone")

