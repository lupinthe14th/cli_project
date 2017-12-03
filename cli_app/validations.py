#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from schematics.models import Model
from schematics.types import EmailType
from schematics.types import DateType
from schematics.types import TimestampType

class PositionalArgs(Model):
    fromaddr = EmailType(required=True)
    toaddr = EmailType(required=True)
    datetime = DateType(required=True)
    datetime = TimestampType()

# vim fileencoding=utf-8
