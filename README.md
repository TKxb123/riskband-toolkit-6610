# Riskband Toolkit

Maintained reference implementation of the Product Safety Risk Banding (PSRB)
methodology used by incident triage pipelines. This package turns the two
1-5 supplier ratings into the standard A-D risk band.

## Usage

```python
from riskband import classify_band

band = classify_band(likelihood=5, severity=4)  # -> "A"
```

## Version

1.4.2 (see VERSION)

## Notes

The toolkit is dependency free and targets Python 3.9+. Band cut-offs are
defined in `riskband/classify.py` and covered by the regression tests in
`tests/`.
