# Import necessary ZAP libraries or modules
from zapv2 import ZAPv2

# Configure ZAP spider options
spider_options = {
    'maxChildren': 5
}

# Initialize ZAP API client
zap = ZAPv2()

# Execute spider scan with configured options
zap.spider.scan_as_user('zap_user', spider_options)
