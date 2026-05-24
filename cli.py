#!/usr/bin/env python3
"""Command-line demo runner for DeFi Sentinel Swarm."""
from __future__ import annotations
import argparse, json
from backend.swarm import SCENARIOS, analyze_scenario, batch_analyze

parser = argparse.ArgumentParser(description='DeFi Sentinel Swarm operator console')
parser.add_argument('--scenario', choices=SCENARIOS, help='Scenario to analyze')
parser.add_argument('--all', action='store_true', help='Run all built-in scenarios')
args = parser.parse_args()

payload = batch_analyze() if args.all else analyze_scenario(args.scenario).to_dict()
print(json.dumps(payload, indent=2))
