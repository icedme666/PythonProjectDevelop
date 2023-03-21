from apps.settings import *


#####################################
# Xml test runner
#####################################
TEST_RUNNER = "xmlrunner.extra.djangotestrunner.XMLTestRunner"
TEST_OUTPUT_DIR = "test_reports"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "jenkins.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
