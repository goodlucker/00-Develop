一般性规范
2019年9月27日, 星期五

9:47

1.

Coding format

a.

b.

Update the header part

Indent the statement as needed

c.

Replace the absolute path with macro defined in msetup.sas

d.

e.

Keep consistent in the case for variable name in whole code

Add the comment as needed

f.

Remove mprint/mlogic/msymbogen after program completed

g.

h.

Remove commented code after program finalized

Fill revision history when updating after delivery

2.

Tracking-sheet

a.

b.

Fill the blank cell with ‘N/A’ or ‘No comment’ accordingly

QC can fill the comments in BLACK first, then DEV replies with 'Updated' or any explanation in RED. After Qcer confirmed the

response, you can make the whole comment in black to close the comment. Otherwise keep in RED. New comments can be

added in RED
Stat/senior/leader review comments can populated in Review Tab

c.

3.

Spec

a.

b.

c.

d.

递交后的修改需要填写修改记录

中文项目尽量使用中文符号，只有当符号在英文（包括数字）之间时使用英文符号. 对于单位括号用英文括号，前面按需加一空格

对于结果（xxORRES)为‘未查’,‘ND','UN'等无效结果的，SDTM需要保留到xxREASND,同时xxSTAT='未做'.ADaM中保留xxREASND和xxSTAT,
一般AVAL/AVALC留空。但如果table和listing需要用到可以取过来替换空的AVALC使用。非结果变量的‘未查’可以不处理。
考虑到Listing中可能需要保留类似‘12导联心电图检查’列同时其他子检查横向排列，此列将对应PARAMCD='XXALL'同时在Listing中补充
‘是’的信息, 如下图。对于竖向的可以去掉XXALL.

e.

spec中术语（CT)如果没有起到解释作用可以仅保留名称而不加链接和术语列表（codelist).

◊

◊

English： 如果术语是可扩展（extension),不需要特意去调整结果符合术语，可直接使用CRF值；不可以扩展则需要调整。如果调整
了术语请同时保留CRF值到SUPP，以便后续使用
中文：中文目前没有标准术语，可以直接使用CRF值。但对于可直接赋值的，尽量参考翻译版术语

f.

CodeList Template

a.

b.

c.

对于CRF中为全部列出的code如果不想list出来，可以只保留CT名字，不加链接

如果CT在多个数据集通用可以不填数据集名，比如VISIT

CT名字一样，但是想区别的，可以填上数据集名，比如CM中的FREQ，DOMAIN

4.

日期时间比较

日期时间变量比较仅考虑共有部分，比如2019-11-27 与 2019-11-27T14:46比较数量级上算相等
对于部分缺失变量用对应字符变量比较更合理。特别留意PREFL,TRTEMFL,ONTRTFL.
尽量使用xxxDAT_RAW这种字符结果转ISO8601. 然后利用冒号(:) 修改符，比如 strip("2019-11")<=:strip("2019-11-12")

a.
b.
c.
数据截断

5.

a.

b.

在SDTM/ADaM中字符长度定义统一长度为200.tlf数据集如果有合并变量可以超200，否则也按照200定义。比如AETERM和AEDECOD在同一列合
并的时候该列长度可以为400
通过macro判断EDC数据中是否存在真实长度超200的字符，如有请考虑拆分

6.

复筛受试者两种处理方法

项目处理 Page 1

Updates on
Handling ...

a.

b.

在SDTM/ADaM中字符长度定义统一长度为200.tlf数据集如果有合并变量可以超200，否则也按照200定义。比如AETERM和AEDECOD在同一列合
并的时候该列长度可以为400
通过macro判断EDC数据中是否存在真实长度超200的字符，如有请考虑拆分

6.

复筛受试者两种处理方法

a.

b.

按照FDA TCG处理以最后的受试编号衍生USUBJID/SUBJID,
１.
２.
３.
算作2个不同的受试者

EDC中编号保留为SUPPxx.SUBJIDC
RFICDTC取最早的，DS里面保留全部记录
VISIT/EPOCH合并

Updates on
Handling ...

7.

文件版本升级

a.
b.
c.

每次dry run应该升级文件版本，包括acrf,sdtm spec, adam spec 等
Final run之前应该升级版本为1.0
如果有post DBL 较大更新可以考虑升级版本为1.1或以上

8.

是否应答术语选择

a.
b.
c.
d.

新项目中优先使用Y/N,特别是flag类变量
'是/否' 做为结果在CRF收集的可以保留中文
系列项目请和之前的保持一致
listing中需要使用中文‘是/否'

项目处理 Page 2

程序编码

Tuesday, February 22, 2022

1:07 PM

1.

SAS编码
a.
b.

中文项目根据EDC数据集编码选择SAS编码
英文项目优先使用英文SAS, 如果存在无法读取非ASCII字符，可以使用UTF8读取后在SDTM中换成
ASCII字符。

2.

编码调整

a.
b.
c.

利用%turn_prog对全部程序进行编码转换
删除之前产生的数据集
检查是否有截断。其中LIBNAME中CVP/CVPMUTIPLIER= 可以扩充字符所占字节仅能用于读取数据
集。CVP默认是1.5倍，CVPMUTIPLIER=3是3倍

项目处理 Page 3

非盲管理

Thursday, March 17, 2022

11:11 AM

1.

2.

3.

4.

5.

6.

建立非盲文件夹(\unblind), 和\csr平级，管理文件夹权限只能非盲人员有权限。

非盲人员可以开通盲态文件夹只读权限，便于文件传输

非盲数据(PK结果)问题只能和非盲人员讨论，否则会出现破盲。盲态数据不影响。比如访

视, 日期等

分析结果进行zip加密传输，密码邮件单独发送非盲人员

如果结果不会揭示个人信息以及分组信息可以分享给盲态人员，否则请保密

可以将全部随机号进行完全打乱(避免遗漏对照组仅仅组内打乱)准备dummy的盲态数据供

编程使用

项目处理 Page 4

IDMC
2024年9月30日

10:38

数据传输流程

•

•

•

•

各参与人员（客户，非盲第三方，康龙，指定文件发送与接收方）

递交文件内容（raw edc data, external data, acrf , sdtm data（or pgs?), adam data（or pgs?), tlfs pgs and output ect.)

递交文件格式

考虑到递交数据量可能比较大，建议提前申请大文件外发系统，避免邮件附件传输限制

注意是否需要流程图给到客户

数据盲态保持
开门会议（盲态）

•

•

闭门会议（康龙盲态团队基于测试用随机表进行，具体揭盲过程给到第三方去进行）

注意开门和闭门会议所需要tlfs呈现是否变化，如仅是组别差异，考虑同一套tlfs程序出两份output，减少项目管理时间；

若是呈现内容变动，建议分两套tlfs程序出output。

adam数据集在闭门会议过程中，需要结合揭盲文件重新生成，需要运行tlfs程序生成闭门会议结果。

Timeline
同统计师及时沟通，按照5-7个工作日（sdtm+adam+tlfs rerun）计划，根据任务量多少适当加减，若有需要调整再视具体要求协调

Rerun按照2-3个工作日进行

及时沟通

•

•

•

内部有疑问提前沟通协调，尽早做好准备

检查自身程序(特别是TLFs程序），避免程序冗余，保证结构完整，逻辑清晰；关键结果对程序进行第三方review

外部出现审阅意见，注意基于数据实际情况检查，确实有问题的需要提高注意，避免重复犯错

数据截止日期提前确定

项目处理 Page 5

acrf

Monday, March 29, 2021

2:22 PM

1.

%acrf_bookmark 宏: Visit sorted with visit+page number, Forms sorted with form name+visit。使用带选项的

空白CRF做标注

2.

--TEST本身作为结果收集需要标注在CRF, 来源为CRF， 同时如果--TEST有较多不符合术语，还可以同时添加SUPP.

(e.g., xxTESTOR).

每个--TEST对应一个变量收集可以不标注CRF, 来源为Assigned

--TESTCD作为条件出现在--ORRES标注中，来源是Assigned

为方便理解，对于等号右边值的部分加双引号括起来(MSG v2.0并不推荐, 所以客户不要求就不执行)

如果mapping不是通过变量结果而是CRF里面的描述则标记虚线框。注意有时候Unit在CRF不是变量，但实际数据集里

面是变量，这个时候要用实线框。

CRF

Dataset

acrf

Origin

Comment

Y

Y

N

N

Y

N

Y

N

实

CRF 包括因CT控制需要调整变量

虚 Assigned 比如form name做xxCAT， 每个检查是变量时的xxTEST

NA

Assigned 比如Unit做变量

虚 Assigned 比如DSCAT，xxTESTCD

3.

4.

5.

6.

7.

项目处理 Page 6

PDF file

2025年3月3日

11:37

项目处理 Page 7

注释要求

2024年7月17日

11:16

General rules:

•
•
•
•
•

•
•

•
•

•
•

•

All individual annotations should be text-based and searchable using standard PDF viewers.
All CRFs fields should be annotated.
All text in the annotations that represent variable and domain names should be capitalized.
If possible, the annotations should not obstruct any text on the CRF page.
All individual annotations should be annotated with text box. color of box border is black and thickness
of box border is 1 pt.
All text description in the annotations should be bold, Italic and Arial (12 pt. font).
To distinguish the domain level annotations from the variable annotations, we would use black font
color for Domain annotations and red font color for variable annotations.
Arrows and Boxes are optional to use when necessary.
If more than one domain exists on a page as each domain annotation, and all of its variables, should be
color-coded. It is not necessary to continue the color scheme for a domain across CRF pages. A standard
default color scheme will be used across all CRF pages. if two or more domains exist on a single page
then different color schemes should be used. The following hierarchy fill color is used: BLUE(E55),
GREEN(E54), YELLOW(E53), PINK(E51).
Make sure no personal information (e.g. Author).
Set the Navigation Tab to open to “Bookmarks Panel and Page”, set the layout and magnification to
default.
The annotated CRFs should be named as “acrf.pdf”.

项目处理 Page 8

导入导出注释示例

2024年7月17日

11:18

项目处理 Page 9

项目处理 Page 10

项目处理 Page 11

多重结果

2022年12月12日

14:51

1.

对于多重结果的mapping请参考SDTMIG3.3 - 4.2.8 Multiple Values for a Variable

项目处理 Page 12

随机或入组失败原因

2022年12月12日

14:51

1.

出现随机或入组失败可以按照下面mapping

2.

筛选成功因为没有protocol milestone 对应的CT可用，故可以参考EOT将筛选成功和失败一起算一个

Disposition Event

项目处理 Page 13

Cut Off

2020年3月17日, 星期二 21:20

1.

2.

3.

4.

5.

Cut off 通常作用于ADaM数据集，但也能考虑从raw中cut off

Cut off的目的是去掉数据中cut off之后的记录，一般可以通过xxDTC/xxSTDTC判断, xxENDTC

通常不考虑

如果存在Listing直接从raw出的，请同时考虑cut off

需要留意涉及日期的duration，flag等间接变量

如果日期不可用可以同时考虑通过VISIT实现cut off

项目处理 Page 14

Datasets Review

Tuesday, December 27, 2022

2:20 PM

Intervention flag checking:

proc freq data=cm_;

        tables PREFL*ONTRTFL*ASTDY*AENDY*CMONGO/missing list;

run;

项目处理 Page 15

SDTM
2020年7月15日, 星期三

13:16

1.

'异常, 有临床意义' 作为结果可以拆开映射到--ORRES和--CLSIG，或者仅到--ORRES但--STRESC需要调整为‘异常'。保持系列项目一致。如果不是结果可以直接放到

--CLSIG。 ADaM可以按照需要合并到AVALC

2.

3.

4.

5.

6.

7.

8.

9.

'Other, specify'作为PETEST, 根据PETEST得到PETESTCD, PEGRPID='OTHER'. 否则不输出该记录; 或者不存在'Other, specify'时按照PETESTCD='OTHPE'处理

MHONGO=‘否’ 赋值MHENRTPT='之前', 同时MHONGO='是' 赋值MHENRTPT='持续’ 并且MHENTPT=筛选期日期，否则留空。 对于AE/CM/PR同样处理，但

xxENTPT=RFPENDTC。

xxSTAT='未查', xxREASND尽量填写，如果xxSTAT是针对是否的问题同时没有具体原因xxREASND可以直接赋值‘未查'；如果是结果中的'ND', 'UK'可以赋值给xxREASND

在CODELIST中按需添加完整的CT方便define准备，同时为支持编程理解可以使用hyperlink函数进行link。不添加codelist可以仅保留CT名

备注（comment）可以通过%finalSDTM中的参数plusvarlist=输出到sdtmplus中

LBNRIND如果CRF有收集直接使用CRF结果，否则可以通过原始单位范围判断（标准单位转换后可能有精度丢失)。对于RAVE系统LAB里面的Labflag/RefFlag/AlertFlag可以

