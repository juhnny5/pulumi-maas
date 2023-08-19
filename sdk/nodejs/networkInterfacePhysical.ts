// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class NetworkInterfacePhysical extends pulumi.CustomResource {
    /**
     * Get an existing NetworkInterfacePhysical resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfacePhysicalState, opts?: pulumi.CustomResourceOptions): NetworkInterfacePhysical {
        return new NetworkInterfacePhysical(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'maas:index/networkInterfacePhysical:NetworkInterfacePhysical';

    /**
     * Returns true if the given object is an instance of NetworkInterfacePhysical.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkInterfacePhysical {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkInterfacePhysical.__pulumiType;
    }

    /**
     * The physical network interface MAC address.
     */
    public readonly macAddress!: pulumi.Output<string>;
    /**
     * The identifier (system ID, hostname, or FQDN) of the machine with the physical network interface.
     */
    public readonly machine!: pulumi.Output<string>;
    /**
     * The MTU of the physical network interface. This argument is computed if it's not set.
     */
    public readonly mtu!: pulumi.Output<number>;
    /**
     * The physical network interface name. This argument is computed if it's not set.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A set of tag names to be assigned to the physical network interface. This argument is computed if it's not set.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * VLAN the physical network interface is connected to. Defaults to `untagged`.
     */
    public readonly vlan!: pulumi.Output<string | undefined>;

    /**
     * Create a NetworkInterfacePhysical resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkInterfacePhysicalArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkInterfacePhysicalArgs | NetworkInterfacePhysicalState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkInterfacePhysicalState | undefined;
            resourceInputs["macAddress"] = state ? state.macAddress : undefined;
            resourceInputs["machine"] = state ? state.machine : undefined;
            resourceInputs["mtu"] = state ? state.mtu : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["vlan"] = state ? state.vlan : undefined;
        } else {
            const args = argsOrState as NetworkInterfacePhysicalArgs | undefined;
            if ((!args || args.macAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'macAddress'");
            }
            if ((!args || args.machine === undefined) && !opts.urn) {
                throw new Error("Missing required property 'machine'");
            }
            resourceInputs["macAddress"] = args ? args.macAddress : undefined;
            resourceInputs["machine"] = args ? args.machine : undefined;
            resourceInputs["mtu"] = args ? args.mtu : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vlan"] = args ? args.vlan : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NetworkInterfacePhysical.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NetworkInterfacePhysical resources.
 */
export interface NetworkInterfacePhysicalState {
    /**
     * The physical network interface MAC address.
     */
    macAddress?: pulumi.Input<string>;
    /**
     * The identifier (system ID, hostname, or FQDN) of the machine with the physical network interface.
     */
    machine?: pulumi.Input<string>;
    /**
     * The MTU of the physical network interface. This argument is computed if it's not set.
     */
    mtu?: pulumi.Input<number>;
    /**
     * The physical network interface name. This argument is computed if it's not set.
     */
    name?: pulumi.Input<string>;
    /**
     * A set of tag names to be assigned to the physical network interface. This argument is computed if it's not set.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * VLAN the physical network interface is connected to. Defaults to `untagged`.
     */
    vlan?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NetworkInterfacePhysical resource.
 */
export interface NetworkInterfacePhysicalArgs {
    /**
     * The physical network interface MAC address.
     */
    macAddress: pulumi.Input<string>;
    /**
     * The identifier (system ID, hostname, or FQDN) of the machine with the physical network interface.
     */
    machine: pulumi.Input<string>;
    /**
     * The MTU of the physical network interface. This argument is computed if it's not set.
     */
    mtu?: pulumi.Input<number>;
    /**
     * The physical network interface name. This argument is computed if it's not set.
     */
    name?: pulumi.Input<string>;
    /**
     * A set of tag names to be assigned to the physical network interface. This argument is computed if it's not set.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * VLAN the physical network interface is connected to. Defaults to `untagged`.
     */
    vlan?: pulumi.Input<string>;
}
