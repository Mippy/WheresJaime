# Tweepy
# Copyright 2010-2019 Joshua Roesslein
# See LICENSE for details.

from datetime import datetime
from email.utils import parsedate

from libs import six


def parse_datetime(string):
  return datetime(*(parsedate(string)[:6]))


def parse_html_value(html):
  return html[html.find('>') + 1:html.rfind('<')]


def parse_a_href(atag):
  start = atag.find('"') + 1
  end = atag.find('"', start)
  return atag[start:end]


def convert_to_utf8_str(arg):
  # written by Michael Norton (http://docondev.blogspot.com/)
  if isinstance(arg, six.text_type):
    arg = arg.encode('utf-8')
  elif not isinstance(arg, bytes):
    arg = six.text_type(arg).encode('utf-8')
  return arg


def list_to_csv(item_list):
  if item_list:
    return ','.join([str(i) for i in item_list])