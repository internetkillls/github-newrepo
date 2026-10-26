"""Optional read-only VCT/AREX mathematical admissibility handoff.

This bridge always computes real dispatcher probes; a mathematical verdict
never issues a write grant. It is NOT applicable to a nonmathematical canary.
"""
from __future__ import annotations
from autopatcher_core import digest,GateError


def evaluate_model_before_patch(spec:dict)->dict:
    from heuristic_dispatcher import dispatch,DispatchInputError
    try:report=dispatch(spec)
    except (DispatchInputError,KeyError,ValueError,TypeError) as e:
        return {'finding':'UNSUPPORTED','disposition':'CHANGE_METHOD','reason':str(e),
                'can_issue_write_authorization':False}
    gate=report['decision_gate']
    mapping={
      'CONDITIONAL_NUMERICAL_WITNESS':('PROVISIONAL','CONTINUE','model result is conditional; target tests remain mandatory'),
      'ORIGINAL_CLAIM_REFUTED_REFINED_VARIANT_PASSES':('CONTRADICTED','REVISE_PREMISE','original model invalid; refinement is new case'),
      'MODEL_CLAIM_REFUTED_OR_NONIDENTIFIABLE':('CONTRADICTED','REVISE_PREMISE','counterexample or nonidentifiability'),
      'NEEDS_DISCRIMINATING_OBSERVATION':('UNVERIFIED','WITHHOLD_CLAIM','more observations needed'),
      'INVALID_OBSERVATION_OR_PROBE':('UNSUPPORTED','CHANGE_METHOD','invalid typed probe'),
    }
    finding,disposition,reason=mapping.get(gate,('UNVERIFIED','WITHHOLD_CLAIM','unrecognized status'))
    return {'finding':finding,'disposition':disposition,'decision_gate':gate,'reason':reason,
            'calculation_executed':bool(report['pipeline_executed_in_python']),
            'report_sha256':digest(report),'arex_evidence':report.get('arex_discovery'),
            'candidate_math_tasks':report.get('task_graph'),
            'can_issue_write_authorization':False,
            'write_eligibility_note':'Only an independent authorized operator can mint grants; mathematically supported estimates are not permissions.'}
