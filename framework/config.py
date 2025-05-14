import os

DISPLAY_VISIBLE = False
DISPLAY_WIDTH = 2560
DISPLAY_HEIGHT = 1440
WAIT_TIMEOUT = 30
SHADOW_WAIT_TIMEOUT = 15

MAX_FIX_ATTEMPTS_PER_FAILURE_POINT = 5

DEFAULT_CHROME_OPTION_ARGS = [
        "--enable-automation",
        "--disable-field-trial-config",
        # "--disable-background-networking",
        "--enable-features=NetworkService,NetworkServiceInProcess",
        "--disable-features="
        + (
            "ImprovedCookieControls"
            ",LazyFrameLoading"
            ",GlobalMediaControls"
            ",DestroyProfileOnBrowserClose"
            ",MediaRouter"
            ",DialMediaRouteProvider"
            ",AcceptCHFrame"
            ",AutoExpandDetailsElement"
            ",CertificateTransparencyComponentUpdater"
            ",AvoidUnnecessaryBeforeUnloadCheckSync"
            ",Translate"
        ),
        "--disable-background-timer-throttling",
        "--disable-backgrounding-occluded-windows",
        "--disable-back-forward-cache",
        "--disable-breakpad",
        "--disable-client-side-phishing-detection",
        "--disable-component-extensions-with-background-pages",
        "--disable-component-update",
        "--no-default-browser-check",
        "--disable-default-apps",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-features",
        "--allow-pre-commit-input",
        "--disable-hang-monitor",
        "--disable-ipc-flooding-protection",
        "--disable-popup-blocking",
        "--disable-prompt-on-repost",
        "--disable-renderer-backgrounding",
        "--disable-sync",
        "--force-color-profile",
        "--metrics-recording-only",
        "--no-first-run",
        "--password-store",
        "--use-mock-keychain",
        "--no-service-autorun",
        "--export-tagged-pdf",
        "--no_sandbox",
        "--ignore-certificate-errors",
        "--disable-blink-features=AutomationControlled",
        "--incognito",
        "--disable-extensions",
        "--disable-infobars",
        "--start-maximized",
        "--disable-dev-shm-usage",
        "--window-size=1920,1080"
    ]

download_path = 'testoutput'
absolute_download_path = os.path.abspath(download_path)
CHROME_PREFS = {
    "download.default_directory": absolute_download_path,  # Set the download path
    "download.prompt_for_download": False,  # Don't ask for download location
    "download.directory_upgrade": True,  # Automatically download to the specified directory
    "safebrowsing.enabled": True,  # Allow downloading without safety check
    "profile.default_content_settings.popups": 0,  # Disable popups
    "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,  # Allow automatic downloads
    "download.extensions_to_open": "",  # Leave empty to avoid automatically opening files after download
    "download.restrictions": 0,  # To allow all downloads
    # no effective way to disable the chrome save as dislog now......
    'browser.enabled_labs_experiments': ['download-bubble@2', 'download-bubble-v2@2'],

    "profile.default_content_setting_values.cookies": 1,  # 1 = Allow, 2 = Block
    "profile.default_content_setting_values.images": 1,
    "profile.default_content_setting_values.javascript": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.automatic_downloads": 1,
    "profile.default_content_setting_values.mixed_script": 1,
    "profile.default_content_setting_values.media_stream": 1,
    "profile.default_content_setting_values.stylesheets": 1,
    "profile.managed_default_content_settings": {
        "cookies": 1,  # Allow cookies
        "images": 1,
        "javascript": 1,
        "geolocation": 1,
        "automatic_downloads": 1,
        "mixed_script": 1,
        "media_stream": 1,
        "stylesheets": 1
    }
}
