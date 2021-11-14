#!/usr/bin/env python
# coding: utf-8


from __future__ import annotations

import sublime
import sublime_plugin


class SideBarEventListener(sublime_plugin.EventListener):

    def on_new_window(self, window: sublime.Window) -> None:
        if not window.is_sidebar_visible():
            window.set_sidebar_visible(True)

    # def on_load_project(self, window):
    #     if not window.is_sidebar_visible():
    #         window.set_sidebar_visible(True)

    on_load_project = on_new_window
