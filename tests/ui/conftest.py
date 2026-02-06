# # ═══════════════════════════════════════════════════════════════════════════════
# # conftest.py - Pytest configuration and fixtures for UI tests
# # Configures Playwright browser for headless testing with screenshot capture
# # ═══════════════════════════════════════════════════════════════════════════════
#
# import pytest
#
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):                                  # Configure browser context
#     return {
#         **browser_context_args,
#         "viewport"           : {"width": 1920, "height": 1080},                  # Full HD resolution
#         "ignore_https_errors": True,                                             # Allow self-signed certs
#     }
#
#
# @pytest.fixture(scope="session")
# def browser_type_launch_args(browser_type_launch_args):                          # Configure browser launch
#     return {
#         **browser_type_launch_args,
#         "headless": True,                                                        # Run headless for CI/CD
#         "slow_mo" : 100,                                                         # Slow down for stability
#     }
