# Failure Modes and Design Responses

| Failure mode | Possible consequence | Design response | Validation |
|---|---|---|---|
| Reversed battery | device/board damage | reverse-polarity input stage | polarity test with current-limited source |
| Harness/input transient | VM overstress | local ceramic + optional bulk + application TVS | oscilloscope VM during start/stop/reversal |
| Motor stall | high current/heating | xISEN current regulation, fuse coordination | controlled stall/current-limit test |
| Output short | high fault current | internal OCP + source protection | lab-only fault test |
| Driver overheating | shutdown/reliability loss | PowerPAD, ground copper, thermal vias, current derating | dual-channel thermal test |
| MCU reset/floating controls | unintended motion | nSLEEP default-low behavior | reset/brownout test |
| Sense resistor open | current regulation lost/abnormal | critical-component selection and inspection | continuity + functional current-limit test |
| Sense resistor short | current limit raised | critical-component selection, footprint/assembly review | resistance verification |
| nFAULT not observed | hidden protection events | exposed header/test point and firmware logging | induce/reproduce controlled fault |
| Wrong motor connector order | reversed direction | silkscreen + software direction mapping | first-spin test with wheel/load safe |
