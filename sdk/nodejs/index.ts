// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { BlockDeviceArgs, BlockDeviceState } from "./blockDevice";
export type BlockDevice = import("./blockDevice").BlockDevice;
export const BlockDevice: typeof import("./blockDevice").BlockDevice = null as any;
utilities.lazyLoad(exports, ["BlockDevice"], () => require("./blockDevice"));

export { DnsDomainArgs, DnsDomainState } from "./dnsDomain";
export type DnsDomain = import("./dnsDomain").DnsDomain;
export const DnsDomain: typeof import("./dnsDomain").DnsDomain = null as any;
utilities.lazyLoad(exports, ["DnsDomain"], () => require("./dnsDomain"));

export { DnsRecordArgs, DnsRecordState } from "./dnsRecord";
export type DnsRecord = import("./dnsRecord").DnsRecord;
export const DnsRecord: typeof import("./dnsRecord").DnsRecord = null as any;
utilities.lazyLoad(exports, ["DnsRecord"], () => require("./dnsRecord"));

export { FabricArgs, FabricState } from "./fabric";
export type Fabric = import("./fabric").Fabric;
export const Fabric: typeof import("./fabric").Fabric = null as any;
utilities.lazyLoad(exports, ["Fabric"], () => require("./fabric"));

export { GetFabricArgs, GetFabricResult, GetFabricOutputArgs } from "./getFabric";
export const getFabric: typeof import("./getFabric").getFabric = null as any;
export const getFabricOutput: typeof import("./getFabric").getFabricOutput = null as any;
utilities.lazyLoad(exports, ["getFabric","getFabricOutput"], () => require("./getFabric"));

export { GetSubnetArgs, GetSubnetResult, GetSubnetOutputArgs } from "./getSubnet";
export const getSubnet: typeof import("./getSubnet").getSubnet = null as any;
export const getSubnetOutput: typeof import("./getSubnet").getSubnetOutput = null as any;
utilities.lazyLoad(exports, ["getSubnet","getSubnetOutput"], () => require("./getSubnet"));

export { GetVlanArgs, GetVlanResult, GetVlanOutputArgs } from "./getVlan";
export const getVlan: typeof import("./getVlan").getVlan = null as any;
export const getVlanOutput: typeof import("./getVlan").getVlanOutput = null as any;
utilities.lazyLoad(exports, ["getVlan","getVlanOutput"], () => require("./getVlan"));

export { InstanceArgs, InstanceState } from "./instance";
export type Instance = import("./instance").Instance;
export const Instance: typeof import("./instance").Instance = null as any;
utilities.lazyLoad(exports, ["Instance"], () => require("./instance"));

export { MachineArgs, MachineState } from "./machine";
export type Machine = import("./machine").Machine;
export const Machine: typeof import("./machine").Machine = null as any;
utilities.lazyLoad(exports, ["Machine"], () => require("./machine"));

export { NetworkInterfaceLinkArgs, NetworkInterfaceLinkState } from "./networkInterfaceLink";
export type NetworkInterfaceLink = import("./networkInterfaceLink").NetworkInterfaceLink;
export const NetworkInterfaceLink: typeof import("./networkInterfaceLink").NetworkInterfaceLink = null as any;
utilities.lazyLoad(exports, ["NetworkInterfaceLink"], () => require("./networkInterfaceLink"));

export { NetworkInterfacePhysicalArgs, NetworkInterfacePhysicalState } from "./networkInterfacePhysical";
export type NetworkInterfacePhysical = import("./networkInterfacePhysical").NetworkInterfacePhysical;
export const NetworkInterfacePhysical: typeof import("./networkInterfacePhysical").NetworkInterfacePhysical = null as any;
utilities.lazyLoad(exports, ["NetworkInterfacePhysical"], () => require("./networkInterfacePhysical"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SpaceArgs, SpaceState } from "./space";
export type Space = import("./space").Space;
export const Space: typeof import("./space").Space = null as any;
utilities.lazyLoad(exports, ["Space"], () => require("./space"));

export { SubnetArgs, SubnetState } from "./subnet";
export type Subnet = import("./subnet").Subnet;
export const Subnet: typeof import("./subnet").Subnet = null as any;
utilities.lazyLoad(exports, ["Subnet"], () => require("./subnet"));

export { SubnetIpRangeArgs, SubnetIpRangeState } from "./subnetIpRange";
export type SubnetIpRange = import("./subnetIpRange").SubnetIpRange;
export const SubnetIpRange: typeof import("./subnetIpRange").SubnetIpRange = null as any;
utilities.lazyLoad(exports, ["SubnetIpRange"], () => require("./subnetIpRange"));

export { TagArgs, TagState } from "./tag";
export type Tag = import("./tag").Tag;
export const Tag: typeof import("./tag").Tag = null as any;
utilities.lazyLoad(exports, ["Tag"], () => require("./tag"));

export { UserArgs, UserState } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));

