# ADP C2 Isolated Sandbox

This repository is an isolated, non-trading test target for project-portability validation.
No broker API, production credentials, Issuer, account, order, or scheduler access.

The bootstrap contains *no Codex-generated implementation*. It only installs a protected
Python test fixture and a self-test CI workflow. Subsequent Codex development requires a
separately authorized Project Adapter Writer, isolated identity, and new immutable baseline.
