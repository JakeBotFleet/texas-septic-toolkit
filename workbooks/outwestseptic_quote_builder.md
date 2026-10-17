# Out West Septic — Quote Builder Workbook Spec

**Out West Septic — outwestseptic.com**
**TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX**
**Owner: James "Tanner" Coupland | 940.452.0598**
**Serving Palo Pinto County & Rural North Texas**

Build spec for `outwestseptic_quote_builder.xlsm`. The quote builder is the print-ready handoff from the site assessment to the homeowner. It generates a one-page quote with line-item costs, terms, and Out West Septic branding.

## Sheet 1 — Quote (single page print)

| Cell | Label |
|------|-------|
| B2 | OUT WEST SEPTIC |
| B3 | Quote |
| B4 | TCEQ OSSF Installer I — License OS0041298 |
| B5 | outwestseptic.com  •  940.452.0598 |
| B7 | Customer |
| D7 | (input — pulled from Site Assessment) |
| B8 | Job site |
| D8 | (input) |
| B9 | Quote # |
| D9 | (auto — `=TEXT(TODAY(),"yy")&"-"&TEXT(ROW(),"000")`) |
| B10 | Issue date |
| D10 | (auto — `=TODAY()`) |
| B11 | Valid through |
| D11 | (formula — `=D10+30`) |

## Sheet 2 — Line Items

| Cell | Category | Item | Qty | Unit | Unit Cost | Subtotal |
|------|----------|------|-----|------|-----------|----------|
| B2 | Site Prep | Clearing (per acre) | 1 | acre | input | formula |
| B3 | Site Prep | Excavation (per cubic yard) | input | cty | input | formula |
| B4 | Site Prep | Fill/compaction | input | load | input | formula |
| B5 | Site Prep | Building pad prep | 1 | each | input | formula |
| B7 | Tank | Tank (gallons) | 1 | tank | input | formula |
| B8 | Tank | Risers + lids | input | pair | input | formula |
| B9 | Tank | Concrete/antifloat collar | 1 | each | input | formula |
| B10 | Tank | Filter | 1 | each | input | formula |
| B12 | Drainfield | Trench excavation (per foot) | input | ft | input | formula |
| B13 | Drainfield | Gravel | input | cty | input | formula |
| B14 | Drainfield | Pipe | input | ft | input | formula |
| B15 | Drainfield | Fabric | input | roll | input | formula |
| B16 | Drainfield | Distribution box | 1 | each | input | formula |
| B17 | Drainfield | Lateral install labor | input | ft | input | formula |
| B18 | Drainfield | Inspection ports | input | each | input | formula |
| B20 | Permitting | TCEQ OSSF permit fee | 1 | each | input | input |
| B21 | Permitting | DR fee (county) | 1 | each | input | input |
| B22 | Permitting | Perc test | 1 | each | input | input |
| B24 | Misc | Haul-off | input | load | input | formula |
| B25 | Misc | Rock adder | input | cty | input | formula |
| B26 | Misc | Pump truck utility (referred) | input | each | input | formula |
| B27 | Misc | Restoration (topsoil, seed) | 1 | each | input | formula |

**Subtotal (B29):** `=SUM(F2:F27)`

**Sales tax (B30):** `=B29*0.0825` (default Texas sales tax — editable)

**Grand total (B31):** `=B29+B30`

## Sheet 3 — Terms

| Cell | Label |
|------|-------|
| B2 | Quote valid for 30 days from issue. |
| B3 | 50% deposit due at signing; balance due on completion. |
| B4 | Permit fees paid separately as incurred. |
| B5 | Rock encountered during excavation is billed at the rock adder rate per cubic yard. |
| B6 | Out West Septic installs conventional gravity septic systems only. Aerobic systems are referred. |
| B7 | Out West Septic does not run a pump truck — pumping is the homeowner's responsibility, scheduled per the maintenance guide. |
| B8 | Workmanship warranty: 1 year on install labor; manufacturer warranties pass through on components. |
| B9 | Payment methods: check, cash, ACH. |

## Sheet 4 — Print Header & Footer

- Header: Out West Septic • TCEQ OSSF Installer I OS0041298 • outwestseptic.com • 940.452.0598
- Footer: Serving Palo Pinto County & Rural North Texas • Lone Camp, TX
- Page numbers: yes

## Branding

- Title color: Out West Septic teal `#007787`
- Accents: orange `#cc5500`
- Quote letterhead per cell B2-B5

## Print settings

- Letter, portrait, fit to 1 page wide
- Show gridlines: off
- Print area: A1:G35 (one-page quote) plus optional second sheet for line-item detail if requested

## Macro stubs (optional)

```vba
Sub GeneratePDF()
    Dim fname As String
    fname = ThisWorkbook.Path & Application.PathSeparator & _
            "OutWestSeptic_Quote_" & Range("D7").Value & "_" & _
            Format(Range("D10").Value, "yyyymmdd") & ".pdf"
    Sheets("Quote").ExportAsFixedFormat Type:=xlTypePDF, Filename:=fname
End Sub

Sub EmailCopy()
    ' Opens default mail client with the quote attached.
    Dim fname As String
    GeneratePDF
    fname = ThisWorkbook.Path & Application.PathSeparator & _
            "OutWestSeptic_Quote_" & Range("D7").Value & "_" & _
            Format(Range("D10").Value, "yyyymmdd") & ".pdf"
    Shell "explorer.exe """ & fname & """", vbNormalFocus
End Sub
```

---

*Out West Septic — outwestseptic.com — 940.452.0598 — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX*
*Serving Palo Pinto County, Mineral Wells, Graford, Possum Kingdom Lake, and rural North Texas*