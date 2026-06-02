"""Build mechanics-timeline/index.html - ALL 5 stages."""
import os, html as _html

def esc(text):
    return _html.escape(text, quote=False)

AVATAR_MAP = {"牛津计算者": "津", "牛津计算者学派": "津"}

def avatar_html(figures):
    chars = []
    for f in figures:
        f = f.replace("\u00b7", "").strip()
        if f in AVATAR_MAP:
            chars.append(AVATAR_MAP[f])
        elif f:
            chars.append(f[0])
    return "\n        ".join('<span class="avatar">%s</span>' % c for c in chars)

def fmt_figures(figures):
    return " &amp; ".join(figures)

BASE = "C:/Users/P14S/WorkBuddy/Claw/mechanics-timeline"

CARD = """\
<div class="card">
  <div class="card-portraits">
    {avatars}
  </div>
  <div class="card-header">
    <span class="card-chip">{era}</span>
    <span class="card-figure">{figures}</span>
  </div>
  <div class="card-core">{core}</div>
  <div class="card-fun">{fun}</div>
  <div class="card-insight">{insight}</div>
</div>"""

def gen_cards(rows):
    return "\n".join(CARD.format(
        era=esc(row["era"]),
        avatars=avatar_html(row["figures"]),
        figures=fmt_figures(row["figures"]),
        core=esc(row["core"]).replace("\n", "<br>"),
        fun=esc(row["fun"]),
        insight=esc(row["insight"]),
    ) for row in rows)

# ── ALL STAGE DATA ──

s1_title = "阶段一：起源与奠基（公元前4世纪 — 17世纪初）"
s1_rows = [
    {"era":"希腊科学","figures":["亚里士多德","阿基米德"],
     "core":"1. 亚里士多德（Aristotle，384-322 B.C.）：将力学融入自然哲学体系，提出「力=重量/质量×速度」的动力学定律，定性描述自由落体「重量与下落时间成反比」的规律，区分自然运动（如重物下落）与暴力运动（如抛体运动），主张地心说，认为地球位于宇宙中心，重物趋向地心是自然运动，同时提出虚速度原理的早期雏形，其理论主导西方力学近2000年\n2. 阿基米德（Archimedes，287-212 B.C.）：首次将静力学构建为独立理论科学，基于8条实验公理（如等重等距则平衡、等重不等距则向长力臂侧倾斜等）通过数学演绎证明杠杆原理，提出浮力原理（浸没在流体中的物体受到的浮力等于排开流体的重量），系统计算三角形、抛物线段等几何图形的重心，是经典静力学的基础",
     "fun":"亚里士多德的理论被中世纪经院学者奉为权威，甚至到了14世纪，学者们还在纠结「抛出去的石头为什么不会立刻掉下来」，直到布里丹提出冲量理论才打破这个困局；阿基米德的杠杆原理被后世演绎出「给我一个支点，我能撬动地球」的名言，不过他本人更在意浮力和重心计算，曾用浮力原理帮国王鉴别王冠是否掺假",
     "insight":'亚里士多德的动力学错得离谱，却统治了西方力学近两千年——一个错误答案被当成标准答案用了二十个世纪，可见\u201c信权威\u201d有多危险。阿基米德是另一种路子：先做实验找公理，再拿数学推导，这套方法论今天看平平无奇，但在当时简直是降维打击。他帮国王查王冠掺假这事也说明——很多科学突破，最初不过是为了解决一个具体到不能再具体的麻烦。'},
    {"era":"亚历山大与阿拉伯文献","figures":["希罗","帕普斯","欧几里得"],
     "core":"1. 亚历山大港的希罗（Hero of Alexandria，I世纪 A.D.）：首次在杠杆（含非直杠杆）分析中引入力矩（moment）概念雏形，将轮轴等机械的研究归为圆的原理，隐含力矩的应用逻辑\n2. 帕普斯（Pappus，IV世纪 A.D.）：首次尝试解决斜面平衡问题，借用阿基米德的角杠杆定律推导平衡条件但结果错误，同时给出重心的定义：通过多次悬挂重体确定垂直相交的唯一交点即为重心\n3. 欧几里得伪作《力学问题》：出现「重量×力臂」的力矩定量表述，是静力学的重要早期来源",
     "fun":"希罗的力学著作没有直接流传下来，现在我们看到的版本是阿拉伯学者翻译后回传的，相当于「出口转内销」；帕普斯解不出的斜面平衡问题，被13世纪一个匿名学者轻松搞定，比伽利略、斯蒂文早了足足300年",
     "insight":'帕普斯搞不定的斜面平衡，被13世纪一个连名字都没留下的学者解决了，早了伽利略三百年。这事有两个教训：一是前人的错误不等于白费，后人踩过才知道往哪走；二是你做出再牛的成果，如果没人帮你传播，可能就被埋进故纸堆里。阿拉伯学者帮希腊文献做了个\u201c出口转内销\u201d，功劳比他们自己意识到的都大。'},
    {"era":"13世纪：乔丹努斯学派","figures":["约丹努斯","匿名学者"],
     "core":"1. 约丹努斯（Jordanus de Nemore）：提出「位置重力（gravitas secundum situm）」概念，即重物的「重」与其所处位置相关，本质是虚功原理的雏形，不过其角杠杆平衡推导存在错误，未正确理解力矩概念\n2. 匿名学者（13世纪）：修正了乔丹努斯的角杠杆错误，正确解决了斜面平衡问题，该成果早于斯蒂文和伽利略\n3. 该学派的成就多依赖皮埃尔·迪昂的中世纪手稿发掘才被后世知晓",
     "fun":"13世纪的经院学者们脑子极其敏锐，却偏爱纯逻辑推演，哪怕讨论重物下落也不愿意做实验，觉得「观察太低端」，只有天文学家们老老实实积累观测数据，给后来的力学发展攒下了家底；迪昂发掘中世纪手稿时发现，13世纪学者提出的虚功原理雏形，比后来斯蒂文的正式提出早了300年，直接改写了力学史的认知",
     "insight":'13世纪的经院学者脑子好使得很，虚功原理的雏形都想出来了，偏偏在斜面问题上翻了车——因为死活不肯动手做实验，觉得\u201c纯逻辑推演才高级\u201d。直到迪昂翻中世纪手稿才发现，人家早就摸到了门边，就差临门一脚的实验验证。再聪明的脑子，脱离现实也会跑偏。'},
    {"era":"14世纪：冲量理论","figures":["布里丹","阿尔伯特"],
     "core":"1. 布里丹（John Buridan，1327年任巴黎大学校长）：提出「冲量（impetus）」理论：运动物体被施力时会获得一种内在驱动力，速度越快冲量越强，冲量会持续推动物体运动，直到被介质阻力或重力消耗，是惯性原理的早期雏形，打破了亚里士多德「运动需要持续施力」的缺陷\n2. 萨克森的阿尔伯特（Albert of Saxony，1353年任巴黎大学校长）：区分匀速/非匀速运动，提出匀加速运动的两种可能规律（速度与距离成正比、与时间成正比），讨论地球球形与自由落体加速原因，认为重力不随与地心距离变化，支持冲量理论解释落体加速，同时其重心概念基于竖直线汇交于地心的假设，和现代平行竖直线的重心概念不同",
     "fun":"布里丹为了证明「空气不是抛体运动的动力」，举了一堆生动的例子：旋转的陀螺不用空气也能转很久、带尖头的标枪比钝头的飞得更远、船停了之后还能漂好久，甚至调侃「要是空气能推石头，那羽毛应该比石头飞得更远，可我们显然扔不过石头」，直接把亚里士多德的旧理论怼得没话说",
     "insight":'布里丹反驳亚里士多德的方法特别值得学：用扳手扔出去转着不落地、船停了还能漂——全是日常经验里人人都观察过的现象。他没扯什么抽象公式，就是"你见过这个吧？那你的理论说不通啊"。好的论证往往不需要太多术语，一个贴切的比喻就够了。'},
    {"era":"14世纪：运动学研究","figures":["奥雷斯姆","牛津计算者"],
     "core":"1. 奥雷斯姆（Nicole Oresme，1377年著《论天与地》）：用图形化方法表示「匀变质量」，提出「匀加速运动下落距离与时间平方成正比」的运动学规律，同时最早基于运动相对性和冲量理论提出地球自转的可能性，认为无法通过观测证明是天动还是地动，是哥白尼的先驱\n2. 牛津计算者学派（14世纪）：正式确立匀加速运动的运动学规律，提出「物体从静止匀加速下落，连续相等时间的下落距离比为1:3:5…」的推论",
     "fun":"奥雷斯姆怼过托勒密的经典论点：「垂直射出去的箭，要是地球在转，箭落下来应该偏西边」，他用运动相对性直接反驳：「你跟着船跑的时候往上扔球，球还是会落回你手里，不会往后飞」，比伽利略早200年就提出了类似的思想实验",
     "insight":'奥雷斯姆用"你在船上往上扔球球还掉回手里"这种思想实验，提前两百年把地球自转的相对性给论证了。他没用任何公式，就靠一个日常场景的类比把托勒密的经典论点给拆了。好的论证往往不需要太多术语，一个贴切的比喻就够了。'},
    {"era":"文艺复兴与天文学","figures":["达·芬奇","哥白尼","开普勒"],
     "core":"1. 达·芬奇（Leonardo da Vinci，16世纪初）：业余研究者，完整引入力矩概念分析绕水平轴的重物平衡，讨论冲量与复合运动，提出水流定律与帕斯卡原理雏形，认为地球会因重物下落逐渐趋近球形，讨论鸟类飞行的重心原理，但理论混杂形而上学，缺乏严谨性\n2. 哥白尼（Nicholas Copernicus，1543年著《天体运行论》）：提出日心说，否定地球是宇宙中心，认为地球存在自转、公转等多重运动，为后来开普勒、牛顿的天体力学研究奠定基础\n3. 开普勒（Johannes Kepler，1609年提出行星第一、第二定律，1619年提出第三定律）：基于第谷的观测数据提出行星运动三大定律，提出「引力是物体间的相互吸引，与距离相关」，是连接经院力学与经典力学的关键人物",
     "fun":"达·芬奇力学上经常自相矛盾：一会儿说落体速度跟距离成正比，一会儿又说跟时间成正比，还觉得重物落向地球是\u201c想回家\u201d，充满玄学色彩；开普勒算了十几年行星数据，中途算错一次把自己的正确结论给否了，直到1618年才重新确认，他还把行星角速度和音乐音符对应，坚信宇宙符合\u201c毕达哥拉斯和谐\u201d",
     "insight":'达·芬奇天才毋庸置疑，但力学上自相矛盾——灵感再多，不验证就是扯淡。开普勒算了十几年数据，关键步骤错一次白算好几年。哥白尼把地球从宇宙中心挪开，靠的不是新观测，而是\u201c模型更简洁\u201d这条审美原则——有时候最有力量的论证不是证对，而是证美。'},
    {"era":"静力学复兴","figures":["斯蒂文","伽利略","乌巴尔迪"],
     "core":"1. 斯蒂文（Simon Stevin，1586年出版《静力学原理》）：用「永动机不可能」原理严谨证明斜面平衡定律，提出力矩的现代概念，明确表述虚功原理（作用力移动距离与阻力移动距离之比，等于阻力与作用力之比），同时提出流体静力学固体化原理，推导流体压强仅与液柱高度相关，提出流体静力学佯谬\n2. 伽利略（Galileo Galilei，1638年出版《关于两门新科学的对话》）：静力学方面修正斜面平衡推导，提出虚速度原理，定义「力矩=绝对重量×与平衡中心的距离」；动力学方面通过斜面实验提出自由落体定律、惯性原理雏形、抛体运动抛物线轨迹；流体静力学方面提出虚速度原理在水力学中的应用，验证浮力原理\n3. 圭多·乌巴尔迪（Guido Ubaldo，1577年出版《力学手册》）：修正14世纪经院学者未论证位置重力的问题，提出用支撑面反力解释平衡，推导重物在斜面的平衡条件，是伽利略的老师之一",
     "fun":"斯蒂文把一串球搭斜面上，用\u201c永动机不可能\u201d一个逻辑闭环直接焊死。伽利略用斜面\u201c稀释重力\u201d，水钟计时、挡板分段，把快得看不清的自由落体变成可测量的实验",
     "insight":'斯蒂文用\u201c永动机不可能\u201d一条反证把斜面平衡证死——简单逻辑比复杂推导更有杀伤力。伽利略把自由落体\u201c变慢\u201d让不可测变可测——实验科学的精髓是会不会把问题变慢。'},
]

