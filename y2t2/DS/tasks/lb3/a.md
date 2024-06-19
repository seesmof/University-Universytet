### Побудова продукційної моделі

#### Мета роботи

Навчитися аналізувати й описувати предметну область та подавати бази знань інтелектуальних систем у вигляді семантичної мережі

#### Conclusions 

Таким чином, ми навчилися аналізувати й описувати предметну область та подавати бази знань інтелектуальних систем у вигляді семантичної мережі

#### Завдання до роботи 

- Предметна область: діагностика несправностей комп’ютерів

#### Theory

Продукцією (продукційним правилом) називають вираз виду: $\displaystyle (i): Q; P; A_1, A_2, \ldots, A_n \rArr B_1, B_2, \ldots, B_k; N$, де i - ім'я продукції, в якості котрого може виступати деяка лексема, що відбиває суть даної продукції або її порядковий номер; Q - елемент, що характеризує сфера застосування продукції; А1,А2,...Ан->Б1,Б2,...Бк - ядро продукції і знак -> то є знак секвенції; Аі - іта передумова (умова) правила; Бж - житий висновок (наслідок), правила; P - умова застосування ядра продукції; N - постумови продукції 

Сфера застосування - визначає для яких випадків може бути застосована продукція, тобто задає множину елементів для якої продукція є застосовною. Поділ знань на окремі сфери дозволяє заощаджувати час на пошук потрібних знань.

Ядро продукції складається з двох частин:
- антецедент (передумова, умова правила) - являє собою комбінацію умов правила (припущень про наявність)

#### Мета створення бази знань

Метою створення бази знань для предметної областсі «Діагностика несправностей комп’ютерів» є подальша розробка фреймової моделі для цієї предметної області, а також для подальшої роботи з нею.

#### Results 

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

#### Questions
