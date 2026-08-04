# contract-detector

Detects recurring contracts and subscriptions from any transaction stream, flags price increases, and reminds about cancellation windows.

Part of the [wealthdock](https://github.com/wealthdock) organization — see the [org profile](https://github.com/wealthdock/.github) for how the repos fit together.

## Development Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --all-extras
```

Run linting and type checking:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
```

Run the test suite:

```bash
uv run pytest
```

Run the CLI:

```bash
uv run contract-detector --version
```

## License

MIT — see [LICENSE](LICENSE).
