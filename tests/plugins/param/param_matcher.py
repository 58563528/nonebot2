from typing import Any, TypeVar, Union

from nonebot.adapters import Event
from nonebot.matcher import Matcher
from nonebot.params import (
    LastReceived,
    PausePromptResult,
    Received,
    ReceivePromptResult,
)


async def matcher(m: Matcher) -> Matcher:
    return m


async def postpone_matcher(m: "Matcher") -> Matcher:
    return m


async def legacy_matcher(matcher):
    return matcher


async def not_legacy_matcher(matcher: int): ...


class FooMatcher(Matcher): ...


async def sub_matcher(m: FooMatcher) -> FooMatcher:
    return m


class BarMatcher(Matcher): ...


async def union_matcher(
    m: Union[FooMatcher, BarMatcher],
) -> Union[FooMatcher, BarMatcher]:
    return m


M = TypeVar("M", bound=Matcher)


async def generic_matcher(m: M) -> M:
    return m


CM = TypeVar("CM", Matcher, None)


async def generic_matcher_none(m: CM) -> CM:
    return m


async def not_matcher(m: Union[int, Matcher]): ...


async def receive(e: Event = Received("test")) -> Event:
    return e


async def last_receive(e: Event = LastReceived()) -> Event:
    return e


async def receive_prompt_result(result: Any = ReceivePromptResult("test")) -> Any:
    return result


async def pause_prompt_result(result: Any = PausePromptResult()) -> Any:
    return result