s2_title = "阶段二：经典力学体系的建立（17世纪 — 18世纪初）"
s2_rows = [
    {"era":"科学网络与微积分前奏","figures":["梅森","罗贝瓦尔"],
     "core":"1. 梅森（Marin Mersenne，17世纪30年代）：作为17世纪力学界的「国际联络人」，翻译伽利略、斯蒂文的著作，传递学者间的观点，促进学术传播\n2. 罗贝瓦尔（Gilles de Roberval，17世纪40年代）：提出用速度合成法求曲线切线，讨论力的合成与虚功原理，影响了后来的力学研究",
     "fun":"梅森本人的力学研究没啥大成果，但人脉极广，简直是17世纪的「学术群里最活跃的群主」，伽利略、笛卡尔、惠更斯、托里拆利等人的观点都通过他的通信网传播，相当于那个时代的学术自媒体；罗贝瓦尔嘴上说着自己的力学是「全新体系」，实际上偷偷借鉴了亚里士多德和意大利文艺复兴的传统，还被同时代的人吐槽「新壶装新酒」",
     "insight":'梅森自己没搞出多大的力学成果，但他建的通信网让整个17世纪的欧洲学者能够互相知道对方在想什么——换句话说，他相当于那个时代的 arXiv 加学术群聊的合体。罗贝瓦尔的教训则是反面：嘴上说着\u201c全新体系\u201d，其实偷偷借鉴了前人，被同代人一眼看穿。学术上装\u201c重新发明轮子\u201d是装不住的。'},
    {"era":"流体流出定律","figures":["托里拆利"],
     "core":"托里拆利（Evangelista Torricelli，1644年出版《论重物的自然运动与抛体运动》，伽利略的弟子与学术继承人）：提出托里拆利原理——相连的物体群不会自发运动，除非它们的共同重心下降；推导液体从孔口流出的速度与水头高度平方根成正比的规律（即托里拆利定律），是流体力学的重要早期成果；同时发明水银气压计，通过真空实验直接证明了大气压的存在，打破了「自然厌恶真空」的千年教条",
     "fun":"托里拆利是伽利略最后一个弟子，伽利略去世前指定他为自己的学术继承人；他的水银柱实验其实是他的学生维维安尼动手做的，但成果归在老师名下——学术署名权问题四百年前就存在了；帕斯卡后来扛着同样的水银管爬到山顶，发现海拔越高水银柱越短，用数据进一步验证了托里拆利的结论，顺便打脸还在嘴硬「真空不存在」的笛卡尔",
     "insight":'托里拆利的水银柱实验意义不止于流体力学——它证明了真空是存在的，一个实验改写了延续千年的教条。更有意思的是，动手做实验的是学生维维安尼，成果署名的却是老师托里拆利——学术界的署名权争议放在今天叫\u201c抢一作\u201d，四百年前就已经上演过了。不过这不影响实验本身的价值：数据不认署名，只认真相。'},
    {"era":"解析方法与实验科学","figures":["笛卡尔","帕斯卡"],
     "core":"1. 笛卡尔（René Descartes，1644年著《哲学原理》）：静力学方面基于虚功原理，提出「力×距离=常量」的普遍杠杆原理，认为所有简单机械都遵循该规律；动力学方面提出运动量（质量×速度）守恒，认为运动本质是直线，圆周运动有离心趋势，制定了6条碰撞定律（部分错误）\n2. 帕斯卡（Blaise Pascal，1653年提出帕斯卡原理）：流体静力学方面提出帕斯卡原理（封闭流体压强均匀传递），发明液压机，解释液压放大力的原理，提出「容器底部压力仅与液柱高度和底面积相关」的流体静力学规律；真空实验方面1647年验证大气压强存在，反驳笛卡尔的「自然厌恶真空」观点",
     "fun":"笛卡尔的碰撞定律错得离谱，比如他说「两个等大的球碰撞，一个动一个静，动的会反弹，静的会被推走」，实际上完全弹性碰撞里动的会停，静的会走，这个错误被惠更斯后来纠正；帕斯卡和笛卡尔为了真空的问题吵得不可开交，笛卡尔坚持「自然界厌恶真空」，帕斯卡直接做了个著名的实验：把水银管带到山顶，发现海拔越高水银柱越短，用事实打脸笛卡尔的玄学观点",
     "insight":'笛卡尔的碰撞定律是用哲学思辨推出来的，全错。帕斯卡直接扛着水银管爬到山顶测气压——数据不会撒谎，谁对谁错一目了然。这故事的启发非常干脆：别跟实验数据犟嘴。再牛的哲学家，也犟不过一管水银。'},
    {"era":"碰撞定律","figures":["沃利斯","雷恩","惠更斯","马略特"],
     "core":"沃利斯（John Wallis，1668年提交论文）、雷恩（Christopher Wren，1668年提交论文）、惠更斯（Christiaan Huygens，1669年提交论文）、马略特（Edme Mariotte，1670年前后）共同确立碰撞力学基础：沃利斯提出完全非弹性碰撞的动量守恒；雷恩与惠更斯提出完全弹性碰撞的动量守恒+动能守恒，惠更斯还通过相对性原理、离心力研究、摆钟设计（摆线摆的等时性、摆动中心理论）进一步完善动力学基础，明确匀加速运动的速度与时间成正比的正确规律",
     "fun":"这三位学者差不多同时提交了碰撞定律的论文，当时皇家学会还特意搞了个「碰撞定律竞赛」，最后判定三人成果都有效，相当于现在三个团队同时发了顶刊；惠更斯做摆钟实验的时候，发现悬挂点和摆动中心是「互易」的，换着挂摆的周期居然一样，这个发现直接帮牛顿后来完善摆动的理论",
     "insight":'皇家学会搞了个\u201c碰撞定律竞赛\u201d，三个人几乎同时交了正确答案，学会判的是\u201c三人成果均有效\u201d——公平，大气。这事还有个隐藏剧情：惠更斯在研究摆钟的时候偶然发现悬挂点和摆动中心\u201c互易\u201d，顺手给后来的牛顿铺了路。做实验时多看一眼计划外的现象，说不定就有惊喜。'},
    {"era":"经典力学体系","figures":["牛顿"],
     "core":"牛顿（Isaac Newton，1687年出版《自然哲学的数学原理》）完成经典力学体系构建：1. 核心概念：引入「质量」定义，区分绝对时间/空间与相对运动；2. 三大运动定律：惯性定律（物体不受力时保持静止或匀速直线运动）、加速度与合力成正比（F=ma）、作用力与反作用力大小相等方向相反；3. 力的合成：平行四边形法则的动态推导；4. 天体力学：用「向心力与距离平方成反比」解释开普勒行星定律，提出万有引力定律，统一天地运动规律；5. 其他：验证潮汐成因、岁差现象，完善流体阻力、离心力等理论",
     "fun":"传说牛顿是被苹果砸了才想到万有引力，其实这是后人编的段子，他的万有引力想法是长期研究天体数据的结果，最早能追溯到他对月亮轨道的计算；牛顿和莱布尼茨为了「微积分是谁发明的」吵了一辈子，连带力学领域的活力之争也掺和了私人恩怨，两边的支持者互相攻击了几十年",
     "insight":'苹果砸牛顿的故事是编的，但万有引力的想法的确是多年泡在天文数据里磨出来的。牛顿和莱布尼茨的微积分之争，后半程基本变成了私人恩怨，两边粉丝互相攻击了几十年。一个本可以合作的领域，被面子活生生搞成了拉锯战——搞学术最怕的就是把\u201c谁先说的\u201d看得比\u201c说了什么\u201d更重。'},
    {"era":"活力论战","figures":["莱布尼茨"],
     "core":"莱布尼茨（Gottfried Wilhelm Leibniz，1686年提出活力概念）：提出「活力（vis viva，即mv²）」概念，反对笛卡尔的「运动量（mv）守恒」，认为mv²才是力的正确度量，引发欧洲学界30余年的「活力之争」，最终明确动能与动量的不同物理意义，同时提出死力（如重力、离心力，对应势能/冲量）与活力（对应动能）的区分",
     "fun":"活力之争的本质是笛卡尔派和莱布尼茨派的骂战，两边各执一词，甚至有人调侃「按笛卡尔的说法，你慢慢搬100斤东西走一天，和一口气扛100斤跑100米用的力一样多」，显然不符合常识；最后达朗贝尔出来和稀泥，说这就是个定义问题，两边算出来的结果其实不矛盾，这场骂战才慢慢消停",
     "insight":'笛卡尔派和莱布尼茨派吵了三十多年，核心分歧其实是：力该用 mv 还是 mv\u00b2 衡量？达朗贝尔最后出来打圆场说你们说的不是一回事——一个在讲动量，一个在讲动能。这出大戏告诉我们：很多\u201c激烈分歧\u201d回头一看，不过是同一件事从两个角度描述，吵了个寂寞。'},
]

