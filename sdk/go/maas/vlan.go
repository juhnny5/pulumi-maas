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

type Vlan struct {
	pulumi.CustomResourceState

	// Boolean value. Whether or not DHCP should be managed on the new VLAN. This argument is computed if it's not set.
	DhcpOn pulumi.BoolOutput `pulumi:"dhcpOn"`
	// The identifier (name or ID) of the fabric for the new VLAN.
	Fabric pulumi.StringOutput `pulumi:"fabric"`
	// The MTU to use on the new VLAN. This argument is computed if it's not set.
	Mtu pulumi.IntOutput `pulumi:"mtu"`
	// The name of the new VLAN. This argument is computed if it's not set.
	Name pulumi.StringOutput `pulumi:"name"`
	// The space of the new VLAN. Passing in an empty string (or the string `undefined`) will cause the VLAN to be placed in
	// the `undefined` space. This argument is computed if it's not set.
	Space pulumi.StringOutput `pulumi:"space"`
	// The traffic segregation ID for the new VLAN.
	Vid pulumi.IntOutput `pulumi:"vid"`
}

// NewVlan registers a new resource with the given unique name, arguments, and options.
func NewVlan(ctx *pulumi.Context,
	name string, args *VlanArgs, opts ...pulumi.ResourceOption) (*Vlan, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Fabric == nil {
		return nil, errors.New("invalid value for required argument 'Fabric'")
	}
	if args.Vid == nil {
		return nil, errors.New("invalid value for required argument 'Vid'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Vlan
	err := ctx.RegisterResource("maas:index/vlan:Vlan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVlan gets an existing Vlan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVlan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VlanState, opts ...pulumi.ResourceOption) (*Vlan, error) {
	var resource Vlan
	err := ctx.ReadResource("maas:index/vlan:Vlan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Vlan resources.
type vlanState struct {
	// Boolean value. Whether or not DHCP should be managed on the new VLAN. This argument is computed if it's not set.
	DhcpOn *bool `pulumi:"dhcpOn"`
	// The identifier (name or ID) of the fabric for the new VLAN.
	Fabric *string `pulumi:"fabric"`
	// The MTU to use on the new VLAN. This argument is computed if it's not set.
	Mtu *int `pulumi:"mtu"`
	// The name of the new VLAN. This argument is computed if it's not set.
	Name *string `pulumi:"name"`
	// The space of the new VLAN. Passing in an empty string (or the string `undefined`) will cause the VLAN to be placed in
	// the `undefined` space. This argument is computed if it's not set.
	Space *string `pulumi:"space"`
	// The traffic segregation ID for the new VLAN.
	Vid *int `pulumi:"vid"`
}

type VlanState struct {
	// Boolean value. Whether or not DHCP should be managed on the new VLAN. This argument is computed if it's not set.
	DhcpOn pulumi.BoolPtrInput
	// The identifier (name or ID) of the fabric for the new VLAN.
	Fabric pulumi.StringPtrInput
	// The MTU to use on the new VLAN. This argument is computed if it's not set.
	Mtu pulumi.IntPtrInput
	// The name of the new VLAN. This argument is computed if it's not set.
	Name pulumi.StringPtrInput
	// The space of the new VLAN. Passing in an empty string (or the string `undefined`) will cause the VLAN to be placed in
	// the `undefined` space. This argument is computed if it's not set.
	Space pulumi.StringPtrInput
	// The traffic segregation ID for the new VLAN.
	Vid pulumi.IntPtrInput
}

func (VlanState) ElementType() reflect.Type {
	return reflect.TypeOf((*vlanState)(nil)).Elem()
}

type vlanArgs struct {
	// Boolean value. Whether or not DHCP should be managed on the new VLAN. This argument is computed if it's not set.
	DhcpOn *bool `pulumi:"dhcpOn"`
	// The identifier (name or ID) of the fabric for the new VLAN.
	Fabric string `pulumi:"fabric"`
	// The MTU to use on the new VLAN. This argument is computed if it's not set.
	Mtu *int `pulumi:"mtu"`
	// The name of the new VLAN. This argument is computed if it's not set.
	Name *string `pulumi:"name"`
	// The space of the new VLAN. Passing in an empty string (or the string `undefined`) will cause the VLAN to be placed in
	// the `undefined` space. This argument is computed if it's not set.
	Space *string `pulumi:"space"`
	// The traffic segregation ID for the new VLAN.
	Vid int `pulumi:"vid"`
}

// The set of arguments for constructing a Vlan resource.
type VlanArgs struct {
	// Boolean value. Whether or not DHCP should be managed on the new VLAN. This argument is computed if it's not set.
	DhcpOn pulumi.BoolPtrInput
	// The identifier (name or ID) of the fabric for the new VLAN.
	Fabric pulumi.StringInput
	// The MTU to use on the new VLAN. This argument is computed if it's not set.
	Mtu pulumi.IntPtrInput
	// The name of the new VLAN. This argument is computed if it's not set.
	Name pulumi.StringPtrInput
	// The space of the new VLAN. Passing in an empty string (or the string `undefined`) will cause the VLAN to be placed in
	// the `undefined` space. This argument is computed if it's not set.
	Space pulumi.StringPtrInput
	// The traffic segregation ID for the new VLAN.
	Vid pulumi.IntInput
}

func (VlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vlanArgs)(nil)).Elem()
}

type VlanInput interface {
	pulumi.Input

	ToVlanOutput() VlanOutput
	ToVlanOutputWithContext(ctx context.Context) VlanOutput
}

func (*Vlan) ElementType() reflect.Type {
	return reflect.TypeOf((**Vlan)(nil)).Elem()
}

func (i *Vlan) ToVlanOutput() VlanOutput {
	return i.ToVlanOutputWithContext(context.Background())
}

func (i *Vlan) ToVlanOutputWithContext(ctx context.Context) VlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VlanOutput)
}

// VlanArrayInput is an input type that accepts VlanArray and VlanArrayOutput values.
// You can construct a concrete instance of `VlanArrayInput` via:
//
//	VlanArray{ VlanArgs{...} }
type VlanArrayInput interface {
	pulumi.Input

	ToVlanArrayOutput() VlanArrayOutput
	ToVlanArrayOutputWithContext(context.Context) VlanArrayOutput
}

type VlanArray []VlanInput

func (VlanArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Vlan)(nil)).Elem()
}

