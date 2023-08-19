// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package maas

import (
	"context"
	"reflect"

	"errors"
	"github.com/juhnny5/pulumi-maas/sdk/go/maas/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Machine struct {
	pulumi.CustomResourceState

	// The architecture type of the machine. Defaults to `amd64/generic`.
	Architecture pulumi.StringPtrOutput `pulumi:"architecture"`
	// The domain of the machine. This is computed if it's not set.
	Domain pulumi.StringOutput `pulumi:"domain"`
	// The machine hostname. This is computed if it's not set.
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
	// set.
	MinHweKernel pulumi.StringOutput `pulumi:"minHweKernel"`
	// The resource pool of the machine. This is computed if it's not set.
	Pool pulumi.StringOutput `pulumi:"pool"`
	// A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
	// for a list of the available power parameters for each power type.
	PowerParameters pulumi.StringMapOutput `pulumi:"powerParameters"`
	// A power management type (e.g. `ipmi`).
	PowerType pulumi.StringOutput `pulumi:"powerType"`
	// The MAC address of the machine's PXE boot NIC.
	PxeMacAddress pulumi.StringOutput `pulumi:"pxeMacAddress"`
	// The zone of the machine. This is computed if it's not set.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewMachine registers a new resource with the given unique name, arguments, and options.
func NewMachine(ctx *pulumi.Context,
	name string, args *MachineArgs, opts ...pulumi.ResourceOption) (*Machine, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PowerParameters == nil {
		return nil, errors.New("invalid value for required argument 'PowerParameters'")
	}
	if args.PowerType == nil {
		return nil, errors.New("invalid value for required argument 'PowerType'")
	}
	if args.PxeMacAddress == nil {
		return nil, errors.New("invalid value for required argument 'PxeMacAddress'")
	}
	if args.PowerParameters != nil {
		args.PowerParameters = pulumi.ToSecret(args.PowerParameters).(pulumi.StringMapInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"powerParameters",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Machine
	err := ctx.RegisterResource("maas:index/machine:Machine", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMachine gets an existing Machine resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMachine(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MachineState, opts ...pulumi.ResourceOption) (*Machine, error) {
	var resource Machine
	err := ctx.ReadResource("maas:index/machine:Machine", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Machine resources.
type machineState struct {
	// The architecture type of the machine. Defaults to `amd64/generic`.
	Architecture *string `pulumi:"architecture"`
	// The domain of the machine. This is computed if it's not set.
	Domain *string `pulumi:"domain"`
	// The machine hostname. This is computed if it's not set.
	Hostname *string `pulumi:"hostname"`
	// The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
	// set.
	MinHweKernel *string `pulumi:"minHweKernel"`
	// The resource pool of the machine. This is computed if it's not set.
	Pool *string `pulumi:"pool"`
	// A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
	// for a list of the available power parameters for each power type.
	PowerParameters map[string]string `pulumi:"powerParameters"`
	// A power management type (e.g. `ipmi`).
	PowerType *string `pulumi:"powerType"`
	// The MAC address of the machine's PXE boot NIC.
	PxeMacAddress *string `pulumi:"pxeMacAddress"`
	// The zone of the machine. This is computed if it's not set.
	Zone *string `pulumi:"zone"`
}

type MachineState struct {
	// The architecture type of the machine. Defaults to `amd64/generic`.
	Architecture pulumi.StringPtrInput
	// The domain of the machine. This is computed if it's not set.
	Domain pulumi.StringPtrInput
	// The machine hostname. This is computed if it's not set.
	Hostname pulumi.StringPtrInput
	// The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
	// set.
	MinHweKernel pulumi.StringPtrInput
	// The resource pool of the machine. This is computed if it's not set.
	Pool pulumi.StringPtrInput
	// A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
	// for a list of the available power parameters for each power type.
	PowerParameters pulumi.StringMapInput
	// A power management type (e.g. `ipmi`).
	PowerType pulumi.StringPtrInput
	// The MAC address of the machine's PXE boot NIC.
	PxeMacAddress pulumi.StringPtrInput
	// The zone of the machine. This is computed if it's not set.
	Zone pulumi.StringPtrInput
}

func (MachineState) ElementType() reflect.Type {
	return reflect.TypeOf((*machineState)(nil)).Elem()
}

type machineArgs struct {
	// The architecture type of the machine. Defaults to `amd64/generic`.
	Architecture *string `pulumi:"architecture"`
	// The domain of the machine. This is computed if it's not set.
	Domain *string `pulumi:"domain"`
	// The machine hostname. This is computed if it's not set.
	Hostname *string `pulumi:"hostname"`
	// The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
	// set.
	MinHweKernel *string `pulumi:"minHweKernel"`
	// The resource pool of the machine. This is computed if it's not set.
	Pool *string `pulumi:"pool"`
	// A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
	// for a list of the available power parameters for each power type.
	PowerParameters map[string]string `pulumi:"powerParameters"`
	// A power management type (e.g. `ipmi`).
	PowerType string `pulumi:"powerType"`
	// The MAC address of the machine's PXE boot NIC.
	PxeMacAddress string `pulumi:"pxeMacAddress"`
	// The zone of the machine. This is computed if it's not set.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a Machine resource.
type MachineArgs struct {
	// The architecture type of the machine. Defaults to `amd64/generic`.
	Architecture pulumi.StringPtrInput
	// The domain of the machine. This is computed if it's not set.
	Domain pulumi.StringPtrInput
	// The machine hostname. This is computed if it's not set.
	Hostname pulumi.StringPtrInput
	// The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
	// set.
	MinHweKernel pulumi.StringPtrInput
	// The resource pool of the machine. This is computed if it's not set.
	Pool pulumi.StringPtrInput
	// A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
	// for a list of the available power parameters for each power type.
	PowerParameters pulumi.StringMapInput
	// A power management type (e.g. `ipmi`).
	PowerType pulumi.StringInput
	// The MAC address of the machine's PXE boot NIC.
	PxeMacAddress pulumi.StringInput
	// The zone of the machine. This is computed if it's not set.
	Zone pulumi.StringPtrInput
}

func (MachineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*machineArgs)(nil)).Elem()
}

type MachineInput interface {
	pulumi.Input

	ToMachineOutput() MachineOutput
	ToMachineOutputWithContext(ctx context.Context) MachineOutput
}

func (*Machine) ElementType() reflect.Type {
	return reflect.TypeOf((**Machine)(nil)).Elem()
}

func (i *Machine) ToMachineOutput() MachineOutput {
	return i.ToMachineOutputWithContext(context.Background())
}

func (i *Machine) ToMachineOutputWithContext(ctx context.Context) MachineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MachineOutput)
}

// MachineArrayInput is an input type that accepts MachineArray and MachineArrayOutput values.
// You can construct a concrete instance of `MachineArrayInput` via:
//
//	MachineArray{ MachineArgs{...} }
type MachineArrayInput interface {
	pulumi.Input

	ToMachineArrayOutput() MachineArrayOutput
	ToMachineArrayOutputWithContext(context.Context) MachineArrayOutput
}

type MachineArray []MachineInput

func (MachineArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Machine)(nil)).Elem()
}

func (i MachineArray) ToMachineArrayOutput() MachineArrayOutput {
	return i.ToMachineArrayOutputWithContext(context.Background())
}

func (i MachineArray) ToMachineArrayOutputWithContext(ctx context.Context) MachineArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MachineArrayOutput)
}

