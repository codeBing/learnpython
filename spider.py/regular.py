# -*- coding: utf-8 -*-
import re
# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

pattern = re.compile(r'world')
match = re.search(pattern,'hello world!')
if match:
    print match.group()

pattern = re.compile(r'\d+')
print re.split(pattern,'one1two22three333four')

content = '''










<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta property="wb:webmaster" content="cb81e216cbe9a3b9" />


<meta name="description" content="糗事百科笑话段子分享社区,在这里你可以发现校园、办公室、家庭中正在发生的形形色色的搞笑糗事,分享身边有内涵的笑话故事。将无节操无底线进行到底。娱乐自己,放松大家,爆笑态度面对生活。"/>

<title>














【纯文笑话】- 糗事百科

</title>
<link href="http://static.qiushibaike.com/css/dist/web/app.min.css?v=53220" media="screen, projection" rel="stylesheet" type="text/css" />
<script>
window.app = {}; // global app object init
var _hmt = _hmt || []; // Baidu tongji API
</script>
<script type="text/javascript">
document.createElement('video');document.createElement('audio');document.createElement('track');
</script>
<style>
body {
padding-top: 0px !important;
}
</style>
<style type="text/css">
.adsbygoogle,.mb-m[style],.userbar + a[href^="http://item.taobao.com"] {display:none!important;display:none}</style>
</head>
<body>

<!-- Header Start -->
<div id="header" class="head">
<div class="content-block">
<div class="logo">
<a href="/">糗事百科</a>
</div>
<div id="menu" class="menu-bar clearfix">
<div class="menu clearfix">
<ul>
<li>
<a  href="/8hr">热门</a>
</li>
<li>
<a  href="/imgrank">纯图</a>
</li>
<li>
<a  id="highlight"  href="/text">纯文</a>
</li>
<li>
<a  href="/videorank">视频</a>
</li>
</ul>
</div>
</div>
<div class="userbar clearfix">
<div class="ad" id="qv-banner" >
<a target="_blank" href="http://www.qiushibaike.com/topic" onclick="clickQv()">
<img src="/static/images/v2/video12.png">
</a>
</div>
<div class="login hidden">
<a href="/my" class="username" id="uname" target="_blank"></a>
<div><a href="/logout" class="exit">退出</a></div>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' title="糗百账号登录">登录/注册 </a>
</div>
</div>
</div>
</div>
<script>var qvkey = 'qv12'</script>
<script type="text/javascript" src="http://static.qiushibaike.com/js/src/qvbanner.js?v=22ad9"></script>
<!-- Header End -->





<!-- Main content Start -->
<div id="content" class="main">
<div class="content-block clearfix">

<div id="content-left" class="col1">
<div class="v2_change clearfix" id="v2_change" >
<div class="menu_list">



<ul>
<li  class="act" >
<a href="/text">最热</a>
</li>
<span></span>
<li >
<a href="/textnew" class="no_border">最新</a>
</li>
</ul>


</div>
<div class="v2_check clearfix">

<a class="fn-signin-required check_tie" href="javascript:void(0);" data-go="http://webinsp.qiushibaike.com/inspect">
<span>审贴</span>
</a>

<a  class="fn-signin-required write_tie" href="javascript:void(0);" data-go="/add">
<span>投稿</span>
</a>
<div class="clear"></div>
</div>
</div>




<div class="article block untagged mb15" id='qiushi_tag_106903002'>

<div class="author">
<a href="/users/16749385">
<img src="http://pic.qiushibaike.com/system/avtnew/1674/16749385/medium/20150420102736.jpg" alt="王八与蛋" />
</a>
<a href="/users/16749385">王八与蛋 </a>
</div>


<div class="content">

哥们打电话给我，说估计被托下套了，我问对方点了什么酒？他说没点酒，就是对方点了三碗（特大）饭，已经吃掉两碗了。我无奈的回答他：“她不是托，是饭桶！你也是！”
<!--2015-05-27 06:40:08-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">5262</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106903002?list=text&s=4775696" id="c-106903002" class="qiushi_comments" title="31条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">31</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106903002" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106903002" class="up">
<a href="javascript:voting(106903002,1)" class="voting" data-article="106903002" id="up-106903002" title="5473个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">5473</span>
</a>
</li>
<li id="vote-dn-106903002" class="down">
<a href="javascript:voting(106903002,-1)" class="voting" data-article="106903002" id="dn-106903002" title="-211个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-211</span>
</a>
</li>

<li class="comments">
<a href="/article/106903002?list=text&s=4775696" id="c-106903002" class="qiushi_comments" title="31条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106902044'>

<div class="author">
<a href="/users/28647990">
<img src="http://pic.qiushibaike.com/system/avtnew/2864/28647990/medium/20150527005307.jpg" alt="麻辣个批" />
</a>
<a href="/users/28647990">麻辣个批 </a>
</div>


<div class="content">

刚吃了麻辣串，女友说很辣，爽。我就想起小时候和表弟去山坡上放牛，两人对着一窝野山椒尿尿，然后脑袋进水了就扯了红辣椒涂着对方的小弟弟玩。大概三秒钟，我们对望了一眼就鬼哭狼嚎的一起飞奔下山，跳进村口的池塘里泡了半天还是穿心的辣，那个蛋抽啊，害我几十年了都不敢摸辣椒。
<!--2015-05-27 04:29:31-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">8978</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106902044?list=text&s=4775696" id="c-106902044" class="qiushi_comments" title="91条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">91</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106902044" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106902044" class="up">
<a href="javascript:voting(106902044,1)" class="voting" data-article="106902044" id="up-106902044" title="9427个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">9427</span>
</a>
</li>
<li id="vote-dn-106902044" class="down">
<a href="javascript:voting(106902044,-1)" class="voting" data-article="106902044" id="dn-106902044" title="-449个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-449</span>
</a>
</li>

<li class="comments">
<a href="/article/106902044?list=text&s=4775696" id="c-106902044" class="qiushi_comments" title="91条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106872532'>


<div class="content">

一天晚上无聊，便拿起手机玩起微信摇一摇。随手一摇，便有个小妹，某人甚是开心，二人便云里雾里的侃侃而谈。3个小时过后某人感觉应该可以拿下的时候，便要求加对方好友准备见面了。怎知对方来了一句，我老公刚刚出去了，一会回来你们继续哈！我靠当时无语…
<!--2015-05-26 13:48:23-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">6087</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106872532?list=text&s=4775696" id="c-106872532" class="qiushi_comments" title="33条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">33</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106872532" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106872532" class="up">
<a href="javascript:voting(106872532,1)" class="voting" data-article="106872532" id="up-106872532" title="6394个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">6394</span>
</a>
</li>
<li id="vote-dn-106872532" class="down">
<a href="javascript:voting(106872532,-1)" class="voting" data-article="106872532" id="dn-106872532" title="-307个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-307</span>
</a>
</li>

<li class="comments">
<a href="/article/106872532?list=text&s=4775696" id="c-106872532" class="qiushi_comments" title="33条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106900436'>

<div class="author">
<a href="/users/24373952">
<img src="http://pic.qiushibaike.com/system/avtnew/2437/24373952/medium/20150101220521.jpg" alt="光腚捉鬼" />
</a>
<a href="/users/24373952">光腚捉鬼 </a>
</div>


<div class="content">

今天带着大虎 b女友去银行办信用卡，被告知信誉度不够，出门时那厮一脸的不悦，说道:“平时xing欲不是挺强的吗？怎么到银行xing欲度就不够了？”
<!--2015-05-27 01:29:14-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">4708</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106900436?list=text&s=4775696" id="c-106900436" class="qiushi_comments" title="42条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">42</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106900436" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106900436" class="up">
<a href="javascript:voting(106900436,1)" class="voting" data-article="106900436" id="up-106900436" title="4941个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">4941</span>
</a>
</li>
<li id="vote-dn-106900436" class="down">
<a href="javascript:voting(106900436,-1)" class="voting" data-article="106900436" id="dn-106900436" title="-233个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-233</span>
</a>
</li>

<li class="comments">
<a href="/article/106900436?list=text&s=4775696" id="c-106900436" class="qiushi_comments" title="42条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106870514'>

<div class="author">
<a href="/users/25572936">
<img src="http://pic.qiushibaike.com/system/avtnew/2557/25572936/medium/20150320084845.jpg" alt="炖碗棒子骨汤*" />
</a>
<a href="/users/25572936">炖碗棒子骨汤* </a>
</div>


<div class="content">

说个大一军训时候的..割割...大太阳晒了一个月，黑的啊... 军训完闺蜜请吃饭。     晚上，我都到餐馆了，那货明明就看到我了，还打个电话说：“你在哪啊？我咋看不到你？麻烦你吧牙露出来。” 牙露出来......
<!--2015-05-26 12:57:17-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">3336</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106870514?list=text&s=4775696" id="c-106870514" class="qiushi_comments" title="41条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">41</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106870514" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106870514" class="up">
<a href="javascript:voting(106870514,1)" class="voting" data-article="106870514" id="up-106870514" title="3498个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">3498</span>
</a>
</li>
<li id="vote-dn-106870514" class="down">
<a href="javascript:voting(106870514,-1)" class="voting" data-article="106870514" id="dn-106870514" title="-162个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-162</span>
</a>
</li>

<li class="comments">
<a href="/article/106870514?list=text&s=4775696" id="c-106870514" class="qiushi_comments" title="41条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106899468'>

<div class="author">
<a href="/users/253171">
<img src="http://pic.qiushibaike.com/system/avtnew/25/253171/medium/20150516235112.jpg" alt="动感超人…哔哔哔" />
</a>
<a href="/users/253171">动感超人…哔哔哔 </a>
</div>


<div class="content">

查驾照的交警看到了我驾驶证里面夹着的安全套，对我说：注意系安全套，不要疲劳驾驶。。。交警大哥，你到底几个意思？？
<!--2015-05-27 00:43:55-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2461</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106899468?list=text&s=4775696" id="c-106899468" class="qiushi_comments" title="21条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">21</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106899468" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106899468" class="up">
<a href="javascript:voting(106899468,1)" class="voting" data-article="106899468" id="up-106899468" title="2580个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">2580</span>
</a>
</li>
<li id="vote-dn-106899468" class="down">
<a href="javascript:voting(106899468,-1)" class="voting" data-article="106899468" id="dn-106899468" title="-119个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-119</span>
</a>
</li>

<li class="comments">
<a href="/article/106899468?list=text&s=4775696" id="c-106899468" class="qiushi_comments" title="21条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106899738'>

<div class="author">
<a href="/users/4620473">
<img src="http://pic.qiushibaike.com/system/avtnew/462/4620473/medium/20150527004809.jpg" alt="乳痣波班" />
</a>
<a href="/users/4620473">乳痣波班 </a>
</div>


<div class="content">

今晚宵夜吃冒菜，夹起一大块豆腐板往嘴里塞，一咬那些汤汁从鼻孔里喷出来，瞬间整个场面HOLD住了…
<!--2015-05-27 00:54:22-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2384</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106899738?list=text&s=4775696" id="c-106899738" class="qiushi_comments" title="24条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">24</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106899738" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106899738" class="up">
<a href="javascript:voting(106899738,1)" class="voting" data-article="106899738" id="up-106899738" title="2518个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">2518</span>
</a>
</li>
<li id="vote-dn-106899738" class="down">
<a href="javascript:voting(106899738,-1)" class="voting" data-article="106899738" id="dn-106899738" title="-134个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-134</span>
</a>
</li>

<li class="comments">
<a href="/article/106899738?list=text&s=4775696" id="c-106899738" class="qiushi_comments" title="24条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106902624'>

<div class="author">
<a href="/users/28607112">
<img src="http://pic.qiushibaike.com/system/avtnew/2860/28607112/medium/20150524173647.jpg" alt="一糗遮百醜" />
</a>
<a href="/users/28607112">一糗遮百醜 </a>
</div>


<div class="content">

有天上課小明在睡覺，老師就讓小明起來回答問題，老師：小明，如果你在森林里迷路了，遇見一直熊，你怎麼辦？ 小明：拿槍打死它。老師：如果沒有槍呢？小明：那就拿刀捅死它。老師：如果沒有刀呢？小明：老師，你是多想叫我死？
<!--2015-05-27 06:09:17-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1884</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106902624?list=text&s=4775696" id="c-106902624" class="qiushi_comments" title="23条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">23</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106902624" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106902624" class="up">
<a href="javascript:voting(106902624,1)" class="voting" data-article="106902624" id="up-106902624" title="1993个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">1993</span>
</a>
</li>
<li id="vote-dn-106902624" class="down">
<a href="javascript:voting(106902624,-1)" class="voting" data-article="106902624" id="dn-106902624" title="-109个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-109</span>
</a>
</li>

<li class="comments">
<a href="/article/106902624?list=text&s=4775696" id="c-106902624" class="qiushi_comments" title="23条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106870988'>


<div class="content">

不发不快:<br/>昨天领导换了一个房子，居然摆了十桌，下限最低200，上限不限。<br/>这种人简直太不要脸了，怎么当上领导的，<br/>这是我见过最不要脸的敛财方式！
<!--2015-05-26 13:09:06-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2452</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106870988?list=text&s=4775696" id="c-106870988" class="qiushi_comments" title="108条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">108</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106870988" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106870988" class="up">
<a href="javascript:voting(106870988,1)" class="voting" data-article="106870988" id="up-106870988" title="2599个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">2599</span>
</a>
</li>
<li id="vote-dn-106870988" class="down">
<a href="javascript:voting(106870988,-1)" class="voting" data-article="106870988" id="dn-106870988" title="-147个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-147</span>
</a>
</li>

<li class="comments">
<a href="/article/106870988?list=text&s=4775696" id="c-106870988" class="qiushi_comments" title="108条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106871974'>

<div class="author">
<a href="/users/27867194">
<img src="http://pic.qiushibaike.com/system/avtnew/2786/27867194/medium/20150423152313.jpg" alt="没想好叫啥呢1" />
</a>
<a href="/users/27867194">没想好叫啥呢1 </a>
</div>


<div class="content">

第一次发，不会割，有没有小时候像我一样春天的时候跟小伙伴捉迷藏，藏在狗窝里。邻居家的狗狗还很配合的堵在狗窝门口，晚上回家的时候发现自己身上刮了很多狗毛(春天狗掉毛）被自己老妈一顿狠K的？
<!--2015-05-26 13:33:52-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1440</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106871974?list=text&s=4775696" id="c-106871974" class="qiushi_comments" title="14条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">14</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106871974" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106871974" class="up">
<a href="javascript:voting(106871974,1)" class="voting" data-article="106871974" id="up-106871974" title="1524个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">1524</span>
</a>
</li>
<li id="vote-dn-106871974" class="down">
<a href="javascript:voting(106871974,-1)" class="voting" data-article="106871974" id="dn-106871974" title="-84个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-84</span>
</a>
</li>

<li class="comments">
<a href="/article/106871974?list=text&s=4775696" id="c-106871974" class="qiushi_comments" title="14条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106871214'>

<div class="author">
<a href="/users/12214086">
<img src="http://pic.qiushibaike.com/system/avtnew/1221/12214086/medium/20140330175948.jpg" alt="流浪巨巨巨" />
</a>
<a href="/users/12214086">流浪巨巨巨 </a>
</div>


<div class="content">

真事不割 今天兄弟伙外公过九十九大寿    吃饭的时候 七大姑八大姨各种敬酒 轮到兄弟的时候 这货说“外公 祝你生日快乐 长命百岁 ” 刚说完 他大姨一巴掌呼头上 你这是在咒你外公明年死么 尼玛 饭后就我和兄弟两人洗碗 据说是被罚的
<!--2015-05-26 13:14:59-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">3474</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106871214?list=text&s=4775696" id="c-106871214" class="qiushi_comments" title="34条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">34</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106871214" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106871214" class="up">
<a href="javascript:voting(106871214,1)" class="voting" data-article="106871214" id="up-106871214" title="3690个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">3690</span>
</a>
</li>
<li id="vote-dn-106871214" class="down">
<a href="javascript:voting(106871214,-1)" class="voting" data-article="106871214" id="dn-106871214" title="-216个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-216</span>
</a>
</li>

<li class="comments">
<a href="/article/106871214?list=text&s=4775696" id="c-106871214" class="qiushi_comments" title="34条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106898360'>

<div class="author">
<a href="/users/11528456">
<img src="http://pic.qiushibaike.com/system/avtnew/1152/11528456/medium/20140717145714.jpg" alt="我要睡春晚" />
</a>
<a href="/users/11528456">我要睡春晚 </a>
</div>


<div class="content">

我就想知道，糗百上一天天发照片说嫁不出去的妹子，看照片一个比一个漂亮，怎么就嫁不出去了，这么多单身的，气谁那，不匿了，糗百汉子们顶上去让他们看看！
<!--2015-05-27 00:10:36-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2258</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106898360?list=text&s=4775696" id="c-106898360" class="qiushi_comments" title="111条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">111</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106898360" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106898360" class="up">
<a href="javascript:voting(106898360,1)" class="voting" data-article="106898360" id="up-106898360" title="2398个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">2398</span>
</a>
</li>
<li id="vote-dn-106898360" class="down">
<a href="javascript:voting(106898360,-1)" class="voting" data-article="106898360" id="dn-106898360" title="-140个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-140</span>
</a>
</li>

<li class="comments">
<a href="/article/106898360?list=text&s=4775696" id="c-106898360" class="qiushi_comments" title="111条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106901694'>

<div class="author">
<a href="/users/26821082">
<img src="http://pic.qiushibaike.com/system/avtnew/2682/26821082/medium/20150413233422.jpg" alt="我早干嘛去了" />
</a>
<a href="/users/26821082">我早干嘛去了 </a>
</div>


<div class="content">

晚上上夜班，中间有两个小时的休息时间。一个女同事刚睡醒跑过来和我说她冷，我就告诉她抱一下就不冷了，然后抱了她一会就放手了。她说还是冷，我好尴尬…
<!--2015-05-27 03:30:07-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">3089</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106901694?list=text&s=4775696" id="c-106901694" class="qiushi_comments" title="62条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">62</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106901694" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106901694" class="up">
<a href="javascript:voting(106901694,1)" class="voting" data-article="106901694" id="up-106901694" title="3288个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">3288</span>
</a>
</li>
<li id="vote-dn-106901694" class="down">
<a href="javascript:voting(106901694,-1)" class="voting" data-article="106901694" id="dn-106901694" title="-199个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-199</span>
</a>
</li>

<li class="comments">
<a href="/article/106901694?list=text&s=4775696" id="c-106901694" class="qiushi_comments" title="62条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106870548'>

<div class="author">
<a href="/users/3783453">
<img src="http://pic.qiushibaike.com/system/avtnew/378/3783453/medium/20120925172926.jpg" alt="金满仓" />
</a>
<a href="/users/3783453">金满仓 </a>
</div>


<div class="content">

老婆脾气越来越差了<br/>时不时就发脾气 ……歌……有一次被骂操了想揍她 手举起来了突然迷茫了：打哪里呢？脸打坏了给我自己丢人 胸/屁股/腿打坏了以后我自己用着不爽 肚子是我未来孩子的老家 更不能打 纠结了半天 最后一耳光干自己脸上了
<!--2015-05-26 12:58:00-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2002</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106870548?list=text&s=4775696" id="c-106870548" class="qiushi_comments" title="75条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">75</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106870548" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106870548" class="up">
<a href="javascript:voting(106870548,1)" class="voting" data-article="106870548" id="up-106870548" title="2134个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">2134</span>
</a>
</li>
<li id="vote-dn-106870548" class="down">
<a href="javascript:voting(106870548,-1)" class="voting" data-article="106870548" id="dn-106870548" title="-132个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-132</span>
</a>
</li>

<li class="comments">
<a href="/article/106870548?list=text&s=4775696" id="c-106870548" class="qiushi_comments" title="75条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106899460'>

<div class="author">
<a href="/users/28558290">
<img src="http://pic.qiushibaike.com/system/avtnew/2855/28558290/medium/20150521232430.jpg" alt="╯▂╰风吹裤衩" />
</a>
<a href="/users/28558290">╯▂╰风吹裤衩 </a>
</div>


<div class="content">

一朋友早上起来上厕所，经过他父母的房间的时候，发现没人，以为他爸跟他妈都去上班去了（其实他爸在厨房做早餐）。于是心血来潮，放声高歌：“我家住在黄土高坡，我爸是我妈表哥，两人还没结婚就偷偷摸摸，于是就有了我，有了……后面那个“我”字还没唱出口，一只锅铲破门而入厕所，哥们带着吓尿的声音问：谁？厨房里传来了一个熟悉的声音：“你妈她表哥”。
<!--2015-05-27 00:43:32-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">901</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106899460?list=text&s=4775696" id="c-106899460" class="qiushi_comments" title="49条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">49</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106899460" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106899460" class="up">
<a href="javascript:voting(106899460,1)" class="voting" data-article="106899460" id="up-106899460" title="957个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">957</span>
</a>
</li>
<li id="vote-dn-106899460" class="down">
<a href="javascript:voting(106899460,-1)" class="voting" data-article="106899460" id="dn-106899460" title="-56个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-56</span>
</a>
</li>

<li class="comments">
<a href="/article/106899460?list=text&s=4775696" id="c-106899460" class="qiushi_comments" title="49条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106872126'>

<div class="author">
<a href="/users/9478565">
<img src="http://pic.qiushibaike.com/system/avtnew/947/9478565/medium/20140925152721.jpg" alt="会哭的小人o若若" />
</a>
<a href="/users/9478565">会哭的小人o若若 </a>
</div>


<div class="content">

世界上最悲伤的事儿，就是你刚进公司实习，还在维持良好形象的阶段，说话不敢大声，啃鸡腿不敢大口，却在用牙齿开果冻的时候磕到牙龈，流了好多血……公司里的人已经笑翻了，我去冷静一下。。。
<!--2015-05-26 13:37:55-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1563</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106872126?list=text&s=4775696" id="c-106872126" class="qiushi_comments" title="21条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">21</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106872126" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106872126" class="up">
<a href="javascript:voting(106872126,1)" class="voting" data-article="106872126" id="up-106872126" title="1668个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">1668</span>
</a>
</li>
<li id="vote-dn-106872126" class="down">
<a href="javascript:voting(106872126,-1)" class="voting" data-article="106872126" id="dn-106872126" title="-105个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-105</span>
</a>
</li>

<li class="comments">
<a href="/article/106872126?list=text&s=4775696" id="c-106872126" class="qiushi_comments" title="21条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106903284'>

<div class="author">
<a href="/users/14902534">
<img src="http://pic.qiushibaike.com/system/avtnew/1490/14902534/medium/20140506190353.jpg" alt="终于可以改昵称了，改成啥子呢？" />
</a>
<a href="/users/14902534">终于可以改昵称了，改成啥子呢？ </a>
</div>


<div class="content">

看到一个说自己是升旗手的突然想起高中那会，升旗手把绳子卡在旗杆顶端的转轮上了，然后我就上去了，嗖嗖嗖就顺旗杆爬，快顶时“吱”，尼玛，裆开了，下面全场笑崩了，回头一看那场面……还是赶紧取开绳子下去吧!
<!--2015-05-27 06:57:33-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1351</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106903284?list=text&s=4775696" id="c-106903284" class="qiushi_comments" title="14条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">14</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106903284" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106903284" class="up">
<a href="javascript:voting(106903284,1)" class="voting" data-article="106903284" id="up-106903284" title="1442个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">1442</span>
</a>
</li>
<li id="vote-dn-106903284" class="down">
<a href="javascript:voting(106903284,-1)" class="voting" data-article="106903284" id="dn-106903284" title="-91个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-91</span>
</a>
</li>

<li class="comments">
<a href="/article/106903284?list=text&s=4775696" id="c-106903284" class="qiushi_comments" title="14条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106871056'>

<div class="author">
<a href="/users/23552473">
<img src="http://pic.qiushibaike.com/system/avtnew/2355/23552473/medium/20150515134545.jpg" alt="哇大锤" />
</a>
<a href="/users/23552473">哇大锤 </a>
</div>


<div class="content">

刚有个人给我打电话说我儿子在他手上，我问他觉不觉得黏，他居然骂我神经病，怎么回事啊，
<!--2015-05-26 13:10:38-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1578</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106871056?list=text&s=4775696" id="c-106871056" class="qiushi_comments" title="36条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">36</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106871056" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106871056" class="up">
<a href="javascript:voting(106871056,1)" class="voting" data-article="106871056" id="up-106871056" title="1689个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">1689</span>
</a>
</li>
<li id="vote-dn-106871056" class="down">
<a href="javascript:voting(106871056,-1)" class="voting" data-article="106871056" id="dn-106871056" title="-111个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-111</span>
</a>
</li>

<li class="comments">
<a href="/article/106871056?list=text&s=4775696" id="c-106871056" class="qiushi_comments" title="36条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106872202'>

<div class="author">
<a href="/users/26611052">
<img src="http://pic.qiushibaike.com/system/avtnew/2661/26611052/medium/20150315091356.jpg" alt="理工小王子" />
</a>
<a href="/users/26611052">理工小王子 </a>
</div>


<div class="content">

今天在路上，听到两个妹子在讨论怎么请领导吃饭，一妹子说我们请他吃牛排，另外一个突然来了一句，我们请他吃“草”怎么样？草！！！！妹子，你是组织的吧！
<!--2015-05-26 13:39:39-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1412</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106872202?list=text&s=4775696" id="c-106872202" class="qiushi_comments" title="13条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">13</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106872202" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106872202" class="up">
<a href="javascript:voting(106872202,1)" class="voting" data-article="106872202" id="up-106872202" title="1511个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">1511</span>
</a>
</li>
<li id="vote-dn-106872202" class="down">
<a href="javascript:voting(106872202,-1)" class="voting" data-article="106872202" id="dn-106872202" title="-99个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-99</span>
</a>
</li>

<li class="comments">
<a href="/article/106872202?list=text&s=4775696" id="c-106872202" class="qiushi_comments" title="13条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="article block untagged mb15" id='qiushi_tag_106898096'>

<div class="author">
<a href="/users/28329096">
<img src="http://pic.qiushibaike.com/system/avtnew/2832/28329096/medium/20150511122059.jpg" alt="花式撸管华东冠军" />
</a>
<a href="/users/28329096">花式撸管华东冠军 </a>
</div>


<div class="content">

二逼同学到上海来找我，让我接他！下面是通话内容。我：喂，你在哪？ 二逼：早到了，我现在自己溜达溜达呢！我：那告诉我在什么位置！我马上来接你.  二逼： 我旁边有个肯德基。我：尼玛，上海那么多肯德基我哪知道你在哪，说什么路！二逼：博友路 我：博友路肯德基对吗？ 二逼：恩，快来吧！咱俩待会喝一杯。挂了电话，招了辆出租车，师傅，到博友路！ 师傅愣了几秒说：兄弟啊！ 上海百分之八九十都是柏油路，其它是水泥路！我也不知道你说的是哪条柏油路啊……发完这条关机了，就让那二逼在外面自生自灭吧！
<!--2015-05-27 00:04:09-->

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2802</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/106898096?list=text&s=4775696" id="c-106898096" class="qiushi_comments" title="47条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="number">47</i> 回复
</a>



</span>
</div>
<div id="qiushi_counts_106898096" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-106898096" class="up">
<a href="javascript:voting(106898096,1)" class="voting" data-article="106898096" id="up-106898096" title="3013个顶">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">3013</span>
</a>
</li>
<li id="vote-dn-106898096" class="down">
<a href="javascript:voting(106898096,-1)" class="voting" data-article="106898096" id="dn-106898096" title="-211个拍">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-211</span>
</a>
</li>

<li class="comments">
<a href="/article/106898096?list=text&s=4775696" id="c-106898096" class="qiushi_comments" title="47条评论" target="_blank" onclick="_hmt.push(['_trackEvent', 'post', 'click', 'signlePost'])">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a title="分享到微信" href="###" class="jiathis_button_weixin"></a>
<a title="分享到QQ好友" href="###" class="jiathis_button_cqq"></a>
<a title="分享到QQ空间" href="###"class="jiathis_button_qzone"></a>
<a title="分享到新浪微博" href="###" class="jiathis_button_tsina"></a>
<a title="分享到百度贴吧" href="###" class="jiathis_button_tieba"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>






<div class="pagebar clearfix">
<div class="clearfix">

<a class="prev disabled" href="javascript:void(0);" title="上一页">
<i class="iconfont">&#xf0022;</i>
</a>


<span class="current" >1</span>




<a href="/text/page/2?s=4775696" title="第2页">2</a>



<a href="/text/page/3?s=4775696" title="第3页">3</a>



<a href="/text/page/4?s=4775696" title="第4页">4</a>



<a href="/text/page/5?s=4775696" title="第5页">5</a>



<span class="dots">…</span>


<a href="/text/page/35?s=4775696" title="第35页">35</a>


<a class="next" href="/text/page/2?s=4775696" title="下一页">
下一页<i class="iconfont">&#xf0025;</i>
</a>

</div>
</div>

</div>



<div class="col2">
<div id="sidebar" class="sidebar">
<div class="shopwindow">
<script async src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
style="display:inline-block;width:300px;height:250px"
data-ad-client="ca-pub-4939841000086153"
data-ad-slot="7972904204"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
<div class="shopwindow">
<script type="text/javascript">
/*右侧2*/
var cpro_id = "u693365";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</div>
<div class="sidebar-tutorial">
<h5>小提示</h5>
<div class="sidebar-tutorial-block">
<div class="sidebar-tutorial-keyboard"></div>
<div class="sidebar-tutorial-text">按 Ctrl+D 键，<br/>把糗事百科加入收藏夹</div>
<div class="sidebar-clear"></div>
</div>
</div>
<div class="sidebar-hot">
<h5>爆笑糗事精选</h5>
<ul>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

<li>
<a target="_blank" href="/article/105357566?ref=yc">
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="/>
<p></p>
</a>
</li>

</ul>
<div class="sidebar-clear"></div>
</div>
<div class="sidebar-tag">
<h5>热门话题标签</h5>
<div class="sidebar-tag-block">
<a href="/tag/%E5%A4%A9%E7%8E%8B%E7%9B%96%E5%9C%B0%E8%99%8E">天王盖地虎</a>
<a href="/tag/%E5%B0%8F%E9%B8%A1%E7%82%96%E8%98%91%E8%8F%87">小鸡炖蘑菇</a>
<a href="/tag/%E4%B8%80%E5%8F%A5%E8%AF%9D%E4%B8%8D%E5%89%B2">一句话不割</a>
<a href="/tag/%E9%80%86%E5%A4%A9">逆天</a>
<a href="/tag/%E9%BA%BB%E8%BE%A3%E7%83%AB">麻辣烫</a>
<a href="/tag/%E7%82%AB%E5%AF%8C">炫富</a>
<a href="/tag/%E6%83%85%E4%BE%A3">情侣</a>
<a href="/tag/%E4%BC%A4%E4%B8%8D%E8%B5%B7">伤不起</a>
<a href="/tag/%E6%A0%A1%E5%9B%AD">校园</a>
<a href="/tag/%E5%9B%B4%E8%A7%82">围观</a>
<a href="/tag/JJ">JJ</a>
<a href="/tag/ML">ML</a>
<a href="/tag/%E9%9D%9E%E4%B8%BB%E6%B5%81">非主流</a>
<a href="/tag/%E7%A9%BF%E8%B6%8A">穿越</a>
<a href="/tag/%E7%A7%92%E6%9D%80">秒杀</a>
<a href="/tag/%E8%90%9D%E8%8E%89">萝莉</a>
<a href="/tag/hold">hold</a>
<a href="/tag/%E8%85%90%E5%A5%B3">腐女</a>
<a href="/tag/TT">TT</a>
<a href="/tag/%E5%BE%A1%E5%A7%90">御姐</a>
<a href="/tag/%E6%AD%A3%E5%A4%AA">正太</a>
<a href="/tag/%E6%B2%99%E5%B0%98%E6%9A%B4">沙尘暴</a>
<a href="/tag/%E9%80%9F%E5%BA%A6%E4%B8%8E%E6%BF%80%E6%83%85">速度与激情</a>
<a href="/tag/%E5%A5%94%E8%B7%91%E5%90%A7%E5%85%84%E5%BC%9F">奔跑吧兄弟</a>
<a href="/tagcloud/1">更多标签</a>
<div class="sidebar-clear"></div>
</div>
</div>
<div class="shopwindow">
<script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "http://p.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script>
</div>

<div class="shopwindow">
<script type="text/javascript">
/*右侧3*/
var cpro_id = "u1101312";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</div>
</div>
</div>



</div>
</div>
<!-- Main content end -->
<!-- 适配微信分享img -->
<img src="http://static.qiushibaike.com/images/sharelogox.png?v=41921" style="position: absolute; left: -9999px; top: -9999px;">

<!-- Footer Start -->
<div class="foot">
<!-- ad-bottom-->
<div style="clear: both;text-align: center;background: #f3f1ec;padding-bottom: 20px;padding-top: 10px;">
<script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_32512564"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_32512564";
tanx_s.async = true;
tanx_s.src = "http://p.tanx.com/ex?i=mm_108378320_8760716_32512564";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script>
</div>
<div class="foot-nav">
<div class="foot-nav-1">
<h5>关于</h5>
<ul>
<li><a href="http://about.qiushibaike.com/about.html" target="_blank">糗事百科</a></li>
<li><a href="http://about.qiushibaike.com/jobs.html" target="_blank">加入我们</a></li>
<li><a href="http://about.qiushibaike.com/feedback.html" target="_blank">在线反馈</a></li>
<li><a href="http://about.qiushibaike.com/agreement.html" target="_blank">用户协议</a></li>
<li><a href="http://about.qiushibaike.com/policy.html" target="_blank">隐私政策</a></li>
</ul>
</div>
<div class="foot-nav-2">
<h5>手机</h5>
<ul>
<li><a href="http://android.myapp.com/android/appdetail.jsp?appid=107431&icfa=15144196000105020000&lmid=2031" target="_blank" class="foot-icon-download">安卓客户端</a></li>
<li><a href="http://itunes.apple.com/app/id422853458" target="_blank" class="foot-icon-download">iPhone客户端</a></li>
<li>手机访问 m.qiushibaike.com</li>
</ul>
</div>
<div class="foot-nav-3">
<h5>订阅</h5>
<ul>
<li><a href="http://weibo.com/qiushibaike" target="_blank">新浪微博</a></li>
<li><a href="http://user.qzone.qq.com/1492495058" target="_blank">QQ空间</a></li>
<li><a href="#" class="foot-wechat">微信<span class="foot-icon-wechat"></span></a></li>
<li><a href="http://t.qq.com/qiushibaike" target="_blank">腾讯微博</a></li>
<li><a href="http://mail.qq.com/cgi-bin/bookcol?colid=314" target="_blank">QQ邮箱订阅</a></li>
</ul>
</div>
<div class="foot-nav-4">
<h5>合作</h5>
<ul>
<li>糗百粉丝群：<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank" class="foot-icon-qq">全国</a></li>
<li>商务合作：<a href="mailto:marketing@qiushibaike.com">marketing@qiushibaike.com</a></li>
</ul>
</div>
<div class="foot-clear"></div>
</div>
<div class="foot-copyrights">
&copy; Qiushibaike.com 版权所有<span class="foot-col-line">|</span>
京ICP备14028348号<span class="foot-col-line">|</span>
京ICP证140448号<span class="foot-col-line">|</span>
京公网安备11010502026088
</div>
</div>
<!-- Footer End -->

<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">使用合作账号登录 /免邀请码注册</h4>
<a oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat" onclick="_hmt.push(['_trackEvent', 'login', 'click', 'wechat'])">
使用 微信 账号</a>
<a oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fsession" class="social-btn social-weibo" onclick="_hmt.push(['_trackEvent', 'login', 'click', 'weibo'])">
使用 微博 账号</a>
<a oauth_href href="http://openapi.qzone.qq.com/oauth/show?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/session?src=qq" class="social-btn social-qq" onclick="_hmt.push(['_trackEvent', 'login', 'click', 'qq'])">
使用 QQ 账号</a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">使用糗百账号登录</h4>
<form method="post" action="/session">
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit" onclick="_hmt.push(['_trackEvent', 'login', 'click', 'qiubai'])">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a href="/new4/fetchpass" class="fetch-password" onclick="_hmt.push(['_trackEvent', 'login', 'click', 'fetchpass'])">忘记密码?</a>
<!--<a href="/new4/signup" onclick="_hmt.push(['_trackEvent', 'login', 'click', 'signup'])">注册</a>-->
</div>
</div>
<div class="sigin-right">
<img src="http://static.qiushibaike.com/images/erweima.png?v=98c9c">
<span>扫一扫，下载手机客户端</span>
</div>
</div>

<!-- BackToTop Start-->
<div class="float-nav">
<a class="float-nav-feedback" href="http://about.qiushibaike.com/feedback.html" target="_blank">
<span class="float-nav-feedback-icon"></span>
反馈
</a>
<a class="float-nav-backtop" href="#">
<span class="float-nav-backtop-icon"></span>
顶部
</a>
</div>
<!-- BackToTop End-->

<!--[if gte IE 6]>
<script type="text/javascript" src="http://static.qiushibaike.com/js/src/web/json3.js?v=3a7f6"></script>
<![endif]-->
<script type="text/javascript" src="http://static.qiushibaike.com/js/dist/web/libs.min.js?v=0774b"></script>
<script type="text/javascript" src="http://static.qiushibaike.com/js/dist/web/app.min.js?v=7c3da"></script>
<!--分享部分页面-->
<script type="text/javascript" src="http://v3.jiathis.com/code/jia.js?uid=2019687" charset="utf-8"></script>
<script type="text/javascript" >
var jiathis_config={
data_track_clickback:true,
summary:' ',
appkey:{
"tsina":"63372306",
"tqq":"100251437"
},
shortUrl:false,
hideMore:false
}
function setShare(title, url,pic) {
jiathis_config.pic= pic;
jiathis_config.title = title;
jiathis_config.url = url;
}
$(".article").each(function(){
var o = $(this);
o.find(".single-share").on("mouseover",function(){
var url = o.find(".qiushi_comments").attr("href");
url = url ? "http://"+window.location.host+url : window.location.href;
var content = o.find(".content").html();
var title = "@糗事百科 "+ $.trim(content).replace(/\<[^\>]+\>/g,"");
var pic = o.find(".thumb img").attr("src");
if(!pic) pic = o.find(".video_cover").attr("src");
pic = pic ? pic : "http://"+window.location.host+"/static/images/v2/tumb.png";
setShare(title,url,pic);
});
});
</script>



<!-- Scripts init -->
<script type="text/javascript">
$(document).ready(function(){
// bottom nav
bottomNav.init();
// float ad
setTimeout(function(){
var left = $('.main .content-block .col1');
var sidebar = $('#sidebar');
if (left.height() > sidebar.height()) {
window._floatAd = activeFloatAd($('#sidebar'),'bottom');
}
},500);
// Recommender
$('#recommender').find('img.thumb-small').each(function() {
Recommender.resize(134, $(this));
});
// key binding
key('left', function(){
var singlePager = $('#pager-new');
var archivePager = $('.content-block .pagebar');
if (singlePager.length) {
window.location.href = $('#pager-new a.pager-pre').attr('href');
}
if (archivePager.length && archivePager.find('a.prev').length) {
window.location.href = archivePager.find('a.prev').attr('href');
}
});
key('right', function(){
var singlePager = $('#pager-new');
var archivePager = $('.content-block .pagebar');
if (singlePager.length) {
window.location.href = $('#pager-new a.pager-next').attr('href');
}
if (archivePager.length && archivePager.find('a.next').length) {
window.location.href = archivePager.find('a.next').attr('href');
}
});
// placeholder
$('input[placeholder], textarea[placeholder]').placeholder();
});
</script>
<!-- Baidu tongji -->
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F2670efbdd59c7e3ed3749b458cafaa37' type='text/javascript'%3E%3C/script%3E"));
</script>

</body>
</html>
'''.decode('utf-8')
content.replace(r'</br>','')
pattern = re.compile('<div.*?class="author".*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content".*?>(.*?)<!--(.*?)-->.*?</div>.*?<span.*?<i.*?>(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0]+' '+item[2],item[1],item[3]