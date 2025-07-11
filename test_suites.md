# Test Suite Strategy

This framework supports modular test execution using Behave tags.

## Tags & Suites

| Tag         | Purpose                                 |
|-------------|------------------------------------------|
| `@smoke`     | Quick connectivity checks (1–2 critical scenarios) |
| `@sanity`    | Light functional validation of happy paths |
| `@regression`| Full functional suite covering major flows |
| `@negative`  | Negative/edge-case testing scenarios |

## How to Run

Run specific suites via CLI:

```bash
behave -t @smoke
behave -t @regression
behave -t @sanity
