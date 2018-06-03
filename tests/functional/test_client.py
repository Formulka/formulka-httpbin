# -*- coding: utf-8 -*-
# Copyright (c) 2018 Petr Olah <djangoguru@gmail.com>
#
# this file is part of the project "Petr Olah HTTPBin Client" released under the "MIT" open-source license
import json
import httpretty

from formulka_httpbin import HttpBinClient


@httpretty.httprettified
def test_httpbinclient_post():
    ("HttpBinClient.post() should return a dict with deserialized JSON data")

    # Given that I fake a response from httpbin.org
    httpretty.register_uri(
        httpretty.POST,
        'https://httpbin.org/post',
        body=json.dumps({
            "this": "is",
            "a fake": "JSON response"
        })
    )

    # And an instance of HttpBinClient
    client = HttpBinClient()

    # When I call .post()
    result = client.post()

    # Then it should return a dict
    result.should.equal({
        "this": "is",
        "a fake": "JSON response",
    })
