# ReportLab PDF Toolkit

- [Documentation](https://docs.reportlab.com/reportlab/userguide/ch1_intro/)
- [Package (PyPi)](https://pypi.org/project/reportlab/)

## Site Configuration

- See `reportlab/rl_settings.py` for defaults and variables, which can be
  overwritten (e.g. by `~/.reportlab_settings` or `RL_*` environment variables).
    - `TTFSearchPath`: directories queried for TTF files
    - `showBoundary`: draw boundary lines
    - `pageCompression`: compress PDF
    - `trustedHosts`: trusted image tag sources
    - `trustedSchemes`: trusted protocols (HTTPS?)
- See `reportlab/lib/pagesizes.py` for page sizes.

## Graphics and Text with `pdfgen`

[Source](https://docs.reportlab.com/reportlab/userguide/ch2_graphics/)

- lowest level interface for PDF creation
- works on canvas, `(0,0)` coordinates at **lower left corner** of the page
