#!/usr/bin/env python
# coding: utf-8


import sublime
import sublime_plugin

import datetime
from typing import (
    Union
)


class Clock:

    CLOCK_ID: str = '00_clock'
    text: str = ''

    running: bool = False

    @classmethod
    def start(cls) -> None:
        cls.running: bool = True
        cls._tick()

    @classmethod
    def stop(cls) -> None:
        cls.running: bool = False
        for window in sublime.windows():
            try:
                v: Union[sublime.View, None] = window.active_view()
                if v is None: continue
                v.erase_status(cls.CLOCK_ID)
            except Exception:
                pass

    @classmethod
    def paint(cls, view: sublime.View) -> None:
        view.set_status(cls.CLOCK_ID, cls.text)

    @classmethod
    def _tick(cls) -> None:
        try:
            if cls.running:
                sublime.set_timeout(cls._tick, cls._update())
        except Exception as e:
            print('Clock: ', e)
            cls.stop()

    @classmethod
    def _update(cls) -> int:
        now = datetime.datetime.now()
        current_date: str = now.strftime('%y-%m-%d')
        current_calweek: str = now.strftime('%V').lstrip('0')
        current_time: str = now.strftime('%H:%M')
        cls.text: str = f'{current_date} (CW{current_calweek}) {current_time}'
        for window in sublime.windows():
            try:
                v: Union[sublime.View, None] = window.active_view()
                if v is None: continue
                cls.paint(v)
            except Exception:
                pass
        return 1000 * (60 - now.second)


class EventListener(sublime_plugin.EventListener):
    def on_activated_async(self, view: sublime.View) -> None:
        # Redraw in case the view belongs to a new window.
        Clock.paint(view)


def plugin_loaded() -> None:
    Clock.start()


def plugin_unloaded() -> None:
    Clock.stop()
