
# Overview
This interface implements the basic form of the `udp` interface protocol.

# Usage
## Provides

By providing the `udp` interface, your charm is providing an UDP endpoint. 

Your charm need only to provide the port on which it is serving its service, as soon as the `endpoint.{relation-name}.joined` state is set:
```
@when('endpoint.udp.joined')
def configure_tcp():
    udp = endpoint_from_flag('endpoint.udp.joined')
    udp.configure(port=hookenv.config('port'))
```

## Requires
By requiring the `udp` interface, is consuming one or more UDP services.

This interface layer will set the following states, as appropriate:
- `endpoint.{relation-name}.joined` indicates that at least one service is connected. This state is **automatically** removed.
- `endpoint.{relation-name}.update` is set whenever a change happened. This is triggered when a providing charm sends new/updated info or when a relation departs. This state needs to be **manually** removed.

Use the `udp_services()` method to return a list of available UDP services:
```
[
    {
        'service_name': name_of_service,
        'hosts': [
            'host': private_address_of_host,
            'port': port_for_host,
        ],                
    }
]
```

## Authors

This software was created in the [IDLab research group](https://www.ugent.be/ea/idlab) of [Ghent University](https://www.ugent.be) in Belgium. This software is used in [Tengu](https://tengu.io), a project that aims to make experimenting with data frameworks and tools as easy as possible.

 - Sander Borny <sander.borny@ugent.be>

