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

__all__ = ['BlockDeviceArgs', 'BlockDevice']

@pulumi.input_type
class BlockDeviceArgs:
    def __init__(__self__, *,
                 machine: pulumi.Input[str],
                 size_gigabytes: pulumi.Input[int],
                 block_size: Optional[pulumi.Input[int]] = None,
                 id_path: Optional[pulumi.Input[str]] = None,
                 is_boot_device: Optional[pulumi.Input[bool]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partitions: Optional[pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a BlockDevice resource.
        :param pulumi.Input[str] machine: The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        :param pulumi.Input[int] size_gigabytes: The size of the block device (given in GB).
        :param pulumi.Input[int] block_size: The block size of the block device. Defaults to `512`.
        :param pulumi.Input[str] id_path: Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
               on the boot order or kernel version. This argument is computed if it's not given.
        :param pulumi.Input[bool] is_boot_device: Boolean value indicating if the block device is set as the boot device.
        :param pulumi.Input[str] model: Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[str] name: The block device name.
        :param pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]] partitions: List of partition resources created for the new block device. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
               not given.
        :param pulumi.Input[str] serial: Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        """
        pulumi.set(__self__, "machine", machine)
        pulumi.set(__self__, "size_gigabytes", size_gigabytes)
        if block_size is not None:
            pulumi.set(__self__, "block_size", block_size)
        if id_path is not None:
            pulumi.set(__self__, "id_path", id_path)
        if is_boot_device is not None:
            pulumi.set(__self__, "is_boot_device", is_boot_device)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if partitions is not None:
            pulumi.set(__self__, "partitions", partitions)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def machine(self) -> pulumi.Input[str]:
        """
        The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        """
        return pulumi.get(self, "machine")

    @machine.setter
    def machine(self, value: pulumi.Input[str]):
        pulumi.set(self, "machine", value)

    @property
    @pulumi.getter(name="sizeGigabytes")
    def size_gigabytes(self) -> pulumi.Input[int]:
        """
        The size of the block device (given in GB).
        """
        return pulumi.get(self, "size_gigabytes")

    @size_gigabytes.setter
    def size_gigabytes(self, value: pulumi.Input[int]):
        pulumi.set(self, "size_gigabytes", value)

    @property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> Optional[pulumi.Input[int]]:
        """
        The block size of the block device. Defaults to `512`.
        """
        return pulumi.get(self, "block_size")

    @block_size.setter
    def block_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "block_size", value)

    @property
    @pulumi.getter(name="idPath")
    def id_path(self) -> Optional[pulumi.Input[str]]:
        """
        Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
        on the boot order or kernel version. This argument is computed if it's not given.
        """
        return pulumi.get(self, "id_path")

    @id_path.setter
    def id_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id_path", value)

    @property
    @pulumi.getter(name="isBootDevice")
    def is_boot_device(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean value indicating if the block device is set as the boot device.
        """
        return pulumi.get(self, "is_boot_device")

    @is_boot_device.setter
    def is_boot_device(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_boot_device", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
        computed if it's not given.
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The block device name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def partitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]]]:
        """
        List of partition resources created for the new block device. Parameters defined below. This argument is processed in
        [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
        not given.
        """
        return pulumi.get(self, "partitions")

    @partitions.setter
    def partitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]]]):
        pulumi.set(self, "partitions", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        """
        Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
        computed if it's not given.
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _BlockDeviceState:
    def __init__(__self__, *,
                 block_size: Optional[pulumi.Input[int]] = None,
                 id_path: Optional[pulumi.Input[str]] = None,
                 is_boot_device: Optional[pulumi.Input[bool]] = None,
                 machine: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partitions: Optional[pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 size_gigabytes: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BlockDevice resources.
        :param pulumi.Input[int] block_size: The block size of the block device. Defaults to `512`.
        :param pulumi.Input[str] id_path: Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
               on the boot order or kernel version. This argument is computed if it's not given.
        :param pulumi.Input[bool] is_boot_device: Boolean value indicating if the block device is set as the boot device.
        :param pulumi.Input[str] machine: The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        :param pulumi.Input[str] model: Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[str] name: The block device name.
        :param pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]] partitions: List of partition resources created for the new block device. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
               not given.
        :param pulumi.Input[str] path: Block device path.
        :param pulumi.Input[str] serial: Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[int] size_gigabytes: The size of the block device (given in GB).
        :param pulumi.Input[str] uuid: Block device UUID.
        """
        if block_size is not None:
            pulumi.set(__self__, "block_size", block_size)
        if id_path is not None:
            pulumi.set(__self__, "id_path", id_path)
        if is_boot_device is not None:
            pulumi.set(__self__, "is_boot_device", is_boot_device)
        if machine is not None:
            pulumi.set(__self__, "machine", machine)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if partitions is not None:
            pulumi.set(__self__, "partitions", partitions)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if size_gigabytes is not None:
            pulumi.set(__self__, "size_gigabytes", size_gigabytes)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> Optional[pulumi.Input[int]]:
        """
        The block size of the block device. Defaults to `512`.
        """
        return pulumi.get(self, "block_size")

    @block_size.setter
    def block_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "block_size", value)

    @property
    @pulumi.getter(name="idPath")
    def id_path(self) -> Optional[pulumi.Input[str]]:
        """
        Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
        on the boot order or kernel version. This argument is computed if it's not given.
        """
        return pulumi.get(self, "id_path")

    @id_path.setter
    def id_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id_path", value)

    @property
    @pulumi.getter(name="isBootDevice")
    def is_boot_device(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean value indicating if the block device is set as the boot device.
        """
        return pulumi.get(self, "is_boot_device")

    @is_boot_device.setter
    def is_boot_device(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_boot_device", value)

    @property
    @pulumi.getter
    def machine(self) -> Optional[pulumi.Input[str]]:
        """
        The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        """
        return pulumi.get(self, "machine")

    @machine.setter
    def machine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "machine", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
        computed if it's not given.
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The block device name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def partitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]]]:
        """
        List of partition resources created for the new block device. Parameters defined below. This argument is processed in
        [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
        not given.
        """
        return pulumi.get(self, "partitions")

    @partitions.setter
    def partitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BlockDevicePartitionArgs']]]]):
        pulumi.set(self, "partitions", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Block device path.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        """
        Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
        computed if it's not given.
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter(name="sizeGigabytes")
    def size_gigabytes(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the block device (given in GB).
        """
        return pulumi.get(self, "size_gigabytes")

    @size_gigabytes.setter
    def size_gigabytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size_gigabytes", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        Block device UUID.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


class BlockDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_size: Optional[pulumi.Input[int]] = None,
                 id_path: Optional[pulumi.Input[str]] = None,
                 is_boot_device: Optional[pulumi.Input[bool]] = None,
                 machine: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BlockDevicePartitionArgs']]]]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 size_gigabytes: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a BlockDevice resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] block_size: The block size of the block device. Defaults to `512`.
        :param pulumi.Input[str] id_path: Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
               on the boot order or kernel version. This argument is computed if it's not given.
        :param pulumi.Input[bool] is_boot_device: Boolean value indicating if the block device is set as the boot device.
        :param pulumi.Input[str] machine: The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        :param pulumi.Input[str] model: Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[str] name: The block device name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BlockDevicePartitionArgs']]]] partitions: List of partition resources created for the new block device. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
               not given.
        :param pulumi.Input[str] serial: Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[int] size_gigabytes: The size of the block device (given in GB).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BlockDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BlockDevice resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BlockDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BlockDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_size: Optional[pulumi.Input[int]] = None,
                 id_path: Optional[pulumi.Input[str]] = None,
                 is_boot_device: Optional[pulumi.Input[bool]] = None,
                 machine: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BlockDevicePartitionArgs']]]]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 size_gigabytes: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BlockDeviceArgs.__new__(BlockDeviceArgs)

            __props__.__dict__["block_size"] = block_size
            __props__.__dict__["id_path"] = id_path
            __props__.__dict__["is_boot_device"] = is_boot_device
            if machine is None and not opts.urn:
                raise TypeError("Missing required property 'machine'")
            __props__.__dict__["machine"] = machine
            __props__.__dict__["model"] = model
            __props__.__dict__["name"] = name
            __props__.__dict__["partitions"] = partitions
            __props__.__dict__["serial"] = serial
            if size_gigabytes is None and not opts.urn:
                raise TypeError("Missing required property 'size_gigabytes'")
            __props__.__dict__["size_gigabytes"] = size_gigabytes
            __props__.__dict__["tags"] = tags
            __props__.__dict__["path"] = None
            __props__.__dict__["uuid"] = None
        super(BlockDevice, __self__).__init__(
            'maas:index/blockDevice:BlockDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            block_size: Optional[pulumi.Input[int]] = None,
            id_path: Optional[pulumi.Input[str]] = None,
            is_boot_device: Optional[pulumi.Input[bool]] = None,
            machine: Optional[pulumi.Input[str]] = None,
            model: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            partitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BlockDevicePartitionArgs']]]]] = None,
            path: Optional[pulumi.Input[str]] = None,
            serial: Optional[pulumi.Input[str]] = None,
            size_gigabytes: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            uuid: Optional[pulumi.Input[str]] = None) -> 'BlockDevice':
        """
        Get an existing BlockDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] block_size: The block size of the block device. Defaults to `512`.
        :param pulumi.Input[str] id_path: Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
               on the boot order or kernel version. This argument is computed if it's not given.
        :param pulumi.Input[bool] is_boot_device: Boolean value indicating if the block device is set as the boot device.
        :param pulumi.Input[str] machine: The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        :param pulumi.Input[str] model: Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[str] name: The block device name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BlockDevicePartitionArgs']]]] partitions: List of partition resources created for the new block device. Parameters defined below. This argument is processed in
               [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
               not given.
        :param pulumi.Input[str] path: Block device path.
        :param pulumi.Input[str] serial: Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
               computed if it's not given.
        :param pulumi.Input[int] size_gigabytes: The size of the block device (given in GB).
        :param pulumi.Input[str] uuid: Block device UUID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BlockDeviceState.__new__(_BlockDeviceState)

        __props__.__dict__["block_size"] = block_size
        __props__.__dict__["id_path"] = id_path
        __props__.__dict__["is_boot_device"] = is_boot_device
        __props__.__dict__["machine"] = machine
        __props__.__dict__["model"] = model
        __props__.__dict__["name"] = name
        __props__.__dict__["partitions"] = partitions
        __props__.__dict__["path"] = path
        __props__.__dict__["serial"] = serial
        __props__.__dict__["size_gigabytes"] = size_gigabytes
        __props__.__dict__["tags"] = tags
        __props__.__dict__["uuid"] = uuid
        return BlockDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> pulumi.Output[Optional[int]]:
        """
        The block size of the block device. Defaults to `512`.
        """
        return pulumi.get(self, "block_size")

    @property
    @pulumi.getter(name="idPath")
    def id_path(self) -> pulumi.Output[str]:
        """
        Only used if `model` and `serial` cannot be provided. This should be a path that is fixed and doesn't change depending
        on the boot order or kernel version. This argument is computed if it's not given.
        """
        return pulumi.get(self, "id_path")

    @property
    @pulumi.getter(name="isBootDevice")
    def is_boot_device(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value indicating if the block device is set as the boot device.
        """
        return pulumi.get(self, "is_boot_device")

    @property
    @pulumi.getter
    def machine(self) -> pulumi.Output[str]:
        """
        The machine identifier (system ID, hostname, or FQDN) that owns the block device.
        """
        return pulumi.get(self, "machine")

    @property
    @pulumi.getter
    def model(self) -> pulumi.Output[str]:
        """
        Model of the block device. Used in conjunction with `serial` argument. Conflicts with `id_path`. This argument is
        computed if it's not given.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The block device name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def partitions(self) -> pulumi.Output[Sequence['outputs.BlockDevicePartition']]:
        """
        List of partition resources created for the new block device. Parameters defined below. This argument is processed in
        [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html). And, it is computed if it's
        not given.
        """
        return pulumi.get(self, "partitions")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Block device path.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        Serial number of the block device. Used in conjunction with `model` argument. Conflicts with `id_path`. This argument is
        computed if it's not given.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter(name="sizeGigabytes")
    def size_gigabytes(self) -> pulumi.Output[int]:
        """
        The size of the block device (given in GB).
        """
        return pulumi.get(self, "size_gigabytes")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        Block device UUID.
        """
        return pulumi.get(self, "uuid")

