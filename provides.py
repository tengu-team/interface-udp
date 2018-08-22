from charmhelpers.core import hookenv
from charms.reactive import Endpoint


class UdpProvides(Endpoint):

    def get_ingress_address(self, rel_id=None):
        if rel_id is None:
            rel_id = self.relations[0].relation_id
        return hookenv.ingress_address(rel_id, hookenv.local_unit())

    def configure(self, port, host=None):
        for relation in self.relations:
            relation.to_publish.update({
                'port': port,
                'host': host or self.get_ingress_address(relation.relation_id)
            })