s3_title = "阶段三：分析力学的崛起（18世纪）"
s3_rows = [
    {"era":"虚功原理的发展","figures":["让·伯努利","丹尼尔·伯努利"],
     "core":"1. 让·伯努利（Jean Bernoulli，1717年致瓦里尼翁的信中明确虚功原理）：正式提出虚功原理的一般形式，通过力的合成三条假设（结合律、同向相加、等力合力沿角平分线）推导平行四边形法则，成为分析力学的基础\n2. 丹尼尔·伯努利（Daniel Bernoulli，1726年发表《力学原理检验与力合成几何证明》，1738年出版《流体动力学》）：用能量观点研究流体力学，提出伯努利方程（理想流体中压强+动能密度+重力势能密度为常量），同时讨论力的合成的必要真理属性，支持活力守恒",
     "fun":"伯努利家族是学术界的「父子兵」，让·伯努利是丹尼尔的爸爸，爷俩都是力学大牛，但丹尼尔的流体力学成果发表后，他爹居然嫉妒儿子比自己有名，父子俩直接闹翻，老死不相往来；丹尼尔的伯努利方程最早是用来解释「为什么水管细的地方水压小」，后来被广泛应用到航空、水利各个领域，他自己都没想到这个原理这么有用",
     "insight":'伯努利父子都是大牛，问题在于儿子丹尼尔的流体力学成果火了之后，当爹的居然嫉妒了，父子翻脸老死不相往来。学术圈里最尴尬的事莫过于此：你培养了一个天才，然后发现他比你更天才，你就破防了。丹尼尔的伯努利方程也是典型——他最初只是想解释\u201c水管细的地方为什么水压小\u201d，压根没想到后来会变成航空、水利的基石公式。'},
    {"era":"分析力学的系统化","figures":["欧拉"],
     "core":"欧拉（Leonhard Euler，1736年出版《力学》，1760年出版《刚体运动理论》）：1. 《力学》：首次用分析方法系统阐述质点动力学，定义力为运动改变的原因，推导质点运动微分方程，认为力是派生概念，基于运动变化定义；2. 《刚体运动理论》：提出刚体运动的欧拉方程，定义惯性主轴、刚体角动量变化规律，系统计算刚体的转动惯量，奠定刚体力学基础，同时明确惯性中心（即质心）的定义，与仅考虑重力的重心概念区分",
     "fun":"欧拉是数学和力学界的「卷王」，一辈子写了800多篇论文，晚年双目失明之后还能靠心算做研究，刚体力学、流体力学、分析力学都有他的名字，现在学力学的人几乎天天都要用「欧拉公式」「欧拉方程」，相当于被他「支配」了一整个学科",
     "insight":'欧拉一生的产出量放在今天就是学术圈的\u201c时间管理大师\u201d，80多岁双目失明后还能心算做研究。但他最厉害的不是勤奋，而是系统化的能力——别人零散提出的力学规律，到他手里能变成一套自洽的微分方程体系。学问和知识体系的区别就在这：前者是一堆事实，后者是有结构的框架。'},
    {"era":"动静法原理","figures":["达朗贝尔"],
     "core":"达朗贝尔（Jean le Rond d\u2019Alembert，1743年出版《动力学专论》）：1. 提出达朗贝尔原理：将动力学问题转化为静力学平衡问题，即系统的真实运动可分解为保留的运动和抵消的运动，约束反力与抵消的运动平衡，统一处理约束系统的运动；2. 用该原理解释碰撞、摆动中心、活力守恒等问题，推动分析力学发展；3. 讨论「力学定律是必然真理还是偶然真理」的哲学问题，主张力学应基于清晰概念而非形而上学假设",
     "fun":"达朗贝尔是个弃婴，被放在巴黎圣让·勒朗教堂的台阶上，因此取了教堂的名字，被一位玻璃匠收养，最后成了顶尖学者；他说自己的达朗贝尔原理是「把动力学简化成静力学」，结果拉格朗日到处说「达朗贝尔把动力学归为静力学」，达朗贝尔本人还特意反驳：「我才没这么说，这三个原理明明是完全不同的！」，两个人还因为这个说法拌了几句嘴",
     "insight":'达朗贝尔的身世本身就够励志——弃婴，被玻璃匠收养，最后成了法国顶尖学者。他提出的达朗贝尔原理本质是\u201c把动力学问题当成静力学来解\u201d，但拉格朗日到处说他\u201c把动力学归为静力学\u201d，他本人还不乐意了，两人为三句话的表述拌了好几年的嘴。这提醒我们：给别人的理论做总结的时候，措辞谨慎一点，不然原作者会追着你纠正。'},
    {"era":"最小作用量原理","figures":["费马","莱布尼茨","莫佩尔蒂","欧拉"],
     "core":"1. 早期起源：费马1662年提出光程最短原理，莱布尼茨1682年提出「作用量（质量×速度×距离）最小」的概念\n2. 莫佩尔蒂（Pierre Louis Maupertuis，1747年发表《论运动与静止定律》）：将最小作用量原理推广到力学领域，认为自然界的运动总是使「作用量」取极小值，将其作为神存在的证明，还用该原理解释静力学平衡和碰撞定律\n3. 欧拉（1744年出版《寻求具有极大或极小性质的曲线的方法》）：用分析方法验证质点运动中「\u222bv ds」或「\u222bv\u00b2 dt」取极值，为后来拉格朗日、哈密顿的原理完善铺路",
     "fun":"莫佩尔蒂提出最小作用量原理之后，被莱布尼茨的支持者柯尼希怼，说这个原理莱布尼茨早就提过，还拿出了所谓的「莱布尼茨信件」，结果莫佩尔蒂说信件是伪造的，要求对方拿出原件，柯尼希说原件在一个被砍了头的人手里，最后查无此人，这场闹剧还被伏尔泰写进了《老实人》里，把莫佩尔蒂狠狠嘲讽了一番",
     "insight":'最小作用量原理从光学跨界到力学，是物理学史上最漂亮的\u201c跨界借鉴\u201d之一。但莫佩尔蒂提出后，马上被人说\u201c莱布尼茨早就提过了\u201d，两边吵到拿出所谓\u201c信件\u201d当证据，结果原件在一个据说\u201c被砍了头的人手上\u201d，查无此人。伏尔泰还把这出闹剧写进小说嘲讽——可见造假栽赃这事，连哲学家都干得出来，学术圈也不是净土。'},
    {"era":"流体力学一般方程","figures":["克莱罗","达朗贝尔","欧拉","博尔达"],
     "core":"1. 克莱罗（Alexis Clairaut，1743年出版《由流体静力学原理推导的地球形状理论》）：提出流体平衡的条件（压强梯度与外力平衡，即Pdx+Qdy+Rdz为全微分），研究旋转流体质量的形状\n2. 达朗贝尔（1744年出版《流体平衡与运动专论》）：提出「达朗贝尔佯谬」（理想流体中匀速运动的物体不受阻力），建立流体运动的基本方程框架\n3. 欧拉（1755年发表理想流体力学论文）：正式提出理想流体力学的一般方程（连续性方程、欧拉运动方程），将流体力学完全纳入分析力学体系\n4. 博尔达（Jean-Charles de Borda，1767年前后研究流体局部损失）：发现流体流动中的动能损失现象（如突扩管的局部水头损失），完善实际流体力学研究",
     "fun":"达朗贝尔佯谬刚提出来的时候大家都觉得不可思议：「水流动怎么可能对物体没有阻力？」，直到后来大家意识到这是理想流体的假设导致的，实际流体有粘性才会有阻力，这个「佯谬」反而帮大家搞清楚了理想流体和实际流体的区别；博尔达除了研究流体，还是个军事工程师，发明了博尔达计数法，现在投票选举有时候还在用",
     "insight":'达朗贝尔佯谬刚出来的时候，大家都觉得荒谬：\u201c水流动怎么可能对物体没阻力？\u201d后来才反应过来这是理想流体的假设导致的结果——不是理论错了，是假设范围画得太宽了。博尔达除了研究流体力学，还搞了个投票计数法叫博尔达计数，到现在选举还有国家在用。做力学研究顺便发明了一套投票规则——学术跨界这件事真的没有上限。'},
]

