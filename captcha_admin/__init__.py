VERSION = (0, 1, 0, 'rc', 1)

__author__ = u'Daniel Barreto'


__license__ = u'MIT'
__maintainer__ = u'Daniel Barreto'
__email__ = 'daniel.barreto.n@gmail.com'
__status__ = 'Beta'

def get_version(version=VERSION):
    "Returns a PEP 386-compliant version number from VERSION."
    if version is None:
        return '0.0'
    else:
        assert len(version) == 5
        assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return str(main + sub)

from django.contrib import admin
from django.contrib.admin import autodiscover
from .sites import AdminSite
site = AdminSite()
admin.site = site
