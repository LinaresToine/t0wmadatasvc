from WMCore.REST.Server import RESTEntity, restcall, rows
from WMCore.REST.Tools import tools
from WMCore.REST.Validation import *
from WMCore.REST.Format import JSONFormat, PrettyJSONFormat
from T0WmaDataSvc.Regexps import *
from operator import itemgetter

class PrimaryDatasetConfig(RESTEntity):
  """REST entity for retrieving a specific primary dataset."""
  def validate(self, apiobj, method, api, param, safe):
    """Validate request input data."""
    validate_str('primary_dataset', param, safe, RX_PRIMARY_DATASET, optional = True)

  @restcall(formats=[('text/plain', PrettyJSONFormat()), ('application/json', JSONFormat())])
  @tools.expires(secs=300)
  def get(self, primary_dataset):
    """Retrieve Reco configuration and its history for a specific primary dataset

    :arg str primary_dataset: the primary dataset name (optional, otherwise queries for muon 0)
    :returns: PrimaryDataset, Acquisition era, minimum run, maximum run, CMSSW, PhysicsSkim, DqmSeq, GlobalTag"""

    sql = """
            SELECT primds, acq_era, min_run, max_run, cmssw, global_tag, physics_skim, dqm_seq
            FROM primary_dataset_config
            """
    sql_with_primds = "WHERE primds = :primary_dataset"
    sql_order_with_primds = "ORDER BY min_run desc"
    sql_order_without_primds = "ORDER BY primds, min_run desc"


    if primary_dataset is not None:
        sql += sql_with_primds
        sql += sql_order_with_primds
        c, _ = self.api.execute(sql, primds = primary_dataset)
    else:
        sql += sql_order_without_primds
        c, _ = self.api.execute(sql, primds = '')

    results=c.fetchall()

  
    configs = []
    for primds, acq_era, min_run, max_run, cmssw, global_tag, physics_skim, dqm_seq in results:

        config = { "primary_dataset" : primds,
                   "acq_era" : acq_era,
                   "min_run" : min_run,
                   "max_run" : max_run,
                   "cmssw" : cmssw,
                   "global_tag" : global_tag,
                   "physics_skim" : physics_skim,
                   "dqm_seq" : dqm_seq
                   }
        configs.append(config)

    return configs