export { VlanArgs, VlanState } from "./vlan";
export type Vlan = import("./vlan").Vlan;
export const Vlan: typeof import("./vlan").Vlan = null as any;
utilities.lazyLoad(exports, ["Vlan"], () => require("./vlan"));

export { VmHostArgs, VmHostState } from "./vmHost";
export type VmHost = import("./vmHost").VmHost;
export const VmHost: typeof import("./vmHost").VmHost = null as any;
utilities.lazyLoad(exports, ["VmHost"], () => require("./vmHost"));

export { VmHostMachineArgs, VmHostMachineState } from "./vmHostMachine";
export type VmHostMachine = import("./vmHostMachine").VmHostMachine;
export const VmHostMachine: typeof import("./vmHostMachine").VmHostMachine = null as any;
utilities.lazyLoad(exports, ["VmHostMachine"], () => require("./vmHostMachine"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "maas:index/blockDevice:BlockDevice":
                return new BlockDevice(name, <any>undefined, { urn })
            case "maas:index/dnsDomain:DnsDomain":
                return new DnsDomain(name, <any>undefined, { urn })
            case "maas:index/dnsRecord:DnsRecord":
                return new DnsRecord(name, <any>undefined, { urn })
            case "maas:index/fabric:Fabric":
                return new Fabric(name, <any>undefined, { urn })
            case "maas:index/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "maas:index/machine:Machine":
                return new Machine(name, <any>undefined, { urn })
            case "maas:index/networkInterfaceLink:NetworkInterfaceLink":
                return new NetworkInterfaceLink(name, <any>undefined, { urn })
            case "maas:index/networkInterfacePhysical:NetworkInterfacePhysical":
                return new NetworkInterfacePhysical(name, <any>undefined, { urn })
            case "maas:index/space:Space":
                return new Space(name, <any>undefined, { urn })
            case "maas:index/subnet:Subnet":
                return new Subnet(name, <any>undefined, { urn })
            case "maas:index/subnetIpRange:SubnetIpRange":
                return new SubnetIpRange(name, <any>undefined, { urn })
            case "maas:index/tag:Tag":
                return new Tag(name, <any>undefined, { urn })
            case "maas:index/user:User":
                return new User(name, <any>undefined, { urn })
            case "maas:index/vlan:Vlan":
                return new Vlan(name, <any>undefined, { urn })
            case "maas:index/vmHost:VmHost":
                return new VmHost(name, <any>undefined, { urn })
            case "maas:index/vmHostMachine:VmHostMachine":
                return new VmHostMachine(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("maas", "index/blockDevice", _module)
pulumi.runtime.registerResourceModule("maas", "index/dnsDomain", _module)
pulumi.runtime.registerResourceModule("maas", "index/dnsRecord", _module)
pulumi.runtime.registerResourceModule("maas", "index/fabric", _module)
pulumi.runtime.registerResourceModule("maas", "index/instance", _module)
pulumi.runtime.registerResourceModule("maas", "index/machine", _module)
pulumi.runtime.registerResourceModule("maas", "index/networkInterfaceLink", _module)
pulumi.runtime.registerResourceModule("maas", "index/networkInterfacePhysical", _module)
pulumi.runtime.registerResourceModule("maas", "index/space", _module)
pulumi.runtime.registerResourceModule("maas", "index/subnet", _module)
pulumi.runtime.registerResourceModule("maas", "index/subnetIpRange", _module)
pulumi.runtime.registerResourceModule("maas", "index/tag", _module)
pulumi.runtime.registerResourceModule("maas", "index/user", _module)
pulumi.runtime.registerResourceModule("maas", "index/vlan", _module)
pulumi.runtime.registerResourceModule("maas", "index/vmHost", _module)
pulumi.runtime.registerResourceModule("maas", "index/vmHostMachine", _module)
pulumi.runtime.registerResourcePackage("maas", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:maas") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});