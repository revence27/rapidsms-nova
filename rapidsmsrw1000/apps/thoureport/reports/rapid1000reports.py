# vim: expandtab ts=2
from .reports import *

class RedReport(ThouReport):
  'Red Reports'
  pass

# Testing report.
class RevenceReport(ThouReport):
  'Testing keyword, Revence Reports'
  pass

REPORT_SET = {
  # 'PRE':  PregReport,
  # 'REF':  RefReport,
  # 'ANC':  ANCReport,
  # 'DEP':  DepReport,
  # 'RISK': RiskReport,
  'RED':  RedReport,
  # 'BIR':  BirReport,
  # 'CHI':  ChildReport,
  # 'DTH':  DeathReport,
  # 'RES':  ResultReport,
  # 'RAR':  RedResultReport,
  # 'NBC':  NBCReport,
  # 'CCM':  CCMReport,
  # 'CMR':  CMRReport,
  # 'CBN':  CBNReport,
  # 'PNC':  PNCReport,

  # 'TIM':  TimothyReport,
  'REV': RevenceReport,
}