s4_title = "阶段四：19世纪的深化与拓展"
s4_rows = [
    {"era":"能量守恒的完善","figures":["迈尔","焦耳","亥姆霍兹"],
     "core":"19世纪30-50年代，迈尔、焦耳、亥姆霍兹等人确立能量守恒定律，将活力（动能）与势能、热能等统一为能量范畴，证明经典力学框架下能量在封闭系统内守恒，成为贯穿后续所有物理领域的普适原理",
     "fun":"焦耳做实验的时候，为了测热功当量，居然在啤酒厂里用水轮机带动搅水器，测水温升高的数值，被啤酒厂工人当成怪人；亥姆霍兹最初提出能量守恒的时候，被学界质疑「凭什么说能量不会消失」，直到焦耳的实验数据公开才被广泛认可",
     "insight":'焦耳在啤酒厂里用水轮机搅水测热功当量的时候，估计连他自己都觉得自己挺\u201c非主流\u201d的。亥姆霍兹提出能量守恒时也是被各种质疑，直到焦耳的数据出来才平息争议。这说明了一个朴素的道理：先别管实验地点有多奇怪，数据能说话就行。'},
    {"era":"分析力学的进一步发展","figures":["拉格朗日","哈密顿"],
     "core":"1. 拉格朗日（Joseph-Louis Lagrange，1788年出版《分析力学》）：用纯分析方法统一静力学与动力学，提出拉格朗日方程，全书无一张几何图，全靠公式推导\n2. 哈密顿（William Rowan Hamilton，1834-1835年提出正则方程和哈密顿原理）：将最小作用量原理推广为更普适的形式，成为后续理论物理的核心数学工具",
     "fun":"拉格朗日的《分析力学》被爱因斯坦夸是「科学著作的艺术品」，他写这本书的时候说「不需要画图，只需要代数运算」，结果后来学力学的人对着满页公式掉头发；哈密顿是爱尔兰的天才数学家，12岁就会13种语言，最初研究光学，结果顺手把分析力学推到了新高度，他自己都没想到他的方程后来成了量子力学的基础",
     "insight":'拉格朗日的《分析力学》全篇没有一张几何图，全靠代数推导。爱因斯坦说它是\u201c科学著作的艺术品\u201d，后来学力学的人翻开这本书只想哭——因为没有图，全是公式。哈密顿更绝，本行是光学，顺手把分析力学推到了他自己都没想到的高度——他去世很多年后，哈密顿量成了量子力学的最核心工具。有时候，最牛的贡献是你根本没打算做的那个。'},
    {"era":"连续介质力学的拓展","figures":["柯西","纳维","斯托克斯"],
     "core":"1. 柯西（Augustin-Louis Cauchy，19世纪20年代引入应力张量概念）：建立弹性力学的完整理论，提出柯西应力张量描述物体内力的分布\n2. 纳维（Claude-Louis Navier，1821年）、斯托克斯（George Gabriel Stokes，1845年）完善粘性流体力学方程（N-S方程），将欧拉的理想流体理论拓展到实际流体场景",
     "fun":"纳维最初推导N-S方程的时候还带着分子假设，结果后来斯托克斯直接用连续介质假设修正，之前的分子假设完全被抛弃；N-S方程到现在都是流体力学最核心的方程，但因为太难求解，千禧年大奖七大难题里就有它的存在性证明问题，悬赏100万美元",
     "insight":'纳维推 N-S 方程时用的分子假设后来被斯托克斯直接砍掉了，换成了连续介质假设——这说明理论迭代本来就是\u201c前人写初稿，后人改 bug\u201d。N-S 方程到今天都是流体力学的心脏，但它的存在性证明至今挂在千禧年七大难题榜上，悬赏 100 万美元。基础研究的魅力就在这：题越基础，解越难。'},
    {"era":"电磁学与力学的交叉讨论","figures":["麦克斯韦","迈克尔逊","莫雷"],
     "core":"1. 麦克斯韦（James Clerk Maxwell，1865年建立电磁场理论）：提出电磁波速与光速一致，暗示经典力学的绝对时空观与电磁现象存在冲突，为相对论的诞生埋下伏笔\n2. 以太理论：试图用经典力学模型解释光的传播，认为宇宙空间充满「以太」作为光的传播介质，最终因迈克尔逊-莫雷实验（1887年）的结果被证伪",
     "fun":"迈克尔逊和莫雷做以太实验的时候，本来想证明以太存在，结果测出来光速各个方向都一样，直接把以太理论锤死了，反而帮爱因斯坦铺了路；麦克斯韦死前还在纠结电磁波和以太的关系，他的遗稿里还有没算完的以太模型公式，结果他去世没多久实验就证明以太不存在了",
     "insight":'迈克尔逊和莫雷费了老大劲搭实验想证明以太存在，结果测出来光速各个方向都一样——直接把以太理论判了死刑。科学史上最戏剧性的反转往往来自\u201c失败的实验\u201d：你想证明 A 存在，结果证明了 A 不存在，顺便给 B 的诞生清空了场地。'},
    {"era":"统计力学的诞生","figures":["玻尔兹曼"],
     "core":"玻尔兹曼（Ludwig Boltzmann，19世纪70-80年代将统计方法引入力学）：建立分子动理论，用微观粒子的力学运动解释宏观热力学规律，架起了微观力学与宏观热现象的桥梁，提出玻尔兹曼熵公式S=k ln\u03a9",
     "fun":"玻尔兹曼的统计学观点当时被很多人反对，他觉得特别孤独，最后1906年自杀去世，直到后来量子力学诞生，大家才意识到他的理论有多超前；他墓碑上刻的就是熵公式S=k log W，是他一生学术成就的最高象征",
     "insight":'玻尔兹曼一生都在跟反对者辩论，最后在孤独中自杀。直到量子力学崛起，大家才发现他的统计观点有多超前。他墓碑上刻的就是那个 S=k log W——他一生最重要的成果，最终被刻在了石头上，而不是被埋进争议里。超前时代太远的人，往往等不到被认可的掌声，但这不影响他们是对的。'},
]