用来cross-check

RFENDTC通常可以直接使用RFXENDTC, 但在DS有收集结束用药日期时可以使用这个收集日期

HCG(妊娠试验) 将不做到ADaM,对应Listing直接从SDTM.LB出。标准单位为IU/L, 如果有不一致无法换算可以不统一

10.

乙肝/梅毒等感染检查mapping到MB

11.

LBTOX: CTCAE 对于基线和基线前的计算，如果规则涉及到基线，请在不使用基线的情况下判断。比如ALP的toxcity grade对于基线和基线前只考虑用ULN

12.

LabCTCAE中目前仅ALT, ALP, AST, GGT, Triglycerides(TRIG)考虑了包含Grade 1升高左边界

13.

中文LB mapping， LBTEST去掉简写直接使用，LBTESTCD符合CT

14.

调整EX mapping, 如果EDC里面EXDOSEU和protocol 不同就使用EC, EX通过EC衍生，否则直接mapping到EX。

15.

在盲态试验, ECTRT/EXTRT可以根据ACTARM调整为具体药品

16.

EOT 当天将包含在Treatment EPOCH， 而不是Follow-up

17.

ETHNIC 英文CT不可扩展，中文暂时不考虑CT, 可以直接把‘汉族’保留在ETHNIC

18.

SMQ中如果仅包含PT(level=4)则以PT为关键变量，如果也包含LLT(level=5)时以LLT作为关键变量进行判断，没有LLT可以使用PT或xxTERM代替

19.

‘是/否’做为结果在CRF收集的可以保留中文，否则优先使用‘Y/N’

20.

QSORRES保留描述性文字, QSSTRESC/QSSTRESN 保留标准分值，包括RS中ECOG

21.

--TEST和变量label不要使用疑问句，最后也不需要保留问号。比如‘是否进行靶病灶评估’对应的TRTEST='靶病灶评估'

22.

TS中的TSPARM='ACTSUB', 'DCUTDTC', 'SENDTC' 在dry run的时候可以暂时留空，且不需要填TSVALNF. P21里面可以解释，final run再补上即可

23.

当IETEST改变时，可以使用X, Y, Z作为IETESTCD的后缀来表示有改动，避免这种情况：INCL01A改变之后不好命名

24.

为避免P21因翻译无法检查知情同意日期，需要翻译为DSDECOD="获得知情同意"

项目处理 Page 16

EPOCH

2020年1月14日, 星期二

13:25

SDTMIG v3.3

4.1.3.1 EPOCH variable Guidance

When EPOCH is included in a Findings class domain, it should be based on the --DTC

variable, since this is the date/time of the test or, for tests performed on specimens, the

date/time of specimen collection. For observations in Interventions or Events class

domains, EPOCH should be based on the --STDTC variable, since this is the start of the

Intervention or Event. A possible, though unlikely, exception would be a finding based

on an interval specimen collection that started in one epoch but ended in another. --

ENDTC might be a more appropriate basis for EPOCH in such a case.

Sponsors should not impute EPOCH values, but should, where possible, assign EPOCH

values on the basis of CRF instructions and structure, even if EPOCH was not directly

collected and date/time data was not collected with sufficient precision to permit

assignment of an observation to an EPOCH on the basis of date/time data alone. If it is

not possible to determine the EPOCH of an observation, then EPOCH should be null.

Methods for assigning EPOCH values can be described in the Define-XML document.

Since EPOCH is a study-design construct, it is not applicable to Interventions or Events

that started before the subject's participation in the study, nor to Findings performed

before their participation in the study. For such records, EPOCH should be null. Note

that a subject's participation in a study includes screening, which generally occurs

before the reference start date, RFSTDTC, in the DM domain.

来自 <https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-v3-3#Adverse+Events>

项目处理 Page 17

SI unit

2025年3月3日

11:30

参考文件

SI_Unit_E

汇总

SI-Brochure-9 完整描述

项目处理 Page 18

单位转换

Wednesday, September 1, 2021

11:17 AM

mEq/L=(mg/L)×原子价/化学结构式量

mg/L=(mEq/L)×化学结构式量/原子价

mg/L = mmol/l×化学结构式量

所以mEq/L=mmol/L×原子价

(注：化学结构式量=原子量或分子量)

酶活性单位：

1 IU=1 umol/min （1 min能转化1 umol底物的酶量）

1kat=1mol/s       (1 s 能转化1 mol底物的酶量)

1 ukat = 60 IU  1 IU=16.67 nkat

LabUnit

LABDICT_A
LL_2014_...

项目处理 Page 19

AE同一事件判定

Tuesday, February 22, 2022

1:14 PM

a.

b.

c.

肿瘤试验通常会将AE按照CTCAE等级记录，故需要判断同一事件

对于首尾时间相连且前一个AE的转归（AEOUT)不为‘恢复’的同一个AE, AEGRPID保持不变

同一个AEGRPID中如果吃药后CTCAE增加，后者将标记为TEAE

项目处理 Page 20

SV 日期纳入考虑

2024年7月17日

11:15

项目处理 Page 21

AE vs CE

2023年5月23日

17:31

1.

AETRTEM: 是否需要保守考虑？--R:

项目处理 Page 22

DM

2024年7月17日

11:25

DM1.

a.

出现Not treated 那就按照ARM, ACTARM 设置为空，ARMNRS 为“NOT TREATED”，

RFSTDTC, RFENDTC为空

b.

知情同意时assign dose group, 对应ARM相应赋值

2.

Rfpendtc:
Date/time when subject ended participation or follow-up in a trial, as defined in the protocol, in
ISO 8601
character format. Should correspond to the last known date of contact. Examples include
completion date,
withdrawal date, last follow-up, date recorded for lost to follow up, and death date.

注意需要包含最后的随访日期(评估日期需要看情况）

项目处理 Page 23

MH

2024年7月2日

11:23

1.

对于过敏史，SDTMIG中认定是其中一种病史，放在MH中会比较符合；若无数据，可以考虑

且单独form收集，可以考虑加--presp, --occur变量，--term赋值为“过敏”

2.

MHONGO 是否持续放到SUPP, 同时MHONGO='是‘ 赋值MHENRTPT='持续’ 并且MHENTPT=

筛选期日期，否则留空。 对于AE/CM/PR同样处理，但--ENTPT=RFPENDTC

项目处理 Page 24

DS

2024年7月17日

11:23

1.

更正下上午小组会上提问的中文版P21检查，这个目前不会单独对CT中的value 去核查是否满足规

则了；但对于部分核查逻辑，在3.2版基础上，当判断时会去根据CT中的值进行匹配后再判断

比如：DSCAT不等于 'DISPOSITION EVENT' or '方案重大事件'时填有EPOCH变量

会匹配对应的DSCAT按照CT上的标准值后去进行检查是否应该填写EPOCH，现在中文的P21检查感

觉并不是很准确

项目处理 Page 25

--ENRTPT

2024年7月17日

11:20

项目处理 Page 26

1. 对于筛选失败或未分组的受试者，RFENDTC为null才对，而RFPENDTC是针对的所有受试

者，--ENRF相对于RFSTDTC跟RFENDTC这个研究时段的，所以在定义PRENRF的时候，可以加

项目处理 Page 27

者，--ENRF相对于RFSTDTC跟RFENDTC这个研究时段的，所以在定义PRENRF的时候，可以加

上"RFENDTC非空时"

项目处理 Page 28

ADaM
2020年7月15日, 星期三

13:16

Spec

a.

人群为否的原因可以按照继承关系继承。通常‘筛选失败’为第一个原因可以继承到下一个子人群. 目前统计决定由他们提供在最后的外部数据不需要程序判断。通常外部

数据只包括入组（随机）受试者。筛选失败可以程序补上

LAB 中仅提取对应的正常值范围和临床意义判断, 同时比较LBNRIND是否一致

AVAL/AVALC在PARAM level 判断使用哪一个变量，尽量不要同时使用。除非IG中的特殊情况（IG1.1 Page 43)

保留xxSEQ(单个SDTM, 放最后)或者SRCDOM/SRCSEQ(多个SDTM,放最后)帮助保留Traceability。如果是横向(MERGE)合并的，只需要考虑主要数据集。ADaM内部衍

