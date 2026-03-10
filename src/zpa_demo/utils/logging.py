import logging
import sys
from pathlib import Path
from typing import List, Optional

import colorlog


def configure_logging(
    debug: bool = False,
    extra_loggers: Optional[List[logging.Logger]] = None,
    filename: Optional[str] = None,
) -> None:
    """Configure logging for a Jupyter / VS Code notebook."""

    level = logging.DEBUG if debug else logging.INFO

    # 1) Root logger
    root = logging.getLogger()
    root.setLevel(level)

    # Clear ANY existing handlers (ipykernel, etc.)
    root.handlers.clear()

    # 2) Stream handler to STDOUT (so it shows as normal cell output)
    sh = colorlog.StreamHandler(stream=sys.stdout)
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s%(reset)s | %(asctime)s | %(name)s | %(message)s"
    )
    sh.setFormatter(formatter)
    root.addHandler(sh)

    # 3) Optional file handler
    if filename is not None:
        fh = logging.FileHandler(filename, encoding="utf-8")
        fh.setFormatter(
            logging.Formatter("%(levelname)s | %(asctime)s | %(name)s | %(message)s")
        )
        root.addHandler(fh)

    # 4) Optional extra named loggers - they should propagate to root
    if extra_loggers:
        if not isinstance(extra_loggers, list):
            extra_loggers = [extra_loggers]
        for lg in extra_loggers:
            lg.setLevel(level)
            lg.propagate = True  # bubble up to root
            lg.handlers.clear()  # no own handlers

    # Optional: route warnings through logging
    logging.captureWarnings(True)


def _get_base_logger() -> logging.Logger:
    return logging.getLogger(_get_package_name())


def _get_package_name() -> str:
    name, _ = __name__.split(".", maxsplit=1)
    return name


def format_log_kv(**fields: object) -> str:
    """Format key/value fields for standardized log messages.

    Keys are emitted in sorted order for deterministic, scan-friendly output.
    """
    out = []
    for key in sorted(fields):
        value = fields[key]
        if isinstance(value, BaseException):
            value = str(value)
        if isinstance(value, Path):
            value = str(value)
        if isinstance(value, bool):
            value = str(value).lower()
        if value is None:
            rendered = "null"
        else:
            rendered = str(value)
            if (not rendered) or any(ch.isspace() for ch in rendered):
                rendered = f'"{rendered}"'
        out.append(f"{key}={rendered}")
    return " ".join(out)


def log_event(
    logger: logging.Logger,
    phase: str,
    source: str,
    event: str,
    status: str,
    **fields: object,
) -> None:
    """Emit a normalized event log line.

    Message shape:
        [<phase>|<source>] event=<event> status=<status> key=value ...
    """
    valid_status = {"start", "ok", "fail"}
    if status not in valid_status:
        raise ValueError(f"Unsupported log status: {status}")

    level = fields.pop("level", None)
    exc_info = bool(fields.pop("exc_info", False))
    if "error" in fields and isinstance(fields["error"], BaseException):
        fields["error"] = str(fields["error"])

    payload = format_log_kv(**fields)
    msg = f"[{phase}|{source}] event={event} status={status}"
    if payload:
        msg = f"{msg} {payload}"

    if exc_info:
        logger.exception(msg)
        return None

    if not isinstance(level, int):
        level = logging.ERROR if status == "fail" else logging.INFO
    logger.log(level, msg)
    return None