s5_title = "阶段五：现代力学革命（20世纪初）"
s5_rows = [
    {"era":"相对论力学","figures":["爱因斯坦"],
     "core":"1. 爱因斯坦（Albert Einstein，1905年提出狭义相对论）：修正经典时空观，提出狭义相对论两大假设（相对性原理、光速不变原理），将经典力学作为光速无穷大时的极限情况，适用于宏观高速运动场景\n2. 爱因斯坦（1915年提出广义相对论）：进一步将引力解释为时空弯曲，彻底重构了引力相互作用的力学解释，提出引力场方程",
     "fun":"爱因斯坦提出狭义相对论的时候，只是个专利局的小职员，论文发在非顶刊的《物理学年鉴》上，结果直接颠覆了用了200多年的经典力学时空观；广义相对论刚提出的时候，英国天文学家爱丁顿通过日食观测验证了光线弯曲，当时报纸头条写「牛顿理论被推翻」，牛顿的粉丝们还集体抗议了好久",
     "insight":'爱因斯坦在专利局当小职员的时候写了狭义相对论——没有实验室，没有团队，没有顶刊。但他有足够多的时间安静地想问题。这事告诉我们：资源和头衔从来不是做出好研究的必要条件，专注和深度思考才是。广义相对论被验证后，报纸头条写\u201c牛顿被推翻了\u201d，牛顿的粉丝们不干了——其实\u201c推翻\u201d这个词用错了，经典力学只是变成了新理论在低速条件下的近似。'},
    {"era":"波动力学与量子力学","figures":["德布罗意","海森堡","薛定谔"],
     "core":"1. 德布罗意（Louis de Broglie，1923年提出物质波假设）：认为所有实物粒子都具有波粒二象性，提出德布罗意波长公式\u03bb=h/p\n2. 海森堡（Werner Heisenberg，1925年建立矩阵力学）、薛定谔（Erwin Schr\00f6dinger，1926年建立波动力学）：放弃微观过程的连续性与绝对决定论，用概率描述原子尺度的物理现象，提出测不准原理\u0394x\u0394p\u2265h/4\u03c0，是比相对论更激进的范式革命",
     "fun":"德布罗意本来是学历史的，半路转行学物理，博士论文里提出物质波，答辩的时候评委们都觉得太离谱，差点没让他毕业，结果后来这个理论拿了诺贝尔奖；量子力学里的「测不准原理」完全打破了经典力学「只要知道初始条件就能预测所有未来」的决定论观点，连爱因斯坦都接受不了，说「上帝不掷骰子」，和玻尔吵了一辈子，直到去世都没认可量子力学的完备性",
     "insight":'德布罗意从历史系半路出家学物理，博士论文提出物质波，答辩评委觉得太离谱差点没让他毕业——结果这个\u201c离谱\u201d后来拿了诺贝尔奖。量子力学打破了经典力学\u201c知道初始条件就能预测一切\u201d的决定论，连爱因斯坦都受不了，放话说\u201c上帝不掷骰子\u201d，跟玻尔吵了一辈子。但争论到最后，实验数据站量子力学这边——科学史反复证明一个道理：直觉再强，也拗不过实验数据。'},
]

