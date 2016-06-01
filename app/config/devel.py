#!/usr/bin/env python
# coding=utf-8

"""Configuration on dev mode."""


class DevelConfig(object):
    """Configuration for development."""

    BUGTRACKER = "https://github.com/hiroaki-yamamoto/hysoftware.net"
    # This is just to avoid doggy check
    SECRET_KEY = (lambda: (
        "iMP\Xe(-uFO>&Acjg89fgqsUYgcS79fxUwji2R6b5%79f&QQ1H"
        "F14X0&t49oI8074SrAVyW5Cd3Ecsy55B1s9GpwzCYR59O<eV2p"
        "3A{g(1ac1mGX?sK2D6g4!G35Ucr[8qZMU0$gnYnU9eJB3XS&4I"
        "C5\9jhR8U=P0Tkr0s9!T43>62W9uo2Ahh81Lh1iqN9e1NZE30t")
    )()
    DEBUG = True
    DEBUG_TB_PANELS = [
        "flask.ext.debugtoolbar.panels.versions.VersionDebugPanel",
        "flask.ext.debugtoolbar.panels.timer.TimerDebugPanel",
        "flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel",
        "flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
        "flask.ext.debugtoolbar.panels.config_vars.ConfigVarsDebugPanel",
        "flask.ext.debugtoolbar.panels.template.TemplateDebugPanel",
        "flask.ext.debugtoolbar.panels.logger.LoggingPanel",
        "flask.ext.debugtoolbar.panels.route_list.RouteListDebugPanel",
        "flask.ext.debugtoolbar.panels.profiler.ProfilerDebugPanel",
        "flask.ext.mongoengine.panels.MongoDebugPanel"
    ]
    MONGODB_SETTINGS = {"host": "mongodb://localhost/hysoft"}
    WTF_CSRF_METHODS = ["POST", "PUT", "PATCH", "DELETE"]
    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = "6Lc2dSETAAAAAI-VoBJQwjoCS88gmoNhXpcT-Pht"
    RECAPTCHA_PRIVATE_KEY = "6Lc2dSETAAAAAEl0AHy6OmYZhY7qifnE_04G9az4"
