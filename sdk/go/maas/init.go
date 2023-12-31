// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package maas

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/juhnny5/pulumi-maas/sdk/go/maas/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "maas:index/blockDevice:BlockDevice":
		r = &BlockDevice{}
	case "maas:index/dnsDomain:DnsDomain":
		r = &DnsDomain{}
	case "maas:index/dnsRecord:DnsRecord":
		r = &DnsRecord{}
	case "maas:index/fabric:Fabric":
		r = &Fabric{}
	case "maas:index/instance:Instance":
		r = &Instance{}
	case "maas:index/machine:Machine":
		r = &Machine{}
	case "maas:index/networkInterfaceLink:NetworkInterfaceLink":
		r = &NetworkInterfaceLink{}
	case "maas:index/networkInterfacePhysical:NetworkInterfacePhysical":
		r = &NetworkInterfacePhysical{}
	case "maas:index/space:Space":
		r = &Space{}
	case "maas:index/subnet:Subnet":
		r = &Subnet{}
	case "maas:index/subnetIpRange:SubnetIpRange":
		r = &SubnetIpRange{}
	case "maas:index/tag:Tag":
		r = &Tag{}
	case "maas:index/user:User":
		r = &User{}
	case "maas:index/vlan:Vlan":
		r = &Vlan{}
	case "maas:index/vmHost:VmHost":
		r = &VmHost{}
	case "maas:index/vmHostMachine:VmHostMachine":
		r = &VmHostMachine{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:maas" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"maas",
		"index/blockDevice",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/dnsDomain",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/dnsRecord",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/fabric",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/instance",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/machine",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/networkInterfaceLink",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/networkInterfacePhysical",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/space",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/subnet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/subnetIpRange",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/tag",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/user",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/vlan",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/vmHost",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"maas",
		"index/vmHostMachine",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"maas",
		&pkg{version},
	)
}
