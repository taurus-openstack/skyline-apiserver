from . import base

list_rules = (
    base.Rule(
        name="context_is_admin",
        check_str=("role:admin"),
        description="No description",
    ),
    base.Rule(
        name="admin_or_owner",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="No description",
    ),
    base.Rule(
        name="admin_api",
        check_str=("rule:context_is_admin"),
        description="No description",
    ),
    base.Rule(
        name="admin_or_user",
        check_str=("is_admin:True or user_id:%(user_id)s"),
        description="No description",
    ),
    base.Rule(
        name="cluster_user",
        check_str=("user_id:%(trustee_user_id)s"),
        description="No description",
    ),
    base.Rule(
        name="deny_cluster_user",
        check_str=("not domain_id:%(trustee_domain_id)s"),
        description="No description",
    ),
    base.APIRule(
        name="magnum:bay:create",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Create a new bay.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/bays"}],
    ),
    base.APIRule(
        name="magnum:bay:delete",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Delete a bay.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/bays/{bay_ident}"}],
    ),
    base.APIRule(
        name="magnum:bay:detail",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of bays with detail.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/bays"}],
    ),
    base.APIRule(
        name="magnum:bay:get",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve information about the given bay.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/bays/{bay_ident}"}],
    ),
    base.APIRule(
        name="magnum:bay:get_all",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of bays.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/bays/"}],
    ),
    base.APIRule(
        name="magnum:bay:update",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Update an existing bay.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/bays/{bay_ident}"}],
    ),
    base.APIRule(
        name="magnum:baymodel:create",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Create a new baymodel.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/baymodels"}],
    ),
    base.APIRule(
        name="magnum:baymodel:delete",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Delete a baymodel.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/baymodels/{baymodel_ident}"}],
    ),
    base.APIRule(
        name="magnum:baymodel:detail",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of baymodel with detail.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/baymodels"}],
    ),
    base.APIRule(
        name="magnum:baymodel:get",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve information about the given baymodel.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/baymodels/{baymodel_ident}"}],
    ),
    base.APIRule(
        name="magnum:baymodel:get_all",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of baymodel.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/baymodels"}],
    ),
    base.APIRule(
        name="magnum:baymodel:update",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Update an existing baymodel.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/baymodels/{baymodel_ident}"}],
    ),
    base.APIRule(
        name="magnum:baymodel:publish",
        check_str=("(role:admin)"),
        description="Publish an existing baymodel.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/baymodels"},
            {"method": "PATCH", "path": "/v1/baymodels"},
        ],
    ),
    base.APIRule(
        name="magnum:certificate:create",
        check_str=("(is_admin:True or user_id:%(user_id)s) or (user_id:%(trustee_user_id)s)"),
        description="Sign a new certificate by the CA.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/certificates"}],
    ),
    base.APIRule(
        name="magnum:certificate:get",
        check_str=("(is_admin:True or user_id:%(user_id)s) or (user_id:%(trustee_user_id)s)"),
        description="Retrieve CA information about the given bay/cluster.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/certificates/{bay_uuid/cluster_uuid}"}],
    ),
    base.APIRule(
        name="magnum:certificate:rotate_ca",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Rotate the CA certificate on the given bay/cluster.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/certificates/{bay_uuid/cluster_uuid}"}],
    ),
    base.APIRule(
        name="magnum:cluster:create",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Create a new cluster.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/clusters"}],
    ),
    base.APIRule(
        name="magnum:cluster:delete",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Delete a cluster.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:delete_all_projects",
        check_str=("(role:admin)"),
        description="Delete a cluster from any project.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:detail",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of clusters with detail.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters"}],
    ),
    base.APIRule(
        name="magnum:cluster:detail_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve a list of clusters with detail across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters"}],
    ),
    base.APIRule(
        name="magnum:cluster:get",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve information about the given cluster.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:get_one_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve information about the given cluster across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:get_all",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of clusters.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/"}],
    ),
    base.APIRule(
        name="magnum:cluster:get_all_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve a list of all clusters across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/"}],
    ),
    base.APIRule(
        name="magnum:cluster:update",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Update an existing cluster.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:update_health_status",
        check_str=("(is_admin:True or user_id:%(user_id)s) or (user_id:%(trustee_user_id)s)"),
        description="Update the health status of an existing cluster.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:update_all_projects",
        check_str=("(role:admin)"),
        description="Update an existing cluster.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/clusters/{cluster_ident}"}],
    ),
    base.APIRule(
        name="magnum:cluster:resize",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Resize an existing cluster.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/clusters/{cluster_ident}/actions/resize"}],
    ),
    base.APIRule(
        name="magnum:cluster:upgrade",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Upgrade an existing cluster.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/clusters/{cluster_ident}/actions/upgrade"}],
    ),
    base.APIRule(
        name="magnum:cluster:upgrade_all_projects",
        check_str=("(role:admin)"),
        description="Upgrade an existing cluster across all projects.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/clusters/{cluster_ident}/actions/upgrade"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:create",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Create a new cluster template.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/clustertemplates"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:delete",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Delete a cluster template.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/clustertemplate/{clustertemplate_ident}"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:delete_all_projects",
        check_str=("(role:admin)"),
        description="Delete a cluster template from any project.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/clustertemplate/{clustertemplate_ident}"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:detail_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve a list of cluster templates with detail across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clustertemplates"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:detail",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of cluster templates with detail.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clustertemplates"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:get",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve information about the given cluster template.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clustertemplate/{clustertemplate_ident}"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:get_one_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve information about the given cluster template across project.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clustertemplate/{clustertemplate_ident}"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:get_all",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of cluster templates.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clustertemplates"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:get_all_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve a list of cluster templates across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clustertemplates"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:update",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Update an existing cluster template.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/clustertemplate/{clustertemplate_ident}"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:update_all_projects",
        check_str=("(role:admin)"),
        description="Update an existing cluster template.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/clustertemplate/{clustertemplate_ident}"}],
    ),
    base.APIRule(
        name="magnum:clustertemplate:publish",
        check_str=("(role:admin)"),
        description="Publish an existing cluster template.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/clustertemplates"},
            {"method": "PATCH", "path": "/v1/clustertemplates"},
        ],
    ),
    base.APIRule(
        name="magnum:federation:create",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Create a new federation.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/federations"}],
    ),
    base.APIRule(
        name="magnum:federation:delete",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Delete a federation.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/federations/{federation_ident}"}],
    ),
    base.APIRule(
        name="magnum:federation:detail",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of federations with detail.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/federations"}],
    ),
    base.APIRule(
        name="magnum:federation:get",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve information about the given federation.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/federations/{federation_ident}"}],
    ),
    base.APIRule(
        name="magnum:federation:get_all",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Retrieve a list of federations.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/federations/"}],
    ),
    base.APIRule(
        name="magnum:federation:update",
        check_str=("(not domain_id:%(trustee_domain_id)s)"),
        description="Update an existing federation.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/federations/{federation_ident}"}],
    ),
    base.APIRule(
        name="magnum:magnum-service:get_all",
        check_str=("(role:admin)"),
        description="Retrieve a list of magnum-services.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/mservices"}],
    ),
    base.APIRule(
        name="magnum:quota:create",
        check_str=("(role:admin)"),
        description="Create quota.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/quotas"}],
    ),
    base.APIRule(
        name="magnum:quota:delete",
        check_str=("(role:admin)"),
        description="Delete quota for a given project_id and resource.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/quotas/{project_id}/{resource}"}],
    ),
    base.APIRule(
        name="magnum:quota:get",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Retrieve Quota information for the given project_id.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/quotas/{project_id}/{resource}"}],
    ),
    base.APIRule(
        name="magnum:quota:get_all",
        check_str=("(role:admin)"),
        description="Retrieve a list of quotas.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/quotas"}],
    ),
    base.APIRule(
        name="magnum:quota:update",
        check_str=("(role:admin)"),
        description="Update quota for a given project_id.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/quotas/{project_id}/{resource}"}],
    ),
    base.APIRule(
        name="magnum:stats:get_all",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Retrieve magnum stats.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/stats"}],
    ),
    base.APIRule(
        name="magnum:nodegroup:get",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Retrieve information about the given nodegroup.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/{cluster_id}/nodegroup/{nodegroup}"}],
    ),
    base.APIRule(
        name="magnum:nodegroup:get_all",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Retrieve a list of nodegroups that belong to a cluster.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/{cluster_id}/nodegroups/"}],
    ),
    base.APIRule(
        name="magnum:nodegroup:get_all_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve a list of nodegroups across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/clusters/{cluster_id}/nodegroups/"}],
    ),
    base.APIRule(
        name="magnum:nodegroup:get_one_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve infornation for a given nodegroup.",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/clusters/{cluster_id}/nodegroups/{nodegroup}"},
        ],
    ),
    base.APIRule(
        name="magnum:nodegroup:create",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Create a new nodegroup.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/clusters/{cluster_id}/nodegroups/"}],
    ),
    base.APIRule(
        name="magnum:nodegroup:delete",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Delete a nodegroup.",
        scope_types=["project"],
        operations=[
            {"method": "DELETE", "path": "/v1/clusters/{cluster_id}/nodegroups/{nodegroup}"},
        ],
    ),
    base.APIRule(
        name="magnum:nodegroup:update",
        check_str=("(is_admin:True or project_id:%(project_id)s)"),
        description="Update an existing nodegroup.",
        scope_types=["project"],
        operations=[
            {"method": "PATCH", "path": "/v1/clusters/{cluster_id}/nodegroups/{nodegroup}"},
        ],
    ),
)

__all__ = ("list_rules",)
