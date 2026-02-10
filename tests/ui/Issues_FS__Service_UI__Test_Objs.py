# # ═══════════════════════════════════════════════════════════════════════════════
# # Issues_FS__Service_UI__Test_Objs - Shared test objects for UI testing
# # Provides singleton test infrastructure for Playwright browser automation
# # ═══════════════════════════════════════════════════════════════════════════════
#
# import os
# from pathlib                                                                     import Path
# from osbot_utils.type_safe.Type_Safe                                             import Type_Safe
# from osbot_utils.utils.Env                                                       import load_dotenv
#
# # ═══════════════════════════════════════════════════════════════════════════════
# # Environment Configuration
# # ═══════════════════════════════════════════════════════════════════════════════
#
# ENV_FILE_PATH         = Path(__file__).parent.parent.parent / '.local-server.env'
# SCREENSHOTS_PATH      = Path(__file__).parent / 'screenshots'
# DEFAULT_PORT          = 10041
# DEFAULT_TIMEOUT       = 30000                                                    # 30 seconds
#
#
# class Issues_FS__Service_UI__Test_Objs(Type_Safe):                               # Shared test objects singleton
#     base_url         : str  = ''
#     api_key_name     : str  = ''
#     api_key_value    : str  = ''
#     screenshots_path : str  = ''
#     setup_completed  : bool = False
#
# issues_fs_service_ui_test_objs = Issues_FS__Service_UI__Test_Objs()              # Singleton instance
#
#
# def setup__issues_fs_service_ui__test_objs():                                    # Initialize test objects
#     with issues_fs_service_ui_test_objs as _:
#         if _.setup_completed is False:
#             load_dotenv(ENV_FILE_PATH)                                           # Load auth credentials
#
#             port               = os.getenv('ISSUES_FS__UI__PORT', str(DEFAULT_PORT))
#             _.base_url         = f'http://localhost:{port}'
#             _.api_key_name     = os.getenv('FAST_API__AUTH__API_KEY__NAME' , '')
#             _.api_key_value    = os.getenv('FAST_API__AUTH__API_KEY__VALUE', '')
#             _.screenshots_path = str(SCREENSHOTS_PATH)
#             _.setup_completed  = True
#
#             SCREENSHOTS_PATH.mkdir(parents=True, exist_ok=True)                  # Ensure screenshots dir exists
#
#     return issues_fs_service_ui_test_objs
