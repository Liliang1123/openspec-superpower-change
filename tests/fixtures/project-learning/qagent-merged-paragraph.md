# Merged paragraph learning candidate

- symptom: a whole-row note disappears after table conversion
- prior assumption: every colspan row is tabular data
- correction evidence: repeated human correction plus independent Review
- generalized semantic invariant: a merged paragraph row is a table-level annotation, not tabular data
- engineering invariant: normalization must preserve annotations outside rectangular cell expansion
- mechanical regression: an edge fixture must preserve leading and trailing merged paragraph rows
