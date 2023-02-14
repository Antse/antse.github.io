# Restrict access on the infrastructure using tailscale ACL's

## Introduction

Tailscale is a great mesh vpn with minimal setup to be able to join a private
network on top of internet.

One of the great feature is to use a **relay[1]** to forward your traffic from
your laptop to your Cloud infrastructure and only using private IP
addresses.

One of the drawback of this feature is that anyone on the mesh can access your
infrastructure.

Godd news is that we can setup **ACL[2]** to restrict access to people.

## Setup ACL's
### Initial scope

Let's start with 2 teams: 
- Developers folks
- Platform guys

The Platform guys need to have access all part of the infrastructure.
The Developers folks need only to read some data on staging Databases.

Let's assume that Staging Databases are located on a dedicated subnet:
`10.0.42.0/24`

### Use tags and acl

There is a file defining the global access policy to tailscale, it's a big JSON
file.

the simplest way to implement our scope policy is to define 2 groups : 

- platform
- developer

	"groups": {
			"group:platform": [
				"jean@corp.com",
				"paulette@corp.com",
			],
			"group:developer": [
				"pierre@corp.com",
				"rachel@corp.com",
			],
			"group:datanalyst": [
				"quentin@corp.com",
				"david@corp.com",
			],
		},

### Define the proper ACL

At this stage, we have 2 user groups then we need to define acl's blocks to
restrict access.

	// Access control lists.
	"acls": [
		// Match absolutely everything.
		// Comment this section out if you want to define specific restrictions.
		// Full access
		{"action": "accept", "src": ["group:platform"], "dst": ["*:*"]},
		// Access to the websites
		{"action": "accept", "src": ["group:developer"], "dst": ["*:80"]},
		// Access to the database 
		{"action": "accept", "src": ["group:datanalyst"], "dst": ["*:5432"]},
	],

## References

[1]: <https://tailscale.com/kb/1021/install-aws/>

[2]: <https://tailscale.com/kb/1068/acl-tags/>
