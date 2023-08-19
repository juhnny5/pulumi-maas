// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface BlockDevicePartition {
    bootable?: boolean;
    fsType?: string;
    label?: string;
    mountOptions?: string;
    mountPoint?: string;
    path: string;
    sizeGigabytes: number;
    tags?: string[];
}

export interface InstanceAllocateParams {
    hostname?: string;
    minCpuCount?: number;
    minMemory?: number;
    pool?: string;
    tags?: string[];
    zone?: string;
}

export interface InstanceDeployParams {
    distroSeries?: string;
    enableHwSync?: boolean;
    hweKernel?: string;
    userData?: string;
}

export interface InstanceNetworkInterface {
    ipAddress?: string;
    name: string;
    subnetCidr?: string;
}

export interface SubnetIpRange {
    comment?: string;
    endIp: string;
    startIp: string;
    type: string;
}

export interface VmHostMachineNetworkInterface {
    fabric?: string;
    ipAddress?: string;
    name: string;
    subnetCidr?: string;
    vlan?: string;
}

export interface VmHostMachineStorageDisk {
    pool?: string;
    sizeGigabytes: number;
}

