# reproduce

unexpected! adding `pylint: disable=invalid-name` on `b.py:8:0` does not help

```
$ pylint --load-plugins=pylint_django \
         --django-settings-module=pylint_test.settings \
         $(git ls-files "*.py" | grep -v "^bin/")
************* Module b
b.py:8:0: C0103: Attribute name "laLa" doesn't conform to snake_case naming style (invalid-name)
************* Module manage
manage.py:11:8: C0415: Import outside toplevel (django.core.management.execute_from_command_line) (import-outside-toplevel)
************* Module polls.admin
polls/admin.py:1:0: C0114: Missing module docstring (missing-module-docstring)
polls/admin.py:1:0: W0611: Unused admin imported from django.contrib (unused-import)
************* Module polls.apps
polls/apps.py:1:0: C0114: Missing module docstring (missing-module-docstring)
polls/apps.py:4:0: C0115: Missing class docstring (missing-class-docstring)
************* Module polls.models
polls/models.py:1:0: C0114: Missing module docstring (missing-module-docstring)
polls/models.py:1:0: W0611: Unused models imported from django.db (unused-import)
************* Module polls.tests
polls/tests.py:1:0: C0114: Missing module docstring (missing-module-docstring)
polls/tests.py:1:0: W0611: Unused TestCase imported from django.test (unused-import)
************* Module polls.urls
polls/urls.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module polls.views
polls/views.py:1:0: C0114: Missing module docstring (missing-module-docstring)
polls/views.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.97/10 (previous run: 7.97/10, +0.00)
```
