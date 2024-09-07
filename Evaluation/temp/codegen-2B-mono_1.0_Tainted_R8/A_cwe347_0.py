'''

    # create an API object
    apicon = bb.api.Apicon(self.bb, user=self.bb.config.vendordict[self.vendorname],
                           auth=self.bb.auth, service='vhostd',
                           projname=self.project, retry=self.bb.config.bbapi_retry)

    api_versions = apicon.get('version', {})
    self.service_name = api_versions.get('vhostd', True)
    self.service_url = self.url + '/' + self.service_name

    # Create a host record to add, for both internal and external
    uuid = api.create_url('/hosts/', self.host)
    api.create_url('/hosts/', self.host, uuid, '127.0.0.1',
                   ['1.1.1.1', 1], self.port)
    uuid = self.uuid

    # add a zone
    zones = self.create_zone_obj(uuid)
    