生数据集不需要

ADY/ASTDY/AENDY只在需要的时候添加，比如日期有填补之后考虑flag，或者多个来源需要合并xxDY。否则直接保留xxDY/xxSTDY/xxENDY就好了

Confirmed BOR注意确认中间的NE算不算有效结果

ADRS里面检查下有没有开始新的抗肿瘤之前没有PD出现的，正常是不应该存在的

ADRS中总体疗效评估(OVRLRESP)非PD时日期取对应访视下TR中的最大日期，否则取PD相关检查的最小日期 <refer to FDA NSCLC 2015 Page15>

ADaM中添加变量按照IG排列，对于SDTM直接保留的变量放在相关变量前面，无相关变量就往后放

‘最后有效测量’在table中和访视同级，考虑增加记录实现

滴度为稀释的倍数，通常记为‘ADA滴度为1:20’, 即 AVAL=20

ADaM中衍生结果不做小数位数处理，除非SAP有特别说明。Table/Listing中按照EDC收集情况进行保留

b.

c.

d.

e.

f.

g.

h.

i.

j.

k.

l.

m.

APERIOD可以根据项目需求考虑对于pre-treatment部分如何赋值

a.

b.

Pre-treatment包含在第一个period会有利于baseline的标记，不利于APERSDT/APEREDT的衍生

IG中有实例支持Pre-treatment时留空，利于APERSDT/APEREDT衍生，period结束日期为下一个period开始的前一天。baseline可以通过添加记录调整

TRTP/TRTA等的值来实现

n.

ADaM中date/time format 对应中文可以使用e8601da, e8601dt, e8601tm, 但英文考虑到JMP不识别e8601系列，需要使用date9.,datetime19.,time8.

1.paramcd 需要唯一

项目处理 Page 29

基线

Thursday, December 9, 2021

2:26 PM

a.
b.
c.
d.
e.
f.

如无特别说明或者明确判断（Time/xxTPT),吃药当天记录会被考虑到基线的范畴
如果同时有时间部分，应该考虑进来。同时可以参考xxTPT/VISIT的描述筛选
基线是针对受试者参数（比如PARAM)的，即使当前结果缺失也可以有基线
CHG只针对基线后（post-baseline)的有效值
用药前逻辑判断：trtsdt>=adt>. and not (adtm>trtsdtm>.)
用药后逻辑判断：adt>trtsdt>. or adtm>trtsdtm>.

项目处理 Page 30

超窗

Thursday, December 9, 2021

2:27 PM

a.

对于‘吃药前30分钟’：

ARELTM(分析相对时间)=发生时间-吃药时间点，同时如果-30<=ARELTM<=0则ARELTM=0

            ARELPT(分析相对计划时间)= ARELTM
对于用药后：

ARELTM(分析相对时间)=发生时间-吃药时间点

           ARELPT(分析相对计划时间)= ARELTM-ATPTN
           POUTWIND(超窗百分比)=ARELPT/ATPTN*100%

项目处理 Page 31

BLOQ处理
2020年1月7日, 星期二 10:00

BLOQ在PK浓度总结（包括平均曲线浓度图）和个人曲线浓度/PK参数计算时会有不同的处理原则。
在通常的PK浓度总结描述时，前者都视作0为计算，更多的是从“均值”等统计量考虑的，
若考虑PK参数计算的时候一样的规则：在Tmax之后视作缺失，在曲线的消除相后期的时间点，往
往会出现后面时间点的均值（因BLOQ太多）会高于前面时间点的均值。主要是这样的考虑。

a.
b.

也附上PK分析中常用的BLOQ的处理原则供您参考：

The following general rules are applied in all cases (以下NQ等同于BLOQ);

1)

2)

NQs at the beginning of a subject profile (i.e. before the first incidence of a measurable concentration) are
deemed to be zero as it is assumed that in this circumstance no drug is yet measurable in the blood.
For NQs at the end of the subject profile (i.e. after the last incidence of a measurable concentration);

a.

b.

for individual plots and pharmacokinetic analyses these are dropped (set to missing) as they do not
provide any useful information (and can erroneously indicate that absolutely no drug is present)
for summary statistics these are set to 0 (to avoid skewing of the summary statistics)

项目处理 Page 32

增加记录或增加变量

Thursday, December 9, 2021

2:28 PM

Worst Post-baseline （Lab中存在2个方向，选取最先发生的)

a.

b.

增加flag ：WOCFL (Worst Post-baseline Flag) - 统计师方便查看记录

增加记录:  AVISIT=Worst Post-baseline  - ADaM IG v1.2 #4.5.3 (P88)有实例，适合需要和计划访视一起使用的时候

1.

分析数据集中如果只有基线+基线后一种情况，加分析flag 标记就可以；如果合并2个及以上基线

后访视进行输出，则进行观测衍生

2.

DTYPE
I apologize for any confusion caused earlier. In the ADaM (Analysis Data Model) standard, the "DTYPE" attribute is not

used to indicate whether a parameter is derived or not. The "DTYPE" attribute is primarily used to specify the data type of

a variable, such as character, numeric, date, or time.

To indicate that a parameter is derived in ADaM, it is not done through the "DTYPE" attribute. Instead, you can follow the

previously mentioned approach of using a flag variable or another designated method to indicate the derivation status of

a parameter.

By creating a separate flag variable and assigning appropriate flag values, you can clearly indicate whether a parameter is

derived or not in an ADaM dataset. This flag variable should be well-documented, allowing users to understand the

derivation status and meaning of the parameter during subsequent data analysis and interpretation.

From <https://chat.openai.com/c/4befacb9-1203-4f43-9194-73eebc7fbeae>

项目处理 Page 33

日期填补示例

Thursday, November 4, 2021

4:32 PM

参考code

   /*仅将开始填补为年或月的第一天并结合第一次用药调整，结束填补为年或月最后一天*/

    if scan(cmstdtc,1,'-','m')='' then astdtf='Y';
    else if scan(cmstdtc,2,'-','m')='' then astdtf='M';
    else if scan(cmstdtc,3,'-','m')='' then astdtf='D';
    else astdtf='';
    if scan(cmendtc,1,'-','m')='' then aendtf='';
    else if scan(cmendtc,2,'-','m')='' then aendtf='M';
    else if scan(cmendtc,3,'-','m')='' then aendtf='D';
    else aendtf='';

    astdt=input(cats(scan(cmstdtc,1,'T'),'-01-01'),??yymmdd10.);
   if astdtf='Y' then astdt=trtsdt;
    else if astdtf ne '' and intck(ifc(astdtf='M','year','month'),astdt,trtsdt)=0 then astdt=trtsdt;

    aendt=input(cats(scan(cmendtc,1,'T'),'-12-31'),??yymmdd10.);
    if aendtf ne '' then aendt=intnx('month', aendt,0,'e');
    if aendt>eosdt then aendt=eosdt;

    if astdt>aendt>. then astdt=aendt;

项目处理 Page 34

ADAE
Tuesday, February 22, 2022

1:14 PM

同一事件判定(AEGRPID) (请提前了解AE具体收集规则)

1.

2.

3.

肿瘤试验通常会将AE按照CTCAE等级记录，故需要判断同一事件

a.

b.

开始日期为上一等级结束相等或+1天的日期，结束日期为等级变化日期

开始日期为等级变化日期，结束日期为整个事件结束日期

对于首尾时间间隔<=1天且前一个AE的转归（AEOUT)不为 '恢复' 和'恢复有后遗症'的相同AETERM, AEGRPID保持不变

同一个AEGRPID中如果吃药后CTCAE增加，后者将标记为TEAE

TEAE
首选填补之后进行判断，逻辑更清晰。否则可以考虑按照字符通过排除法判断

1.
2.
3.
4.

RFSTDTC 为空 则不是TEAE
AEENDTC非空且AEENDTC<RFSTDTC 则不是TEAE
AESTDTC>RFENDTC则不是TEAE (NOTE: 如果不考虑截止日期这一条可以去掉)
剩下的都是TEAE

   if rfstdtc='' then trtemfl='';
   else if ''<aeendtc<rfstdtc then trtemfl='';
   else if aestdtc>rfendtc then trtemfl='';
   else trtemfl='Y';

AESI至缓解时间

1.
2.

先判断同一AESI,提取到同一AESI的开始结束日期，最大毒性，是否持续
如果进行KM分析，可以在ADAE中添加相关变量，然后在ADTTE中每个AEDECOD一个PARAM

AESI持续时间

1.
2.

先判断同一AESI,提取到同一AESI的开始结束日期，最大毒性，是否持续
分析表格中进行求和处理

1.

2.

3.

4.

RELGRx变量的创建更具分析需求设置

重点关注TRTEMFL, PREFL；需要保守考虑的情况参见SAP，日期缺失的情况一般保守考虑为
TRTEMFL="Y"

AEOUT, AEFREQ等存在

注意AE收集形式，如果是分开不同观测记录的同一条AE情况，需要添加AEGRPID进行标记，

以便后续分析

项目处理 Page 35

CTCAE
2023年1月19日

20:22

1.

如没有说明血清钙(CA)不考虑校正，如需要校正可以仅在算grade的时候处理，不影响测量结果分析

矫正血清钙公式=总血钙[测量值 ( mmol/L) ] + 0.02 x [40-血中白蛋白浓度 ( g/L)]（白蛋白<=40）；

血清钙公式=总血钙[测量值 ( mmol/L) ] （白蛋白>40）

肌酐 (CREAT) 增高: 按照取base和ULN的较大值判断, 避免正常值存在Grade

血红蛋白（HGB）增高: 按照取base和ULN的较大值判断, 避免正常值存在Grade

基线异常判断：默认使用当前记录范围且同方向的异常才算，但有的客户可能要求使用基线范围判断或者不同方向异常也算异常

当ULN和BULN(基线上限)不一致时，目前使用BASE和ULN比较而不是BULN是为了避免正常值存在Grade，可以和客户确认

2.

3.

4.

5.

项目处理 Page 36

Visit window

Thursday, December 16, 2021

1:52 PM

o

绿叶和青龙高科部分visit window （针对提前退出等特殊的计划外访视）

-------提前退出访视（等需要remap的访视）的remapping 注意不要remap 到已经存在的计划访视
ASMB完整visit window （包含全部访视）

o

-------所有访视visit window 访视mapping基本原则遵循窗口无间隔，保证所有时间能mapping

项目处理 Page 37

Define
2022年5月16日

Define Spec

16:46

1.

2.

3.

