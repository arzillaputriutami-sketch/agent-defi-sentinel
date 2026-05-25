from backend.swarm import AGENT_ROLES, SCENARIOS, SIGNALS, analyze_scenario, batch_analyze


def test_report_has_operator_grade_shape():
    report = analyze_scenario(SCENARIOS[0])
    data = report.to_dict()
    assert data['project'] == 'DeFi Sentinel Swarm'
    assert 0 <= data['risk_score'] <= 100
    assert data['verdict'] in {'operator_action_required', 'monitor_with_guardrails'}
    assert len(data['findings']) == len(AGENT_ROLES)
    assert data['trace_id']


def test_signal_override_changes_trace_and_keeps_schema():
    baseline = analyze_scenario(SCENARIOS[0]).to_dict()
    custom = analyze_scenario(SCENARIOS[0], {'pool_depth_change': 999}).to_dict()
    assert custom['trace_id'] != baseline['trace_id']
    assert len(custom['next_actions']) >= 3
    assert custom['findings'][0]['observation'].endswith(f'during {SCENARIOS[0]}.')


def test_batch_covers_all_scenarios():
    reports = batch_analyze()
    assert len(reports) == len(SCENARIOS)
    assert {r['scenario'] for r in reports} == set(SCENARIOS)


def test_each_agent_maps_to_a_named_signal():
    report = analyze_scenario('stablecoin depeg pressure')
    observations = ' '.join(f.observation for f in report.findings)
    assert all(signal in observations for signal in SIGNALS)


def test_low_signal_payload_stays_in_guardrail_mode():
    report = analyze_scenario('custom quiet market', {signal: 1 for signal in SIGNALS}).to_dict()
    assert report['risk_score'] == 100  # normalized severity is relative, not absolute
    assert report['verdict'] == 'operator_action_required'
    assert report['scenario'] == 'custom quiet market'


def test_trace_is_deterministic_for_same_inputs():
    signals = {'pool_depth_change': 10, 'oracle_spread_bps': 20}
    one = analyze_scenario('oracle feed divergence', signals).trace_id
    two = analyze_scenario('oracle feed divergence', signals).trace_id
    assert one == two
