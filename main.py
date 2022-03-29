import requests
import json
import logging
result = requests.get("https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=tTMygh7G3EqdEgi7KoKpvgdPUjHq2c2xp9bXqJiU&lat=40&lon=-105")

result.status_code

print(result.text)

print(result.json())


sw_versions_data = {'blackbox_exporter': {'version': '0.17.0-0.0.3', 'nvchecker_config': 'source = "github"\ngithub = "prometheus/blackbox_exporter"\nuse_latest_release = true\n'}, 'dellhw_exporter': {'version': '1.7.0', 'checksum': 'aaea2ce1e5efc04dcedef1145001d0d3df545eb3801c785630450db8be272768', 'nvchecker_config': 'source = "github"\ngithub = "galexrt/dellhw_exporter"\nuse_latest_release = true\n'}, 'dex': {'version': '2.28.1', 'nvchecker_config': 'source = "github"\ngithub = "dexidp/dex"\nuse_latest_release = true\n'}, 'etcd': {'version': '3.4.18', 'nvchecker_config': 'source = "github"\ngithub = "etcd-io/etcd"\nuse_max_tag = true\ninclude_regex = \'v[0-9.]+\'\n'}, 'gitlab': {'version': '14.8.2-ee.0', 'nvchecker_config': 'source = "gitlab"\ngitlab = "gitlab-org/gitlab"\nuse_max_tag = true\ninclude_regex = \'v[0-9.]+-ee\'\n'}, 'gitlab_runner': {'version': '14.8.2', 'nvchecker_config': 'source = "gitlab"\ngitlab = "gitlab-org/gitlab-runner"\nuse_max_tag = true\ninclude_regex = \'v[0-9.]+\'\n'}, 'harbor': {'version': '2.1.1-cps-0.7', 'nvchecker_config': 'source = "github"\ngithub = "goharbor/harbor"\nuse_max_tag = true\ninclude_regex = \'v[0-9.]+\'\n'}, 'harbor_exporter': {'version': '0.6.4', 'nvchecker_config': 'source = "github"\ngithub = "c4po/harbor_exporter"\nuse_latest_release = true\n'}, 'matchbox': {'version': '0.8.3', 'checksum': '571a6285cc27af9f1490b5829a279c9329de736ca06355ee0f23aaa8bd9da89e', 'nvchecker_config': 'source = "github"\ngithub = "poseidon/matchbox"\nuse_latest_release = true\n'}, 'nginx': {'version': '1.18.0', 'nvchecker_config': 'source = "container"\ncontainer = "library/nginx"\ninclude_regex = \'[0-9]+\\.[0-9]+\\.[0-9]+\'\n'}, 'node_exporter': {'version': '0.18.1', 'checksum': 'b2503fd932f85f4e5baf161268854bf5d22001869b84f00fd2d1f57b51b72424', 'nvchecker_config': 'source = "github"\ngithub = "prometheus/node_exporter"\nuse_latest_release = true\n'}, 'prometheus': {'version': '2.34.0', 'nvchecker_config': 'source = "github"\ngithub = "prometheus/prometheus"\nuse_latest_release = true\n'}, 'approleid_provisioner': {'version': '1.0.2', 'nvchecker_config': 'source = "gitlab"\ngitlab = "acc/approleid-provisioner"\nhost = "acc-gitlab-live.server.lan"\nuse_max_tag = true\n'}, 'vault': {'version': '1.9.2', 'nvchecker_config': 'source = "github"\ngithub = "hashicorp/vault"\nuse_max_tag = true\ninclude_regex = \'v[0-9.]+\'\n'}, 'asset_downloader': {'version': '1.3.6', 'nvchecker_config': 'source = "gitlab"\ngitlab = "acc/asset-downloader"\nhost = "acc-gitlab-live.server.lan"\nuse_max_tag = true\n'}, 'docker_ce': {'version': '19.03.14', 'nvchecker_config': 'source = "github"\ngithub = "docker/cli"\nuse_max_tag = true\ninclude_regex = \'v[0-9.]+\'\nfrom_pattern = \'v([0-9]+)\\.([0-9]+).*\'\nto_pattern = \'\\1.\\2\'\n'}}


def dic_key_update(sw_versions_data_items):
    new_keys = []
    old_keys = []
    prefix = " project"
    for i, (k, v) in enumerate(sw_versions_data_items.items()):
        old_keys.append(k)
        new_keys.append(k + str(prefix))
    for old_key, new_key in zip(old_keys, new_keys):
        print('old {}, new {}'.format(old_key, new_key))
        if new_key != old_key:
            sw_versions_data_items[new_key] = sw_versions_data_items.pop(old_key)
    return sw_versions_data_items


sw_versions = dic_key_update(sw_versions_data)
logging.info('My change sw_versions data is: {}' .format(sw_versions_data))

