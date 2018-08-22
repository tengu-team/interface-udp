from charms.reactive import (
    when_any,
    when_not,
    set_flag,
    clear_flag,
    Endpoint,
)


class UdpRequires(Endpoint):

    @when_any('endpoint.{endpoint_name}.changed.port',
              'endpoint.{endpoint_name}.changed.host',
              'endpoint.{endpoint_name}.departed')
    def udp_changed(self):
        set_flag(self.expand_name('update'))
        clear_flag(self.expand_name('changed.port'))
        clear_flag(self.expand_name('changed.host'))
        clear_flag(self.expand_name('departed'))

    def udp_services(self):
        """
        Returns a list of available UDP services.

        The return value is a list of dicts of the following form:

        [
            {
                'service_name': name_of_service,
                'hosts': [
                    'host': private_address_of_host,
                    'port': port_for_host,
                ],                
            }
        ]
        """
        services = {}
        for relation in self.relations:
            data = relation.joined_units.received
            service_name = relation.application_name
            service = services.setdefault(service_name, {
                'service_name': service_name,
                'hosts': [],
            })
            host = data['host']
            port = data['port']
            if host and port:
                service['hosts'].append({
                    'host': host,
                    'port': port,
                })
        return [s for s in services.values() if s['hosts']]
