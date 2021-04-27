"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.requestCounter = 0
        self.responseCounter = 0

    def request(self, flow):
        self.requestCounter = self.requestCounter + 1
        ctx.log.info("We've seen %d request flows" % self.requestCounter)

    def response(self, flow):
        self.responseCounter = self.responseCounter + 1
        ctx.log.info("We've seen %d response flows" % self.responseCounter)

addons = [
    Counter()
]