4.

5.

6.

7.

8.

9.

调整spec里面的Conversion Definition 列, 尽量使用描述语句代替SAS语句。同一变量描述尽量一致，比如USUBJID

Conversion Definition 列的"RAW." 和 “SDTM."可以去掉，特别是raw不会递交不能出现RAW里面的数据集/变量

Conversion Definition 列的外部文件不会递交，需要调整描述或者作为附录加到review guide

如果有link外部sheet，比如LBTEST sheet, 因不会递交这个sheet需要把里面的内容用描述语句替代。如果特别复杂的也可以考虑使用review guide

注意检查Trial Design 是不是在CONTENT添加好

运行define macro生成define spec初稿，按需进行手动修改调整。不需要每次修改都运行程序

注意检查变量有多个来源的情况: 如果该变量有VLM可以变量来源留空，否则define macro会优先使用“CRF”

SDTM通常只对Derived添加描述(i.e., Method)，Assigned/Protocol可以选择添加描述(i.e., Comment)

SDTM Codlist 需要依照CRF完整列出来，包括数据中未出现的分类，主要检查DM/DS/AE。需要依照CT进行适当调整。

10.

检查Codelist中配对变量是否匹配, 排序是否合理

11.

只需Y结果的时候调整YN为YNULL，比如DTHFL/xxBLFL

12.

直接赋值为空的CT可以去掉, 如果xxORRES同时有字符和数字结果不用加CT或者CT加在VLM中

13.

如果变量需要多个CT的，比如DSDECOD可以考虑添加VLM

14.

VLM中需要调整出现多个来源或CRF出现多页的情况

15.

VLM中来源是对应检查结果（xxORRES/QVAL)的具体来源, 存在VLM的变量自身的来源可以留空或全部VLM来源的集合

16.

检查Method中有没有"#NAME?"的错误或者字符错误显示为"?"

17.

结合Method检查VLM的合理性，应该针对这条VLM，而不是整个变量。有VLM的变量其自身的conversion可以留空

18.

P21不能直接用SAS输出的Excel，可以保存一下使用

19.

每次修改记得运行P21单独对define进行检查, 确保没有报错

20.

注意检查define 中review guide 引用页码是不是对

21.

Review guide 每次都记得检查目录是否更新，link是不是对的

22.
23.

ADRG/cSDRG/define之间需要保持一致，包括试验设计部分，数据标签等
Standard调整位置
搜索关键字"<def:Standard"，按顺序对SDTMIG 3.3、ADaMIG 1.2、CDISC/NCI SDTM、CDISC/NCI ADaM的位置进行调整

项目处理 Page 38

SDTM code
2023年9月28日

14:12

1.setup0define.sas

2.step01_doc_dic_study.sas

3.step02_datasets.sas

1)
2)

3)
4)

Line 67: standard="&ig_type.IG &ig_type"; --> standard="&ig_type.IG &ig_version";
Line 109:
data input.sheet_datasets;
    set content;
    if data in ("&filelist") then nodata=unicode("No");
    else do;         *可以对nodata的dataset增加comments;
        nodata=unicode("Yes");
        comment=data;
        commentsfordefine='未收集到数据';
    end;
class、subclass保持为英文输出，在define.xml再修改为中文，避免出现数据集排序问题；
adam L107: 去掉keep中的purpose；

4.step03_variables.sas

1)

2)

L308: if origin in (unicode("&assign"), unicode("&derive"), unicode("&protocol")) then source=unicode("&sponsor");
*中文未定义assign宏变量，unicode不支持in，可改成or;
基于现在的spec格式，origin/source需重新赋值，CRF-->Collected & Investigator，eDT-->Collected & Vendor
    if origin="CRF" then do;
        origin=unicode("&collect");
        source=unicode("&investigator");
    end;
    else if origin="eDT" then do;
        origin=unicode("&collect");
        source=unicode("&vendor");
    end;
    else if origin=unicode("&assign") or origin=unicode("&derive") or origin=unicode("&protocol") then source=unicode("&sponsor");
L306:  if cmiss(length)=0 then nodata=unicode("No"); else nodata=unicode("Yes"); *length在前面对日期变量置空了，nodata取空的length不对;
考虑做法：

a.
b.

L114/130: length函数改成lengthn，令结果为空的变量长度=0；
L306：
if length='0' then nodata=unicode("Yes");
else nodata=unicode("No");
if length in ('0','') and (type=unicode("&datetime") or type=unicode("&date") or type=unicode("&time"))=0 then length="1";
*数据集nodata时length=''，变量nodata时length='0'，都赋值为长度'1'；

3)

4)
5)

对nodata变量增加comments；
if nodata="Yes" then do;
method="";
comment=strip(sheetname)||'.'||strip(variablename);
end;
var_type、origin和source保持为英文输出，在define2-1-0.xsl再修改为中文，避免P21 report出现过多CT值报错；
sdtm/adam L178: common $1 --> common $3;

5.step04_valuelevel.sas

1)
2)
3)
4)
5)

L50: val_ds数据集中需排除掉nodata的domain，否则下面读取set xptfile.&&data&i将报错
L156: val_qnam1(drop=val_origin pages method predecessor val_com) 中drop加上source；
var_type、origin和source保持为英文输出，在define2-1-0.xsl再修改为中文，避免P21 report出现过多CT值报错；
目前的QVAL是取自xpt数据集的，若该数据集nodata则无法获得想要的SUPP变量，可考虑从spec读取，将spec中所有SUPP变量输出；
%vlm仅能输出xxTESTCD EQ xxx，但FA/LB一般存在不同xxCAT下相同的xxTESTCD，可考虑加上xxCAT EQ xxx 作为AND条件；

6.step05_codelists.sas

1)
2)
3)

L41: codelist数据集中需排除掉nodata的domain，否则下面读取set xptfile.&&data&i将报错
L153: YNULL是ADaM CT，do语句增加codelist_ver="ADaM &adam_ct_version";
L160/163: comment-->codelist_comment（或Step06中的codelist_comment-->comment），codelist_var-->codelist_ver

项目处理 Page 39

3)
4)
5)
6)

L160/163: comment-->codelist_comment（或Step06中的codelist_comment-->comment），codelist_var-->codelist_ver
L127/133: 加上codelist_ver;
L192/193: in1、in2改为sdtm、adam;
中文项目考虑将codelist_name改为变量label

7.step06_definespecs.sas
1) L37: subcalss改为subclass

项目处理 Page 40

Define2.0

Tuesday, March 30, 2021

3:45 PM

中文define

1.

2.

3.

4.

P21 网站可以下载中文版define style

中文define中可能会数据集排序不对，可以使用DefineEditor/NOTEPAD++修改或者spec中保留英文Class，最后define.xml里面改成中文。比

如SDTM中试验设计（TRIAL DESIGN)类排第一个<参考Define-XML-2-0-Specification.pdf #3.4.2: ‘不良事件分析数据集’换成‘事件发生数据

结构’>

中文版define spec里面先用“Predecessor", 通过P21产生的define再调整为 "继承"。中文style中需要添加条件【 or $OriginType = '继承' 】

显示ISO 8601，中文style中添加【or $itemDef/@DataType='日期型' or $itemDef/@DataType='日期时间型' or $itemDef/@DataType='时间型'  】

项目处理 Page 41

Define2.1

2022年5月16日

16:46

1.

ValueLevel 的 Where Clause 书写格式，eg., LBTESTCD IN (HCT, WBC) and LBSPEC EQ BLOOD and LBNAM EQ "LOCAL LAB"

Spec Origin Define Type Define Source

CRF

eDT

2.

Collected

Investigator

Collected

Vendor

Assigned

Assigned

Sponsor

Derived

Derived

Sponsor

Protocol

Protocol

Sponsor

3.

修改中文define.xml，打开Notepad++打开进行编辑：

1.

Standard调整位置

搜索关键字"<def:Standard"，按顺序对SDTMIG 3.3、ADaMIG 1.2、CDISC/NCI SDTM、CDISC/NCI ADaM的位置进行调整

ADam define spec:

Define 2.1中对adam 变量来源要求supp变量时，对应在adam中用继承

Part1: Define sheet
注意输出格式

Part2: Datasets sheet

i.

Class, Subclass 翻译中文会影响xml中展示顺序，现在通过修改xsl 样式表进行调整

ii.

Comment列用来指定ID链接comments sheet，比如数据集的筛选说明描述（文件形式或者文字形式）

Part3: Variables sheet

i.

注意format列是否有额外的值，若有修改ADaM spec

ii.

注意codelist列是否遗漏，若有修改ADaM spec，补齐CT，例如PARCAT1, PARCAT1N；是否持续（Y/N)

iii.

iv.

检查在CT中去掉的Codelist列是否删除

存在VLM的字段，对应字段本身下列可以置空

Origin Source Pages Method

v.

define role大家看看，后面客户如果提问。可以用这个回复。

Part4: ValueLevel sheet

i.

注意非AVAL， AVALC变量是否纳入并描述说明

ii.

对VLM视情况判断是否需要添加单独的计算方法

iii.

Where 条件中是否有空值，若有空值更新描述

iv.

根据具体要求对非结果变量创建VLM

v.

https://www.pinnacle21.com/forum/dd0038-missing-value-level-metadata-qval-dataset
supp变量为什么需要VLM

Part5: Codelists sheet

i.

ID列与Name 列是否有重复的情况

ii.

NCI列需要补充的是否补充

iii.

iv.

AVISIT, AVISITN 需要检查对应顺序（程序按照字符型顺序呈现，或者考虑Define中不要放CT）

注意字符、数值变量的decode value 是否配套对应

v.

删除SDTM中未做的--STRESC ct

vi.

UNIT注意是否有希腊字母不匹配

vii.

对于PARAM, PARCAT1等建议要么做成衍生，要么做成继承，不再用Codelist控制--待检查

Part6: Dictionaries sheet

Part7: Methods sheet

i.

去掉描述中最后的句号

Part8: Comments sheet

i.

填补Comment sheet中Description 的数据集描述

注意没有数据的变量在此处进行说明"未收集到数据"

项目处理 Page 42

ii.

注意没有数据的变量在此处进行说明"未收集到数据"

<span class="unresolved">[<xsl:value-of select="$whereOID"/>]</span>

1.

去掉incl处的“[]”

PARAMN&gt;=2 and PARAMN&lt;=8
2&lt;=PARAMN&lt;=8

102&lt;=AVISITN&lt;=107

项目处理 Page 43

中文define2-1-0.xsl

2023年9月28日

16:21

