import json
import subprocess
import sys

from cli import report_to_markdown, run


def test_cli_single_json_is_parseable():
    payload = json.loads(run(['--scenario', 'oracle feed divergence']))
    assert payload['scenario'] == 'oracle feed divergence'
    assert payload['trace_id']


def test_cli_all_json_covers_all_scenarios():
    payload = json.loads(run(['--all']))
    assert len(payload) == 3
    assert {item['scenario'] for item in payload} == {
        'stablecoin depeg pressure',
        'DEX pool depth collapse',
        'oracle feed divergence',
    }


def test_cli_signal_file_changes_trace(tmp_path):
    signal_file = tmp_path / 'signals.json'
    signal_file.write_text('{"scenario":"stablecoin depeg pressure","signals":{"pool_depth_change":999}}')
    baseline = json.loads(run(['--scenario', 'stablecoin depeg pressure']))
    custom = json.loads(run(['--signals', str(signal_file)]))
    assert custom['trace_id'] != baseline['trace_id']
    assert custom['scenario'] == 'stablecoin depeg pressure'
    assert custom['findings'][0]['observation'].startswith('pool_depth_change is reading 999.00')


def test_markdown_export_has_operator_sections():
    payload = json.loads(run(['--scenario', 'DEX pool depth collapse']))
    md = report_to_markdown(payload)
    assert '# DeFi Sentinel Swarm' in md
    assert '## Agent findings' in md
    assert '## Next actions' in md


def test_real_cli_module_executes():
    proc = subprocess.run(
        [sys.executable, 'cli.py', '--scenario', 'oracle feed divergence'],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(proc.stdout)['scenario'] == 'oracle feed divergence'
