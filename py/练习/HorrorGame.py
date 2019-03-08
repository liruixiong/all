import time
superdict = {
'page1':'''你和同事合租了一间房子，那天下午你们呆在家里，门铃响了，是快递。
2.签收
3.拒收

''',

'page2':'''你签收了快递，打开是一个盒子里面有一封有些泛黄的信。
你把信打开，同事也感兴趣的凑过来看，信上写道：你好，首先你接到这封信开始你的寿命已经不长了，想延长寿命吗？那就要成功完成我下面给你的任务了。
任务：去XX路XX街XX号大楼，这是一家废弃的医院，我需要你帮我去三楼的产房和底楼的太平间取出我的死亡证明和出生证明，不去，后果自负。
4.去
5.不去

''',

'page3':'''你与快递人员争吵了1小时，最后还是签收了，遭到白眼。
打开是一个盒子里面有一封有些泛黄的信。
你把信打开，同事也感兴趣的凑过来看，信上写道：你好，首先你接到这封信开始你的寿命已经不长了，想延长寿命吗？那就要成功完成我下面给你的任务了。
任务：去XX路XX街XX号大楼，这是一家废弃的医院，我需要你帮我去三楼的产房和底楼的太平间取出我的死亡证明和出生证明，不去，后果自负。
4.去
5.不去

''',

'page4':'''你打开了网络，去百度搜了废弃医院的相关资料，并和你的同事开始了冒险。
你在搜索栏里打了“废弃医院”四个字，出来了很多条可参考的资料，你选择了一条你和你的情况相似的点了进去，但这时你的电脑黑屏了。
6.去修电脑
7.换笔记本重新搜索

''',

'page5':'''当天晚上你和你同事都死了，死因不明
''',

'page6':'''“咚”你们听到窗户被重重敲击的声音，你们走过去看，窗户上面渐渐显出了血字，你们消耗的时间太多了，你们感到一下子被抽取了氧气，死了。
''',

'page7':'''你麻利的打开电脑很快重新找到了刚才那个网页，并顺利点开。
网站上写到：“我现在正在医院里面，这也许是我的遗书了，如果不接收快递，也不会有这一系列的事，我的同伴已经死了，这个医院原来是一家很好的妇产科医院，因为一次手术，出现了一个畸形的婴儿，医院不负责，所以把婴儿埋了，,医院就开始发生灵异的事件，最后发生了火灾，医院就废弃了。”我现在才知道，给我们写信的就是那个畸形的婴儿，他已经变成了冤魂，却不想离开人世，它要的是报仇，报仇！报仇！你同事的心动摇了。
8.说服同事继续探险
9.放弃继续，扔掉信

''',

'page8':'''你刚准备关掉网页出发，同事发现了网页上的最后15个字，完成任务后真的可以延长寿命。
“真的可以延长寿命”，我嘴里一遍遍重复到，同事说：“喂，回过神来，要走快走，不然我们随时都会死的。”对啊，我们时间不多了，我才反应过来，带上信和手电筒和同事出去了，但一出门才发现事情已经不对了，原来的楼道已不再是楼道，在你们面前的而是三道门，第一道门紧锁着，第二道门里面充满了花香和阳光，第三道门半虚掩着，给人一种阴森的感觉。
10.第一道门
11.第二道门
12.第三道门

''',

'page9':'''听到一声笑声，死了……
''',

'page10':'''没有找到钥匙，由于时间过长，你的寿命到了，死了。
''',

'page11':'''那门是假象，幻像消失后，你和你的同事从8楼跳了下去。
''',

'page12':'''直接通往了废弃医院，恐怖的场景映入眼帘。
刚才还是白天，但现在的天空已经是死气沉沉的灰色了，眼前有一道墙和一扇门，门的前面铺满了盐，很久以前传说盐可以辟邪和抵御冤魂厉鬼，墙那边则很高，爬上去随时都有摔死的可能，倒也许会安全。
13.走门
14.爬墙

''',

'page13':'''抵御冤魂是不让里面的冤魂出来，所以门里面那个所谓的保安室里都是冤魂，还有一条狗的尸体，所以，死了。
''',

'page14':'''墙上有暗门，顺利了走进废弃医院。
你来到了里面，看到了大厅悬挂着母子相，十分阴森恐怖，你现在要干什么？
15.去产房拿出生证明
16.去太平间拿出生证明
17.继续寻找线索

''',

'page15':'''母子相证明产房有厉鬼，所以死。
''',

'page16':'''找楼梯的过程中并没有危险，走到楼梯口，发现门被反锁了，左边有一个旧的生锈的梯子，都可以通向底楼的太平间。
18.继续研究楼梯。
19.爬梯子下去。

''',

'page17':'''浪费了很多时间，却一无所获，寿命耗尽
''',

'page18':'''你走到楼梯口，轻轻一推门，发现门是开着的，你走下了楼梯，到达目的地太平间，到了太平间以后，你会：
20.回头看看
21.继续往前走

''',

'page19':'''当你和你同事爬到一半的时候，梯子断了，死了。
''',

'page20':'''你们屏住呼吸，冤魂冲的很快，并没有注意你们，逃过一劫。
你们害怕前面厉鬼会更多，决定去开窗，因为鬼会害怕阳光，你们继续往前走，但是地下室只有一个很高的窗，你们怎么都够不着，你们在旁边发现一个很大很破的梯子，和一个破旧的箱子。
22.用梯子爬上去
23.打开箱子看看有没有可以用的
24.再找别的工具

''',

'page21':'''冤魂冲了过来，你们被发现了，元气被吸走，死了。
''',

'page22':'''梯子很旧很破，搬动它声音太响了，惊动了里面的厉鬼，死了。
''',

'page23':'''打开箱子，里面有一封泛黄的信件，上面还有一点点血迹。
你从箱子里拿出那封信，打开看，信上写道：你们还不错，到现在都没有死，怎么没去产房啊，呵呵，不过这里虽然没有很多厉鬼，但里面也有你好受的，也别指望开窗，你没那个能力，你应该庆幸你带了手电筒。
25.继续试图打开窗户
26.打开手电筒走进去

''',

'page24':'''里面走越来越黑，几乎看不了，厉鬼适应黑暗，死了
''',

'page25':'''你从箱子里拿出一根长杆子，打开了窗户，厉鬼的确怕光，所以都附在了太平间的尸体里，冲出来咬你，死了。
''',

'page26':'''照着光走了进去，发现太平间的门并没有锁。
你推开太平间的门，浓烈的腐蚀味扑鼻而来，你和同事连连作呕，你并不知道畸形婴儿的名字，所以唯一的办法就是一个个去翻出尸体箱子看，太平间里的绿光照的你心里发慌，你拉开第一个抽屉，是分解的四肢拼凑出来的人，你看到他身体下面有一张纸。
27.把尸体翻过来拿出那张纸
28.把抽屉拉回去就当没有看到

''',

'page27':'''是一张死亡证明，而且据同事说每个尸体下面都压了一张死亡证明。
你们几乎快看完了所有的抽屉，还是没有找到，突然你同事大叫了一声你的名字，你吓了一跳，问他什么事啊，一惊一乍吓死人的！你同事说不好意思哦，这个抽屉是锁着的。这有什么好叫的，你往同事那边走去，发现上面贴着一张纸，禁忌：千万不要打开这个抽屉，不然封存的鬼印就出来了。
29.打开抽屉
30.按照禁忌上说的不打开

''',

'page28':'''抽屉合上后，里面传来了敲抽屉的声音。你又把抽屉打开，里面的尸体爬了出来，对你冷笑，对你说你失败了！然后死了。
''',

'page29':'''当你撬开锁打开抽屉的瞬间，一团血肉模糊的东西爬了出来，但是你们成功拿到了沾满血迹和肉酱的死亡证明。
你们害怕极了，躲着那团东西，往外面冲。离门很近了的时候，你的同事摔了下去，你同事大喊，救救我！！不要先走！你真的舍得抛弃关系如此亲密的同事吗？
31.抛下同事
32.去救同事

''',

'page30':'''咚咚咚，抽屉里面传来剧烈的冲撞声，一团血肉模糊的东西冲破抽屉，冲向你们，将你们吞噬。
''',

'page31':'''你冲了出去，关上了太平间的门，里面传来了同事的尖叫声，你流下了眼泪，但是，你还活着。
你手里紧紧拿着死亡证明，心里害怕极了，你擦掉眼泪，往产房出发。你刚走上楼梯，听到后面有脚步声。
你转身一看，你同事正向你走来，天呐！你没死！你惊叫道，刚想向他跑去，发现他脸色不对，你停下了脚步，同事怒吼了一声，冲了过来。
你跑到了一楼，往外面冲，你现在必须找一个人可以躲的地方。
33.母子相后面
34.树丛中

''',

'page32':'''是的，你死了。
''',

'page33':'''同事往母子相这边走来，但看到母子相却非常惧怕，走了。
你见同事已经走远，从母子相后面走了出来，扶着母子相，大口大口的喘气。呵呵，呵呵呵呵呵呵，你听到了一个女人的笑声。你心里一紧，呵呵呵，呵呵呵呵呵，又来了，好像是从上面传来的。你抬头一看，母子相的女人正对着你冷冷的笑着，你吓的尖叫了起来，并且惊动了你的同事，他从大楼里跑了出来，你吓的拼了命往前跑。那个女人对你说，呵呵，跑什么，刚不是离我很近的么，回来啊。不要！！你大声喊着。不要么，呵呵，话音刚落，整个医院里都传来了婴儿的哭声，这声音多么刺耳。不知不觉，你晕了过去。当你醒来时，你发现你在一个小屋子里。面前有一个中年人正在帮你的同事抽血。
35.趁机逃跑
36.留下询问

''',

'page34':'''即使杂草丛生，但不是瞎子都能看到的好么？
''',

'page35':'''外面依旧是婴儿的哭声，所以一出去就被杀死了。
''',

'page36':'''你是谁？”你语气略带试探的问道。“别多问，先来帮我忙，把镜子拿过来。”那个中年人严肃的说道。你只好先去拿镜子，你递给那个中年人，只见中年人拿着那镜子照向同事，一道金光闪现，“啊——”你同事尖叫了起来，疯狂的挣扎起来。你吓得躲在一边，捂住耳朵。尖叫声渐渐地停了，你往中年人那边看去，同事躺着不动了。“你在做什么！”你对中年人大叫道。“他被附身了。”那个中年人一点也不生气，还很有耐心的和你解释。“我在帮他消除体内的东西，他一会儿就醒了。”“哦。”你发现自己误会他了，感到有点愧疚。“你是谁啊，你在网上应该看过我的帖子吧？”中年人并没有直接回答你的问题。“哦！你是网上的写帖子的那个人！”你激动地站了起来，发现同事不在了。“那个……我同事不见了。”你对中年人说。那位中年人转过头去一看，喃喃的说：“哎呀，完了。”这时却传来了敲门声。“喂，是我啊，我是你同事，快放我进来，再不开门我要被杀死了。”
37.开门
38.不开门

''',

'page37':'''门外真的是你的同事，他活着进来了。
同事一进来就对你大叫：“不要关门，不要关门！！”你对他说：“你疯了么？不关门，你要我们都死啊！”中年人转过头来，看了一眼同事，突然对你大喊：“把他赶出去！快！把他赶出去！马上！”同事却满脸疑惑的说：“我怎么了啊？干嘛把我赶出去？”
39.赶出去
40.留下来

''',

'page38':'''同事又被附身了，最后的遗言是我恨你。
你觉得自己做错事了，听到同事的那一句“我恨你”，心里难过极了，你决定把同事的尸体拉进来，不让他在受到冤魂厉鬼的吞噬。你打开门，外面一片安静，你小心翼翼的把同事的尸体拖了进来。中年人转过头来，看了一眼同事，脸色大变大喊道：“扔出去！快！扔出去！马上！！”
39.扔出去
40.留下来

''',

'page39':'''中年人是正确的，同事突然不见了，显然是被冤魂带出去的。当然是附身着进来的，当你的同事出去的一刹那他眼睛变红，要向你冲过来，幸好你及时关上了门。
你冲动的跑过去抓着中年人：“为什么！为什么会这样！！你不是帮他了吗！！他怎么还会这样！！”中年人淡定的推开你的手：“这么厉害的冤魂，如果这一照就可以消除，我也不会躲在这里了。”“你！”你很激动但却说不出些什么，当你平静下来，你对他说：“我们去拿出生证明吧。”“呵，你死亡证明都没拿到就拿到出生证明，去找死？”你不服气的从口袋里拿出死亡证明，中年人脸上出现了一丝笑意却又马上收回了。“走，我们往后门走。”
41.独自往前门走
42.跟中年人往后门走

''',

'page40':'''留下来开始几分钟的确没事，渐渐的同事开始不对劲了，眼睛开始变红，突然他站了起来，嘴里念叨着：“报仇！报仇！！”向你和中年人冲了过来，你们死了。
''',

'page41':'''独自往前门走，门外一片安静，显然同事已经不在了。你紧紧的握着死亡证明，来到了二楼。
你来到了二楼，一片漆黑。你按动手电筒的开关，手电筒亮了几下，就暗了。“该死的，没电了！”你说着，尽量靠边往前走。“呵呵呵呵呵呵，呵呵呵呵……”那熟悉又阴森的笑声又响起了，母子相！！这是你的第一反应。该怎么办，怎么办？现在二楼都走了一半了，不可能再回到那个小屋了，你该躲到哪里去呢？
43.伸手不见五指的办公室
44.住院病房
45.原地不动

''',

'page42':'''跟着中年人往后门走，你们刚出后门，中年人就一把抢过你手中的死亡证明，并拿出匕首把你杀了
''',

'page43':'''你走了进去，里面一片漆黑，你什么也看不见。“呵呵呵……”你又听到了那个笑声，你感觉到背后凉凉的。“你真聪明啊，你来找我了……”你转过身去看，母子相就在你后面对着你笑。死。
''',

'page44':'''你找了一个床铺躺了下来，装死。母子相从办公室走了出来，正当你心里庆幸你没有躲在办公室的时候，母子相走进了住院病房。你屏住呼吸，躺着装死。母子相在病房里走了一圈，就出去了。
脚步声渐渐没了，你从病房里走了出来。刚踏出住院病房的门，你撞到了一个东西，你害怕极了，你摔在地上，眯着眼睛看那是什么。中年人，你撞到了中年人！中年人看到是你，对你说：“喂，你怎么跑到这里来了？刚找你呢！”
46.保护好死亡证明逃跑
47.和中年人一起去找出生证明

''',

'page45':'''母子相从办公室里走出来一眼就看到你了。死。
''',

'page46':'''中年人察觉你发现他的计划，气急败坏。拿出匕首，飞奔了过来。你来不及闪躲，被刺中心脏。你躺在地上流着血，亲眼看着中年人抢走你的死亡证明。
''',

'page47':'''和中年人一起去找出生证明：你知道中年人的计划，但并没有拆穿。因为你知道，只要你不说中年人在拿到出生证明之前，你是不会有任何生命危险的。于是你们安全的到了三楼。
刚走到三楼，你们听到了一个阴冷的声音。“真难得，你们来了啊，母子相竟然没找到你们，真是奇怪了啊。”你们抬头一看，原本那团血肉模糊的东西，已经现出它畸形的模样了。它手中还提着你的同事。
48.不管三七二十一，冲进去
49.往楼下走，逃跑

''',

'page48':'''你们跑到一个未知的房间，关死了门。“咚咚咚……”外面传来了那东西撞门的声音。过了一会儿渐渐停止了，显然畸形的婴儿放弃了。
你不知道这个房间是干嘛的，当你刚打开手电筒，就看到中年人在翻箱倒柜的找着什么。你上前去询问：“喂，你在找什么？”“你给我闭嘴！”中年人没好气的说。你只好拿着手电筒四处看看其他的。你看到了柜子上诡异的排放着胚胎、工具还有很多很多抽屉，你不小心被什么东西绊了一跤，撞到了柜子。这时，上面有一张纸飘了下来。
50.叫上中年人一起来看
51.独自拿起纸，翻过来看

''',

'page49':'''正巧撞见了母子相，母子相一阵阴笑，你们尝试了最恐怖的折磨与死亡的真谛，死。
''',

'page50':'''没错那张纸就是要找的出生证明。中年人看到你找到了出生证明，冷冷的对你说了一句：“哼，你已经没有利用价值了！”咚的一声，你眼前一片漆黑。死。
''',

'page51':'''发现这是出生证明，偷偷的放在口袋里，假装成若无其事的样子继续找着。
你沉浸在假装的氛围里，并没有在意中年人。当你转过头去看中年人的时候发现中年人盯着你看很久了，你心里一慌。中年人正慢步向你走来，走到你身旁时低声对你说：“现在乖乖的把出生证明和死亡证明都交出来！”
52.找附近的东西敲他，然后逃出房间
53.依旧信任的把出生证明和死亡证明交给他

''',

'page52':'''在找东西的时候被发现了，死。
''',

'page53':'''中年人暂时没在意，你们并没有离开那个房间，你下定了决心，要抢回中年人手里的出生证明和死亡证明。你变小了幅度继续寻找着。你发现墙角有很多的干柴，你决定把那些干柴收起来，你藏在了衣服里。中年人转过来对你说：“我们该出去了。”你点了点头跟在后面。
54.直接把出生证明和死亡证明抢回来
55.跟着中年人再走一段。

''',

'page54':'''你们太大的动静引起了畸形婴儿的注意，发现了你们，死。
''',

'page55':'''你们悄悄来到了二楼，开始躲避母子相的攻击。由于你的注意力都集中在你衣服里藏的干柴，并没有注意到脚下。“咔嚓”，你不知踩到了什么东西，你还没来得及低下头看踩到了什么，就听到了婴儿的哭声。接着是一阵笑声：“呵呵呵呵呵呵呵呵呵，你把我的孩子吵醒了！”那是母子相的声音！你害怕极了，这时中年人对你大喊：“快点过来，到这个房间来！”
56.跟着中年人跑进那个房间
57.冲过去抢走中年人手中的出生证明和死亡证明，冲到一楼去

''',

'page56':'''中年人看你冲了过来，立刻把门关上，你被关在了门外。被母子相追上来，杀死了。中年人趁着你被杀的时候，逃走了。死。
''',

'page57':'''中年人一直在等你进来，可以有机会逃跑，没想到你竟然没有跟着进来。中年人也没有来得及关门，母子相冲了进去，把中年人杀了，成功的跑到一楼。
你的心脏受到了打击，还在扑通扑通跳个不停，你现在又饥又渴，然后在墙壁上摸索，突然摸索到一个开关，你一按下去，先是开灯，然后墙上出现了三个穴，三个穴都一模一样，你回头看了一下，有一个包包，然后你把包包捡起来，打开，发现里面有一只手电筒两个面包，一瓶水和一瓶牛奶，还有一本笔记本，里面什么也没有写，还有一支笔还有一面镜子，接着又有一袋盐，你惊叹了一下，谁留下来的，这么多东西。
你看着墙上的三个穴口，现在必须要选一个跳进去，这时候三个穴口的顶上都出现了三条语录，
第一个：快进来！！
第二个：不要进1也不要进我这里！去3！
第三个：第一个是危险的！来我这里！
你将选择：
58.第一个洞穴
59.第二个洞穴
60.第三个洞穴

'''
,
'page58':'''最危险的地方就是最安全的地方，你成功甩掉了畸形婴儿。
一进入洞穴，你便拼了命的往前跑，担心畸形婴儿追上你， 相比畸形婴儿，你肯定没他的实力强，而且你钻到这里来他肯定也知道，你没跑多久，就听到洞穴四周的墙发出声音，又是那个令你恐惧的声音，咚咚咚，一声一声，你感觉你的心马上跳出来了，暗想，不要这么快就进来！你疯狂的往前跑，突然撞到了某物，你惊吓得大叫啊啊啊啊啊啊！某物伸出手捂住你的嘴巴，对你说：“嘘小声点，被畸形婴儿发现可不好，看见发着血光的物体必须屏着呼吸。”他顿了一下子，又说：“我也被困在这里了。”你若有所思地点点头，问他饿不饿，渴不渴，他耸了耸肩说他吃过东西了，你感觉你找到一个如同事般好的人，正在你这么想的时候，他用手指捅了捅你，问：“你叫什么名字啊？”
你不回答，因为看到前面一片明亮，诶？是要到终点了吗？你再也忍受不了这种折磨了，可是一走近却是三个人，在争吵一张“死亡证明”，你走近一看，吓了一跳，和自己这一张一模一样，连上面专有的污垢都一模一样，那三个人是一位老太太一位青年人还有一位小女孩，这时你会……
61.告诉他们这张纸是假的，你的手上那张才是真正的
62.捡起那张纸，对他们说，你们石头剪刀布谁赢了给谁。你还要快点忙去呢……

''',

'page59':'''你们失败得最悲哀，里面是母子相大人，母子相一把抓着你，把你变成她怀里的孩子，那就是说没有下一个顶替者你就得一辈子在她的怀抱里呆着。——死。
''',

'page60':'''此地无银三百两……第三个下面是个绞肉机，里面有许多和你一样被搅成肉馅的人们，你一进去，没听完“欢迎来到绞肉机”，你才听到“欢迎来到……”，你就被搅成肉馅了……
''',

'page61':'''他们没有你想得这么恐怖，只是你后遗症太重了，婆婆竟然还冷静的笑笑，说：“哎……原来是假的啊，刚刚还害了我们在这里吵了半天，谢谢你啊，你尽管很疑惑，但还是为了自己的生命着想……
你微笑的和他们再见，然后又继续往前走，可是那片亮光竟然很奇异的失踪了，你的心跳马上又开始怦怦跳，你又跺了跺脚，让自己不这么害怕，你甩甩头，突然又看见了一台奇异的机器，你连忙跑过去，看到的是一个装满了人肉的绞肉机！你大惊失色，突然后面传来了母子相的笑声，双重的恐惧使你的脚不停地颤抖，你想着用什么对付她？
63.手电筒
64.镜子
65.牛奶

''',

'page62':'''他们一同以为你脑子有病，不分青红皂白的把你和你旁边的这位一起推下了绞肉机，——死。
''',

'page63':'''光刺激到鬼，母子相残忍地把你吃掉。——死。
''',

'page64':'''你大手一挥！拿出了一面镜子……母子相一下子被自己的样貌给震惊了，忙从你的手上拿走了镜子，你不敢大声嚷嚷，留下母子相在那里自恋了。
你把镜子给她了之后，目瞪口呆地看了她三秒，觉得很奇异，母子相竟然觉得自己长得很好看！！但是有点危险，先走为妙，马上就走了，走了一段路，暂时摆脱了母子相，但你刚刚放松了一会儿，上面就有几滴水滴下来，吓得你一下子蹦起来，却碰上了一个软绵绵的东西，你抬头一看，一个吊死的人，全身血红，滴下来的是。。。。尸油嘛！？当你疑惑时，那只东西说话了，她说：“呵呵。。别怕我，我会帮助你的，给我点牛奶吧。。。。”你有点犹豫。。 
66.一个已经吊shi的人……给了吧…… 
67.有阴谋！绝对不给！！

''',

'page65':'''你对她说：“来吧，喝瓶三鹿牛奶，对身体有益。”那母子相惊奇的看着你，她就觉得你要伤害她，一口吃掉你了。——死
''',

'page66':'''你太心软了，那只女尸活过来了，依然是那副鬼样子，尽管你怎么求饶，她想也不想把你弄到绳子上，你就将此成为了一吊shi鬼…… 
''',

'page67':'''女尸有阴谋，给牛奶会活过来找你当替死鬼，幸好你不给，女鬼说了几句话之后就全身软软的了，掉下了一东西，那就是……牛奶。
你差点仰头长啸了。我勒个去。她自己不是有牛奶么，和你要这么多有个鬼用啊……想着，捡起那包有点诡异的三鹿牌牛奶君，从挂掉的人身上拿到的东西总该有点恶心吧。。你想着里面会不会有尸油蛋白神马的，慢慢走，听到了一种吹泡泡的声音，你沿着声音，走到了一个井旁，发现一个眉目清秀的小女孩在吹泡泡。吹泡泡声音传得好远，你这时需要。。 
68.过去询问应该怎么走 
69.置之不理。

''',

'page68':'''小女孩，又长又卷的睫毛抬起来，看了你一下，笑着对你说：“=w=。。往右边走，有个房子，你就进去吧，你会有惊喜的” 
你按照小女孩的指示去行事了，果然看到了一间屋子，但是觉得女孩有点诡异，终究没有敢大胆的走进去，而是在门口，发现里面传来三声有规律的敲门声“笃笃笃”有规律，不失惊悚，凭你的常识，知道这是有人在求救，你怕遇到什么像畸形婴儿什么的鬼东西，不敢开门，可是如果真的是自己的同伙呢，你犹豫了，但是你需要大胆的决定 
70.推门而入，不过碰到什么恐怖的东西也不一定 
71.不进入屋子，从窗子里看看，不过可能容易被吓死……

''',

'page69':'''不询问你是打算要在这里一辈子呆下去么！ 
''',

'page70':'''你破门而入了，发现一个皮全部剥开了的人，那个人受了惊吓然后，施了法术（强大了），血肉模糊使你眼前一黑，就什么都不知道了——死。
''',

'page71':'''都经历过这么多冒险了还怕个鬼啊！
你在窗子里看见里面有个皮全部剥开了的人，顿时吓傻了，转身看看那小女孩还在不在，发现突然不见了，反而多出了一个小黑屋，你会？ 
72.进去 
73.等着 
74.走开继续探险

''',

'page72':'''进去你发现有个叫“小贞”女孩的被纸团闭住了嘴巴，双手双脚都被捆住了，她被绑架了，你成功地营救了“小贞”。
你救出那位女孩时.女孩指着另一门，阴森森的说：那里..你被抓走的同事就在那里..。”你想不通这小女孩怎么知道你有个同事被抓走了，想来想去犹豫要不要去， 
75.不去 
76.去

''',

'page73':'''等的过程中贞子出来把你杀了。 
''',

'page74':'''听到“呵呵呵呵呵呵呵呵”一声，就死了 
''',

'page75':'''正好母子相闯入了这屋子——死。 
''',

'page76':'''“我想还是过去，看看会发生什么事儿？”你说着，进去后，里面是一条地道，墙上挂着个牌子上面写着“没想到你竟然能到这里.你的同事就在地道尽头的学校里.”地道尽头的确是有一所学校.我加快步伐.没想到地道旁边的一扇小门突然间的打开，我被吓的摔倒了.里面出来的竟然是贞子..贞子说“呵呵呵呵呵呵..我需要一把刀..你能借我用一用么...” 
77.借
78.不借

''',

'page77':'''贞子拿了你的刀.结果把你的头砍下来.然后全身体解剖——死。 
''',

'page78':'''你没有借给贞子.拿出符咒.把贞子定住了。
把贞子征服了以后【maya..征服！？】，走向地道的出口.已经天黑了.你在想往哪里走的时候.突然背后一阵凉风.让你毛骨悚然.一只冰凉的双手伸到你的脖子... 
79.转头 
80.不转头，逃走

''',

'page79':'''转头后，那位老奶奶对你说“我不是坏鬼....我是好厉鬼..【哦凑我还好丽友捏】你灰常的害怕眼前这脸色发青的老奶奶，颤抖的说“那..那这所学校是什么学校..怎么..怎么连个保安都木有啊！！！！？” 
老奶奶说“这里是恐怖学校……呵..里面都是鬼...你，敢跟我一起上楼么？”老奶奶做出一个非常恐怖的表情..加上她脸上发青..显得更恐怖...你有点害怕.. 
81.上楼 
82.不上楼

''',

'page80':'''被校园内的学生鬼弄死了！！ 
''',

'page81':'''老奶奶对你说“不错，真勇敢啊孩子！”
因为楼梯内的电灯泡不知道怎么回事.竟然是绿色的...一闪一闪..我扶着栏杆.慢慢的走上去.突然感觉似乎有什么东西滴到我脸上..你放进嘴巴尝了尝..竟然是血！然而你的手沾满了鲜血.老奶奶也不知去了哪儿..因为受到了鲜血的惊吓..不小心被什么东西绊倒了..原来那是一具尸体！皮被全部剥开..血肉模糊..眼睛被挖掉了..两只眼睛在地上直盯着你看..背后传来母子相的声音， 
83.回头直冲楼下冲到另一栋楼 
84.不停的往上跑

''',

'page82':'''你在校园里被一年级小厉鬼杀害——死。
''',

'page83':'''恭喜你冲到了另一栋楼暂时保住生命安全。
你走进了学校的教学楼，此时已是深夜，教学楼的灯已经关了。你在黑暗中摸索着，想找到上楼的楼梯。也许学校的老师会给你找个挨过今晚的地方。你很幸运，找到了。但楼梯的门却锁住了。 
你要找到钥匙，但当务之急是找到灯的开关。你不可能摸黑走这么远的路，你怕黑，刚才摸黑走了这么远，已经到了你的极限。 
你在墙上摸索着，摸到一摊湿漉漉的东西。你吓的缩回了手。慌乱中，摸到了口袋里的手机。手机！也许手机的光能让你看清楚面前的东西，顺便还能让你找到开关。但你真的有胆量去照吗？在你的家乡，流传着一个古老的传说：不要尝试用光去照“它们”，否则，你会被厉鬼所杀。你没有胆量去看见它们，更没有死亡的准备。现在，做出你的选择！ 
85.用手电去照，尽管你可能死的很惨？ 
86.独自摸索，尽管你可能永远找不到开关？

''',

'page84':'''你跑到了路的尽头坠下10楼身亡。
''',

'page85':'''你打开了手机，发现正在你面前的是一具自挂东南枝的尸体！你差点就要尖叫出来，但很幸运的，你在她身边找到了开关。
你深吸了一口气，按下了开关。灯光闪了几下，亮了。这个大厅的景象呈现在你眼前。或者。。。已经不是那个大厅了？你发现，你按过的灯的开关没有了，原来的窗户没有了，甚至。。。。连门都没有了。但是，你所摸到的尸体竟是真实的，还在淌着血。而且。。。当你转过身的时候，你发现，身后的墙壁上，有一根根裸露的钢筋，上面。。。竟全是上吊的尸体。但是上面竟有一根是空着的，上面有一捆绳子，就像是为你准备的。你吓得尖叫出来，即使冒着雨，你也要回去！你一刻也不想在这个鬼地方多呆了！但。。。真的回得去吗？你大着胆子，上前去检查那些尸体。他们的脸上。。。竟只有绝望的表情，他们，是因为绝望而自杀的，你断定。但同时，也感到了前所未有的恐惧这时，你在地板上发现了一具尸体，是一个小女孩，大概八、九岁，而她的脸上竟是与年龄不符的狞笑。她的心脏插着一枚大头针，而心脏的位置，密密麻麻的全是小洞。看得出来，这样的死法很痛苦。在她的身边，有一块手帕，上面有一行血字。我知道，我能出去，但我绝不成为它们之中的一员！“它们”是谁？你不知道。但那句“我能出去”引起了你的兴趣。你的目光逐渐移向空的钢筋和绳子。也许和它们有关？但，你真的忍心把小女孩挂在上面么？也许，你可以用你所买来的东西代替？（刚才你捡的东西竟一直没丢。）或者，你应该继续寻找线索？到了做出选择的时候了。 
87.把小女孩挂到上面 
88.把买来的东西放上去 
89.继续探险

''',

'page86':'''你放弃打开手机，坐在墙角边，感到越来越困，睡着了。从此再没有醒来。杀掉你的，不是鬼怪，而是压迫你心脏的恐惧。
''',

'page87':'''绳子突然卷住了你的脖子——死。
''',

'page88':'''钢筋瞬间穿透了你的身体——死。
''',

'page89':'''你从暗门里走了进去，发现你已经在学校的楼梯上了。你在楼梯上走着，楼梯上结满了蜘蛛网，每隔几个楼梯就有一摊干涸的血迹，你害怕极了，但你绝不想在返回那个恐怖的大厅。终于，楼梯到头了，你现在正在二楼的走廊。“嗒。。。嗒。。。。嗒。。。嗒。。。”忽然，你的身后传来了一阵诡异的嗒嗒声，这声音刚开始听不见，后来就越来越清晰，越来越清晰，最后，简直就是在耳边回响。你赶紧往前跑，快！快！那个宿舍就在眼前了！到了那里就安全了！突然，你的一只手被用力一拽，你被拽进了旁边一个小房间里，里面有着一滩滩血迹，甚至你在角落里发现了半个人头和一只残缺的手。“我是这所鬼校的清洁工，你叫我王婆婆吧。”婆婆露出一个奇怪的笑容。“走吧，我带你去找能躲过今晚的地方。”王婆婆好像不会伤害你，但是你想起了你在角落里发现的半个人头和手，这鬼校里真的会有活人吗？但是你想起了刚才的百鬼夜游，如果不是这位婆婆，那你已经。。。。。现在，应该做出选择了。 
90.相信王婆婆，并跟着她走 
91.不相信，赶紧逃跑

''',

'page90':'''你相信了王婆婆，跟着她走到了一个阴冷潮湿的地下室里。
“你就在这里呆一晚吧。记住，千万不要出去。”婆婆把你往地下室里一推，把门关上，走了。你没有发现，在她嘴角的一抹狞笑，以及那双眼睛，竟跟大厅里那以血所绘的女人脸有点相似。。。你站在黑暗的地下室中央。意识到了事情的不妙。你发现了里面几具阴森森的白骨，还有几具未完全腐烂的尸体。你冲到门口，想把门推开，突然发现，门外竟有一张人脸，她的眼睛正透过门缝直勾勾地看着你！你吓得往后退了几步，正好踩到了一具白骨，只听嘎嗒一声脆响，骨头断开了。你听到响声，回头去看，却不止看到了被踩碎的白骨，还看到了。。。看到了大厅里的小女孩的灵魂，正看着你。。。。“你放心，我不会伤害你。”小女孩说道“你不该到这里来，就像我一样。”透过小女孩身上发出来的幽灵的绿光，你勉强看清了这个地下室的样子。地下室的墙壁上竟有一张比大厅里放大了几十倍的人脸，在另外的墙壁上，泼满了鲜血。而残缺的肢体则处处都是。就像你的脚边，就有一节血肉模糊的肠子。。。你问她，怎样才能离开这里，并逃出学校。“我不知道，也许等到白天就能出去了。但是，呆在这的下场，只有死。”她缓缓说道。你知道，你绝不可能在这样一所只有鬼和尸体的学校里呆这么久。 
现在该怎么办？你被困在了这里。但是，你的心里还抱有一丝婆婆会把你带出去的希望，毕竟婆婆是人，而这小女孩是鬼。你应该信任自己的同类。但是，你看着这里残缺的肢体。你难道真的能相信婆婆吗？也许这小女孩是站在你这边的。或者，你应该像在大厅里那样，继续寻找线索？你的选择变得更加复杂。 
92.在原地等待，相信婆婆会把你带出去 
93.听小女孩的，和她一起想办法 
94.把门撞开

''',

'page91':'''王婆婆是厉鬼。你拔腿就跑，但是，你是一个人，你真的跑得过一个永不知疲倦的鬼么？你死去了，在临死之前，你仿佛看到了王婆婆和刚才的百鬼站在一起，朝你冷笑。。——死。
''',

'page92':'''在原地等待，被后来的鬼杀死。
''',

'page93':'''小女孩在你出去后，把你杀了。
''',

'page94':'''你又发现了一扇门，门后还有声音，凭你的常识，知道这是有人在求救，你怕遇到什么像畸形婴儿什么的鬼东西，不敢开门，可是如果真的是自己的同伙呢，你犹豫了，但是你需要大胆的决定
95.推门而入
96.不进入屋子，从窗子里看看

'''
,
'page95':'''你进去了房间，成功保住了自己的性命。
四周都是伸手不见五指的黑暗，迷茫已无法形容你的心情，恐惧早已遍布你的全身，你只能一直像着前方跑着，哪怕前方仍是黑暗，哪怕前方是另一种恐惧，可你，只能这样。身后，母子像的笑声犹如阵阵利剑，刺入你内心深处最黑暗的地方。慌乱之中，你的理智已经不知去向。前方的楼梯将你绊倒，这时你会。
97.爬起向楼梯上跑去
98.爬起向楼梯下跑去
99.吓尿裤子。。。傻了，原地不动。。。

''',

'page96':'''你被后面追来的母子相杀死。
''',

'page97':'''畸形婴睁大着铜铃般的眼睛诡异的看着你，你晕过去了。——死。
''',

'page98':'''母子相在那里，双手掐住了你。——死。
''',

'page99':'''由于您的尿臊味，母子像厌恶地转过身找畸形婴儿帮忙，你趁机逃跑。
你已经身心疲惫，掏出包包里最后一块食物（额，好像是有的哈。）塞进嘴里。跑着，来到一个泳池。泳池里的水竟然是那么清澈，将射出了五颜六色的光泽。这是怎样一幅图啊，是那么的美丽，同时，也是那么的诡异！你一个踉跄，不小心把空空如也的背包掉入水中，奇怪的是，水花没有，诡异的是，背在落6入水中的一瞬间，便消失了。你疑惑的伸手在水中捞了捞，背包竟然再次现身了。这时你会。
100.继续向前跑。
101.整个人跳入水中

''',

'page100':'''你被尾随的鬼追上。——死。
''',

'page101':'''那水有这隐形的神奇力量，且是一块神圣的地方，没有鬼魂啥滴赶接近。当母子像和畸形婴儿追上时，不过多久便走了。
你从水中爬出来，发现眼前这个熟悉的男子，竟然是同事！刚要喘口气，就发现所有的鬼都向你围过来，你无路可逃了。
你大喊到：我们这些人和那些医生是不一样的！为什么要这样害我们？你们为什么不现在就消失？你们。。。你的话还未说完，一阵狂风袭来，你睁不开眼睛。狂风消失，当你睁开眼睛的时候，同事缓缓开口：是呀，你们原本可以早日重新投胎的！重新过好日子的！你失声道：你不是。。不是被附身了。。了。。同事：对不起，我骗了你，最初的快递其实是我寄来的……我是一名除魔师，现在，就让我先把她们消灭吧！
'''
}