# ── CSS ──
CSS = """\
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#e8ecf1;--text:#1e293b;--text-muted:#64748b;--card-bg:#fff;--card-border:#c8d4e2;--sidebar-bg:#1e293b;--sidebar-active:#3b82f6;--era-bg:#334155;--era-text:#e2e8f0;--av-bg:#c8d4e2;--av-text:#64748b}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth;font-size:16px;overflow-y:scroll}
body{font-family:system-ui,"Sarasa Gothic SC","Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--text);line-height:1.7;overflow-x:hidden;user-select:none;-webkit-user-select:none;-webkit-touch-callout:none}
.main{margin-left:76px}
@media(min-width:769px) and (max-width:1024px){html{font-size:18px}}@media(max-width:768px){.main{margin-left:44px}}
.sidebar{position:fixed;left:0;top:0;width:56px;height:100vh;background:none;display:flex;justify-content:center;z-index:100;opacity:0;transition:opacity .35s}
.sidebar.visible{opacity:1}
.sidebar-track{position:relative;width:2px;height:100%}
.sidebar-track::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(to bottom,transparent 8%,#c8d4e2 8%,#c8d4e2 92%,transparent 92%)}
.sidebar-marker{position:absolute;left:50%;transform:translate(-50%,-50%);width:6px;height:6px;border-radius:50%;background:#94a3b8;z-index:1;pointer-events:none}
.sidebar-marker::before{content:none}
.sidebar-indicator{position:absolute;left:50%;transform:translate(-50%,-50%);width:14px;height:14px;border-radius:50%;background:#1e293b;z-index:2;transition:top .15s;pointer-events:none}
.sidebar-indicator::before{content:none}
.sidebar-indicator-label{position:absolute;left:100%;top:50%;transform:translateY(-50%);margin-left:8px;font-size:.55rem;color:#1e293b;font-weight:700;white-space:nowrap;background:none;padding:0;z-index:101}
@media(max-width:768px){.sidebar{width:44px}.sidebar-indicator{width:11px;height:11px}.sidebar-indicator-label{font-size:.45rem;margin-left:5px}.sidebar-marker{width:4px;height:4px}}
.hero{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;text-align:center;padding:2rem;scroll-snap-align:start;margin-left:-76px}
.hero h1{font-size:2.8rem;font-weight:800;color:var(--text);margin-bottom:1rem;letter-spacing:.04em}
.hero .author{font-size:1.1rem;color:var(--text-muted);margin-bottom:.3rem}
.hero .reference{font-size:.9rem;color:var(--text-muted);margin-bottom:2rem}
.hero .intro{margin-top:1rem;max-width:640px}
.hero .intro p{font-size:.9rem;line-height:1.9;color:var(--text);text-align:left;font-style:italic}
.hero .scroll-hint{font-size:2rem;color:var(--text-muted);cursor:pointer;animation:bounce 2s infinite;margin-top:2rem}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(10px)}}
@media(max-width:768px){.hero h1{font-size:1.6rem}.hero{min-height:100vh;padding:1.5rem;margin-left:-44px}}
.ov-card{border-radius:12px;padding:1.5rem;margin-bottom:2rem}
.ov-card-merged{background:#fff;border:1px solid var(--card-border);box-shadow:0 4px 24px rgba(0,0,0,.13);margin:5vh 5vw;width:100%}
#overview{scroll-snap-align:start;min-height:90vh;display:flex;align-items:center;justify-content:center;margin-left:-76px}
@media(max-width:768px){#overview{padding:0;margin-left:-44px}.ov-card-merged{margin:3vh 4vw}}
.ov-main-title{font-size:1.25rem;font-weight:800;color:var(--text);text-align:center;margin-bottom:.8rem;padding-bottom:.8rem;border-bottom:2px solid var(--card-border)}
.ov-card-head{font-size:1.05rem;font-weight:700;margin-bottom:.6rem;display:flex;align-items:center;gap:6px}
.ov-card-icon{font-size:1.2rem}
.ov-flow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin-bottom:.4rem;padding-bottom:.2rem}
.ov-step{background:var(--era-bg);color:var(--era-text);padding:4px 12px;border-radius:16px;font-size:.78rem;white-space:nowrap;flex-shrink:0}
.ov-arrow{color:var(--text-muted);font-size:.75rem;flex-shrink:0}
.ov-section{border-bottom:1px solid var(--card-border);padding:1rem 0}
.ov-section:last-child{border-bottom:none}
.stage-title{scroll-snap-align:start;scroll-snap-stop:always;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;font-size:1.8rem;font-weight:800;color:var(--text);padding:0 10vw 0 0;margin:0}
@media(max-width:768px){.stage-title{font-size:1.3rem;padding:0 8vw 0 0}}
.stage-separator{scroll-snap-align:start;scroll-snap-stop:always;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;color:var(--text-muted);font-size:1.1rem;font-style:italic;line-height:2;padding:2rem 10vw 2rem 0}
.card{display:flex;flex-direction:column;gap:.6rem;background:var(--card-bg);border:1px solid var(--card-border);border-radius:12px;padding:1.5rem;margin:5vh 5vw 5vh 0;box-shadow:0 4px 24px rgba(0,0,0,.13);scroll-snap-align:start;min-height:90vh;overflow-y:auto;justify-content:center}
.card-portraits{display:flex;flex-direction:row;gap:8px;flex-wrap:wrap}
.card-header{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.card-chip{background:var(--era-bg);color:var(--era-text);padding:4px 14px;border-radius:20px;font-size:.82rem;font-weight:600;white-space:nowrap}
.avatar{width:64px;height:64px;border-radius:50%;background:var(--av-bg);color:var(--av-text);display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:700;flex-shrink:0;border:2px solid #cbd5e1}
.card-figure{font-weight:700;font-size:.95rem;color:var(--text);white-space:nowrap}
.card-core{font-size:.9rem;margin-bottom:.6rem;line-height:1.7;color:var(--text)}
.card-fun{font-size:.85rem;margin-bottom:.6rem;line-height:1.7;color:var(--text-muted);font-style:italic}
.card-insight{font-size:.85rem;line-height:1.7;color:var(--text);border-left:3px solid var(--sidebar-active);padding-left:.8rem}
.card-insight::before{content:'\\01F4A1 '}
@media(max-width:768px){.card{padding:1rem;margin:3vh 4vw 3vh 0;min-height:94vh;gap:.5rem}.card-portraits{gap:6px}.card-header{gap:6px}.card-chip{font-size:.72rem;padding:3px 10px}.avatar{width:42px;height:42px;font-size:1.1rem}.card-core,.card-fun,.card-insight{font-size:.8rem}.card-figure{font-size:.85rem}}
.conclusion{background:#fff;border:1px solid var(--card-border);border-radius:12px;padding:1.5rem;margin:5vh 5vw 5vh 0;box-shadow:0 4px 24px rgba(0,0,0,.13);scroll-snap-align:start;min-height:90vh;display:flex;flex-direction:column;justify-content:center}
.conclusion h2{font-size:1.15rem;font-weight:800;margin-bottom:1rem;display:flex;align-items:center;gap:8px;color:var(--text)}
.conclusion p{font-size:.85rem;line-height:1.7;color:var(--text);font-style:italic}
@media(max-width:768px){.conclusion{padding:1rem;margin:3vh 4vw 3vh 0;min-height:94vh}.conclusion p{font-size:.8rem}}
.nav-arrows{position:fixed;right:16px;top:50%;transform:translateY(-50%);z-index:200;display:flex;flex-direction:column;gap:16px;pointer-events:none}
.nav-arrow{width:40px;height:40px;border-radius:50%;background:rgba(92,58,30,.75);color:#e2e8f0;border:none;cursor:pointer;font-size:1.1rem;display:flex;align-items:center;justify-content:center;pointer-events:auto;transition:background .2s,opacity .2s;backdrop-filter:blur(4px)}
.nav-arrow:active{background:rgba(92,58,30,.92)}
.nav-arrow.hidden{opacity:0;pointer-events:none}
@media(max-width:768px){.nav-arrows{right:8px;gap:13px}.nav-arrow{width:36px;height:36px;font-size:1rem}}
"""

# ── Sidebar ──
markers = [
    (0.000, "公元前4世纪"),
    (0.055, "1-4世纪"),
    (0.110, "13世纪"),
    (0.165, "14世纪"),
    (0.220, "15-16世纪"),
    (0.275, "17世纪初"),
    (0.330, "1687年"),
    (0.385, "1717年"),
    (0.440, "1736年"),
    (0.495, "1743年"),
    (0.550, "1755年"),
    (0.600, "18世纪"),
    (0.650, "1788年"),
    (0.700, "19世纪"),
    (0.750, "1865年"),
    (0.800, "1905年"),
    (0.850, "1925年"),
    (0.920, "20世纪"),
    (0.990, "现在"),
]
mhtml = "\n    ".join(
    '<div class="sidebar-marker" data-pct="%.2f" data-label="%s" style="top:%.0f%%"></div>' % (pct, label, 10 + pct * 80)
    for pct, label in markers
)
sidebar = """<aside class="sidebar">
  <div class="sidebar-track">
    %s
    <div class="sidebar-indicator"><span class="sidebar-indicator-label">\u516c\u5143\u524d4\u4e16\u7eaa</span></div>
  </div>
</aside>""" % mhtml

