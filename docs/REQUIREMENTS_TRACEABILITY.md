# Requirements Traceability

`hardware/requirements.csv` is the compact requirements-to-verification matrix for the project. Each requirement has:

- a stable ID
- category and requirement statement
- intended verification method
- current evidence state
- the file or procedure that owns the evidence

The status vocabulary intentionally distinguishes **modeled/contract/policy evidence** from **hardware evidence**. A calculation can verify that a selected resistor mathematically produces the intended reference current, but it cannot prove the assembled board regulates at that value or meets thermal limits.

Run:

```bash
python tools/requirements_lint.py
```

When hardware evidence is produced, add a dated validation record and only change a requirement to `verified-by-hardware` when that record directly supports it.
