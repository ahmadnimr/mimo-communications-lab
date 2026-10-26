# Development conventions

## Mathematical conventions

- `lectures/` is the authoritative mathematical reference for implementing the Python library. Follow the manuscripts' system models, notation, dimensions, and energy normalization.
- Preserve manuscript equation labels where useful when referencing mathematical definitions in algorithm documentation and tests.
- Keep manuscripts `01`–`06` and shared definitions (`math_notation.tex`, `acronyms.tex`, and `preamble.tex`) directly in the flat `lectures/` directory, separate from the installable `mimolab` package.
- Do not modify, rewrite, or rename lecture manuscripts unless explicitly requested. Finalized replacements will be supplied separately.
- Follow the mathematical system models and notation of the MIMO Communications course.
- P2P channel matrices have shape `(Nr, Nt)`.
- MU uplink channel matrices have shape `(Nr, U)`, with one channel vector per column.
- Use `H`, `F`, `W`, `d`, `x`, and `y` where direct correspondence with mathematical notation improves readability.
- Clearly document the mathematical dimensions of all inputs and outputs.
- Use NumPy arrays and `complex128` for complex-valued signal processing.
- Distinguish transmit-symbol energy, total transmitted energy, and receiver-noise variance.
- For normalized precoding, follow the convention `R_d = E_d I` and `||F||_F² <= 1`.
- Complex Gaussian noise with variance `sigma2` must have `E[|v|²] = sigma2`.
- Explicitly distinguish matrix transpose, conjugate transpose, and complex conjugation.
- Prefer linear-system solvers over explicit matrix inversion.

## Programming conventions

- Prefer simple functions over classes unless classes provide a clear benefit.
- Use type hints and NumPy-style docstrings.
- Include mathematical definitions and assumptions in algorithm documentation.
- Use descriptive names for dimensions and physical parameters.
- Support reproducible random experiments through explicit NumPy random generators.
- Separate reusable algorithms from plotting and notebook presentation.
- Avoid hard-coded parameters associated with particular lecture examples.

## Testing conventions

- Use pytest.
- Validate numerical results against mathematical identities and analytical reference cases.
- Test array dimensions, numerical normalization, and complex-valued behavior.
- Use deterministic random seeds in tests.
- Prefer small, fast, reproducible tests.
- Do not add arbitrary numerical tolerances without justification.
