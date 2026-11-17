# Development instructions

- This is a fresh public project. Do not import previous projects or private strategies.
- Python 3.11+; use small tested changes and standard-library code where practical.
- Run `PYTHONPATH=src python -m unittest discover -s tests -v` before commits.
- Current milestone is simulation only. Do not add broker credentials or submit orders.
- Treat strategies/plugins as trusted code, not sandboxed input.
- Never copy private strategy logic, prompts, parameters, real account data, logs or backtests here.
- Public tests must use synthetic fixtures and run independently of private repositories.
- Inspect the complete staged diff before public publication. Ignore files are not access controls.