// MachineMapInput is an input type that accepts MachineMap and MachineMapOutput values.
// You can construct a concrete instance of `MachineMapInput` via:
//
//	MachineMap{ "key": MachineArgs{...} }
type MachineMapInput interface {
	pulumi.Input

	ToMachineMapOutput() MachineMapOutput
	ToMachineMapOutputWithContext(context.Context) MachineMapOutput
}

type MachineMap map[string]MachineInput

func (MachineMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Machine)(nil)).Elem()
}

func (i MachineMap) ToMachineMapOutput() MachineMapOutput {
	return i.ToMachineMapOutputWithContext(context.Background())
}

func (i MachineMap) ToMachineMapOutputWithContext(ctx context.Context) MachineMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MachineMapOutput)
}

type MachineOutput struct{ *pulumi.OutputState }

func (MachineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Machine)(nil)).Elem()
}

func (o MachineOutput) ToMachineOutput() MachineOutput {
	return o
}

func (o MachineOutput) ToMachineOutputWithContext(ctx context.Context) MachineOutput {
	return o
}

// The architecture type of the machine. Defaults to `amd64/generic`.
func (o MachineOutput) Architecture() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringPtrOutput { return v.Architecture }).(pulumi.StringPtrOutput)
}

// The domain of the machine. This is computed if it's not set.
func (o MachineOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.Domain }).(pulumi.StringOutput)
}