func (i VlanArray) ToVlanArrayOutput() VlanArrayOutput {
	return i.ToVlanArrayOutputWithContext(context.Background())
}

func (i VlanArray) ToVlanArrayOutputWithContext(ctx context.Context) VlanArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VlanArrayOutput)
}

// VlanMapInput is an input type that accepts VlanMap and VlanMapOutput values.
// You can construct a concrete instance of `VlanMapInput` via:
//
//	VlanMap{ "key": VlanArgs{...} }
type VlanMapInput interface {
	pulumi.Input

	ToVlanMapOutput() VlanMapOutput
	ToVlanMapOutputWithContext(context.Context) VlanMapOutput
}

type VlanMap map[string]VlanInput

func (VlanMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Vlan)(nil)).Elem()
}

func (i VlanMap) ToVlanMapOutput() VlanMapOutput {
	return i.ToVlanMapOutputWithContext(context.Background())
}

func (i VlanMap) ToVlanMapOutputWithContext(ctx context.Context) VlanMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VlanMapOutput)
}

type VlanOutput struct{ *pulumi.OutputState }

func (VlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Vlan)(nil)).Elem()
}

func (o VlanOutput) ToVlanOutput() VlanOutput {
	return o
}

func (o VlanOutput) ToVlanOutputWithContext(ctx context.Context) VlanOutput {
	return o
}

// Boolean value. Whether or not DHCP should be managed on the new VLAN. This argument is computed if it's not set.
func (o VlanOutput) DhcpOn() pulumi.BoolOutput {
	return o.ApplyT(func(v *Vlan) pulumi.BoolOutput { return v.DhcpOn }).(pulumi.BoolOutput)
}

// The identifier (name or ID) of the fabric for the new VLAN.
func (o VlanOutput) Fabric() pulumi.StringOutput {
	return o.ApplyT(func(v *Vlan) pulumi.StringOutput { return v.Fabric }).(pulumi.StringOutput)
}

// The MTU to use on the new VLAN. This argument is computed if it's not set.
func (o VlanOutput) Mtu() pulumi.IntOutput {
	return o.ApplyT(func(v *Vlan) pulumi.IntOutput { return v.Mtu }).(pulumi.IntOutput)
}

// The name of the new VLAN. This argument is computed if it's not set.
func (o VlanOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Vlan) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The space of the new VLAN. Passing in an empty string (or the string `undefined`) will cause the VLAN to be placed in
// the `undefined` space. This argument is computed if it's not set.
func (o VlanOutput) Space() pulumi.StringOutput {
	return o.ApplyT(func(v *Vlan) pulumi.StringOutput { return v.Space }).(pulumi.StringOutput)
}

// The traffic segregation ID for the new VLAN.
func (o VlanOutput) Vid() pulumi.IntOutput {
	return o.ApplyT(func(v *Vlan) pulumi.IntOutput { return v.Vid }).(pulumi.IntOutput)
}

type VlanArrayOutput struct{ *pulumi.OutputState }

func (VlanArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Vlan)(nil)).Elem()
}

func (o VlanArrayOutput) ToVlanArrayOutput() VlanArrayOutput {
	return o
}

func (o VlanArrayOutput) ToVlanArrayOutputWithContext(ctx context.Context) VlanArrayOutput {
	return o
}

func (o VlanArrayOutput) Index(i pulumi.IntInput) VlanOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Vlan {
		return vs[0].([]*Vlan)[vs[1].(int)]
	}).(VlanOutput)
}

type VlanMapOutput struct{ *pulumi.OutputState }

func (VlanMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Vlan)(nil)).Elem()
}

func (o VlanMapOutput) ToVlanMapOutput() VlanMapOutput {
	return o
}

func (o VlanMapOutput) ToVlanMapOutputWithContext(ctx context.Context) VlanMapOutput {
	return o
}

func (o VlanMapOutput) MapIndex(k pulumi.StringInput) VlanOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Vlan {
		return vs[0].(map[string]*Vlan)[vs[1].(string)]
	}).(VlanOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VlanInput)(nil)).Elem(), &Vlan{})
	pulumi.RegisterInputType(reflect.TypeOf((*VlanArrayInput)(nil)).Elem(), VlanArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VlanMapInput)(nil)).Elem(), VlanMap{})
	pulumi.RegisterOutputType(VlanOutput{})
	pulumi.RegisterOutputType(VlanArrayOutput{})
	pulumi.RegisterOutputType(VlanMapOutput{})
}