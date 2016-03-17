from WMCore.REST.Server import RESTEntity, restcall, rows
from WMCore.REST.Tools import tools
from WMCore.REST.Validation import *
from WMCore.REST.Format import JSONFormat,XMLFormat
from T0WmaDataSvc.Regexps import *
from operator import itemgetter
import json

class DatasetLocked(RESTEntity):
  """REST entity for retrieving list of locked datasets."""
  def validate(self, apiobj, method, api, param, safe):
    """Validate request input data."""
    pass

  @restcall(formats=[('application/json', JSONFormat()), ('application/xml', XMLFormat())])
  @tools.expires(secs=300)
  def get(self):
    """Retrieve list of locked datasets

    :returns: list of datasets names"""

    sql = """SELECT dataset_locked.path
             FROM dataset_locked"""

    c, _ = self.api.execute(sql)

    datasets = []
    for result in c.fetchall():
      if result[0]:
        datasets.append(result[0])

    return sorted(datasets)