// The machine hostname. This is computed if it's not set.
func (o MachineOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.Hostname }).(pulumi.StringOutput)
}

// The minimum kernel version allowed to run on this machine. Only used when deploying Ubuntu. This is computed if it's not
// set.
func (o MachineOutput) MinHweKernel() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.MinHweKernel }).(pulumi.StringOutput)
}

// The resource pool of the machine. This is computed if it's not set.
func (o MachineOutput) Pool() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.Pool }).(pulumi.StringOutput)
}

// A map with the parameters specific to the `power_type`. See [Power types](https://maas.io/docs/api#power-types) section
// for a list of the available power parameters for each power type.
func (o MachineOutput) PowerParameters() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringMapOutput { return v.PowerParameters }).(pulumi.StringMapOutput)
}

// A power management type (e.g. `ipmi`).
func (o MachineOutput) PowerType() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.PowerType }).(pulumi.StringOutput)
}

// The MAC address of the machine's PXE boot NIC.
func (o MachineOutput) PxeMacAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.PxeMacAddress }).(pulumi.StringOutput)
}

// The zone of the machine. This is computed if it's not set.
func (o MachineOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v *Machine) pulumi.StringOutput { return v.Zone }).(pulumi.StringOutput)
}

type MachineArrayOutput struct{ *pulumi.OutputState }

func (MachineArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Machine)(nil)).Elem()
}

func (o MachineArrayOutput) ToMachineArrayOutput() MachineArrayOutput {
	return o
}

func (o MachineArrayOutput) ToMachineArrayOutputWithContext(ctx context.Context) MachineArrayOutput {
	return o
}

func (o MachineArrayOutput) Index(i pulumi.IntInput) MachineOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Machine {
		return vs[0].([]*Machine)[vs[1].(int)]
	}).(MachineOutput)
}

type MachineMapOutput struct{ *pulumi.OutputState }

func (MachineMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Machine)(nil)).Elem()
}

func (o MachineMapOutput) ToMachineMapOutput() MachineMapOutput {
	return o
}

func (o MachineMapOutput) ToMachineMapOutputWithContext(ctx context.Context) MachineMapOutput {
	return o
}

func (o MachineMapOutput) MapIndex(k pulumi.StringInput) MachineOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Machine {
		return vs[0].(map[string]*Machine)[vs[1].(string)]
	}).(MachineOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MachineInput)(nil)).Elem(), &Machine{})
	pulumi.RegisterInputType(reflect.TypeOf((*MachineArrayInput)(nil)).Elem(), MachineArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*MachineMapInput)(nil)).Elem(), MachineMap{})
	pulumi.RegisterOutputType(MachineOutput{})
	pulumi.RegisterOutputType(MachineArrayOutput{})
	pulumi.RegisterOutputType(MachineMapOutput{})
}
