```
REM Medical Expert System

RULE [appendecitis]
If [pain]="in stomach"
  Then [disease]="appendecitis"

RULE [pielonephritis]
If [pain]="in spine"
  Then [disease]="pielonephritis"

RULE [chronic appendecitis]
If [temperature]="normal" and [disease]="appendecitis" and [pain type]="weak"
  Then [diagnosis]="chronic appendecitis"

RULE [acute appendecitis]
If [temperature]="high" and [disease]="appendecitis" and [pain type]="acute"
  Then [diagnosis]="acute appendecitis"

RULE [chronic pielonephritis]
If [temperature]="normal" and [disease]="pielonephritis" and [pain type]="weak"
  Then [diagnosis]="chronic pielonephritis"

RULE [acute pielonephritis]
If [temperature]="high" and [disease]="pielonephritis" and [pain type]="acute"
  Then [diagnosis]="acute pielonephritis"

REM User Dialogs

PROMPT [pain] MultChoice
"In what part of your body is pain?"
"in stomach"
"in spine"

PROMPT [temperature] MultChoice
"What is your temperature?"
"normal"
"high"

PROMPT [pain type] MultChoice
"What kind of pain is it?"
"acute"
"weak"

REM The goal of decision search in knowledge base
GOAL [diagnosis]
```

```shell
REM PC Diagnosis Expert System

RULE [GPU Related]
If [Noise Location]="Upper Case"
  Then [Subtype]="GPU Related"

RULE [PSU Related]
If [Noise Location]="Lower Case"
  Then [Subtype]="PSU Related"

RULE [GPU Hardware Failure]
If [System Performance]="Freezing" and [Monitor Output]="Glitching" and [Subtype]="GPU Related"
  Then [Type]="GPU Hardware Failure"

RULE [GPU Fan Failure]
If [System Performance]="Stable" and [Monitor Output]="Normal" and [Subtype]="GPU Related"
  Then [Type]="GPU Fan Failure"

RULE [PSU Hardware Failure]
If [System Performance]="Freezing" and [Monitor Output]="Glitching" and [Subtype]="PSU Related"
  Then [Type]="PSU Hardware Failure"

RULE [PSU Fan Failure]
If [System Performance]="Stable" and [Monitor Output]="Normal" and [Subtype]="PSU Related"
  Then [Type]="PSU Fan Failure"

REM User Dialogues

PROMPT [System Performance] MultChoice
"What is the system performance?"
"Freezing"
"Stable"

PROMPT [Noise Location] MultChoice
"What is the noise location?"
"Upper Case"
"Lower Case"

PROMPT [Monitor Output] MultChoice
"What is the monitor output?"
"Glitching"
"Normal"

REM Result of running the input data through the expert system
GOAL [Type]
```