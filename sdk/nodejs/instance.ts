// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'maas:index/instance:Instance';

    /**
     * Returns true if the given object is an instance of Instance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Instance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Instance.__pulumiType;
    }

    /**
     * Nested argument with the constraints used to machine allocation. Defined below.
     */
    public readonly allocateParams!: pulumi.Output<outputs.InstanceAllocateParams | undefined>;
    /**
     * The number of CPU cores of the deployed MAAS machine.
     */
    public /*out*/ readonly cpuCount!: pulumi.Output<number>;
    /**
     * Nested argument with the config used to deploy the allocated machine. Defined below.
     */
    public readonly deployParams!: pulumi.Output<outputs.InstanceDeployParams | undefined>;
    /**
     * The deployed MAAS machine FQDN.
     */
    public /*out*/ readonly fqdn!: pulumi.Output<string>;
    /**
     * The deployed MAAS machine hostname.
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * A set of IP addressed assigned to the deployed MAAS machine.
     */
    public /*out*/ readonly ipAddresses!: pulumi.Output<string[]>;
    /**
     * The RAM memory size (in GiB) of the deployed MAAS machine.
     */
    public /*out*/ readonly memory!: pulumi.Output<number>;
    /**
     * Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
     * is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    public readonly networkInterfaces!: pulumi.Output<outputs.InstanceNetworkInterface[] | undefined>;
    /**
     * The deployed MAAS machine pool name.
     */
    public /*out*/ readonly pool!: pulumi.Output<string>;
    /**
     * A set of tag names associated to the deployed MAAS machine.
     */
    public /*out*/ readonly tags!: pulumi.Output<string[]>;
    /**
     * The deployed MAAS machine zone name.
     */
    public /*out*/ readonly zone!: pulumi.Output<string>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstanceState | undefined;
            resourceInputs["allocateParams"] = state ? state.allocateParams : undefined;
            resourceInputs["cpuCount"] = state ? state.cpuCount : undefined;
            resourceInputs["deployParams"] = state ? state.deployParams : undefined;
            resourceInputs["fqdn"] = state ? state.fqdn : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["ipAddresses"] = state ? state.ipAddresses : undefined;
            resourceInputs["memory"] = state ? state.memory : undefined;
            resourceInputs["networkInterfaces"] = state ? state.networkInterfaces : undefined;
            resourceInputs["pool"] = state ? state.pool : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            resourceInputs["allocateParams"] = args ? args.allocateParams : undefined;
            resourceInputs["deployParams"] = args ? args.deployParams : undefined;
            resourceInputs["networkInterfaces"] = args ? args.networkInterfaces : undefined;
            resourceInputs["cpuCount"] = undefined /*out*/;
            resourceInputs["fqdn"] = undefined /*out*/;
            resourceInputs["hostname"] = undefined /*out*/;
            resourceInputs["ipAddresses"] = undefined /*out*/;
            resourceInputs["memory"] = undefined /*out*/;
            resourceInputs["pool"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["zone"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Instance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * Nested argument with the constraints used to machine allocation. Defined below.
     */
    allocateParams?: pulumi.Input<inputs.InstanceAllocateParams>;
    /**
     * The number of CPU cores of the deployed MAAS machine.
     */
    cpuCount?: pulumi.Input<number>;
    /**
     * Nested argument with the config used to deploy the allocated machine. Defined below.
     */
    deployParams?: pulumi.Input<inputs.InstanceDeployParams>;
    /**
     * The deployed MAAS machine FQDN.
     */
    fqdn?: pulumi.Input<string>;
    /**
     * The deployed MAAS machine hostname.
     */
    hostname?: pulumi.Input<string>;
    /**
     * A set of IP addressed assigned to the deployed MAAS machine.
     */
    ipAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The RAM memory size (in GiB) of the deployed MAAS machine.
     */
    memory?: pulumi.Input<number>;
    /**
     * Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
     * is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    networkInterfaces?: pulumi.Input<pulumi.Input<inputs.InstanceNetworkInterface>[]>;
    /**
     * The deployed MAAS machine pool name.
     */
    pool?: pulumi.Input<string>;
    /**
     * A set of tag names associated to the deployed MAAS machine.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The deployed MAAS machine zone name.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * Nested argument with the constraints used to machine allocation. Defined below.
     */
    allocateParams?: pulumi.Input<inputs.InstanceAllocateParams>;
    /**
     * Nested argument with the config used to deploy the allocated machine. Defined below.
     */
    deployParams?: pulumi.Input<inputs.InstanceDeployParams>;
    /**
     * Specifies a network interface configuration done before the machine is deployed. Parameters defined below. This argument
     * is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    networkInterfaces?: pulumi.Input<pulumi.Input<inputs.InstanceNetworkInterface>[]>;
}
