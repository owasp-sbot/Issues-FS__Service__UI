# # ═══════════════════════════════════════════════════════════════════════════════
# # test_Issues_FS__Service_UI__Console - Playwright UI tests for Issues Tracker
# # Tests the web console interface with screenshot evidence capture
# # ═══════════════════════════════════════════════════════════════════════════════
#
# import pytest
# from pathlib                                                                     import Path
# from datetime                                                                    import datetime
# from playwright.sync_api                                                         import Page, expect
# from tests.ui.Issues_FS__Service_UI__Test_Objs                                   import setup__issues_fs_service_ui__test_objs
#
# # ═══════════════════════════════════════════════════════════════════════════════
# # Test Configuration
# # ═══════════════════════════════════════════════════════════════════════════════
#
# CONSOLE_PATH = '/console'
#
#
# class Test_Issues_FS__Service_UI__Console:                                       # UI tests for Issues Tracker console
#
#     @pytest.fixture(autouse=True)
#     def setup(self, page: Page):                                                 # Setup: configure page and auth
#         self.page       = page
#         self.test_objs  = setup__issues_fs_service_ui__test_objs()
#         self.base_url   = self.test_objs.base_url
#
#         page.set_default_timeout(30000)                                          # 30 second timeout
#
#         self.authenticate(page)                                                  # Set auth cookie before tests
#
#     def authenticate(self, page: Page):                                          # Set auth cookie via API
#         api_key_name  = self.test_objs.api_key_name
#         api_key_value = self.test_objs.api_key_value
#
#         page.goto(f"{self.base_url}/auth/set-cookie-form")                       # Navigate to cookie form
#
#         page.fill('input[name="api_key_name"]' , api_key_name )                  # Fill auth form
#         page.fill('input[name="api_key_value"]', api_key_value)
#         page.click('button[type="submit"]')                                      # Submit to set cookie
#
#         page.wait_for_load_state('networkidle')                                  # Wait for redirect
#
#     def capture_screenshot(self, name: str) -> str:                              # Capture screenshot with timestamp
#         timestamp       = datetime.now().strftime('%Y%m%d_%H%M%S')
#         filename        = f"{timestamp}__{name}.png"
#         screenshots_dir = Path(self.test_objs.screenshots_path)
#         filepath        = screenshots_dir / filename
#
#         self.page.screenshot(path=str(filepath), full_page=True)
#
#         return str(filepath)
#
#     # ═══════════════════════════════════════════════════════════════════════════════
#     # Console Loading Tests
#     # ═══════════════════════════════════════════════════════════════════════════════
#
#     def test__console__loads(self):                                              # Test console UI loads successfully
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         screenshot_path = self.capture_screenshot('console_loaded')              # Evidence: console loaded
#
#         assert self.page.title() != ''                                           # Page has title
#         assert 'Issues' in self.page.content() or 'Tracker' in self.page.content()
#
#         print(f"Screenshot saved: {screenshot_path}")                            # Log screenshot path
#
#     def test__console__shows_header(self):                                       # Test header elements visible
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         header = self.page.locator('text=Issues Tracker')                        # Find header text
#         expect(header.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_header')                                # Evidence: header visible
#
#     def test__console__shows_version_selector(self):                             # Test version selector present
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         version_text = self.page.locator('text=Version')                         # Find version selector
#         expect(version_text.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_version_selector')                      # Evidence: version visible
#
#     # ═══════════════════════════════════════════════════════════════════════════════
#     # Navigation Tests
#     # ═══════════════════════════════════════════════════════════════════════════════
#
#     def test__console__root_button_exists(self):                                 # Test Root button present
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         root_button = self.page.locator('text=Root')                             # Find Root button
#         expect(root_button.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_root_button')                           # Evidence: root button
#
#     def test__console__api_docs_button_exists(self):                             # Test API Docs button present
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         api_docs_button = self.page.locator('text=API Docs')                     # Find API Docs button
#         expect(api_docs_button.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_api_docs_button')                       # Evidence: api docs button
#
#     def test__console__new_button_exists(self):                                  # Test + New button present
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         new_button = self.page.locator('text=New')                               # Find New button
#         expect(new_button.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_new_button')                            # Evidence: new button
#
#     # ═══════════════════════════════════════════════════════════════════════════════
#     # Detail Panel Tests
#     # ═══════════════════════════════════════════════════════════════════════════════
#
#     def test__console__shows_details_panel(self):                                # Test details panel visible
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         details_panel = self.page.locator('text=DETAILS')                        # Find DETAILS header
#         expect(details_panel.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_details_panel')                         # Evidence: details panel
#
#     def test__console__shows_messages_panel(self):                               # Test messages panel visible
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         messages_panel = self.page.locator('text=Messages')                      # Find Messages header
#         expect(messages_panel.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_messages_panel')                        # Evidence: messages panel
#
#     # ═══════════════════════════════════════════════════════════════════════════════
#     # Node Detail Tests
#     # ═══════════════════════════════════════════════════════════════════════════════
#
#     def test__console__shows_child_issues_section(self):                         # Test child issues section
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         child_issues = self.page.locator('text=Child Issues')                    # Find Child Issues section
#         expect(child_issues.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_child_issues')                          # Evidence: child issues
#
#     def test__console__shows_comments_section(self):                             # Test comments section
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         comments = self.page.locator('text=Comments')                            # Find Comments section
#         expect(comments.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_comments')                              # Evidence: comments section
#
#     def test__console__shows_relationships_section(self):                        # Test relationships section
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         relationships = self.page.locator('text=Relationships')                  # Find Relationships section
#         expect(relationships.first).to_be_visible(timeout=10000)
#
#         self.capture_screenshot('console_relationships')                         # Evidence: relationships
#
#     # ═══════════════════════════════════════════════════════════════════════════════
#     # Full Page Screenshot Test
#     # ═══════════════════════════════════════════════════════════════════════════════
#
#     def test__console__full_page_screenshot(self):                               # Capture full page as evidence
#         self.page.goto(f"{self.base_url}{CONSOLE_PATH}")
#         self.page.wait_for_load_state('networkidle')
#
#         self.page.wait_for_timeout(2000)                                         # Extra wait for dynamic content
#
#         screenshot_path = self.capture_screenshot('console_full_page')           # Full page evidence
#
#         assert Path(screenshot_path).exists()                                    # Verify screenshot created
#         assert Path(screenshot_path).stat().st_size > 0                          # Verify non-empty file
#
#         print(f"Full page screenshot: {screenshot_path}")
