1. get cfssl
	brew install cfssl
2. generate a local CA
	cfssl print-defaults csr | cfssl gencert -initca - | cfssljson -bare nomad-ca
3. create a `cfssl.json` config file 
``
{
	"signing": {
		"default": {
			"expiry": "87600h",
			"usages": ["signing", "key encipherment", "server auth", "client auth"]
		}
	}
}
``
4. issue server certificates
``
	echo '{}' | cfssl gencert -ca=nomad-ca.pem -ca-key=nomad-ca-key.pem -config=cfssl.json \
    -hostname="server.global.nomad,localhost,127.0.0.1" - | cfssljson -bare server
``
5. issue client certificates
``
	echo '{}' | cfssl gencert -ca=nomad-ca.pem -ca-key=nomad-ca-key.pem -config=cfssl.json \
    -hostname="client.global.nomad,localhost,127.0.0.1" - | cfssljson -bare client
``
6. issue cli certificate
``
echo '{}' | cfssl gencert -ca=nomad-ca.pem -ca-key=nomad-ca-key.pem -profile=client \
  - | cfssljson -bare cli
``
7. copy all those certificates on **/etc/certs** Nomad servers

8. change owner on **/etc/certs**
`$ sudo chown -R nomad:nomad /etc/certs`

9. copy CA certificate on trusted pki CA (each servers)

10. update the nomad config wit hthe following stanza
``
# Require TLS
tls {
  http = true
  rpc  = true

  ca_file   = "nomad-ca.pem"
  cert_file = "server.pem"
  key_file  = "server-key.pem"

  verify_server_hostname = false
  verify_https_client    = false
}
``
11. restart nomad service
`$ sudo service nomad restart`

12. update traefik configuration nomad service endpoint address

13. update traefik configuration nomad service endpoint tls option to not check
CA
