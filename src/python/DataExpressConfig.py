from WMCore.REST.Server import RESTEntity, restcall, rows
from WMCore.REST.Tools import tools
from WMCore.REST.Validation import *
from T0WmaDataSvc.Regexps import *
from operator import itemgetter

class ExpressConfig(RESTEntity):
  """REST entity for retrieving an specific run."""
  def validate(self, apiobj, method, api, param, safe):
    """Validate request input data."""
    validate_str('run', param, safe, RX_RUN, optional = True)
    validate_str('stream', param, safe, RX_STREAM, optional = True)


  @restcall
  @tools.expires(secs=300)
  def get(self,run, stream):
    """Retrieve Express configuration for a specific run (and stream)

    :arg int run: the run number (latest if not specified)
    :arg str stream: the stream name (optional, otherwise queries for all)
    :returns: Run number, CMSSW Release, Global Tag, Scenario"""

    sqlWhereWithRun="express_config.run = :run"
    sqlWhereWithoutRun="express_config.run = (select max(run) from express_config)"
    sqlWhereOptionStream=" AND express_config.stream = :stream"

    sql = """SELECT express_config.run,
                    express_config.stream,
                    express_config.cmssw,
                    express_config.scram_arch,
                    express_config.reco_cmssw,
                    express_config.reco_scram_arch,
                    express_config.global_tag,
                    express_config.scenario
             FROM express_config
             WHERE %s %s"""

    if run is not None and stream is None :
        c, _ = self.api.execute(sql % (sqlWhereWithRun, ''), run = run)
    elif run is not None and stream is not None :
        c, _ = self.api.execute(sql % (sqlWhereWithRun, sqlWhereOptionStream), run = run, stream = stream)
    else :
        c, _ = self.api.execute(sql % (sqlWhereWithoutRun, ''))

    configs = []
    for result in c.fetchall():

        (run, stream, cmssw, scram_arch, reco_cmssw, reco_scram_arch, global_tag, scenario) = result

        config = { "run" : run,
                   "stream" : stream,
                   "cmssw" : cmssw,
                   "scram_arch" : scram_arch,
                   "reco_cmssw" : reco_cmssw,
                   "reco_scram_arch" : reco_scram_arch,
                   "global_tag" : global_tag,
                   "scenario" : scenario }
        configs.append(config)

    return str(configs)
