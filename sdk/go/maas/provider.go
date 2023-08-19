// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package maas

import (
	"context"
	"reflect"

	"github.com/juhnny5/pulumi-maas/sdk/go/maas/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the maas package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// The MAAS API key
	ApiKey pulumi.StringPtrOutput `pulumi:"apiKey"`
	// The MAAS API URL (eg: http://127.0.0.1:5240/MAAS)
	ApiUrl pulumi.StringPtrOutput `pulumi:"apiUrl"`
	// The MAAS API version (default 2.0)
	ApiVersion pulumi.StringPtrOutput `pulumi:"apiVersion"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:maas", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// The MAAS API key
	ApiKey *string `pulumi:"apiKey"`
	// The MAAS API URL (eg: http://127.0.0.1:5240/MAAS)
	ApiUrl *string `pulumi:"apiUrl"`
	// The MAAS API version (default 2.0)
	ApiVersion *string `pulumi:"apiVersion"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// The MAAS API key
	ApiKey pulumi.StringPtrInput
	// The MAAS API URL (eg: http://127.0.0.1:5240/MAAS)
	ApiUrl pulumi.StringPtrInput
	// The MAAS API version (default 2.0)
	ApiVersion pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// The MAAS API key
func (o ProviderOutput) ApiKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiKey }).(pulumi.StringPtrOutput)
}

// The MAAS API URL (eg: http://127.0.0.1:5240/MAAS)
func (o ProviderOutput) ApiUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiUrl }).(pulumi.StringPtrOutput)
}

// The MAAS API version (default 2.0)
func (o ProviderOutput) ApiVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiVersion }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}