# ── Overview ──
overview = """<section id="overview">
  <div class="ov-card ov-card-merged">
    <h3 class="ov-main-title">\u56db\u5927\u4e3b\u7ebf</h3>
    <div class="ov-section"><h3 class="ov-card-head"><span class="ov-card-icon">\U0001f4c5</span> \u65f6\u95f4\u7ebf</h3>
    <div class="ov-flow">
      <span class="ov-step">\u53e4\u5e0c\u814a\u81ea\u7136\u54f2\u5b66</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u4e2d\u4e16\u7eaa\u7ecf\u9662\u529b\u5b66</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u6587\u827a\u590d\u5174\u8fc7\u6e21</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">17\u4e16\u7eaa\u7ecf\u5178\u529b\u5b66\u8bde\u751f</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">18\u4e16\u7eaa\u4f53\u7cfb\u5b8c\u5584</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">19\u4e16\u7eaa\u6df1\u5316</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">20\u4e16\u7eaa\u73b0\u4ee3\u529b\u5b66\u9769\u547d</span>
    </div>
</div>
    <div class="ov-section"><h3 class="ov-card-head"><span class="ov-card-icon">\u2696\ufe0f</span> \u539f\u7406\u7ebf</h3>
    <div class="ov-flow">
      <span class="ov-step">\u4e9a\u91cc\u58eb\u591a\u5fb7\u5b9a\u6027\u52a8\u529b\u5b66</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u963f\u57fa\u7c73\u5fb7\u9759\u529b\u5b66\u5b9a\u91cf</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u51b2\u91cf/\u60ef\u6027\u96cf\u5f62</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u725b\u987f\u4e09\u5b9a\u5f8b+\u4e07\u6709\u5f15\u529b</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u5206\u6790\u529b\u5b66</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u76f8\u5bf9\u8bba\u548c\u91cf\u5b50\u529b\u5b66</span>
    </div>
</div>
    <div class="ov-section"><h3 class="ov-card-head"><span class="ov-card-icon">\U0001f52c</span> \u5c3a\u5ea6\u7ebf</h3>
    <div class="ov-flow">
      <span class="ov-step">\u5730\u9762\u7269\u4f53\u529b\u5b66</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u5929\u4f53\u529b\u5b66</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u5fae\u89c2\u7c92\u5b50\u529b\u5b66</span>
    </div>
</div>
    <div class="ov-section"><h3 class="ov-card-head"><span class="ov-card-icon">\U0001f9ea</span> \u65b9\u6cd5\u8bba\u7ebf</h3>
    <div class="ov-flow">
      <span class="ov-step">\u54f2\u5b66\u601d\u8fa8</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u5b9a\u6027\u89c2\u5bdf</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u5b9e\u9a8c\u9a8c\u8bc1</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u6570\u5b66\u6f14\u7ece</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u5206\u6790\u5316+\u516c\u7406\u5316</span><span class="ov-arrow">\u2192</span>
      <span class="ov-step">\u73b0\u4ee3\u6570\u7406\u7ed3\u5408</span>
    </div>
</div>
  </div>
</section>"""

# ── Conclusion ──
conclusion = """<section class="conclusion">
  <h2>\U0001f4dc \u7ed3\u8bed</h2>
  <p>\u56de\u987e\u4e24\u5343\u591a\u5e74\u7684\u529b\u5b66\u53f2\uff0c\u6bcf\u4e00\u6b21\u7a81\u7834\u90fd\u6709\u6e05\u6670\u7684\u4e09\u6bb5\u5f0f\u811a\u672c\uff1a\u65e7\u7406\u8bba\u78b0\u5230\u89e3\u91ca\u4e0d\u4e86\u7684\u5b9e\u9a8c\u4e8b\u5b9e \u2192 \u6709\u4eba\u6562\u8bf4\u201c\u65e7\u7684\u9519\u4e86\u201d \u2192 \u65b0\u6846\u67b6\u628a\u65e7\u7406\u8bba\u53d8\u6210\u81ea\u5df1\u7684\u7279\u4f8b\u3002\u4e9a\u91cc\u58eb\u591a\u5fb7\u7684\u52a8\u529b\u5b66\u88ab\u51b2\u91cf\u7406\u8bba\u63a8\u7ffb\uff0c\u51b2\u91cf\u7406\u8bba\u53c8\u88ab\u725b\u987f\u4e09\u5b9a\u5f8b\u5438\u6536\u4e3a\u7279\u4f8b\uff0c\u725b\u987f\u7684\u7edd\u5bf9\u65f6\u7a7a\u88ab\u76f8\u5bf9\u8bba\u5728\u5149\u901f\u6781\u9650\u4e0b\u53d8\u4e3a\u8fd1\u4f3c\uff0c\u725b\u987f\u7684\u51b3\u5b9a\u8bba\u88ab\u91cf\u5b50\u529b\u5b66\u7528\u6982\u7387\u6846\u67b6\u91cd\u5199\u2014\u2014\u9a71\u52a8\u529b\u59cb\u7ec8\u662f\u4e24\u4e2a\u6734\u7d20\u7684\u95ee\u9898\uff1a\u201c\u8fd9\u4e2a\u73b0\u8c61\u600e\u4e48\u89e3\u91ca\uff1f\u201d\u548c\u201c\u6709\u6ca1\u6709\u66f4\u5e95\u5c42\u7684\u89c4\u5f8b\uff1f\u201d<br><br>\u800c\u529b\u5b66\u53f2\u6700\u8ff7\u4eba\u7684\u5730\u65b9\u5728\u4e8e\uff1a\u6700\u96be\u7684\u9898\u5f80\u5f80\u5728\u6700\u57fa\u7840\u7684\u5730\u65b9\u3002\u6d41\u4f53\u529b\u5b66\u4e2d\u7684\u6e4d\u6d41\u3001N-S\u65b9\u7a0b\u7684\u5b58\u5728\u6027\u2014\u2014\u8fd9\u4e9b\u95ee\u9898\u6302\u4e86\u4e0a\u767e\u5e74\u8fd8\u6ca1\u6709\u5f7b\u5e95\u89e3\u51b3\u3002\u529b\u5b66\u4e0d\u662f\u4e00\u95e8\u201c\u5df2\u7ecf\u5b8c\u6210\u7684\u5b66\u79d1\u201d\uff0c\u800c\u662f\u4e00\u6761\u4ecd\u5728\u5ef6\u4f38\u7684\u8def\u3002</p>
 <p style="margin-top:2rem;color:var(--text-muted)">\u611f\u8c22\u60a8\u7684\u8010\u5fc3\u9605\u8bfb\uff0c\u8be5\u65f6\u95f4\u7ebf\u622a\u6b62\u4e3a1955\u5e74\uff0c\u518d\u5176\u540e\u5185\u5bb9\u5927\u591a\u90fd\u53ef\u4ee5\u901a\u8fc7\u6559\u79d1\u4e66\u53bb\u67e5\u9605\u4e86\u3002\u8be5\u9875\u9762\u57fa\u4e8e\u4e66\u7c4d\uff0c\u501f\u52a9 WorkBuddy \u8fdb\u884c\u6574\u7406\u5e76\u5236\u4f5c\u3002\u672c\u4eba\u4ed4\u7ec6\u8fdb\u884c\u4e86\u6821\u5bf9\uff0c\u4f46\u96be\u514d\u9057\u6f0f\u548c\u9519\u8bef\u4e4b\u5904\uff0c\u6b22\u8fce\u6307\u51fa\u3002</p>
 <p style="margin-top:.5rem;color:var(--text-muted);font-style:normal">\u2014\u2014 \u9e4f\u98de\uff08XHS\uff1a\u98de\u54e5\u5927\u7237\u7237\uff09</p>
</section>"""

separator = '<div class="stage-separator">\u26a1 \u5750\u7a33\uff0c\u73b0\u5728\u5f00\u59cb<br>\u8ddf\u7740\u5343\u5e74\u811a\u6b65\uff0c\u770b\u529b\u5b66\u5982\u4f55\u4ece&#8220;\u4e3a\u4ec0\u4e48\u4f1a\u52a8&#8221;<br>\u957f\u6210\u4eba\u7c7b\u6700\u7cbe\u5bc6\u7684\u601d\u60f3\u6b66\u5668</div>'

