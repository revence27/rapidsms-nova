# vim: expandtab ts=2
from .reports import *

class PregReport(ThouReport):
  'Pregnancy Reports'
  pass

class RefReport(ThouReport):
  'Refusal Reports'
  pass

class ANCReport(ThouReport):
  'ANC Reports'
  pass

class DepReport(ThouReport):
  'Departure Reports'
  pass

class RiskReport(ThouReport):
  'Risk Reports'
  pass

class BirReport(ThouReport):
  'Birth Reports'
  pass

class ChildReport(ThouReport):
  'Child Reports'
  pass

class DeathReport(ThouReport):
  'Death Reports'
  pass

class ResultReport(ThouReport):
  'Risk Result Reports'
  pass

class RedResultReport(ThouReport):
  'Red Result Reports'
  pass

class NBCReport(ThouReport):
  'NBC Reports'
  pass

class CBNReport(ThouReport):
  'CBN Reports'
  pass

class CCMReport(ThouReport):
  'CCM Reports'
  pass

class CMRReport(ThouReport):
  'CMR Reports'
  pass

class PNCReport(ThouReport):
  'PNC Reports'
  pass

class RedReport(ThouReport):
  'Red Reports'
  pass

# Testing report.
class RevenceReport(ThouReport):
  'Testing keyword, Revence Reports'
  pass

REPORT_SET = {
  'PRE':  PregReport,
  'REF':  RefReport,
  'ANC':  ANCReport,
  'DEP':  DepReport,
  'RISK': RiskReport,
  'RED':  RedReport,
  'BIR':  BirReport,
  'CHI':  ChildReport,
  'DTH':  DeathReport,
  'RES':  ResultReport,
  'RAR':  RedResultReport,
  'NBC':  NBCReport,
  'CCM':  CCMReport,
  'CMR':  CMRReport,
  'CBN':  CBNReport,
  'PNC':  PNCReport,

  'TIM':  TimothyReport,
  'REV': RevenceReport,
}
