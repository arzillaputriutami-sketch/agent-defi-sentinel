import pytest

from backend.app import app


pytestmark = pytest.mark.skipif(app is None, reason='FastAPI not installed')


def test_fastapi_routes_registered():
    paths = {route.path for route in app.routes}
    assert {'/health', '/scenarios', '/analyze', '/demo-report'} <= paths


def test_health_handler_contract():
    route = next(route for route in app.routes if route.path == '/health')
    payload = route.endpoint()
    assert payload['status'] == 'ok'
    assert payload['project'] == 'DeFi Sentinel Swarm'
    assert payload['agents'] == 5
