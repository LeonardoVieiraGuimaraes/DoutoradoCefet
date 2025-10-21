from __future__ import annotations

import sys


def main() -> None:
    """CLI simples para validar o ambiente."""
    py = ".".join(map(str, sys.version_info[:3]))
    print(f"TeoriaGrafos — ambiente Python {py} pronto.")


if __name__ == "__main__":  # pragma: no cover
    main()