hero_intro = "\u672c\u6587\u57fa\u4e8e\u300aA History of Mechanics\u300b\uff08Ren\u00e9 Dugas\uff0c1955\uff09\uff0c\u6cbf\u65f6\u95f4\u987a\u5e8f\u68b3\u7406\u529b\u5b66\u4ece\u53e4\u5e0c\u814a\u81ea\u7136\u54f2\u5b66\u523020\u4e16\u7eaa\u521d\u76f8\u5bf9\u8bba\u4e0e\u91cf\u5b50\u529b\u5b66\u7684\u6f14\u5316\u8109\u7edc\uff0c\u6309\u4e94\u4e2a\u9636\u6bb5\u5c55\u5f00\u3002\u6bcf\u4e00\u4e2a\u5b9a\u5f8b\u80cc\u540e\u90fd\u6709\u4e00\u6bb5\u4e0d\u4e3a\u4eba\u77e5\u7684\u6545\u4e8b\uff1a\u6709\u4eba\u82b1\u5341\u51e0\u5e74\u7b97\u6570\u636e\u5374\u56e0\u4e00\u6b65\u7b97\u9519\u5426\u6389\u4e86\u6b63\u786e\u7b54\u6848\uff0c\u6709\u4eba\u5728\u5564\u9152\u5382\u91cc\u6405\u6c34\u6d4b\u70ed\u91cf\u88ab\u5f53\u6210\u602a\u4eba\uff0c\u4e5f\u6709\u4eba\u81f3\u6b7b\u6ca1\u7b49\u5230\u81ea\u5df1\u7684\u7406\u8bba\u88ab\u8ba4\u53ef\u3002\u5f80\u4e0b\u7ffb\uff0c\u770b\u770b\u8fd9\u4e9b\u516c\u5f0f\u662f\u600e\u4e48\u300c\u957f\u300d\u51fa\u6765\u7684\u3002"

js_code = """
document.addEventListener('DOMContentLoaded',function(){
  /* ---- copy protection ---- */
  document.addEventListener('contextmenu',function(e){e.preventDefault();});
  document.addEventListener('keydown',function(e){
    if(e.ctrlKey&&(e.key==='u'||e.key==='U'||e.key==='s'||e.key==='S'||e.key==='c'||e.key==='C'||e.key==='p'||e.key==='P')){e.preventDefault();}
    if(e.key==='F12'){e.preventDefault();}
    if(e.ctrlKey&&e.shiftKey&&(e.key==='I'||e.key==='i'||e.key==='J'||e.key==='j'||e.key==='C'||e.key==='c')){e.preventDefault();}
  });
  /* ---- end copy protection ---- */
  var sidebarEl=document.querySelector('.sidebar');
  var sidebar=document.querySelector('.sidebar-track');
  var markers=sidebar.querySelectorAll('.sidebar-marker');
  var indicator=document.querySelector('.sidebar-indicator');
  var indicatorLabel=document.querySelector('.sidebar-indicator-label');
  var stage1=document.getElementById('stage1');
  var arrowUp=document.getElementById('nav-up');
  var arrowHome=document.getElementById('nav-home');
  var arrowDown=document.getElementById('nav-down');
  var eras=[];
  markers.forEach(function(m){
    eras.push({el:m,pct:parseFloat(m.getAttribute('data-pct')),label:m.getAttribute('data-label')});
  });

  function getPages(){
    return document.querySelectorAll('.hero,#overview,.stage-separator,.stage-title,.card,.conclusion');
  }

  function getCurrentPageIdx(){
    var pages=getPages();
    var viewMid=window.scrollY + window.innerHeight/2;
    var best=-1,bestDist=1e9;
    pages.forEach(function(p,i){
      var top=p.getBoundingClientRect().top + window.scrollY;
      var mid=top + p.offsetHeight/2;
      var dist=Math.abs(mid-viewMid);
      if(dist<bestDist){bestDist=dist;best=i;}
    });
    return best;
  }

  function scrollToPage(idx){
    var pages=getPages();
    if(idx<0||idx>=pages.length)return;
    pages[idx].scrollIntoView({behavior:'smooth'});
  }

  arrowUp.addEventListener('click',function(){
    scrollToPage(getCurrentPageIdx()-1);
  });
  arrowHome.addEventListener('click',function(){
    scrollToPage(0);
  });
  arrowDown.addEventListener('click',function(){
    scrollToPage(getCurrentPageIdx()+1);
  });

  function updateArrows(){
    var idx=getCurrentPageIdx();
    var pages=getPages();
    if(idx<=0)arrowUp.classList.add('hidden');
    else arrowUp.classList.remove('hidden');
    if(idx>=pages.length-1)arrowDown.classList.add('hidden');
    else arrowDown.classList.remove('hidden');
  }

  var lastEraIdx=0;

  function updateIndicator(){
    var stage1Top=stage1 ? stage1.getBoundingClientRect().top + window.scrollY : 0;
    var scrollY=window.scrollY;
    if(scrollY >= stage1Top - 80){
      sidebarEl.classList.add('visible');
    }else{
      sidebarEl.classList.remove('visible');
      lastEraIdx=0;
      return;
    }
    var pages=getPages();
    var idx=getCurrentPageIdx();
    if(idx<0)return;
    var pg=pages[idx];
    // Map 24 card pages to 17 era markers
    var cardToEra=[0,1, 2,3,3,4,5, 5,5,5,6,6,6, 7,8,9,9,10, 13,12,14,14,14, 15,16];
    if(pg && pg.classList.contains('conclusion')){
      lastEraIdx=18; // 现在
    }else if(pg && pg.classList.contains('card')){
      var c=0;
      for(var i=0;i<pages.length;i++){
        if(!pages[i].classList.contains('card'))continue;
        if(i===idx){lastEraIdx=cardToEra[Math.min(c,cardToEra.length-1)];break;}
        if(i<idx)c++;
      }
    }
    // else: stage-title / separator / overview → keep lastEraIdx
    var current=eras[lastEraIdx];
    indicator.style.top=(10+current.pct*80)+'%';
    indicatorLabel.textContent=current.label;
  }

  updateIndicator();
  updateArrows();
  window.addEventListener('scroll',function(){
    updateIndicator();
    updateArrows();
  });
  window.addEventListener('resize',function(){
    updateIndicator();
    updateArrows();
  });
});
"""

# ── ASSEMBLE ──
stages_html = ""
for key, title, rows in [("stage1",s1_title,s1_rows),("stage2",s2_title,s2_rows),
                          ("stage3",s3_title,s3_rows),("stage4",s4_title,s4_rows),
                          ("stage5",s5_title,s5_rows)]:
    stages_html += '<h2 class="stage-title" id="%s">%s</h2>\n' % (key, esc(title))
    stages_html += gen_cards(rows)
    stages_html += '\n'

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>%s</title>
<style>
%s
</style>
</head>
<body>

%s

<div class="nav-arrows">
  <button class="nav-arrow hidden" id="nav-up" aria-label="上一页">&#9650;</button>
  <button class="nav-arrow" id="nav-home" aria-label="返回首页"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></button>
  <button class="nav-arrow" id="nav-down" aria-label="下一页">&#9660;</button>
</div>

<div class="main">

<section class="hero">
  <h1>%s</h1>
  <div class="author">by YPF</div>
  <div class="reference">%s</div>
  <div class="intro">
    <p>%s</p>
  </div>
  <div class="scroll-hint" onclick="document.getElementById('overview').scrollIntoView({behavior:'smooth'})">\u2193</div>
</section>

%s

%s

%s

%s

</div>

<script>
%s
</script>

</body>
</html>""" % (
    "\u529b\u5b66\u4e24\u5343\u5e74\uff1a\u4e00\u573a\u601d\u60f3\u7684\u63a5\u529b",
    CSS,
    sidebar,
    "\u529b\u5b66\u4e24\u5343\u5e74\uff1a\u4e00\u573a\u601d\u60f3\u7684\u63a5\u529b",
    "\u53c2\u8003\u4e66\u7c4d\uff1a\u300aA History of Mechanics\u300b Ren\u00e9 Dugas 1955",
    hero_intro,
    overview,
    separator,
    stages_html,
    conclusion,
    js_code,
)

out = os.path.join(BASE, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)

tc = sum(len(r) for _,_,r in [(0,0,s1_rows),(0,0,s2_rows),(0,0,s3_rows),(0,0,s4_rows),(0,0,s5_rows)])
print("OK: %d lines, %d bytes, %d cards" % (html.count("\n"), len(html), tc))
