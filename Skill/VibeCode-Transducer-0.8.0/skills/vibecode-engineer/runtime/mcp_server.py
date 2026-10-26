"""Optional MCP adapter (official mcp Python SDK 2.x). Not automatically hosted.

All tools are stateless and read-only. Mathematical operators run as bounded
Python functions, never arbitrary evaluated source code or repository mutations.
"""
from __future__ import annotations
import json
from mcp.server import MCPServer
from vibe_transducer import ContractError, transduce, VERSION
from cloud_math_executor import execute
from math_model_router import ModelContractError
from heuristic_inference import execute as heuristic_execute, HeuristicContractError
from multimodel_engine import execute as multimodel_execute, MultiModelInputError
from heuristic_dispatcher import dispatch as dispatch_heuristics, DispatchInputError
from autopatcher_core import capability_report as autopatch_capabilities
from autopatcher_control import capability_report as control_capabilities

app=MCPServer('VibeCode Transducer')

@app.tool()
def vibecode_status()->dict:
    """Describe actually available Python tools, not claimed ChatGPT host connection."""
    return {'version':'0.8.0','legacy_transducer_version':VERSION,'math_kernel_version':'vct-python-evidence/0.3.0','heuristic_kernel_version':'vct-heuristic-inference/0.4.0',
            'running':'mcp_python_server',
            'multimodel_kernel_version':'vct-multimodel/0.6.0',
            'heuristic_dispatcher_version':'vct-heuristic-dispatcher/0.7.0',
            'tools':['vibecode_status','vibecode_transduce','vibecode_math_execute','vibecode_heuristic_execute','vibecode_multimodel_execute','vibecode_dispatch_execute','vibecode_autopatcher_capabilities'],
            'mutation_enabled':False,'repository_filesystem_access':False,
            'sandbox':'NOT_A_SANDBOX','cloud_connected':'MUST_BE_PROVEN_BY_EXTERNAL_CALL'}

@app.tool()
def vibecode_transduce(task_json:str)->dict:
    """Run bounded static engineering observations; no source code evaluation."""
    if len(task_json.encode('utf-8'))>650_000:
        return {'error':'INPUT_LIMIT','detail':'JSON task exceeds 650KB'}
    try:
        return transduce(json.loads(task_json))
    except (ContractError,TypeError,ValueError,json.JSONDecodeError) as exc:
        return {'error':'INVALID_INPUT','detail':str(exc)}

@app.tool()
def vibecode_math_execute(math_json:str)->dict:
    """Execute bounded mathematical computations on explicitly supplied typed observations.

    Input: JSON object with math_problem and observation_payload, as described in
    cloud-python-decision-contract.md. This calls real Python functions, returns
    SHA-bound results, and does not run arbitrary Python submitted by clients.
    """
    if len(math_json.encode('utf-8'))>650_000:
        return {'error':'INPUT_LIMIT','detail':'Math JSON task exceeds 650KB'}
    try:
        return execute(json.loads(math_json))
    except (ModelContractError,TypeError,ValueError,json.JSONDecodeError) as exc:
        return {'error':'INVALID_INPUT','detail':str(exc)}

@app.tool()
def vibecode_heuristic_execute(heuristic_json:str)->dict:
    """Run bounded representation/admissibility and heuristic inference checks.

    Input JSON: heuristic_problem content with typed representation, optional
    normalization, candidate_discrimination, bounded_decision or demonstration,
    and optional noninjective-label counterexample. Does not execute user code.
    """
    if len(heuristic_json.encode('utf-8'))>650_000:
        return {'error':'INPUT_LIMIT','detail':'Heuristic JSON exceeds 650KB'}
    try:
        return heuristic_execute(json.loads(heuristic_json))
    except (HeuristicContractError,TypeError,ValueError,json.JSONDecodeError) as exc:
        return {'error':'INVALID_INPUT','detail':str(exc)}


@app.tool()
def vibecode_multimodel_execute(multimodel_json:str)->dict:
    """Execute typed cross-representation tests, not source code or formal proof.

    Input is an explicit model/bridge/probe JSON contract documented in
    references/cross-representation-execution.md. Requires separately hosted
    MCP server; adding this function does not deploy the server.
    """
    if len(multimodel_json.encode('utf-8')) > 180_000:
        return {'error':'INPUT_LIMIT','detail':'Multimodel JSON exceeds 180KB'}
    try:
        return multimodel_execute(json.loads(multimodel_json))
    except (MultiModelInputError,TypeError,ValueError,json.JSONDecodeError) as exc:
        return {'error':'INVALID_INPUT','detail':str(exc)}

@app.tool()
def vibecode_dispatch_execute(dispatch_json: str)->dict:
    """Bounded Mahajan-informed Python dispatch loop and optional AREX metadata.

    Always read-only. No external commands, patch writes, remote donor execution,
    or general theorem/behavior certification.
    """
    if len(dispatch_json.encode('utf-8')) > 180_000:
        return {'error':'INPUT_LIMIT','detail':'Dispatch JSON exceeds 180KB'}
    try:
        return dispatch_heuristics(json.loads(dispatch_json))
    except (DispatchInputError,MultiModelInputError,TypeError,ValueError,json.JSONDecodeError) as exc:
        return {'error':'INVALID_INPUT','detail':str(exc)}



@app.tool()
def vibecode_autopatcher_capabilities()->dict:
    """Describe bounded v0.8 canary source; NEVER grant authority or run patches."""
    return {'patch_core':autopatch_capabilities(),'job_control':control_capabilities(),
            'remote_mutation_tool_exposed':False}

if __name__=='__main__':
    # Local-only by default. Cloud connection needs a separately secured deployment.
    app.run(transport='streamable-http',host='127.0.0.1',port=8765,json_response=True)