print('''这是一个灵异恐怖文字冒险游戏，请不要用正常逻辑来玩游戏哦～''')
time.sleep(3)
num=input('''
回复1冒险开始。
>''')
goodend = 101
badend = [5,6,9,10,11,13,15,17,19,21,22,24,25,28,30,32,34,35,40,42,43,45,46,49,50,52,54,56,59,60,62,63,65,66,69,70,73,74,75,77,80,82,84,86,87,88,91,92,93,96,97,98,100]
game=[]
time.sleep(1)
while True:

    game.append(num)
    print(superdict['page'+num])
    time.sleep(3)
    if int(num) == goodend:
        f = open('D:\\游戏记录.txt','a+')
        for x in game:
            f.write(superdict['page'+str(x)]+'\n\n')
            f.close
        input('''

♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
♥  恭喜你！你通过了最终的试炼，活了下来！！！  ♥
♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
游戏记录已保存至D盘根目录下！
点击Enter即可退出游戏~
注：故事情节出自百度贴吧《灵异吧》。
>''')

        break
    if int(num) in badend:
        f = open('D:\\游戏记录.txt','a+')
        for x in game:
            f.write(superdict['page'+str(x)]+'\n\n')
            f.close
        input('''很遗憾，您没能通关！

游戏记录已保存至D盘根目录下！
点击Enter即可退出游戏~
注：故事情节出自百度贴吧《灵异吧》。
>''')
        break
    num = input('请输入数字编码：')