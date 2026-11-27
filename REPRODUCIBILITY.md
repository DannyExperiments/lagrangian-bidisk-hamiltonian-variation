# Reproducing the release

From the repository root, use Python 3.11 or newer to run the standard-library checks.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

With Lean 4.30.0 already installed, run the partial algebra certificate.

    lean -DwarningAsError=true formal/Q1224Certificate.lean

The certificate proves three ring identities and two exact rational statements. The analytic proof is in the manuscript. See [the paper build](paper/BUILD.md), [the figure guide](visualization/README.md), and [the exact replay log](verification/logs/replay.txt).
