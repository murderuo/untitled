# url="https://video.twimg.com/ext_tw_video/1230798013859352576/pu/vid/576x720/-B42TkhfbmahX45m.mp4?tag=10"

# url="https://twitter.com/TBB/status/1230497853728006144"
#
# print(url.split('/')[3])
import re
text="""<!DOCTYPE html>
<html lang="tr">
<head>
<title>Twitter Video Downloader - Twitter Videoyu MP4 ve MP3 olarak indir</title>
<meta name="description" content="Download Twitter Videos - Online, Ücretsiz, hızlı ve kullanımı kolay, Tweet&#039;lerden MP3, MP4&#039;e Twitter Videolarını Kaydet ve GIF&#039;i kaydet. Tek bir tıklama ile herhangi bir Twitter Video veya GIF indirin.">
<meta name="keywords" content="twitter video downloader, twitter videoları kaydet, mp4 twitter, mp3 twitter, twitter videoları indir, twitter video indir, twitter indir gif">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<meta name="HandheldFriendly" content="True">
<meta name="MobileOptimized" content="320">
<meta property="og:image" content="//www.savetweetvid.com/public/assets/images/icon-share.png">
<link rel="icon" href="//www.savetweetvid.com/public/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" type="image/x-icon" href="//www.savetweetvid.com/public/favicon.ico" />
<link rel="stylesheet" type="text/css" href="/public/assets/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="/public/assets/css/style.css?v=4">
<script src="/public/assets/js/jquery.min.js"></script>
<script src="/public/assets/js/bootstrap.min.js"></script>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-2984659695526033",
          enable_page_level_ads: true
     });
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-105090590-3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-105090590-3');
</script>
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js" async="async"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js" async="async"></script>
<![endif]--><link rel="canonical" href="https://www.savetweetvid.com/tr/downloader" />
<link rel="alternate" href="https://www.savetweetvid.com/tr/downloader" hreflang="x-default" />
<link rel="alternate" href="https://www.savetweetvid.com/tr/downloader" hreflang="tr" />
<link rel="alternate" href="https://www.savetweetvid.com/downloader" hreflang="en" />
<link rel="alternate" href="https://www.savetweetvid.com/es/downloader" hreflang="es" />
<link rel="alternate" href="https://www.savetweetvid.com/fr/downloader" hreflang="fr" />
<link rel="alternate" href="https://www.savetweetvid.com/de/downloader" hreflang="de" />
<link rel="alternate" href="https://www.savetweetvid.com/nl/downloader" hreflang="nl" />
<link rel="alternate" href="https://www.savetweetvid.com/it/downloader" hreflang="it" />
<link rel="alternate" href="https://www.savetweetvid.com/pt/downloader" hreflang="pt" />
<link rel="alternate" href="https://www.savetweetvid.com/pl/downloader" hreflang="pl" />
<link rel="alternate" href="https://www.savetweetvid.com/ro/downloader" hreflang="ro" />
<link rel="alternate" href="https://www.savetweetvid.com/ru/downloader" hreflang="ru" />
<link rel="alternate" href="https://www.savetweetvid.com/ja/downloader" hreflang="ja" />
<link rel="alternate" href="https://www.savetweetvid.com/ko/downloader" hreflang="ko" />
<link rel="alternate" href="https://www.savetweetvid.com/zh/downloader" hreflang="zh" />
<link rel="alternate" href="https://www.savetweetvid.com/vi/downloader" hreflang="vi" />
<link rel="alternate" href="https://www.savetweetvid.com/th/downloader" hreflang="th" />
<link rel="dns-prefetch" href="//www.google-analytics.com">
<link rel="dns-prefetch" href="//ssl.google-analytics.com">
<link rel="dns-prefetch" href="//s7.addthis.com">
<link rel="dns-prefetch" href="//m.addthis.com"></head>
<body>
<header>
<nav class="navbar navbar-default no-mrg">
<div class="container">

<div class="navbar-header">
<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="http://www.savetweetvid.com/tr" title="Twitter Video İndiricisi"><img src="/public/assets/images/logo.png" alt="Twitter Video İndiricisi"></a>
</div>
<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
<ul class="nav navbar-nav navbar-right">
<li><a href="http://www.savetweetvid.com/tr">home</a></li>
<li><a href="http://www.savetweetvid.com/tr/extension">Ayriyeten</a></li>
<li class="dropdown">
<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Nasıl <span class="caret"></span></a>
<ul class="dropdown-menu how-to-lists">
<li><a href="http://www.savetweetvid.com/tr/twitter-dan-videolar-nasil-kaydedilir" title="Twitter&#039;dan Videolar Nasıl İndirilir">Twitter&#039;dan video indir</a></li>
<li><a href="http://www.savetweetvid.com/tr/video-twitter-krom-indir" title="Uzantı ile Twitter videoları nasıl indirilir">Twitter videolarını uzantıya göre indirin</a></li>
<li><a href="http://www.savetweetvid.com/tr/mp3-icin-twitter" title="Bir Videoyu Twitter&#039;dan mp3&#039;e dönüştürme">Bir videoyu Twitter&#039;dan mp3&#039;e dönüştür</a></li>
</ul>
</li>
<li><a href="http://www.savetweetvid.com/tr/faq">FAQ</a></li>
<li class="dropdown langs">
<a id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="#">Türk <span class="caret"></span></a>
<ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
<li><a class="dropdown-item" href="http://www.savetweetvid.com/en/downloader">English</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/es/downloader">Español</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/fr/downloader">Français</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/de/downloader">Deutsch</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/nl/downloader">Nederlands</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/it/downloader">Italiano</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/pt/downloader">Português</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/pl/downloader">Polski</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/ro/downloader">Română</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/ru/downloader">Русский</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/ja/downloader">日本語</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/ko/downloader">한국어</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/zh/downloader">繁體中文</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/vi/downloader">Tiếng Việt</a></li>
<li><a class="dropdown-item" href="http://www.savetweetvid.com/th/downloader">ไทย</a></li>
</ul>
</li>
</ul>
</div>
</div>
</nav>
</header>
<script type="text/javascript" src="https://www.dropbox.com/static/api/2/dropins.js" id="dropboxjs" data-app-key="0ladnzgdiyesh12"></script>
<div class="page-content">
<div class="container">
<div class="row">
<div class="col-lg-12 col-centered">
<div class="ads mrg-bt20 text-center">
<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-2984659695526033" data-ad-slot="5734284394"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script> </div>
<div class="card">
<div class="row">
<div class="col-md-4 col-sm-4">
<a href="#myModalVideo" data-toggle="modal" class="card-aside-column img-video" style="height:121px;background: url(https://pbs.twimg.com/ext_tw_video_thumb/1232553260642373637/pu/img/2ec4C_PVXD-4I_Ua.jpg);background-size:cover;">
<span class="btn-play-video"><i class="glyphicon glyphicon-play"></i></span>
<p class="time-video" id="time"></p> </a>
<h5><a href="/profile/XHTurkey/">Xinhua Türkiye <i class="open-new-window"></i></a></h5> <p class="card-text">Bir hemşire, hayatını kurtarmak için sadece 8 saniyede ciddi bir koronavirüs hastasına bir mide besleme tüpü y...</p> </div>
<div class="col-md-8 col-sm-8 col-table">
<table class="table">
<thead>
<tr>
<th>quality</th> <th>format</th>
<th>size</th>
<th>Downloads</th>
</tr>
</thead>
<tbody>
<tr>
<td>360p </td> <td>mp4</td>
<td>4.96 MB</td>
<td>
<a href="https://video.twimg.com/ext_tw_video/1232553260642373637/pu/vid/640x360/BHloYHU0KSzH_K4C.mp4?tag=10" class="btn btn-download" rel="nofollow">İndir</a>
</td>
</tr>
<tr>
<td>270p </td> <td>mp4</td>
<td>1.75 MB</td>
<td>
<a href="https://video.twimg.com/ext_tw_video/1232553260642373637/pu/vid/480x270/8qh7dMBX84XUxl0C.mp4?tag=10" class="btn btn-download" rel="nofollow">İndir</a>
</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="3">MP3 Dönüştür ve İndir</td>
<td>
<a id="convertBtn" href="#" data-url="YUhSMGNITTZMeTkyYVdSbGJ5NTBkMmx0Wnk1amIyMHZaWGgwWDNSM1gzWnBaR1Z2THpFeU16STFOVE15TmpBMk5ESXpOek0yTXpjdmNIVXZkbWxrTHpZME1IZ3pOakF2UWtoc2IxbElWVEJMVTNwSVgwczBReTV0Y0RRL2RHRm5QVEV3" data-type="mp3" data-toggle="modal" data-target="#myModal" class="btn btn-download" rel="nofollow">İndir</a>
</td>
</tr>
</tfoot>
</table>
</div>
</div>
</div>
<div class="ads mrg-tp20 mrg-bt20 text-center">
<ins class="adsbygoogle" style="display:block;" data-ad-client="ca-pub-2984659695526033" data-ad-slot="5734284394" data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script> </div>
<div class="card card-qrcode">
<div class="row">
<div class="col-md-12 qrcode">
<div class="text-center">
<p class="qrcode-p">Akıllı telefonunuza veya tabletinize doğrudan indirmek için aşağıdaki QR kodunu tarayın!</p>
</div>
</div>
<div class="col-md-4 col-centered qrcode">
<div id="qrcode"></div>
<script src="/public/assets/js/qrcode.min.js"></script>
<script type="text/javascript">
								new QRCode(document.getElementById("qrcode"),{
								text: "https://video.twimg.com/ext_tw_video/1232553260642373637/pu/vid/640x360/BHloYHU0KSzH_K4C.mp4?tag=10",
																width: 120,
								height: 120,
								correctLevel : QRCode.CorrectLevel.L
								});
							</script>
</div>
<div class="col-md-4 text-center col-centered">
<a class="dropbox-saver" href="https://video.twimg.com/ext_tw_video/1232553260642373637/pu/vid/640x360/BHloYHU0KSzH_K4C.mp4?tag=10"></a>
</div>
</div>
</div>

<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
<div class="modal-dialog" role="document">
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
<h4 class="modal-title" id="myModalLabel">Xinhua Türkiye</h4>
</div>
<div class="modal-body">
<div class="modal-body">
<div id="process-waiting">
<p class="p-t">
<b>Dosya indirilmeye hazırlanırken lütfen bekleyin</b>
</p>
<div class="progress progress-striped progress-bar-warning active">
<div class="progress-bar progress-bar-success" style="width: 100%;">
<span>Loading...</span>
</div>
</div>
</div>
<div id="process-result">
<script>
										$(document).on('show.bs.modal','#myModal',function(e) {

										    var button = $('#convertBtn');
										    var url = (button).data('url');
										    var type = (button).data('type');

										    $("#process-waiting").css('display', 'block');
										    $("#process-result").empty();

										    $.ajax({
										    type: "POST",
										    url: 'https://www.savetweetvid.com/tr/download_',
										    data: {
										      url:url,
										      type:type
										    },
										    success: function(data){
										      $("#process-result").empty().append(data);
										    }
										  });

										});
									</script>
</div>
<div id="addthis" style="display: none;">
<p class="text-center">
Servisimizi kullandığınız için teşekkür ederiz. Web sitemizi arkadaşlarınızla paylaşabilirseniz, bu çok yardımcı olacaktır.
</p>
<div class="addthis_inline_share_toolbox"></div>
</div>
</div>
</div>
<div class="modal-footer">
<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
</div>
</div>
</div>
</div>
<div class="modal fade" id="myModalVideo" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
<div class="modal-dialog" role="document">
<div class="modal-content">
<div class="modal-body">
<div class="embed-responsive embed-responsive-16by9">
<video controls="controls" allowfullscreen id="video" controlsList="nodownload">
<source src="https://video.twimg.com/ext_tw_video/1232553260642373637/pu/vid/640x360/BHloYHU0KSzH_K4C.mp4?tag=10" type="video/mp4" />
</video>
<div class="playpause"></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<script src="/public/assets/js/scripts.js"></script>
<script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-5b4e4e02b5a61435" async="async"></script>
<script>window.cookieconsent_options={ "message":"Bu web sitesi tarama deneyimini geliştirmek ve ek işlevsellik sağlamak için çerezlerden yararlanır.", "dismiss": "Okay", "learnMore": "Daha fazla bilgi", "link": "http://www.savetweetvid.com/tr/privacy-policy", "theme": "dark-bottom" };</script>
<script src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/cookieconsent.min.js"></script>
<footer>
<div class="top-footer">
<div class="container">
<div class="row">
<div class="col-lg-12">
<p>SaveTweetVid resmi olarak Twitter ile ilişkili değildir. Sunucusunda korsan veya telif hakkı bulunan içeriği barındırmaz veya eğlendirmez ve indirilen tüm videolar doğrudan kendi CDN sunucularından ilgili kullanıcının makinesine yapılır.</p>
</div>
</div>
</div>
</div>
<div class="bottom-footer">
<div class="container">
<div class="row">
<div class="col-lg-12">
<p class="pull-left">Copyright©2020 SaveTweetVid. All Rights Reserved.</p>
<ul class="bottom_ul list-inline pull-right">
<li><a href="http://www.savetweetvid.com/tr/about">About</a></li>
<li><a href="http://www.savetweetvid.com/tr/faq">FAQ</a></li>
<li><a href="http://www.savetweetvid.com/tr/tos">Kullanım Şartları</a></li>
<li><a href="http://www.savetweetvid.com/tr/privacy-policy">Gizlilik Politikası</a></li>
<li><a href="http://www.savetweetvid.com/tr/feedback">Geri bildirim</a></li>
</ul>
</div>
</div>
</div>
</div>
</footer></body>
</html>"""


#        https://video.twimg.com/ext_tw_video/1232553260642373637/pu/vid/640x360/BHloYHU0KSzH_K4C.mp4?tag=10
urls=re.findall('https://video[a-zA-Z0-9_.:/\?=]*',text)
#https://video[a-zA-Z0-9_.:/\?=]*
print(set(urls))

#  /[0-9%-]*/[a-z]*