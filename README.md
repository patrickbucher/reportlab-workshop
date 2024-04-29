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
    - unit: "point" (1/72 of an inch)
- see `hello_world.py`
    - Canvas constructor takes various arguments, e.g. `pageCompression=1` (for
      production output)
- two kinds of commands: drawing or changing state (fill color, font type, ...)
- draw operations of the Canvas object
    - lines/shapes
        - line/lines
        - grid
        - bezier
        - arc
        - rect
        - ellipse
        - wedge
        - circle
        - roundRect
    - strings
        - drawString
        - drawRightString
        - drawCenteredString
    - text
        - beginText; drawText
    - path
        - drawPath
        - clipPath
- use PIL for images
    - [Pillow](https://pypi.org/project/pillow/) (PIL fork)
    - drawImage
    - drawInlineImage (Bitmaps; inefficient)
- ending a page (starting a new one with the next drawing operation)
    - showPage
- fonts
    - setFont(name, size)
- geometry
    - setPageSize
- state
    - saveState: mark current state for later restoration
    - restoreState: restores the last saved state **saved on the same page**
- misc
    - setAuthor
    - addOutlineEntry
    - setTitle
    - setSubject
- text object
    - setTextOrigin
    - moveCursor
    - setFont
    - textOut
    - textLine

# Platypus: Page Layout and Typography Using Scripts

[Source](https://docs.reportlab.com/reportlab/userguide/ch5_platypus/)

- paragraph styles
- page templates
- `DocTemplates`: outermost document container
    - contains 1+ `PageTemplates`: page layouts
        - contains 1+ `Frames`: regions of pages (text, graphics)
            - `Flowables`: text/graphic to be "flowed into" a frame