打开Notepad++打开进行编辑：

1.

DataType翻译，共3处，加这段code：
    <!-- add -->
    <xsl:if test="$g_seqItemDefs[@OID=$whereRefItemOID]/@DataType='text'">

  <td>字符型</td>
</xsl:if>
<xsl:if test="$g_seqItemDefs[@OID=$whereRefItemOID]/@DataType='integer'">
  <td>整数型</td>
</xsl:if>
<xsl:if test="$g_seqItemDefs[@OID=$whereRefItemOID]/@DataType='float'">
  <td>浮点型</td>
</xsl:if>
<xsl:if test="$g_seqItemDefs[@OID=$whereRefItemOID]/@DataType='datetime'">
  <td>日期时间型</td>
</xsl:if>
<xsl:if test="$g_seqItemDefs[@OID=$whereRefItemOID]/@DataType='date'">
  <td>日期型</td>
</xsl:if>
<xsl:if test="$g_seqItemDefs[@OID=$whereRefItemOID]/@DataType='time'">
  <td>时间型</td>

    </xsl:if>
   <!-- add end -->

2.

OriginType、OriginSource翻译，1处，加这段code：
     <div class="linebreakcell">
        <xsl:if test="$OriginPrefix != '0'">
          <span class="prefix"><xsl:value-of select="$PREFIX_ORIGIN_TEXT"/></span>
        </xsl:if>

<!--  add -->

    <xsl:if test="$OriginType='Protocol'">

                      <xsl:text>方案</xsl:text>
            </xsl:if>
            <xsl:if test="$OriginType='Derived'">
                      <xsl:text>衍生</xsl:text>
            </xsl:if>
            <xsl:if test="$OriginType='Assigned'">
                     <xsl:text>指定</xsl:text>
            </xsl:if>
            <xsl:if test="$OriginType='Collected'">
                      <xsl:text>收集</xsl:text>
            </xsl:if>
            <xsl:if test="$OriginType='Predecessor'">
                      <xsl:text>继承</xsl:text>
            </xsl:if>

<!--  add end -->

        <!--  Define-XML v2.1 -->

<xsl:if test="$OriginSource">

          <xsl:text> (</xsl:text>
          <span class="linebreakcell">源:

项目处理 Page 44

          <span class="linebreakcell">源:

  <xsl:if test="$OriginSource='Sponsor'">
  <xsl:text>申办方</xsl:text></xsl:if>
  <xsl:if test="$OriginSource='Investigator'">
  <xsl:text>研究者</xsl:text></xsl:if>
  <xsl:if test="$OriginSource='Vendor'">
  <xsl:text>供应商</xsl:text></xsl:if>
  <xsl:if test="$OriginSource='Subject'">
  <xsl:text>受试者</xsl:text>

</xsl:if>  </span>

          <xsl:text>)</xsl:text>
        </xsl:if>

3.

Purpose翻译，1处，加这段code：
      <td>
        <xsl:value-of select="@def:Structure"/>
      </td>
      <td>
        <xsl:if test="@Purpose='Tabulation'">
          <xsl:text>制表</xsl:text>
        </xsl:if>
        <xsl:if test="@Purpose='Analysis'">
          <xsl:text>分析</xsl:text>
        </xsl:if>
      </td>
      <td>
        <xsl:call-template name="displayItemGroupKeys"/>
      </td>

4.

Class、Subclass翻译
搜索关键字"<def:Class"，通过xsl:when 进行翻译
SUBJECT LEVEL ANALYSIS DATASET  -->  受试者水平分析数据集
BASIC DATA STRUCTURE                    -->  基本数据结构
ADAM OTHER                                      -->  ADAM 其它
OCCURRENCE DATA STRUCTURE     -->  事件发生数据结构
TRIAL DESIGN                                          -->  试验设计

SPECIAL PURPOSE                                  -->  特殊用途

INTERVENTIONS                                      -->  干预类

EVENTS                                                  -->  事件类

FINDINGS                                               -->  发现类

RELATIONSHIP                                       -->  关系类

搜索关键字"<def:SubClass"，或者直接替换
TIME-TO-EVENT                                 -->  事件发生时间
ADVERSE EVENT                         -->  不良事件

项目处理 Page 45

Compute Method

2024年7月24日

11:58

--SEQ
EPOCH
--DY
--BLFL
--LOXBLFL

项目处理 Page 46

修改code地方

2024年7月25日

10:46

项目处理 Page 47

P21 bugs

2024年7月25日

11:54

1.

Repeat comments when converting

excel spec to define.xml

From <https://www.pinnacle21.com/forum/repeat-comments-when-converting-excel-spec-definexml>

2.

sdtm中排序变量添加supp qnam

Potential Define 2.1 Validation

bugs with rules DD0004, DD0007,

DD0011, and DD0124

From <https://www.pinnacle21.com/forum/potential-define-21-validation-bugs-rules-dd0004-dd0007-dd0011-and-
dd0124>

3.

项目处理 Page 48

TLF
2019年9月27日, 星期五

9:49

1.

Display for TL

a.

b.

c.

d.

e.

变量选择：Listing中在可选择的情况下尽量使用CRF对应结果，除非特别要求。比如单位改变，结果是derived

列对齐: 主要使用左对齐， 但为了美观，保证相邻列有足够空白分隔，也可尝试居中或居右。如果效果还不理想可以考虑增加空白列（不需要输出到数据集）。

小数点对齐：如无特别说明将不执行小数点对齐

排序: 如无特别说明，请根据CRF中的展示顺序对子类进行排序；如CRF无展示，可以按照总计数逆序排列，同一计数则按拼音字母顺序。

单项展示：找到CRF中对应信息，通常只需要列出总数非零的单项，但有的项目也要求完整列出，请和统计师确认。

f.

分页：尽量保证同一页展示完整的一块（block),方便阅读，同时又不会留下太多空白

g.

h.

i.

j.

k.

l.

填补通常是为Table准备的，如无特别说明请不要体现在Listing中。比如AE/CM日期填补（xxDY计算），缺失填补都需要在listing中使用填补前结果

未编码：Table中：AEDECOD='~'||AETERM, AESOC='未编码'/ CMDECOD='~'||CMTRT, ATC2='未编码'；Listing中统一留空

计划外访视：计划外访视在SDTM/ADaM中一般会是VISIT=xxx 计划外访视 x, 但listing中只需要表示为'计划外访视',同时保证排序为时间顺序,通常VISITNUM可以控制排序。

亚标题（subtitle)是否加粗，只要项目内保持一致就好了:

a.

b.

默认style是加粗

重新设置不加粗，"@S={fontweight=mediun}xxxxx" or @{style[fontweight=medium]xxxxx}"

最高CTCAE计算3~4级和3~5级对应例数要先去重再归类，这样4级和5级同时存在只计算在3~5级

作图时增加语句提前判断坐标轴是否设置合理

m.

>5% TEAE SOC/PT表只要在完整TEAE表中取出满足条件的行，不需要ADAE删除记录后重新计算，否则影响SOC行。需和统计确认是否需要单独的SOC>5%行

n.

o.

p.

因数据不足导致基线后没有CHG, 可以通过在table中dummy CHG部分

Unicode中排序注意使用sortseq=LINGUISTIC( COLLATION = PINYIN) 保证实现按照拼音排序

因REPORT Procedure改变数据排序后不易于发现，要求QC REPORT语句中输出的数据集

项目处理 Page 49

易错点

2023年6月2日

18:06

表格（Table)

1.

2.

选错population

subgroup用错bigN和分母

列表（listing)

1.

2.

3.

unschedule没有按照日期排序

不良事件，伴随用药没有按照发生日期排序

分页或分行不合理

图表(Figure)

1.

2.

坐标轴不够

颜色没有统一

项目处理 Page 50

命名规则

2022年7月12日

15:30

1.

Naming in TLG process:

Table 14.1.1 Summary of Dose-Limiting Toxicities (DLT)

Programming: t-dlt-summ.sas <abbreviate the title in the name, not the full table number as before >

Output dataset: t140101dltsumm.data7bdat <Remove ‘-’ from RTF name>
data _null_;
    set metadata.headfooter;
    where lowcase(scan(pgmname,1,'.'))=lowcase(substr(scan("&_pgmname",1,'.'),ifn(find("&_pgmname","qc-",'I'),4,1)))
and pgmid="&pgmid";
    call symputx("output",compress(filename,'-_'));
run;

Output RTF: t-14-01-01-dlt-summ.rtf

Validation code: qc-t-dlt-summ.sas <It’s better to be the same as dev code name with prefix ‘qc-’>

Compare result: qc-t-dlt-summ.lst

2.

Variables for TL dataset (Figure不适用，可自行定义合适变量名):

  Only keep below variables based on shell with length=200 for character

subtitle1, ……, subtitlen, (character,通常适用于存在小title的TL，否则不适用)
col1, col2,……, coln, (character)
bign1,……,bignn (numeric,通常是分母，在亚组分析中会根据亚组变化)

Below is the COMPARE Procedure for validation. You can remove leading blank of data or whole blank line
for output format before comparison.
proc compare base=t140101dltsum compare=qc_t140101dltsum listall;
run;

Blank table: <Only for table/listing dataset>
The same variables when it’s not blank. But one row with all variables missing. Below code can help add blank row.

data dummy1;

          if nobs1>0 then set dummy1 nobs=nobs1;

run;

Dummy1 is the blank table, dummy2 is not blank.

项目处理 Page 51

Dummy1 is the blank table, dummy2 is not blank.

项目处理 Page 52

小数位数

2020年3月2日, 星期一

12:07

1.

小数位数如无特别说明按照以下执行

统计量

小数位数保留规则

百分比(percent)

保留一位小数。100不保留小数位数，0不显示百分比结果

例数(n)

算数均值(mean)

标准差(std)

标准误(SE)

中位数(median)

0

X+1

X+2

X+2

X+1

几何均值(Gmean)

X+1

四分位数(quantile)

X+1

最小值(min)

最大值(max)

变异系数(CV)

X

X

1

置信区间(CI)

X+1

P值(p-value)

保留4位。小于0.0001，则显示<0.0001; 大于0.9999， 则显示>0.9999

1. 所有统计量保留的最大位数不超过3位

2. 衍生的变量按照原始变量X+1保留小数位数

3. 如果n=0,其他统计量留空；如果n=1，标准差和变异系数为NA

4. 如无特别说明，血药浓度，血药参数（Cmax, AUC, CL/F, Vd/F等)及其统计描

述结果（CV除外，保留一位)都将保留3位有效数字. 但是Tmax, t1/2, AUC_%

extrap和F按照实际小数位数处理，比如2位小数

项目处理 Page 53

%RowWrap 宏说明

2019年11月18日, 星期一

12:55

%RowWrap 需要在PROC REPORT之前使用，同时和REPORT保持一致，如果REPORT调整需要记得同时调整%RowWrap对应参数

%rowwrap(

  data_in=test, /*输入和输出数据集*/

  groupby= ,  /*排序变量，需要包括后面的pageby, skipby,blockby 对应参数。与REPORT里面的

order/group变量（Page变量除外）保持变量个数和顺序一致 */

  pageby= ,   /*REPORT中的最后一个分页变量（Page变量除外） */

  skipby= ,   /*REPORT中的最后一个加空行变量（Page变量除外） */

  blockby=,   /*REPORT中的最后一个控制block变量（Page变量除外） */

  fsize=10,     /*字体大小*/

  pageno=page,   /*保存计算的分页结果变量*/

  row_display=25,   /*计划的每页显示行数，若分页有问题一般是按需调整该数值*/

  minrow=,   /*每个观测最小行数，通常留空*/

  fstyle=Times， /*字体: Times = Times New Roman; Cour = Courier New */

  _rowandinch=%bquote(_com|3]lbtest|2]) /*REPORT中每个变量定义的长度，注意单位为inch*/

);

项目处理 Page 54

Intext table

Monday, December 20, 2021

10:16 AM

1.

2.

3.

Intext table 不进行分页，故pageof 相关code可以在%rtfinit里面去掉

去掉单个程序中的分页变量xxx(避免多加空白行)和分页语句 break after xxx/page;

Subtitle table需要调整%rtfpost，用于去掉中间的title和footnote

a.

b.

增加参数&subtitn, 定义最后一个subtitle是第几个title

检查&_pgs是否需要调整关键词

c.

添加以下code,
*** Deal with title and footnote;
%if &subtitn>0  %then %do;
    retain _n_titfoot _del_titfoot _subtit 0;
    if find(line,'\sectd\') then _subtit=1;
    if line='{\par}' then _subtit+1;
    if find(line,'{\pard\plain') then do;
        _n_titfoot+1;
        _del_titfoot=1;
    end;
    if _subtit=&subtitn and _n_titfoot>=1 then do;
        if line='{\par}' or line='{ }}}'  then line='{\page}';
        _del_titfoot=0;
    end;

    if _del_titfoot=1 and _n_titfoot<&_pgs then delete;
%end;

项目处理 Page 55

Shift 表（治疗组人数为分母）

2019年11月12日, 星期二

14:01

假定'未查’为无效结果的代表，保留在xxSTAT/xxREASND中。

方法一：

1.

2.

3.

4.

5.

6.

7.

8.

9.

通过ADSL人群dummy出全部参数（PARAM)以及对应基线（Baseline)和基线后访视(AVISIT)（ADLB中得到PARAM/AVISIT,通过SQL笛卡尔合并）

根据SUBJECT,PARAM和AVISIT横向合并（merge)数据集（i.e., ADLB），取到ACLSIG/BCLSIG, 仅保留（1）中记录

若（2）中ACLSIG为缺失请填补‘未查’

若（2）中BCLSIG为缺失请填补为上一个非缺失值（包括未查），对于基线直接赋值为ACLSIG

计算PARAM,AVISIT,TRT,BCLSIG和ACLSIG下的例数，仅保留基线后的ACLSIG

根据PARAM,AVISIT和TRT dummy出BCLSIG和ACLSIG的全部组合，然后和（5）中数据横向（merge)合并，缺失值补0

（6）中结果对ACLSIG转置,然后添加合计行和列

检查‘未查’行对应的合计列值，如果为零即删除。偶尔存在非零

检查‘未查’列，如全部为零可以不输出。偶尔存在全零

方法二：

1.

2.

3.

4.

5.

6.

7.

8.

9.

计算治疗组人数（bigN)，造dummy数据包含PARAM和基线全部有效分类

计算PARAM和TRT下基线有效分类人数（合计列），根据PARAM，TRT和基线分类横向合并（1）数据，缺失值填补为0

添加基线内‘未查’行分类=bigN-基线各有效分类和，‘合计’行=bigN

将（3）中数据按照数据（ADLB)现有PARAM基线后访视dummy出全部有效分类(建议使用SQL笛卡尔合并）

计算PARAM，TRT以及基线分类下基线后访视各有效分类人数

若（5）中基线分类有空值，请调整为'未查'，然后根据PARAM，TRT，基线分类，基线后访视和基线后分类横向合并（4）中数据

（6）中缺失值填补为0，然后根据PARAM，TRT，基线分类和基线后访视将基线后分类例数转置

添加‘未查’列=基线分类-对应行基线后各分类和

添加‘合计’行=治疗组以及基线后访视例数和

10.

检查‘未查’行对应的合计列值，如果为零即删除。偶尔存在非零

11.

检查‘未查’列，如全部为零可以不输出。偶尔存在全零

项目处理 Page 56

-0.00处理

2023年5月30日

13:28

1.

2.

默认不处理，可以解释 --保留负号表示结果偏向于负数方

如果客户要求处理可以参考下面的code, 保留小数位数为3位时

data chk;

    a=-1e-4;

    a1=strip(put(a,15.3)); *常规做法保留负号;

    b1=strip(put(round(a,0.1**3),15.3)); *去负号方法1;

    b2=strip(put(input(strip(put(a,15.3)),best.),15.3)); *去负号方法2;

    put a1= b1= b2=;

run;

项目处理 Page 57

BLOQ处理

2020年1月7日, 星期二

10:00

BLOQ在PK浓度总结（包括平均曲线浓度图）和个人曲线浓度/PK参数计算时会有不同的处理原则。在
通常的PK浓度总结描述时，前者都视作0为计算，更多的是从“均值”等统计量考虑的，若考虑PK参
数计算的时候一样的规则：在Tmax之后视作缺失，在曲线的消除相后期的时间点，往往会出现后面时
间点的均值（因BLOQ太多）会高于前面时间点的均值。主要是这样的考虑。

也附上PK分析中常用的BLOQ的处理原则供您参考：

The following general rules are applied in all cases (以下NQ等同于BLOQ);

1)

2)

NQs at the beginning of a subject profile (i.e. before the first incidence of a measurable concentration) are
deemed to be zero as it is assumed that in this circumstance no drug is yet measurable in the blood.
For NQs at the end of the subject profile (i.e. after the last incidence of a measurable concentration);

a.

b.

for individual plots and pharmacokinetic analyses these are dropped (set to missing) as they do not
provide any useful information (and can erroneously indicate that absolutely no drug is present)
for summary statistics these are set to 0 (to avoid skewing of the summary statistics)

项目处理 Page 58

Patient Profile Listing(PPL)

2022年11月24日

13:54

方法一：直接输出PPL

1.

2.

3.

4.

5.

6.

7.

8.

根据shell准备对应listing数据集，数据集中应该保留公共变量并做好排序，公共变量不限于subjid, trtsdt,

trt01p。其他变量按照常规命名col1, col2, ….

建议同时输出永久数据集用于QC, 临时数据集用于下一步的Report. 辅助变量可以仅在临时数据出现

如果是多人合作，需要各自准备REPORT Procedure, 保证输出能和shell一致，subjid可以作为by 变量使用。

否则可以跳过该步

不建议单个程序使用%rtfinit，title和footnote可以写在程序中

通过%include 或 macro形式调用#2对应的程序，生成数据集备用

提取每个subjid的信息, 通过多个REPORT Procedure结合macro循环实现每个subjid一个RTF文件。可以直接

截取#3的程序

可以修改%rtfinit 和 %rtfpost以满足PPL需求，或者直接在程序中实现

除非有要求，否则不建议一页放多个列表

方法二：先按照每人每个列表一个RTF文件输出，然后通过subjid合并得到PPL

1.

2.

3.

4.

根据shell准备对应listing数据集，数据集中应该保留公共变量并做好排序，公共变量不限于subjid, trtsdt,

trt01p。其他变量按照常规命名col1, col2, ….

建议同时输出永久数据集用于QC, 临时数据集用于下一步的Report. 辅助变量可以仅在临时数据出现

单个程序中通过macro循环实现每个subjid输出一个RTF文件，文件命名可以加上subjid作为前缀方便后续合并

根据subjid合并对应的RTF文件

项目处理 Page 59

DRR listing

Wednesday, January 19, 2022

4:44 PM

•

•

•

•

msetup新加misc_drr逻辑库存放drr listing sas 数据集

用headfooter excel 整理好headfooter_drr excel

导入headfooter_drr excel生成metadata_headfooter）

Notepad 对listing程序关键字统一替换(包括：metadata_headfooter-->metadata_headfooter_drr,

rtfinit-->excelinit, 删除rtfpost macro)

•

以下几点更新程序时注意下：

a.

b.

c.

d.

DEV: DRR listing 程序中统一还需要删除%rtfpost

DEV, QC注意下metadata 和 数据集输出逻辑库名

%rtfinit 换成 %excelinit

listing 中合并的列需要拆分出多个列，方便单列筛选信息和查看（如：SOC/PT, 日期（治疗日））

项目处理 Page 60

Report

Tuesday, September 14, 2021

3:14 PM

1.

Background color

项目处理 Page 61

9999_新人QC 检查与发现

Thursday, October 28, 2021

4:13 PM

1.文档填写：

•

统计编程状态记录表

○

○

○

qc状态分为N/A, Pending, Started, Completed, Passed

Qc 状态非N/A, Pending 需要填写上对应状态填写时间（Date Validated), 若QC完成但没有通过则

为Completed, 若通过QC则为Passed. 若有comments，则填写对应comments并描述清楚具体的

问题；若无comments，则填写"No comments"

在QC completed 完成后，若有comments，在dev 进行更新之后（dev 会回复comments"-已更

新")，QC需要再对comments核对，审阅无意见，可更新为"Passed"

•

统计问题记录表

○

用描述语言对问题进行描述，如果涉及到数据的引用，尽量描述清楚

•

数据问题记录表

○

用描述语言对问题进行描述，如果涉及到数据的引用，尽量描述清楚（尽量不要写第几行，第几列这

类描述，用受试者，访视，检查项目，检查日期（事件开始日期）等描述清楚，可以在文字后加上

EDC中变量名）

2.程序编写

•

•

程序Header(按照template 以及项目leader要求进行统一，注意程序名，客户名等信息不要填写错误)

程序按照GPP

○

○

○

○

○

○

○

缩进，换行，同一行代码长度（缩进不要用Tab 键进行)

不需要出现libname与绝对路径

Length 一般放在data 步后，且格式为"length xxx $200;"，不需要在最后加点

一般不要添加options

尽量少用rename

多余的备注与代码可以在最后保存前删除

QC尽量用于DEV不同的macro

•

程序逻辑

○

ABLFL-->在判断时间后，需要判断对应时点上的检查结果是否是有效值

•

○
TLFs
○

○

○

○

○

○

○

CHG-->针对基线后进行赋值，基线及基线前暂时统一不赋值

Header填写需要准确完整

程序开始需要有清理日志，清理输出代码：DM 'OUTPUT; CLEAR; LOG; CLEAR;';

特殊数值的考虑（①n=1时，对应的std需要用"NA"或"-"进行描述，根据项目lead 统一来确定；②

频数百分比的格式需要统一；③P值的格式；④如果对应分组有受试者，但具体访视没有，需要列出

例数，其他统计量保留空）

分页问题：（①尽量铺满页面；②有分block的table需要尽量同一个block放在同一页）

subtitle使用不要覆盖原始title，footnote 的完整性

逃逸字符，换行尽量不要使用"^"

人群标志：安全分析集，PK分析集都需要用实际治疗变量（TRTA,TRT01A)，其他人群用计划治疗变

量

项目处理 Page 62

    rename cmtrt_ad=cmtrt;
    rename cmdosu_oth=cmdosuo;
    rename cmdosfrm_oth=cmdsfrmo;
    rename cmdosfrq_oth=cmdsfrqo;
    rename cmroute_oth=cmrouteo;
    rename cmindc_ad=cmindc;
    rename cmaeno_ad=cmaeno;
    rename cmmhno_ad=cmmhno;
    rename cmindc_oth=cmindco;
    rename trt01p=trtp;
    rename trt01a=trta;

GTL
2024年8月1日

9:23

https://www.cnblogs.com/SAS-T/p/15580406.html

项目处理 Page 63

Deviation规范

2019年12月5日, 星期四

14:49

1.

2.

3.

4.

5.

偏离定义编程部分通常包括入选标准，排除标准，终点检查，试验药物使用，访视窗口，缺失检查

DV中只考虑入组人群, 从EDC数据直接开始，不考虑cutoff

不调整DVTERM, DERIVATION中用具体变量替代DVTERM中所需部分。对于复杂衍生规则，可以使用临时变量

程序和输出数据集命名 dv_partxx。 xx代表DVSPID整数部分，不足补0。空数据集输出一条空记录。

缺失检查：如果没有访视本身（raw.sv)缺失的检查，则需要根据最后访视dummy出该受试者的完整计划访视进行检查。此时如

果某个访视缺失，该访视下的全部试验过程都需要分别输出一条缺失PD。否则一条PD就够了

6.

时间窗：

实际发生相对时间ARELTM=ADTM-TRTSDTM，如果给药前在窗口内(-30<=ARELTM<=0)则ARELTM=0

偏差DEVIAT=ARELTM-计划相对时间(ATPT)。给药前的计划相对时间是0。

超窗(OUTWIN)=

a.

b.

c.

DEVIAT-左窗口, 如果DEVIAT<左窗口

DEVIAT-右窗口,  如果 DEVIAT>右窗口

OUTWIN=0, 如果 左窗口<=DEVIAT<=右窗口

项目处理 Page 64

Macro

2022年4月15日

19:38

项目处理 Page 65

%RowWrap 宏说明

2019年11月18日, 星期一

12:55

%RowWrap 需要在PROC REPORT之前使用，同时和REPORT保持一致，如果REPORT

调整需要记得同时调整%RowWrap对应参数

%rowwrap(

  data_in=test, /*输入和输出数据集*/

  groupby= ,  /*排序变量，需要包括后面的pageby, skipby,blockby 对应参数。与

REPORT里面的

order/group变量（Page变量除外）保持变量个数和顺序一致 */

  pageby= ,   /*REPORT中的最后一个分页变量（Page变量除外） */

  skipby= ,   /*REPORT中的最后一个加空行变量（Page变量除外） */

  blockby=,   /*REPORT中的最后一个控制block变量（Page变量除外） */

  fsize=10,     /*字体大小*/

  pageno=page,   /*保存计算的分页结果变量*/

  row_display=25,   /*计划的每页显示行数，若分页有问题一般是按需调整该数值*/

  minrow=,   /*每个观测最小行数，通常留空*/

  fstyle=Times， /*字体: Times = Times New Roman; Cour = Courier New */

  _rowandinch=%bquote(_com|3]lbtest|2]) /*REPORT中每个变量定义的长度，注意单

位为inch*/

);

项目处理 Page 66

Mergepk

2025年2月27日

17:37

编程生成Merged pk excel用于PK实验室计算PK参数

1.

在../data, ../prog, ../qcprog 文件夹下建立“mergepk" 子文件夹用于

merge pk 编程产生的sas数据，程序，日志以及输出结果

2.

根据edc数据与pc 浓度外部数据挑选excel template中适用的变量进行

xxxxx
Merged PK

编程拼接，并输出excel文件

项目处理 Page 67

PK 参数

2019年9月19日, 星期四

13:11

描述 (单次）

Cmax 达峰浓度，为实测值

Tmax 达峰时间，为实测值

PPTESTCD PPTEST

Digital/Decimal

CMAX

Max Conc

TMAX

Time of CMAX

3 Digitals

2 Decimal

AUC0-t   从零到最后可测量血药浓度-时间曲线下面积，

AUCLST

AUC to Last Nonzero Conc

3 Digitals

采用梯形法计算：AUC(i, i+1)=(ti+1-ti)(Ci+Ci+1)/2，AUC为所有AUC(i, i+1)之和

AUC0-∞ 从零到无穷大血药浓度-时间曲线下面积,

AUCIFO

AUC Infinity Obs

3 Digitals

AUC0-∞=AUC0-t + Ct/λz (Ct为最后一个可测得时间点的血药浓度)

AUC_%extrap 外推面积百分比

AUCPEO

AUC %Extrapolation Obs

2 Decimal

λz   末端消除速率常数，由消除相浓度点取半对数线性回归而得

LAMZ

Lambda z

3 Digitals

t1/2  末端消除半衰期，按下式计算：t1/2=Ln(2)/ λz

LAMZHL

Half-Life Lambda z

2 Decimal

CL/F 表观机体总清除率。CL/F = 给药剂量/ AUC0-∞，F表示考虑了生物利用度

CLFO

Total CL Obs by F

Vd/F 表观分布容积。Vd/F = CL/F/λz，F表示考虑了生物利用度

VZFO

Vz Obs by F

3 Digitals

3 Digitals

F 相对生物利用度，按下式计算： F=AUC0-t（受试制剂）/AUC0-t（参比制剂) *100% FREL

Relative Bioavailability

2 Decimal

MRT0-∞从零到无穷大平均滞留时间

MRTIVIFO MRT Intravasc Infinity Obs

2 Decimal

R2_adjusted<0.8 或 AUC_%extrap>20%时，消除相相关参数（AUC0-∞ , λz, t1/2, AUC_%extrap,CL/F, Vd/F)将不参与统计分析，需要和统计师确认

描述 (多次）

Cmax,ss 稳态下峰浓度

Cmin,ss 稳态下谷浓度

Cavg,ss 稳态下平均浓度

PPTESTCD PPTEST

Digital/Decimal

SSCMAX Max Conc at Steady State

3 Digitals

SSCMIN

Through Conc at Steady State

3 Digitals

SSCAVG

Ave Conc at Steady State

3 Digitals

Ctau 稳态下给药间隔时间点的血药浓度

CTAU

Conc at Dosing Time Plus Tau

3 Digitals

Tmax,ss 稳态下达峰时间

SSTMAX

Time of CMAX at Steady State

2 Decimal

AUC0-t,ss   稳态下从零到最后可测量血药浓度-时间曲线下面积 SSAUCLST AUC to Last Nonzero Conc at SS

3 Digitals

AUCtau   稳态下给药间隔内的血药浓度-时间曲线下面积

AUCTAU

AUC at Steady State Dosing Interval

3 Digitals

Ctrough是稳态时给药间隔最后的浓度（即全部给药前的浓度统称，不包括首次），直接在ADPC筛选

项目处理 Page 68

Oncology

Friday, October 30, 2020

9:06 AM

Overall Survival(OS, 总生存期) is defined as the time from randomization until death from any cause.

Progression-Free Survival(PFS,无进展生存期) is defined as the time from randomization until objective tumor progression or death, whichever occurs first.
Censor to the last available tumor assessment when alive with no PD.

Time to Progression(TTP, 疾病进展时间) is defined as the time from randomization until objective tumor progression, not include deaths.

Duration of Response (DOR, 持续缓解时间) is defined as the time from the date criteria are firstly met for CR or PR to the first documentation of PD or
death due to disease, whichever occurs earlier.

Disease-Free Survival (DFS, 无病生存期) is defined as the time from randomization until disease recurrence or death from any cause

Time to Response(TTR, 至缓解时间) is defined as the time from randomization to firstly met objective response (CR or PR).

Objective Response Rate(ORR, 客观缓解率) is defined as the proportion of patients with best overall response as complete response (CR) or partial
response (PR) and with minimum duration.

Disease Control Rate (DCR, 疾病控制率) is defined as the proportion of patients with best overall response as complete response (CR), partial response
(PR) or stable disease (SD) and with minimum duration

Best Overall Response (BOR, 最佳总体疗效) : The best overall response on or before first PD, death and new anti-cancer therapy. The selective order is CR>
PR>SD>PD>NE.

肿瘤颜色一般CR limegreen，PR deepskyblue，SD orange，PD red，NE purple

项目处理 Page 69

OS

Monday, December 13, 2021

1:11 PM

出现描述

删失日期描述(CNSDTDSC) 事件或删失

逻辑定义

(EVNTDESC)

死亡

试验截止时生存

最后存活日期

事件

删失

DTHDT有值

DTHDT缺失

ADSL

DTHDT (死亡日期)

LSTALVDT(已知最后生存日期): 受试者排除不相关的收集日期后取到的最大日期。死亡受试者为死亡前(包含)的最大完整日期，利于填补死亡日期。

  排除日期举例包括但不限于：

1.

2.

3.

4.

试验因失访结束的日期

生存随访中死亡或失访对应的随访日期

研究者阅片日期

样本检测日期

项目处理 Page 70

PFS

2021年7月5日

22:04

出现描述(EVNTDESC)

删失日期描述(CNSDTDSC) 事件或删失

逻辑定义

疾病进展

死亡

事件

FSPDDT有值 and (FSPDDT<=NEWATSDT or NEWATSDT缺失) and MMISPDFL

^= 'Y'

事件

FSPDFL 缺失and DTHDT有值 and (DTHDT=NEWATSDT or NEWATSDT缺失)

试验截止日前无进展

末次有效病灶检查日期

无基线或基线后肿瘤评估且数据截止时仍生存

入组日期

开始采用新抗肿瘤药物治疗前无进展或死亡

末次有效病灶检查日期

删失

删失

删失

and  MMSDTHFL ^= 'Y'

FSPDFL，DTHDT和NEWATSDT都缺失 and LSNPD1FL= 'Y'

FSPDFL，DTHDT和NEWATSDT都缺失 and LSNPD1FL 不存在 'Y'

LSNPD2FL= 'Y' and NEWATSDT有值 and (NEWATSDT<min(FSPDDT,DTHDT)

or  (FSPDDT和DTHDT都缺失) )

开始采用新抗肿瘤药物治疗前无进展或死亡且不存在

入组日期

删失

LSNPD2FL 不存在 'Y' and NEWATSDT有值 and

末次有效病灶检查

(NEWATSDT<min(FSPDDT,DTHDT) or  (FSPDDT和DTHDT都缺失) )

遗漏一次以上随访后进展或死亡

末次有效病灶检查日期

删失

LSNPD1FL= 'Y' and (MMISPDFL ='Y' or MMSDTHFL='Y') and

(min(FSPDDT,DTHDT)<=NEWATSDT or NEWATSDT缺失)

遗漏一次以上随访后进展或死亡且不存在末次有效病

入组日期

删失

LSNPD1FL 不存在 'Y' and (MMISPDFL ='Y' or MMSDTHFL='Y')  and

灶检查

(min(FSPDDT,DTHDT)<=NEWATSDT or NEWATSDT缺失)

注：NE 不包括在有效病灶评估中(需和统计师确认)

      入组日期可以是随机日期或用药开始日期

      末次有效病灶检查日期为PD, 死亡和新的抗肿瘤治疗前的末次非PD评估日期, i.e, min(LSNPD1DT, LSNPD2DT)

      一般认为新的抗肿瘤治疗当天的评估或死亡和新抗无关

     程序实现ADTTE的时候可以将变量按照受试者横向合并，保留ADRS标记了flag的相关变量

ADRS

FSPDFL (首次PD评估标记）/ FSPDDT (首次PD评估日期) ：首次PD出现，ADRS中不用考虑其他条件

LSNPD1FL (末次非PD评估标记 1）/ LSNPD1DT (末次非PD评估日期 1) ：标记在首次PD前的最后非PD评估，不包括NE

LSNPD2FL (末次非PD评估标记 2）/ LSNPD2DT (末次非PD评估日期 2) ：标记在新的抗肿瘤治疗前或当天的最后非PD评估，不包括NE

MMISPDFL (遗漏多次评估后PD标记) : 如果FSPDDT - max(LSNPD1DT, 入组日期) > 2*评估间隔 将标记首次PD上

ADSL

DTHDT (死亡日期)

MMSDTHFL (遗漏多次评估后死亡标记) : 死亡前最后一次评估不为PD并且DTHDT-max(最后评估日期，入组日期) > 2*评估间隔，则标记。评估不包括NE

NEWATSDT (新的抗肿瘤治疗开始日期) : 新的肿瘤治疗最小日期，可能需要填补。需要确认是否考虑手术，放疗等局部治疗

如果存在ADEFF，遗漏多次评估后死亡和PD标记可以放在ADEFF里

项目处理 Page 71

DOR

2021年12月12日

22:59

如果有confirm, 人群按照confirmed CR/PR, 开始日期按照收集的第一次CR/PR算

出现描述(EVNTDESC)

删失日期描述(CNSDTDSC) 事件或删失

逻辑定义

疾病进展

死亡

事件

FSPDDT有值 and (FSPDDT<=NEWATSDT or NEWATSDT缺失) and MMISPDFL

^= 'Y'

事件

FSPDFL 缺失and DTHDT有值 and (DTHDT=NEWATSDT or NEWATSDT缺失)

试验截止日前无进展

末次有效病灶检查日期

开始采用新抗肿瘤药物治疗前无进展或死亡

末次有效病灶检查日期

删失

删失

and MMSDTHFL ^= 'Y' and CDTHDIFL='Y'

FSPDFL, CDTHDIFL 和NEWATSDT都缺失 and LSNPD1FL= 'Y'

LSNPD2FL= 'Y' and NEWATSDT有值 and (NEWATSDT<min(FSPDDT,DTHDT)

or  (FSPDDT和DTHDT都缺失))

遗漏一次以上随访后进展或死亡

末次有效病灶检查日期

删失

LSNPD1FL= 'Y' and (MMISPDFL ='Y' or (CDTHDIFL='Y' and MMSDTHFL='Y'))

and ( min(FSPDDT,DTHDT)<=NEWATSDT or NEWATSDT缺失)

注：NE 不包括在有效病灶评估中(需和统计师确认)

      末次有效病灶检查日期为PD, 死亡和新的抗肿瘤治疗前的末次非PD评估日期, i.e, min(LSNPD1DT, LSNPD2DT)

    一般认为新的抗肿瘤治疗当天的评估或死亡和新抗无关

   程序实现ADTTE的时候可以将变量按照受试者横向合并，保留ADRS标记了flag的相关变量

ADRS

FSPDFL (首次PD评估标记）/ FSPDDT (首次PD评估日期) ：首次PD出现，ADRS中不用考虑其他条件

LSNPD1FL (末次非PD评估标记 1）/ LSNPD1DT (末次非PD评估日期 1) ：标记在首次PD前的最后非PD评估，不包括NE

LSNPD2FL (末次非PD评估标记 2）/ LSNPD2DT (末次非PD评估日期 2) ：标记在新的抗肿瘤治疗前或当天的最后非PD评估，不包括NE

MMISPDFL (遗漏多次评估后PD标记) : 如果FSPDDT - max(LSNPD1DT, 入组日期) > 2*评估间隔 将标记首次PD上

ADSL

DTHDT (死亡日期)/CDTHDIFL (疾病原因导致死亡)

MMSDTHFL (遗漏多次评估后死亡标记) : 死亡前最后一次评估不为PD并且DTHDT-max(最后评估日期，入组日期) > 2*评估间隔，则标记。评估不包括NE

NEWATSDT (新的抗肿瘤治疗开始日期)：新的肿瘤治疗最小日期，可能需要填补。需要确认是否考虑手术，放疗等局部治疗

DOR 相比较PFS 不同点：

1.

2.

只考虑存在疾病应答的人群 (e.x., PD和新的抗肿瘤之前存在CR/PR 的人群），故LSNPD1DT/LSNPD2DT 一定有值

死亡限制在疾病原因导致的死亡 （CDTHDIFL)

项目处理 Page 72

Confirm Response

2020年6月14日, 星期日

20:42

1. 移除全部NE(需和统计师确认), 然后按照日期降序排列

2. 对日期和response取lag和lag2

3. 计算lag和lag2与当前记录间隔日期。如果lag2的日期间隔不符合条件请报错

4. 如果lag时间间隔不符合要求请使用lag2日期和response

5. 按照RECIST组合对当前访视进行确认, 考虑SD duration

6. 将移除的NE补充回来

项目处理 Page 73

iRECIST
2020年2月8日

10:17

Time Point Response(TPR)

If the criteria for iUPD have never been met, principles follow RECIST 1.1.

However if the criteria for iUPD have been met, the next TPR could be:

iUPD – no change noted in any category of lesion.

iSD, iPR or iCR. Here iUPD (followed by iCPD) must occur again.

iCPD, if the category in which iUPD was met at the last TPR shows further increase in tumour burden as evidenced (as applicable)

by ≥ 5 mm increase in SOM of target or NLT lesions, further increase in NT or NLNT lesions, or an increase in the number of new

lesions.

iCPD of a category which did NOT meet criteria for iUPD now meets the criteria for RECIST 1.1 PD.

The best TPR on or before the new anti-cancer, the response from good to bad, iCR, iPR, iSD, iCPD, iUPD, NE

You can follow the RECIST 1.1 to confirm iCR and iPR









iBOR

iPFS

The duration from randomization to the first progression or death, whichever is first. The first progression(iPD) is defined as the first

iUPD excluding the iUPD before any iCR/iPR/iSD. Otherwise it will be censored as the last available response date as RECIST1.1

项目处理 Page 74

IMWG

2022年10月12日

20:58

Confirm Response:

sCR, CR, VGPR, PR, MR 需要确认，选择较弱的不低于SD的response, 如果无法确认就当作SD

PD确认：PD之后存在其他response该PD无效，否则当作PD <参考iRECIST中iUPD>

项目处理 Page 75

靶病灶评估衍生

2022年12月7日

9:48

1.

ADTR中当PARAMCD="SUMDIAM"时添加以下变量  (假设存在部分病灶缺失时求和总径AVAL缺失)



















NADIR - 既往最小径

NADCHG - 相对既往最小径变化值

NADPCHG - 相对既往最小径变化百分比

TLMISSFL - 存在靶病灶结果缺失标帜

SDIAMNLY - 非淋巴结总径 (mm)  [注: 存在缺失时应为空]

LYMGT10FL - 存在淋巴结直径大于10 mm 标帜

SDIAMNM - 非缺失靶病灶总径 (mm)

NNADCHG - 非缺失总径对NADIR变化值

NNADPCHG - 非缺失总径对NADIR变化百分比

2.

ADRS中添加PARAMCD='TRGRESPD' 判断如下

if SDIAMNLY=0 and LYMGT10FL^='Y' and TLMISSFL^='Y' then AVALC='CR';

else if .<PCHG<-30 and TLMISSFL^='Y' then AVALC='PR';

else if (NADPCHG>=5 and NADPCHG>=20) or (NNADPCHG>=5 and NNADPCHG>=20) then AVALC='PD';

else if TLMISSFL='Y' then AVALC='NE';

else AVALC='SD';

项目处理 Page 76

Communication

2020年1月7日, 星期二

10:24

沟通是信息的分享

1.

2.

3.

4.

5.

了解彼此

带着目的

找准时间

换位思考

求同存异

项目处理 Page 77

