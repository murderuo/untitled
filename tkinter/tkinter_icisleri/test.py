code=r"""C:\Users\ugurokur\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/ugurokur/PycharmProjects/untitled/tkinter/tkinter_icisleri/login_script.py
<html xmlns="http://www.w3.org/1999/xhtml"><head id="ctl00_ctl00_headMain"><title>
	e-İÇİŞLERİ PROJESİ
</title><meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="Page-Exit" content="progid:DXImageTransform.Microsoft.Fade(duration=.5)"><link href="../../App_Themes/Main/master2011.css" rel="stylesheet" type="text/css"><link href="../../App_Themes/Main/Main.css" rel="stylesheet" type="text/css"><link href="../../App_Themes/Main/Images/Genel/icislerilogo.ico?v=1.1" rel="shortcut icon" type="image/x-icon">
    <script type="text/javascript">

        function RunOnPageLoad() {
            try {//Yeni Yetki Master'i etkin ise footer kapatilir
               // HideMainMasterFooter();
            }
            catch (exception) { }
        }
        
    </script>
    <style type="text/css">
        .SelectedCssClass .rpText
        {
            background-color: Silver;
            text-decoration: underline;
        }
        .SelectedCssClass
        {
            background-color: Silver;
        }
    </style>
    <style>

        .gridPane {
            width:49%;
        }

            .gridPane > table {
                width:100%
            }

        .solidRightBorder {
            border-right:1px solid #cdd0d4;
        }

        .solidBottomBorder {
            border-bottom:1px solid #cdd0d4;
        }

        .scrollable {
            overflow:hidden;
            overflow-y:auto;
            padding-right:17px;
            scrollbar-base-color:#3aa2c9;
            scrollbar-arrow-color: #1f89bd;
        }

        .h600 {
            max-height:600px;
        }

        .h900 {
            max-height:850px;
        }

        .viewerPane {
            width:50%;
        }

        .gridCommands {
            
        }

        .top {
            vertical-align:top;
        }

        .center {
            margin-left:auto; 
            margin-right:auto;
        }

        .viewerButtons {

        }

    </style>
    <link href="../XMLEditor/CSS/ImzaSurecBilgisiTablo.css" rel="stylesheet" type="text/css">

    <script type="text/javascript" language="javascript">
        //Bu master'ı kullanan sayfanın içinde "PrintDiv" isminde bir Div tanımlandığında ve master üzerindeki bir butona tıklandığında
        //tanımlanan Div'in altı HiddenFieldInnerHtml'e aktarılır. Bu hidden field'den InnerHtml alınıp Utils Class'ı altındaki
        //ConvertHtmlToPdf methoduna parametre olarak gönderilir ve PrintDiv altındaki içerik Pdf'e çevrilir, buradan da istenirse yazıcıya gönderilir

        function onGuvenlikSozlesmesi() {
            document.getElementById("overlay").style.display = "block";
            var element = document.getElementById('ctl00_ctl00_divMainMenu');
            element.style.display = "none";
        }

        function offGuvenlikSozlesmesi() {
            document.getElementById("overlay").style.display = "none";
            var element = document.getElementById('ctl00_ctl00_divMainMenu');
            element.style.zIndex = "100";
        }

        function GetInnerHtmlOfPrintDiv() {
            var objDiv = document.getElementById('ctl00_cph1_PrintDiv');
            var objDivY = document.getElementById('ctl00_cph1_PrintDivYatay');

            var objHfld = document.getElementById('ctl00$HiddenFieldInnerHtml');
            var objHfldPgOr = document.getElementById('ctl00$HiddenFieldPageOrientation');

            if (objDiv != null) {
                objHfld.value = objDiv.innerHTML;
                objHfldPgOr.value = "Portrait";
            }
            else if (objDivY != null) {
                objHfldPgOr.value = "Landscape";
                objHfld.value = objDivY.innerHTML;
            }
        }
        //function btnkapatveKaydetVisableTureFalseYap() {
        //    var checkBox =      document.getElementById('ctl00_chbbtnVisible');
        //    var btn = document.getElementById("onaybuttondiv");
        //    if (checkBox.checked == true) {
        //        btn.style.display = "block";
        //    } else {
        //        btn.style.display = "none";
        //    }
        //}
    </script>
    <style type="text/css">
        .YetkiMenuDiv2011 {
            position: fixed;
            top: 3px;
            padding-top: 33px;
            padding-left: 5px;
            z-index: 100;
        }


        #aa {
            font-weight: bold;
            position: fixed;
            left: 0;
            right: 0;
            margin: auto;
            top: 20%;
            -webkit-transform: translateY(-50%);
            -ms-transform: translateY(-50%);
            transform: translateY(-50%);
            height: auto;
            padding: 17px;
            background-color: #eeeeee;
            text-align: center;
            box-sizing: content-box;
            border: 2px solid black;
            margin: 1px 25% 0px 25%;
        }

        .guvenlikBaslikdiv {
            float: left;
            width: 100%;
            display: inline-block;
            word-break: break-all;
            text-align: center;
            margin-top: 3px;
            margin-bottom: 23px;
        }

        .guvenlikAciklamadiv {
            float: left;
            width: 100%;
            display: inline-block;
            word-break: break-all;
            text-align: justify;
            margin-top: 3px;
            margin-bottom: 23px;
        }

        #guvenlikChkboxdiv {
            float: left;
        }

        #onaybuttondiv {
               text-align: center;
                
        }

        #overlay {
            position: fixed;
            display: none;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#0000000,endColorstr=#0000000);
            z-index: 2;
            cursor: pointer;
            background-color:rgba(8, 7, 7, 0.9);
        }

        #text {
            position: absolute;
            top: 50%;
            left: 50%;
            font-size: 50px;
            color: white;
            transform: translate(-50%,-50%);
            -ms-transform: translate(-50%,-50%);
        }

        /* The container */
        .container {
            /*display: block;*/
            position: relative;
            padding-left: 20px;
            margin-bottom: 12px;
            cursor: pointer;
            font-size: 14px;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }

            /* Hide the browser's default checkbox */
            .container input {
                position: absolute;
                opacity: 0;
                cursor: pointer;
                height: 0;
                width: 0;
            }

        /* Create a custom checkbox */
        .checkmark {
            position: absolute;
            top: 2px;
            left: 0;
            height: 13px;
            width: 13px;
            background-color: #fff;
            border: 1px solid;
        }

        .btnOnay {
            /*display: none;*/
            height: 25px;
            border: 1px solid;
            border-radius: 6px;
            font-size: 11pt;
            background-color:rgba(0, 187, 255, 1);
        }
        /* On mouse-over, add a grey background color */
        .container:hover input ~ .checkmark {
            background-color: #ccc;
        }

        /* When the checkbox is checked, add a blue background */
        .container input:checked ~ .checkmark {
            background-color: #2196F3;
        }

        /* Create the checkmark/indicator (hidden when not checked) */
        .checkmark:after {
            content: "";
            position: absolute;
            display: none;
        }

        .lblGuvelikOzlesmesi {
            margin: 40%;
            font-size: 11pt;
        }

        /* Show the checkmark when checked */
        .container input:checked ~ .checkmark:after {
            display: block;
        }

        /* Style the checkmark/indicator */
        .container .checkmark:after {
            left: 4px;
            top: 0px;
            width: 4px;
            height: 7px;
            border: solid white;
            border-width: 0 3px 3px 0;
            -webkit-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
            transform: rotate(45deg);
        }
    </style>
<script type="text/javascript" language="javascript" src="../../Javascript/SessionControl.js"></script><link href="/WebResource.axd?d=9FBPq6ZMdyYvKMIIRnR_-o8DrEyNEck-21LHH59d68llPDGuMtUOHiJf9iwGP2cRIc5YyHQij4qm8qVNvwuv0HZ9pwixpr4AUZF-t3YAbok7Vi3EdvWF4EXiGSq_uJjPy0MKRQ2&amp;t=637384753360000000" type="text/css" rel="stylesheet" class="Telerik_stylesheet"><link href="/WebResource.axd?d=0Y4q-QLpZcne3OG0-sjjaYmyD8h97Zywjuz_OszKzVpCXcNTSsOYeQj_i1LAYZwyhmTKmZxo0RMro8nZHNRHafUhWaTjVOX2WwyX99IoRe1hlO61gmPHQg76k6wdMe-wikmYBA2&amp;t=637384753360000000" type="text/css" rel="stylesheet" class="Telerik_stylesheet"><script>NS_CSM_td=1147974607;NS_CSM_pd=275116667;NS_CSM_u="/clm10";NS_CSM_col="af_collector_10.0.100.85";</script><script type="text/javascript">function sendTimingInfoInit(){setTimeout(sendTimingInfo,0)}function sendTimingInfo(){var wp=window.performance;if(wp){var c1,c2,t;c1=wp.timing;if(c1){var cm={};cm.ns=c1.navigationStart;if((t=c1.unloadEventStart)>0)cm.us=t;if((t=c1.unloadEventEnd)>0)cm.ue=t;if((t=c1.redirectStart)>0)cm.rs=t;if((t=c1.redirectEnd)>0)cm.re=t;cm.fs=c1.fetchStart;cm.dls=c1.domainLookupStart;cm.dle=c1.domainLookupEnd;cm.cs=c1.connectStart;cm.ce=c1.connectEnd;if((t=c1.secureConnectionStart)>0)cm.scs=t;cm.rqs=c1.requestStart;cm.rss=c1.responseStart;cm.rse=c1.responseEnd;cm.dl=c1.domLoading;cm.di=c1.domInteractive;cm.dcls=c1.domContentLoadedEventStart;cm.dcle=c1.domContentLoadedEventEnd;cm.dc=c1.domComplete;if((t=c1.loadEventStart)>0)cm.ls=t;if((t=c1.loadEventEnd)>0)cm.le=t;cm.tid=NS_CSM_td;cm.pid=NS_CSM_pd;cm.ac=NS_CSM_col;var xhttp=new XMLHttpRequest();if(xhttp){var JSON=JSON||{};JSON.stringify=JSON.stringify||function(ob){var t=typeof(ob);if(t!="object"||ob===null){if(t=="string")ob='"'+ob+'"';return String(ob);}else{var n,v,json=[],arr=(ob&&ob.constructor==Array);for(n in ob){v=ob[n];t=typeof(v);if(t=="string")v='"'+v+'"';else if(t=="object"&&v!==null)v=JSON.stringify(v);json.push((arr?"":'"'+n+'":')+String(v));}return(arr?"[":"{")+String(json)+(arr?"]":"}");}};xhttp.open("POST",NS_CSM_u,true);xhttp.send(JSON.stringify(cm));}}}}if(window.addEventListener)window.addEventListener("load",sendTimingInfoInit,false);else if(window.attachEvent)window.attachEvent("onload",sendTimingInfoInit);else window.onload=sendTimingInfoInit;</script><style type="text/css">.highslide img {cursor: url(/App_Themes/Main/highslide/graphics/zoomin.cur), pointer !important;}.highslide-viewport-size {position: fixed; width: 100%; height: 100%; left: 0; top: 0}</style></head>
<body id="ctl00_ctl00_masterBody" style="margin: 0px; padding: 0px; font-family: Tahoma, Geneva, sans-serif; font-size: 12px; color: rgb(51, 51, 51);" onkeyup="SessionUzat();" onmousedown="SessionUzat();" onunload="CarpidanCikisYap();">
    <form name="aspnetForm" method="post" action="./EvrakAnaSayfa.aspx" id="aspnetForm" disabled="disabled">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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">
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=pynGkmcFUV13He1Qd6_TZJSNQQPB4p4mqMsF8MSWLBAr5t1b7mfaZCK3fCBjweh4qYIkMQ2&amp;t=637297793819849385" type="text/javascript"></script>


<script type="text/javascript">
//<![CDATA[
var __cultureInfo = {"name":"tr-TR","numberFormat":{"CurrencyDecimalDigits":2,"CurrencyDecimalSeparator":",","IsReadOnly":true,"CurrencyGroupSizes":[3],"NumberGroupSizes":[3],"PercentGroupSizes":[3],"CurrencyGroupSeparator":".","CurrencySymbol":"₺","NaNSymbol":"NaN","CurrencyNegativePattern":8,"NumberNegativePattern":1,"PercentPositivePattern":2,"PercentNegativePattern":2,"NegativeInfinitySymbol":"-∞","NegativeSign":"-","NumberDecimalDigits":2,"NumberDecimalSeparator":",","NumberGroupSeparator":".","CurrencyPositivePattern":3,"PositiveInfinitySymbol":"∞","PositiveSign":"+","PercentDecimalDigits":2,"PercentDecimalSeparator":",","PercentGroupSeparator":".","PercentSymbol":"%","PerMilleSymbol":"‰","NativeDigits":["0","1","2","3","4","5","6","7","8","9"],"DigitSubstitution":1},"dateTimeFormat":{"AMDesignator":"ÖÖ","Calendar":{"MinSupportedDateTime":"\/Date(-62135596800000)\/","MaxSupportedDateTime":"\/Date(253402289999999)\/","AlgorithmType":1,"CalendarType":1,"Eras":[1],"TwoDigitYearMax":2029,"IsReadOnly":true},"DateSeparator":".","FirstDayOfWeek":1,"CalendarWeekRule":0,"FullDateTimePattern":"d MMMM yyyy dddd HH:mm:ss","LongDatePattern":"d MMMM yyyy dddd","LongTimePattern":"HH:mm:ss","MonthDayPattern":"dd MMMM","PMDesignator":"ÖS","RFC1123Pattern":"ddd, dd MMM yyyy HH\u0027:\u0027mm\u0027:\u0027ss \u0027GMT\u0027","ShortDatePattern":"d.MM.yyyy","ShortTimePattern":"HH:mm","SortableDateTimePattern":"yyyy\u0027-\u0027MM\u0027-\u0027dd\u0027T\u0027HH\u0027:\u0027mm\u0027:\u0027ss","TimeSeparator":":","UniversalSortableDateTimePattern":"yyyy\u0027-\u0027MM\u0027-\u0027dd HH\u0027:\u0027mm\u0027:\u0027ss\u0027Z\u0027","YearMonthPattern":"MMMM yyyy","AbbreviatedDayNames":["Paz","Pzt","Sal","Çar","Per","Cum","Cmt"],"ShortestDayNames":["Pa","Pt","Sa","Ça","Pe","Cu","Ct"],"DayNames":["Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi"],"AbbreviatedMonthNames":["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara",""],"MonthNames":["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık",""],"IsReadOnly":true,"NativeCalendarName":"Miladi Takvim","AbbreviatedMonthGenitiveNames":["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara",""],"MonthGenitiveNames":["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık",""]},"eras":[1,"MS",null,0]};//]]>
</script>

<script src="/ScriptResource.axd?d=uHIkleVeDJf4xS50Krz-yBCrNRY_FYLzyIqABUxKKoUtVOWpeTCBZdkfgQpyOXShBaAAkuf1dcWfPmexpZnPIhvmt_jY0Bvdh6gALFWqpHLVHbN8ZtN0DuuNRgUD44R2E3C9t5Rkp7-Y7jUcKdsRreb33fo1&amp;t=ffffffffce034dab" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=Jw6tUGWnA15YEa3ai3FadKtGf-RtKqKlSKXsEOcjfgUiN0ZJPJ1gpuKxTCrEpcVDArdWlSR-h5LqdZlyHfqdIHI027QmbkE1xhvGVzvp7UNjGnloAj3g0Qtbi2p6WlLyLr5DN45LKqodf2WcMl51xgmelAM1&amp;t=ffffffffce034dab" type="text/javascript"></script>
<script src="../../Javascript/jquery-1.10.2.min.js" type="text/javascript"></script>
<script src="../../Javascript/GenelYeni.js" type="text/javascript"></script>
<script src="../../Javascript/PopUp.js" type="text/javascript"></script>
<script src="../../Javascript/TabStrip.js" type="text/javascript"></script>
<script src="../../Javascript/UyariGoruntule.js" type="text/javascript"></script>
<script src="../../Javascript/UserControlTextBox.js" type="text/javascript"></script>
<script src="../../Javascript/Tarih.js" type="text/javascript"></script>
<script src="../../Javascript/TarihIkili.js" type="text/javascript"></script>
<script src="../../Javascript/GenelTextBox.js" type="text/javascript"></script>
<script src="../../Javascript/json.js" type="text/javascript"></script>
<script src="../../Javascript/jqueryPlugins/jquery.tmpl.min.js" type="text/javascript"></script>
<script src="../../Javascript/jqueryPlugins/JqueryAutoComplete/jquery.autocomplete.js" type="text/javascript"></script>
<script src="../../Javascript/jqueryPlugins/JqueryAutoComplete/AutoCompleteFormat.js" type="text/javascript"></script>
<script src="../../Javascript/UserControlAutoComplete.js" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=8u3ngCqoRB16IXgFyG-fdgjNp10DQaSKkjTSscTLZiq32OqFBf9Xubka18Ipz5Ei9JZ6bvX3M3TcBR6zcCPUZ1M7V3wYZUQ66kvtZYANQztmNrHa0&amp;t=ffffffffae8a8857" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=pL5wgiwL1GpmyqMwhkDjFy0U5k8Ppcvk6GwihoGtDC1Hw9F6PfLlgwuxqIHCGQjuFuZvjwPkPK8AYNNufRt3A2s_h-lce-hXviiGCfQ45HDjdhFO64kt3kjRY5TW4wonZ4xwmw2&amp;t=ffffffffae8a8857" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=dnHi0nMgDDe1Bo6v1KTdpMq0OtJcQNhtRmHhmfz16ySX5OUh_hhjG5UeQ946D05PKClXbdvSSH8KsP_FHTn4cHfK3MiPT0NTRxYinUucNZM7mXsivS0r7Z3OkDPFL6imovMdEQ2&amp;t=ffffffffae8a8857" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=fXuWcQwzGDZIk7t9UCjetZoAw7lzIz2ECawl0HqAzVUsrV73Kg6iqpiEZUpssNzaK8qsR93olHCM5E_W3aL_WVRZL5s17qImKXUJ5IsnPgUbKUKz9yAiUmgMaUNekUgmV5E-IchrwGunH3jxpBP1ovDz7wQ1&amp;t=ffffffffae8a8857" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=Bj-7Nu7LrruNTcLQ-JV4TAI-v8qYX0oEgIFWwarj_Gf6-li4iE95BD1_JYeZpQh58xBzf6_N6cL7LEkMr2_KkIEqh28RuypvZ-bK73Pd9DWm91p4u3tetCZyKQoaOgeNKwnULg2&amp;t=ffffffffae8a8857" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=rlicvrbMGEB1GFbgiKVbMEzxlwUI2DRhJ26kdP8OuERulnEjI-TNPfsjhi7J40UxCBh5Nnay2WQQPfRFRe1Xn36nCZ5m9nAVo4iWPLoQkcRc2RkU47bgXnEY_WhKOYcUZ2mZXQ2&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=5h0NtxUlQa8Df2oWXPhULyDzPIXaBnqXie6AYW3xjcHR-BEfkfdQj5-CjppwKtT5_cykpUIPzWA_60usUQ6N1zGmM2MTVUaUQrBGpiJhd173qjoE5kb5yGCIgKKvJlGyxskgNA2&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=CqwIbZAUnW7FSFSzLAcom0uuPRwDccgMU8wAqobXnmdJJGCXgTVel1HnGZZVt3UVMVFEuOFN9UKa5iiHq5adpHSr-N38t_31oZuJ_O2bqRjHi7NrDuFdKxibZRyqY9C4fG8weA2&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=I5r_uwF_kmHq3vRnqwJ1ARFkRBZfALvciy5yKtdenpGEgn1cZ1GdW7hr6E77zULdE6JL60LQV0nfbuRgYO7QTfzL-Dx7Q3sDewlw5f7gP_SbETPuISEh2HwnZq0iLx8qiovhyd7Z2n5YRJNH2W1dSlRThX41&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=lCgaAwKchW3Jed4tyDtHQ1WnvmlxJXOnw7m6C3-hnsAeoVdpCL6RxbgZbqJcu4cXcwjQvAUwzSCgJqn-wt_JxaBY1XryOUMOX8iEaoETidXSWpG8-R5zzYX0FL64xNiWUaiCghlvl6DYLO1eJNrlTDGa7EtmY_HUACxBC-syi75OyI540&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=6wa3I55aEUG9Dm2RoAuxyHVNPf8tFx-c-t8VrMb7Sc2cs4wwdpfLEmKkIWYgH8HDJ4dQshGFSaIEoWwFym1vWD-2sZm_IX2MGUNkfcaJ_9CoXlrM7dtxh0tKOm19rcPCLz2mqyhJoO9y7VwearuBJgiyoPykB4mQ86TOpPorKoSPLWp10&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=iJc5GC8IP03yL3OMTkjySvcIrPeDLA4eLT6bqJjYRLchlEIWn_RxCCnolXwijyd54WPv9SvxPO0usO7UY4Wie9qI04_3h2N1YS8R2okulbO3HvVQ0e1qBj7MEsfS-g0DjwlnOcwzkX-b1InkhOERYx-9GnU1&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=8atfSV1JXUIsloAr70CRL6HPoYXQ1t4j4AS6a5ZpQWnyEtgZ5zulUq5262c_UByZ0zNxQ58mopkrgO55zUpLeCRYbLuu5SplWzQ6UQ7-vyabINYIATs20R1pOUqx7xTMJk8Gz2Pu64cqQfsfLRGKCenkaSU1&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=1_HN8NE_aonX90W5kRPrGWi16Xb3hUNeNds-BmoXp4SmQKj4EdLiIOILfUYwDqhIqlNXKDJr8G_7JvjaKC0az1kIpRWfWfbgk5BCK7horE9HPVszEDdfXx3Hg5B1iyMyiAM1BUWU1SkwPFiXjTU1OdAvJbI1&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=a8-5fblyF_ztGy9t8kO_wIfSoz89Mr95-EwE6yTrHYPuNbs7X9Yp-2ctC7KMixpm5Og2mw2pME6LlecJSA5qIjevEcY0wGSt-LN5LwMil-yrbbV75GNXHPtPZX5BYMsMLO6qKpG4-bmbaB7-huvKl23CHheEt-tU6tfCorVzA2Ki3ZXc0&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=u2luSl1xdo5oVvzd8PiF7e4aRrP2cZhQp7MCvqK_B_pIHsUV5jSg6lNXAVf0A442J2lhtG1tSgWAO8l910dh8VRhUEeJnefH9L81KZuguEWQKLJUOOt4N_mFIoeaFWHi66Ad8aKV49m-96mhDktHuTtR-lg1&amp;t=1f6c9a90" type="text/javascript"></script>
<script src="../../WebServices/MasterPageWS.asmx/js" type="text/javascript"></script>
<script src="../../WebServices/FillCascadeDdlViaJs.asmx/js" type="text/javascript"></script>
<script src="../../WebServices/BilgiYardimMetni.asmx/js" type="text/javascript"></script>
<script src="../../WebServices/UserControls.asmx/js" type="text/javascript"></script>
<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="6D2DD3E4">
	<input type="hidden" name="__VIEWSTATEENCRYPTED" id="__VIEWSTATEENCRYPTED" value="">
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="i3euMLLAwViYk9xfNbTCbqyXdRkjcoK1bLpjxHmfZJf/GY8tMdOhPhEIc38K5uOc5YGgBkcZkL9UoNIe4nt/HV2u4+PDeBfjJYk6Jh8NHYV68ZUJt004Ejd4r9MbsrIbZYY6iR5bucgzRTcB5jZq2a2azb5bojKe8ol0e6+u3kVtkRi+fnJutxI6CCe5z9OMCDE68A7JHk6i5HYp/gEF27eiq1qaZYP3n0UcvUGhvtw9KuiV0aVbn/lDA9Z1ggs6e89oN4a6ridq5x1mHwV3DJpaUYjOGRoI1EWIuK0AHK/yY5BXJjQCLfDqJcrht2SwBk3FwCNGu+Dwdrdw41OweLR1HGh4yZysD+y2p4pJu8XEqfD6gTFhi2rGV3q7Dx6rRuUyNRS3GgNP1mq9KrhtIPR1IP1m5tWYk1ltXB1+lQgvFz8Lzs5OGNxJ4Tu/28K+oYZpIz1bcEolCnDGJzZttJ4054Vz4ykrEidaoFM3kdprO0Os0CC/P109idQWbjV4OnCOf7oc/NhDrEC4Jw59RwDFDhGCbgjX1VC/e+CH21DTEFOIwHkTLmlg7uZA3kJ9WpSO8wHK02twAKIRePXQi7eEq5vI5hRkEjj7VOey2Oi+JMWogppZJeUXQfFR4c+hIO/RpObQNK1L9NqDeO1byD254vTub23V3AG8u6OYtVK+NcRjfTSwMBaFeFuLkSC1cCAwHcMeF1DkWIhCCMFXNK5FMWSwnFu1eVl/rRaJ672s6rpW0F1svkusZT/NRvDyAVrcre3sITiT2d0zRm94FNhZTwKNhFvtpUFEGUVExkIfdBpTmuaCslJal9CnJzI5exJf0guEiHqMDDNopU3nPTrci8tz3sa8bHQHXKdbqHc2Pecr7c9X/Ji4BLVTuzAYTFjA7hecdA2ss8+LCVmjkHS3AqDXy868ex4BLxjeenZt7z7NBS7+jciE0S477XRXbuUFXmIRUzAIZlDPm1iRkOC5wGlkFdTxtkSI5yrnErtaefTWJu/Wqb4DeW8RwXxklBcruVIvaOfUMkyuzAjb7uD6cfNzLeGUnUsczMW9/2VrwONyU2ZX1FA+9ADw6L8TFdNfJ0lKGJLyYdxu/o5IR5k590kx0kZJGpW13tVDhuqjVMyN/ujqrIftXXmQw9o3e19Wc7z/fgbdBwt2Z8OxRaiKeyNv4l68jJi6KHTE49RePuApGx/V1RtjpKRiOh1UnQPZpwscM6nYGqU1VBWKkVqGIgXLC1dfLLbFrJ0pe19cbKeByO+tI71P2lWTnjRE6hqG+OVDbDZyVflWoZkK+cnbLbPzNq285N4FOv9zJKxfK8XWqHvLdXmsdCM5AKsp0QLHsoXZ27WR2Vd3Otz3HDmNOrY=">
</div>
        <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ctl00$ScriptManager', 'aspnetForm', ['tctl00$ctl00$DropDownSayfaAra$UpdatePanelGenelDropDown','','tctl00$ctl00$UpdatePanelMsgBox','','tctl00$ctl00$SayiKontrolPanel',''], [], [], 90, 'ctl00$ctl00');
//]]>
</script>

        <script language="javascript" type="text/javascript">

            document.onkeydown = DistributeKeydownEventsToRelatedMethods;
            function DistributeKeydownEventsToRelatedMethods(event) {
                //Olmayan bir method çağrıldığında sorun olmaması için, method try-catch içinde çağrılmalı
                try { CallUserControlsKeydownEventMethods(event); } catch (exception) { }
                try { SayfayaOzelKeydownEventDagitici(event); } catch (exception) { }
            }

        </script>
        <div id="ctl00_ctl00_divMainMaster">
            <div id="ctl00_ctl00_divMainMenu" class="YetkiMenuDiv2011">
                
<style type="text/css">
    #sddm
    {
        margin: 0;
        padding: 0;
        z-index: 30;
    }
    #sddm li
    {
        margin: 0;
        padding: 0;
        list-style: none;
        float: left;
        font: bold 11px arial;
    }
    #sddm li a, #sddm li a.TopMenuItem, #sddm li a.TopMenuItem:hover
    {
        display: block;
        margin: 3px 3px 3px 3px;
        color: #FFF;
        vertical-align: middle;
        text-decoration: none;
    }
    #sddm li a.TopMenuItem
    {
        margin: 8px 0 0 15px;
        background: #363636;
    }
    #sddm li a.TopMenuItem:hover
    {
        margin: 8px 0 0 15px;
        background: #363636;
        font: bold 11px arial;
    }
    #sddm li a:hover
    {
        color: #00fffc;
    }
    #sddm div
    {
        position: absolute;
        visibility: hidden;
        width: 300px;
        margin: 0 0 0 5px;
        padding: 0;
        background: #ffffff;
        border: 0px solid #000;
    }
</style>

<script type="text/javascript" language="javascript">
    var timeout = 500;
    var closetimer = 0;
    var ddmenuitem = 0;

    function mopen(id) {
        mcancelclosetime();

        if (ddmenuitem) ddmenuitem.style.visibility = 'hidden';

        ddmenuitem = document.getElementById(id);
        ddmenuitem.style.visibility = 'visible';

    }

    function mclose() {
        if (ddmenuitem) ddmenuitem.style.visibility = 'hidden';
    }

    function mclosetime() {
        closetimer = window.setTimeout(mclose, timeout);
    }

    function mcancelclosetime() {
        if (closetimer) {
            window.clearTimeout(closetimer);
            closetimer = null;
        }
    }

    document.onclick = mclose; 

</script>

<ul id="sddm">
    <li><a class="TopMenuItem" href="#" onmouseover="mopen('m1')" onmouseout="mclosetime()">
        Modüller</a>
        <div id="m1" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
            <span id="ctl00_ctl00_MenuMainMaster1_LabelMenuItems" style="font-size: 13;"><table id="tableHtmlData" width="100%" style="height:20px;"><tbody><tr><td style="background-color:#363636"><a title="" href="/Anasayfa/IBYetkiAnaSayfa.aspx">e-İçişleri Anasayfa</a></td></tr><tr><td style="background-color:#000"><a title="" href="/IdariMaliIsler/HukumetKonagi/HukumetKonagiAnaSayfa.aspx">Hükümet Konağı Anasayfa</a></td></tr></tbody></table></span>
        </div>
    </li>
</ul>
<div style="clear: both">
</div>

            </div>
            <div id="ctl00_ctl00_divMasterHeader" class="MasterHeader" style="z-index: 99; left: 0px; top: 0px; position: fixed;">
                <div class="MasterUstMenu">
                    <table cellpadding="0" cellspacing="0" width="100%">
                        <tbody><tr>
                            <td width="175" valign="top" style="padding-top: 1px;">
                                <input type="image" name="ctl00$ctl00$ImageButton1" id="ctl00_ctl00_ImageButton1" src="../../App_Themes/Main/Images/Master/2011/logo.jpg" alt="E-İçişleri" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$ImageButton1&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" style="border-width:0px;">
                            </td>
                            <td align="center">
                                <table cellpadding="3" cellspacing="0">
                                    <tbody><tr>
                                        <td>
                                            <input type="image" name="ctl00$ctl00$ImageAnaSayfa" id="ctl00_ctl00_ImageAnaSayfa" src="../../App_Themes/Main/Images/Master/2011/btnanasayfa.jpg" style="border-width:0px;">
                                        </td>
                                        <td>
                                            <input type="image" name="ctl00$ctl00$ImageAjanda" id="ctl00_ctl00_ImageAjanda" src="../../App_Themes/Main/Images/Master/2011/btnajanda.jpg" style="border-width:0px;">
                                        </td>
                                        <!--<td>
                                        <input type="image" name="ctl00$ctl00$ImageGorevler" id="ctl00_ctl00_ImageGorevler" src="../../App_Themes/Main/Images/Master/2011/btngorvler.jpg" style="border-width:0px;" />
                                    </td>-->
                                        <td>
                                            <a id="ctl00_ctl00_HyperLinkEmail" href="javascript:CreateWnd('https://www.e-icisleri.gov.tr/Posta/postaSayfasi.aspx', 1024, 768, true);" style="cursor: pointer;"><img src="../../App_Themes/Main/Images/Master/2011/btneposta.jpg" alt="" style="border-width:0px;"></a>
                                        </td>
                                        <td>
                                            <input type="image" name="ctl00$ctl00$ImageEvrak" id="ctl00_ctl00_ImageEvrak" src="../../App_Themes/Main/Images/Master/2011/btnevrak.jpg" style="border-width:0px;">
                                        </td>
                                        <td>
                                            
                                        </td>
                                        <td>
                                            <div id="overlay">
                                                <div id="aa">

                                                    <div id="ctl00_ctl00_guvenlikBaslikdiv" class="guvenlikBaslikdiv">

                                                    </div>
                                                    <br>

                                                    <div id="ctl00_ctl00_guvenlikAciklamadiv" class="guvenlikAciklamadiv">

                                                    </div>
                                                    <br>
                                                    <hr style="border: 1px solid #cecdcd;">
                                                    <br>
                                                    <div id="guvenlikChkboxdiv">
                                                        
                                                        
                                                    </div>
                                                    <div id="onaybuttondiv">
                                                        <input type="submit" name="ctl00$ctl00$btnkapatveKaydet" value="Okudum Ve Onaylıyorum" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$btnkapatveKaydet&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" id="ctl00_ctl00_btnkapatveKaydet" class="btnOnay BtnSuccess">
                                                    </div>

                                                </div>
                                            </div>

                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                            <td width="25" align="left">
                                


<script type="text/javascript" src="/Javascript/highslide/highslide-full.js"></script>

<link rel="stylesheet" type="text/css" href="/App_Themes/Main/highslide/highslide.css">

<script type="text/javascript">
    hs.graphicsDir = '/App_Themes/Main/highslide/graphics/';
    hs.outlineType = 'rounded-white';
    hs.wrapperClassName = 'draggable-header';

    function BilgiYardimMetniniWebMethodIleAl(sender, primaryKey) {
        var dizin = ObjeDizini(sender.id);
        var lblMetin = getObj(dizin + 'LabelMetin');
        if (lblMetin.innerText == '') {
            ShowProgress();
            PageMethods.BilgiYardimMetniniWebMethodIleAl(primaryKey, sender.id, OnBilgiYardimMetniAlindi, OnBilgiYardimMetniAlinirkenHataOlustu, sender.id);
        }
        else
            return hs.htmlExpand(sender);
    }
    
    function BilgiYardimMetniniWebServiceIleAl(sender, primaryKey, modulAdi) {
        var dizin = ObjeDizini(sender.id);
        var lblMetin = getObj(dizin + 'LabelMetin');
        if (lblMetin.innerText == '') {
            ShowProgress();
            BilgiYardimMetni.BilgiYardimMetniniWebServiceIleAl(primaryKey, sender.id, modulAdi, OnBilgiYardimMetniAlindi, OnBilgiYardimMetniAlinirkenHataOlustu, sender.id);
        }
        else
            return hs.htmlExpand(sender);
    }
    function OnBilgiYardimMetniAlindi(result, userContext, methodName) {
        var dizin = ObjeDizini(userContext);
        var lblMetin = getObj(dizin + 'LabelMetin');
        lblMetin.innerHTML = result;
        var imgButton = getObj(userContext);
        HideProgress();
        return hs.htmlExpand(imgButton);
    }
    function OnBilgiYardimMetniAlinirkenHataOlustu(error, userContext, methodName) {
        HideProgress();
        var errMsg = "Bilgi yardım metni alınırken hata oluştu !";
        var hdnObj = getObj(ObjeDizini(userContext) + 'HiddenFieldHataMesaji');
        if (hdnObj.value != '') errMsg = hdnObj.value;
        alert(errMsg);
    }

    function ShowProgress() {
        $("#spanBilgiYardimYukleniyorGif").css("display", "block");
    }

    function HideProgress() {
        $("#spanBilgiYardimYukleniyorGif").css("display", "none");
    }
    
</script>

<input type="hidden" name="ctl00$ctl00$BilgiYardimKullaniciBilgileri$HiddenFieldHataMesaji" id="ctl00_ctl00_BilgiYardimKullaniciBilgileri_HiddenFieldHataMesaji" value="Kullanıcı bilgileri alınırken hata oluştu !">
<span id="spanBilgiYardimYukleniyorGif" style="display: none; text-align: center;
    position: absolute; margin-top: 2px;">
    <img src="../../App_Themes/Main/Images/Ortak/yukleniyor.gif" alt="Yukleniyor">
</span>
<img id="ctl00_ctl00_BilgiYardimKullaniciBilgileri_ImageBilgiYardim" title="Kullanıcı Bilgilerinizi Görmek İçin Tıklayınız" onclick="BilgiYardimMetniniWebServiceIleAl(this,'0','MasterPage'); return false;" src="../../App_Themes/Main/Images/Genel/kullanici.ico" align="absmiddle" style="border-width:0px;cursor: pointer;">
<div class="highslide-maincontent" style="display: none;">
    <table id="ctl00_ctl00_BilgiYardimKullaniciBilgileri_tableBilgiYardim">
	<tbody><tr>
		<td>
                <img id="ctl00_ctl00_BilgiYardimKullaniciBilgileri_ImageBaslik" src="../../App_Themes/Main/Images/MessageBox/basari.gif" style="border-width:0px;">
                <span id="ctl00_ctl00_BilgiYardimKullaniciBilgileri_LabelBaslik" style="font-size:Medium;font-weight:bold;">Kullanıcı Bilgileriniz...</span>
                <br>
                <br>
                <span id="ctl00_ctl00_BilgiYardimKullaniciBilgileri_LabelMetin"></span>
                <br>
                <br>
            </td>
	</tr>
</tbody></table>

</div>

                            </td>
                            <td width="150" valign="top" style="padding: 0px 0px 0px;" align="center">
                                <span id="ctl00_ctl00_LabelKullaniciAdi" style="color:White;font-size:10px;font-weight:bold;">Uğur OKUR</span><br>
                                <span id="ctl00_ctl00_LabelAktifBirim" title="Aktif Birim: İstanbul Bilgi İşlem Şube Müdürlüğü" style="color:White;font-size:9px;font-weight:normal;">İstanbul Bilgi İşlem Şube Mü..</span><br>
                                <span id="ctl00_ctl00_LabelKalanSureMetin" title="Oturumunuzun Kapanması İçin Kalan Süre" style="color: #fff; font-size: smaller;">Kalan Oturum Süreniz (dk.): </span>
                                <a type="text/plain" id="LabelOturumIcinKalanSure" style="color: #fff; font-size: small;" title="Oturumunuzun Kapanması İçin Kalan Süre">
                                    30</a> <a type="text/plain" id="LabelMaksimumOturumSuresi" style="display: none;">
                                        30</a>
                            </td>
                        </tr>
                    </tbody></table>
                    <table cellpadding="0" cellspacing="0" width="100%">
                        <tbody><tr>
                            <td width="490" valign="top">
                                <div class="MasterHeaderSolArac">
                                    <a id="ctl00_ctl00_HyperLinkSikKullanilanlar" title="Sık Kullanılanlar" style="cursor: pointer;">Sık Kullanılanlar</a>
                                    
                                    <img id="ctl00_ctl00_ImageResizePage" title="Sayfa genişliğini ayarlamak için tıklayın" onclick="ResizeScreenWidth(this);" src="../../App_Themes/Main/Images/Genel/resizepage.ico" style="border-width:0px;position: absolute; margin-left: 1px; margin-top: 2px; cursor: pointer; top: 40px; left: 350px;">
                                </div>
                            </td>
                            <td align="center">
                                <table style="margin-top: -10px;">
                                    <tbody><tr>
                                        <td style="text-align: left;">
                                            <div id="ctl00_ctl00_searhcPanel" onkeypress="javascript:return WebForm_FireDefaultButton(event, 'ctl00_ctl00_defaultSearchButton')">
	
                                                
<link href="/App_Themes/Main/Main.css" rel="stylesheet" type="text/css">
<script type="text/javascript">

    var DizinGenelDropDown = '';
    function SetDizinGenelDropDown(sender) {
        var ucAdi = sender.id;
        var parca = ucAdi.split('_');
        var kntrl = parca[parca.length - 1];
        //DizinGenelDropDown = ucAdi.replace(kntrl, "");
        DizinGenelDropDown = ReplaceEnd(ucAdi, kntrl, '');
        GenelDropDownTimerIptal();
        DegiskenleriBosaltGDD();
    }

    function TextBoxFocusGenelDropDown(sender) {
        SetDizinGenelDropDown(sender);
        SetCursorPosition(sender, sender.value.length);

        var txt = getObj(KontrolAdiniDuzenleGenelDropDown('TextBoxGenelDropDown')).value;
        if (txt.substring(0, 1) == '-') CleanTxtBoxOnGotFocus(sender);
        if (getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldTextBoxModundaCalis')).value == '1') return;

        var objTr = document.getElementById(DizinGenelDropDown + 'tdGenelDropDown');
        var yazarakAra = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldYazarakArama')).value
        var kayitSayisi = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldKayitSayisi')).value;
        var btnTemizle = getObj(KontrolAdiniDuzenleGenelDropDown('ImageButtonTemizle'));

        if (objTr.style.display == 'none' && yazarakAra == '1') {
            if (kayitSayisi == '0' || kayitSayisi == '') ZamanlayiciIleAraGDD();
            else {
                objTr.style.display = 'block';
                btnTemizle.focus();
            }
        }
        else {
            objTr.style.display = 'none';
            if (yazarakAra == '1') {
                sender.value = SetTextBoxGenelDropDown();
                btnTemizle.focus();
            }
        }
    }

    function KontrolAdiniDuzenleGenelDropDown(kontrol) {
        kontrol = DizinGenelDropDown + kontrol;
        kontrol = kontrol.replace(/_/g, '$');
        return kontrol;
    }

    function SetTextBoxGenelDropDown() {
        FillValidationTextBox();
        return getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldText')).value
    }

    function ItemSelected(indx) {
        var kontrol = 'ButtonItemSelected';
        getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldKayitSayisi')).value = '0';
        kontrol = KontrolAdiniDuzenleGenelDropDown(kontrol);
        __doPostBack('' + kontrol + '', indx);
    }

    function ItemsSelectedByCheckBoxes() {
        var kontrol = 'ButtonCheckedItemsSelected';
        getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldKayitSayisi')).value = '0';
        var kontrol = KontrolAdiniDuzenleGenelDropDown(kontrol);
        __doPostBack('' + kontrol + '', '');
    }

    function AramaYapGenelDropDown(event) {
        var charCode = GetKeyCode(event);
        var doNotSubmit = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldDoNotSubmit')).value;

        var objUrlCalled = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldUrlCalled'));
        objUrlCalled.value = 'false';

        if (charCode == mBackSpace) { SetTimerGenelDropDown(event); return; }

        if (charCode == mRightArrow) {
            CloseGenelDropDownList();
            return;
        }

        if (charCode == mDownArrow) {
            GenelDropDownTimerIptal();
            if (getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldTextBoxModundaCalis')).value == '1') {
                window.focus();
                return;
            }
            var kontrol = 'ImageButtonGenelDropDown';
            kontrol = KontrolAdiniDuzenleGenelDropDown(kontrol);
            getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldKayitSayisi')).value = '0';
            __doPostBack('' + kontrol + '', '');
        }
        else if (charCode == mEnter) {
            var url = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldUrl')).value;
            if (url != null && url != '') {
                var arananText = getObj(KontrolAdiniDuzenleGenelDropDown('TextBoxGenelDropDown')).value;
                var iW = 380;
                var iH = 500;
                var iL = (screen.width - iW) / 2;
                var iT = (screen.height - iH) / 2;
                var sURL = url + "?SayfaAd=" + arananText;
                var sAd = "SayfaAra";
                var oPopUpWin = window.open(sURL, sAd, 'scrollbars=1,toolbar=0,status=1,menubar=0,location=0,resizable=1,left=' + iL + ',top=' + iT + ',width=' + iW + ',height=' + iH);
                oPopUpWin.focus();
                objUrlCalled.value = 'true';
            }
        }
        if (doNotSubmit) {
            return false;
        }
    }

    var zamanlayiciGDD;
    function SetTimerGenelDropDown(event) {
        GenelDropDownTimerIptal();

        var charCode = GetKeyCode(event);
        if (isOtherValidKey(charCode)) return;

        var tmrInterval = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldTimerInterval')).value
        if (tmrInterval == null || tmrInterval == '') tmrInterval = '2000';   //Default değer 2 sn.
        if (tmrInterval == '0') return; //interval değeri 0 girilmiş ise zamanlayici ile arama iptal edilmiş demektir.
        zamanlayiciGDD = setTimeout(ZamanlayiciIleAraGDD, parseInt(tmrInterval, 10));
    }

    function FillValidationTextBox() {
        if (getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldTextBoxModundaCalis')).value == '1') {
            var txtValidation = getObj(KontrolAdiniDuzenleGenelDropDown('TextBoxValidationGDD'));
            var txtDropDown = getObj(KontrolAdiniDuzenleGenelDropDown('TextBoxGenelDropDown'));
            txtValidation.value = txtDropDown.value;
        }
    }

    function ZamanlayiciIleAraGDD() {
        GenelDropDownTimerIptal();
        var kontrol = 'ImageButtonGenelDropDown';
        kontrol = KontrolAdiniDuzenleGenelDropDown(kontrol);
        __doPostBack('' + kontrol + '', '');
    }

    function GenelDropDownTimerIptal() {
        DegiskenleriBosaltGDD();
        clearTimeout(zamanlayiciGDD);
    }

    function ChkBoxIsaretle(tblRw) {
        if (getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldShowCheckBox')).value == "1") {
            var cell = tblRw.cells[0];
            var chk = cell.childNodes[0].childNodes[0].checked;
            if (chk == false) chk = true; else chk = false;
            cell.childNodes[0].childNodes[0].checked = chk;
        }
    }

    var rwMarkedGDD = false;
    var currentRowIdGDD = 0;

    function KayitSecDropDown(charCode) {
        if (DizinGenelDropDown == '') return;
        var sKSayisi = getObj(KontrolAdiniDuzenleGenelDropDown('HiddenFieldKayitSayisi')).value;
        if (sKSayisi == '') return;
        var iKSayisi = parseInt(sKSayisi, 10);
        var rwID = 0;

        if (iKSayisi > 0) {
            if (charCode == mDownArrow || charCode == mUpArrow) {
                if (charCode == mDownArrow) {
                    rwID = currentRowIdGDD + 1;
                    if (rwID > iKSayisi) { rwID = iKSayisi; currentRowIdGDD -= 1; }
                }
                else if (charCode == mUpArrow) {
                    rwID = currentRowIdGDD - 1;
                    if (rwID < 1) { rwID = 1; currentRowIdGDD += 1; }
                }

                var tableRow1 = document.getElementById(currentRowIdGDD);
                var tableRow2 = document.getElementById(rwID);

                if (tableRow1 != null) Highlight(tableRow1, false, currentRowIdGDD);
                if (tableRow2 != null) Highlight(tableRow2, true, rwID);
                if (tableRow1 != null || tableRow2 != null) {
                    if (charCode == mDownArrow) currentRowIdGDD += 1;
                    else if (charCode == mUpArrow) currentRowIdGDD -= 1;

                    rwMarkedGDD = true;
                    $('#' + DizinGenelDropDown + 'PanelGenelDropDown').animate({ scrollTop: (currentRowIdGDD - 1) * (20) }, 'fast');
                }
            }
            if (charCode == mEnter) if (rwMarkedGDD) ItemSelected(currentRowIdGDD);
            if (charCode == mSpace) ChkBoxIsaretle(document.getElementById(currentRowIdGDD));
        }
    }

    function TemizleGDD() {
        if (DizinGenelDropDown != '') {
            DegiskenleriBosaltGDD();
            var temizle = KontrolAdiniDuzenleGenelDropDown('ImageButtonTemizle');
            __doPostBack('' + temizle + '', '');
        }
    }
    function DegiskenleriBosaltGDD() {
        currentRowIdGDD = 0;
        rwMarkedGDD = false;
    }

    function CloseGenelDropDownList() {
        var objPanel = getObj(DizinGenelDropDown + 'tdGenelDropDown')
        objPanel.style.display = 'none';
        return false;
    }

</script>
<div id="ctl00_ctl00_DropDownSayfaAra_UpdatePanelGenelDropDown">
		
		<table id="ctl00_ctl00_DropDownSayfaAra_tableGenelDropDown">
			<tbody><tr>
				<td>
					<div id="ctl00_ctl00_DropDownSayfaAra_UpdateProgressGenelDropDown" style="display:none;" role="status" aria-hidden="true">
					
							<img id="ctl00_ctl00_DropDownSayfaAra_ImageProgress" src="../../Resim/Ortak/progress.gif" style="border-width:0px;position: absolute; margin-top: 3px; margin-left: 2px">
						
				</div>
					<input name="ctl00$ctl00$DropDownSayfaAra$TextBoxValidationGDD" type="text" id="ctl00_ctl00_DropDownSayfaAra_TextBoxValidationGDD" style="height:10px;width:100px;display: none;">
					
					<input name="ctl00$ctl00$DropDownSayfaAra$TextBoxGenelDropDown" type="text" autocomplete="off" value="-Sayfa Ara..." id="ctl00_ctl00_DropDownSayfaAra_TextBoxGenelDropDown" onmouseout="RenkDegistir(this, '#FFFFFF');" onmouseover="RenkDegistir(this, '#F7F6F3');" onfocus="TextBoxFocusGenelDropDown(this);" onblur="FillTxtBoxOnLostFocus(this,SetTextBoxGenelDropDown());" onkeypress="SetTimerGenelDropDown(event);" onkeydown="AramaYapGenelDropDown(event);" style="border-color:LightSteelBlue;border-width:1px;border-style:None;font-family:Verdana;font-size:Smaller;width:150px;margin-left:10px;margin-top:5px;">
				</td>
				<td style="width: 20px;">
                    <input type="image" name="ctl00$ctl00$DropDownSayfaAra$ImageButtonGenelDropDown" id="ctl00_ctl00_DropDownSayfaAra_ImageButtonGenelDropDown" title="Listele" src="../../App_Themes/Main/Images/Ikonlar/asagi.gif" align="absmiddle" onclick="SetDizinGenelDropDown(this);" style="border-width:0px;display:none;">
				</td>
				<td style="width: 20px;">
                    <input type="image" name="ctl00$ctl00$DropDownSayfaAra$ImageButtonTemizle" id="ctl00_ctl00_DropDownSayfaAra_ImageButtonTemizle" title="Temizle" src="../../App_Themes/Main/Images/Ikonlar/temizle.gif" align="absmiddle" onclick="DegiskenleriBosaltGDD();" style="border-width:0px;display:none;">
				</td>
				<td>
					<input type="image" name="ctl00$ctl00$DropDownSayfaAra$ImageButtonListeyiKapat" id="ctl00_ctl00_DropDownSayfaAra_ImageButtonListeyiKapat" title="Listeyi Kapat" src="../../App_Themes/Main/Images/Ikonlar/yukari.gif" align="absmiddle" onclick="return CloseGenelDropDownList();" style="border-width:0px;display: none;">
				</td>
			</tr>
			<tr>
				<td colspan="4" style="height: 3px;">
				</td>
			</tr>
			<tr>
				<td id="ctl00_ctl00_DropDownSayfaAra_tdGenelDropDown" colspan="4" style="position: absolute; z-index: 99;
					margin-top: -3px; display: none; padding-top: 30px; padding-left: 3px;">
					<div id="ctl00_ctl00_DropDownSayfaAra_PanelGenelDropDown" style="background-color:White;border-color:LightSteelBlue;border-width:1px;border-style:Solid;height:300px;overflow:auto;">
					
						<table id="ctl00_ctl00_DropDownSayfaAra_tableLnkBtnSec" style="width:100%;background-color:#d5e9fb;display:none;">
						<tbody><tr>
							<td style="text-align: left; width: 10px;">
									<span title="Tümünü işaretle/kaldır" style="cursor: pointer;"><input id="ctl00_ctl00_DropDownSayfaAra_CheckBoxSelectAll" type="checkbox" name="ctl00$ctl00$DropDownSayfaAra$CheckBoxSelectAll"></span>
								</td>
							<td style="text-align: left; width: 20px;">
									<a id="Sec" title="İşaretli kayıtları seç" class="LinkButtonCss4" onclick="ItemsSelectedByCheckBoxes();" style="cursor: pointer">Seç</a>
									
								</td>
							<td style="text-align: left">
									&nbsp;&nbsp;&nbsp;
									<a id="ctl00_ctl00_DropDownSayfaAra_LinkButtonKapat" title="Listeyi Kapat" class="LinkButtonCss4" href="javascript:__doPostBack('ctl00$ctl00$DropDownSayfaAra$LinkButtonKapat','')" style="color:Brown;">Kapat</a>
								</td>
						</tr>
					</tbody></table>
					
						<div>

					</div>
					
				</div>
				</td>
			</tr>
			<tr>
				<td colspan="4">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldText" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldText" value="-Sayfa Ara...">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldKayitSayisi" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldKayitSayisi">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldYazarakArama" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldYazarakArama">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldUrl" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldUrl">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldUrlCalled" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldUrlCalled">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldTextBoxModundaCalis" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldTextBoxModundaCalis" value="1">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldTimerInterval" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldTimerInterval" value="3000">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldShowCheckBox" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldShowCheckBox">
					<input type="hidden" name="ctl00$ctl00$DropDownSayfaAra$HiddenFieldDoNotSubmit" id="ctl00_ctl00_DropDownSayfaAra_HiddenFieldDoNotSubmit" value="1">
					<input type="button" name="ctl00$ctl00$DropDownSayfaAra$ButtonItemSelected" value="" onclick="javascript:__doPostBack('ctl00$ctl00$DropDownSayfaAra$ButtonItemSelected','')" id="ctl00_ctl00_DropDownSayfaAra_ButtonItemSelected" style="display: none;">
					<input type="button" name="ctl00$ctl00$DropDownSayfaAra$ButtonCheckedItemsSelected" value="" onclick="javascript:__doPostBack('ctl00$ctl00$DropDownSayfaAra$ButtonCheckedItemsSelected','')" id="ctl00_ctl00_DropDownSayfaAra_ButtonCheckedItemsSelected" style="display: none;">
				</td>
			</tr>
		</tbody></table>
		
	
	</div>

                                                <input type="submit" name="ctl00$ctl00$defaultSearchButton" value="" onclick="return false;WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$defaultSearchButton&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" id="ctl00_ctl00_defaultSearchButton" style="display: none">
                                            
</div>
                                        </td>
                                        <td>
                                            <input type="image" name="ctl00$ctl00$ButtonSayfaAraTemizle" id="ctl00_ctl00_ButtonSayfaAraTemizle" title="Temizle ve Kapat (Kısayolu: 'Delete' tuşu)" src="../../App_Themes/Main/Images/Ikonlar/temizle2.gif" align="absmiddle" onclick="TemizleGDD(); return false;WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$ButtonSayfaAraTemizle&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" style="border-width:0px;">
                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                            <td width="346" align="right" valign="top">
                                <div class="MasterHeaderSagArac">

                                    <a id="ctl00_ctl00_ButtonCikis" title="Çıkış" class="GuvenliCikis" href="javascript:__doPostBack('ctl00$ctl00$ButtonCikis','')">Güvenli Çıkış</a>
                                    <span id="ctl00_ctl00_LabelTarih" title="21 Ekim 2020 Çarşamba - IP=212.175.170.12 - IBS04EBKNW02 - IBS04EBKNW07 - IBS04EBKNW03" style="position: relative; left: -15px">21 Ekim 2020 Çarşamba</span>
                                    <a id="ctl00_ctl00_HyperLinkYardim" title="Yardım Belgeleri" href="javascript:CreateWnd('/Yardim/YeniYardim/YeniPopUpYardim.aspx', 985, 600, true);" style="position: relative; left: -30px; margin-top: 5px">Yardım Belgeleri</a>
                                    <span id="ctl00_ctl00_labelKullaniciSonGiris" title="Son Giriş Tarihiniz" class="labelKullaniciSonGiris">21.10.2020 10:06:46</span>
                                    
                                    
                                </div>
                            </td>
                        </tr>
                    </tbody></table>
                </div>
            </div>
            
            <div style="padding-top: 60px;">
            </div>
            <div class="MasterContainer">
                <div class="MasterContent">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        
                        <tbody><tr>
                            <td colspan="3" align="center">
                                <div id="ctl00_ctl00_UpdatePanelMsgBox">
	
                                        <div id="ctl00_ctl00_UpdateProgressMain" style="display:none;" role="status" aria-hidden="true">
		
                                                <div id="ctl00_ctl00_PanelProgressMain" style="position: fixed; z-index: 99; left: 391px; top: 291px;">
			
                                                    <img id="ctl00_ctl00_ImageProgress" src="../../Resim/Ortak/loading.gif" style="border-width:0px;margin-left: 2px; margin-top: 7px">
                                                
		</div>
                                                
                                            
	</div>
                                        
<link href="/App_Themes/Main/Main.css" rel="stylesheet" type="text/css">

<script language="javascript" type="text/javascript" src="/Javascript/UserControlTextBox.js"></script>

<script language="javascript" type="text/javascript">

    function MsgBoxKapat(sender) {
        var objTable = getObj("ctl00_ctl00_MessageBox1_tableMsgBox");
        var objDiv = getObj("ctl00_ctl00_MessageBox1_divMsgBox");
        objTable.style.display = 'none';
        objDiv.style.display = 'none';

        if (typeof window.onMessageBoxClose === "function") { 
            window.onMessageBoxClose();
        }
        
        return false;
    }

    $(document).ready(function() { ResizeDivMsgBox(); })
    window.onresize = function() { ResizeDivMsgBox(); }
    function ResizeDivMsgBox() {
        var objDiv = getObj("ctl00_ctl00_MessageBox1_divMsgBox");
        if (objDiv.style.display == 'block') {
            objDiv.style.width = GetPageWidth();
            objDiv.style.height = GetPageHeight();
        }
    }
    
</script>

<div id="ctl00_ctl00_MessageBox1_divMsgBox" style="left:0;opacity:0.2;z-index:110;position:absolute;background-color:#000;display:none;top:0;filter:alpha(opacity=20);">
</div>



                                    
</div>
                            </td>
                        </tr>
                        <tr>
                            <td>&nbsp;
                            </td>
                            <td style="width: 100%; text-align: left;">
                                <table id="ctl00_ctl00_tableMainHeader" style="width: 100%;">
	<tbody><tr>
		<td style="width: 10px; position: absolute; padding-left: 15px; padding-top: 6px;">
                                            


<script type="text/javascript" src="/Javascript/highslide/highslide-full.js"></script>

<link rel="stylesheet" type="text/css" href="/App_Themes/Main/highslide/highslide.css">

<script type="text/javascript">
    hs.graphicsDir = '/App_Themes/Main/highslide/graphics/';
    hs.outlineType = 'rounded-white';
    hs.wrapperClassName = 'draggable-header';

    function BilgiYardimMetniniWebMethodIleAl(sender, primaryKey) {
        var dizin = ObjeDizini(sender.id);
        var lblMetin = getObj(dizin + 'LabelMetin');
        if (lblMetin.innerText == '') {
            ShowProgress();
            PageMethods.BilgiYardimMetniniWebMethodIleAl(primaryKey, sender.id, OnBilgiYardimMetniAlindi, OnBilgiYardimMetniAlinirkenHataOlustu, sender.id);
        }
        else
            return hs.htmlExpand(sender);
    }
    
    function BilgiYardimMetniniWebServiceIleAl(sender, primaryKey, modulAdi) {
        var dizin = ObjeDizini(sender.id);
        var lblMetin = getObj(dizin + 'LabelMetin');
        if (lblMetin.innerText == '') {
            ShowProgress();
            BilgiYardimMetni.BilgiYardimMetniniWebServiceIleAl(primaryKey, sender.id, modulAdi, OnBilgiYardimMetniAlindi, OnBilgiYardimMetniAlinirkenHataOlustu, sender.id);
        }
        else
            return hs.htmlExpand(sender);
    }
    function OnBilgiYardimMetniAlindi(result, userContext, methodName) {
        var dizin = ObjeDizini(userContext);
        var lblMetin = getObj(dizin + 'LabelMetin');
        lblMetin.innerHTML = result;
        var imgButton = getObj(userContext);
        HideProgress();
        return hs.htmlExpand(imgButton);
    }
    function OnBilgiYardimMetniAlinirkenHataOlustu(error, userContext, methodName) {
        HideProgress();
        var errMsg = "Bilgi yardım metni alınırken hata oluştu !";
        var hdnObj = getObj(ObjeDizini(userContext) + 'HiddenFieldHataMesaji');
        if (hdnObj.value != '') errMsg = hdnObj.value;
        alert(errMsg);
    }

    function ShowProgress() {
        $("#spanBilgiYardimYukleniyorGif").css("display", "block");
    }

    function HideProgress() {
        $("#spanBilgiYardimYukleniyorGif").css("display", "none");
    }
    
</script>

<input type="hidden" name="ctl00$ctl00$BilgiYardimAciklama$HiddenFieldHataMesaji" id="ctl00_ctl00_BilgiYardimAciklama_HiddenFieldHataMesaji">
<span id="spanBilgiYardimYukleniyorGif" style="display: none; text-align: center;
    position: absolute; margin-top: 2px;">
    <img src="../../App_Themes/Main/Images/Ortak/yukleniyor.gif" alt="Yukleniyor">
</span>

<div class="highslide-maincontent" style="display: none;">
    
</div>

                                        </td>
		<td style="width: 10px; position: absolute; padding-left: 40px; padding-top: 6px;">
                                            
                                        </td>
		<th colspan="3">
                                            <div class="MasterBaslikTile">
                                                <div class="MasterBaslikSol">
                                                    <div class="MasterBaslikSag">
                                                        Evrak Ana Sayfa
                                                    </div>
                                                </div>
                                            </div>
                                            <br>
                                        </th>
	</tr>
</tbody></table>

                                <div>
                                    
    <table width="100%" class="AnaTablo">
        <tbody><tr>
            <td valign="top" align="left" width="15%">
                <table style="width: 100%" cellpadding="0" cellspacing="0">
                    <tbody><tr>
                        <td>
                            <a id="ctl00_ctl00_cph1_HyperLinkEvrakAnaSayfa" class="EvrakAnasayfa" href="EvrakAnaSayfa.aspx">EVRAK ANASAYFA</a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div id="ctl00_ctl00_cph1_RadPanelBarGelenGiden" class="RadPanelBar RadPanelBar_Web20" style="width:100%;">
	<!-- 2009.3.1314.35 --><ul class="rpRootGroup">
		<li class="rpItem rpFirst"><a href="#" title="İşlem Yapmanızı Bekleyen Evraklar Listesi" class="rpLink MainItem rpExpandable rpExpanded"><span class="rpOut"><span class="rpText">İşlem Yapacaklarım</span></span></a><div class="rpSlide" style="display:block;">
			<ul class="rpGroup rpLevel1 " style="display: block; width: 100%;">
				<li class="rpItem rpFirst"><a href="/Evrak/Gelen/IslemiSuren.aspx" title="Gelen Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Gelen Evrak (11)</span></span></a></li><li class="rpItem"><a href="/Evrak/Giden/YeniHazirlanan.aspx" title="Taslak Evraklarım" class="rpLink"><span class="rpOut"><span class="rpText">Taslak (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/Giden/IslemiSuren.aspx" title="Paraf Bekleyen Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Paraf Bekleyen (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/Giden/ImzaBekleyen.aspx" title="İmza Bekleyen Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">İmza Bekleyen (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/Giden/SayiAlmisImzaBekleyen.aspx" title="Sayı Almış e-İmza Bekleyen Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">e-İmza Bekleyen (0)</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/EvrakKlasor/EvrakKlasorum.aspx" title="Klasörümdeki evrak listesi" class="rpLink"><span class="rpOut"><span class="rpText">Evrak Klasörüm</span></span></a></li>
			</ul>
		</div></li><li class="rpItem"><a href="#" title="Kayıt İşlemleri" class="rpLink MainItem rpExpandable rpExpanded"><span class="rpOut"><span class="rpText">Kayıt İşlemleri</span></span></a><div class="rpSlide" style="display:block;">
			<ul class="rpGroup rpLevel1 " style="display: block; width: 100%;">
				<li class="rpItem rpFirst"><a href="/Evrak/XMLEditor/XMLEditor.aspx?Durum=I" title="Evrak Oluştur" class="rpLink"><span class="rpOut"><span class="rpText">Evrak Oluştur</span></span></a></li><li class="rpItem"><a href="/Evrak/XMLEditor/XMLEditor.aspx?Durum=Tebligat" title="Tebligat Oluştur" class="rpLink"><span class="rpOut"><span class="rpText">Tebligat Oluştur</span></span></a></li><li class="rpItem"><a href="/Evrak/Kayit/GelenEvrakHizliKayit.aspx?Durum=I" title="Gelen Evrak Hızlı Kayıt" class="rpLink"><span class="rpOut"><span class="rpText">Gelen Evrak Hızlı Kayıt</span></span></a></li><li class="rpItem"><a href="/Evrak/Kayit/GelenEvrakKayit.aspx?Durum=I" title="Gelen Evrak Detaylı Kayıt" class="rpLink"><span class="rpOut"><span class="rpText">Gelen Evrak Detaylı Kayıt</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/XMLEditor/XMLEditor.aspx?Durum=Onay" title="Onay Oluştur" class="rpLink"><span class="rpOut"><span class="rpText">Onay Oluştur</span></span></a></li>
			</ul>
		</div></li><li class="rpItem"><a href="#" title="Birim Adına İşlem Yapılacak Evraklar Listesi" class="rpLink MainItem rpExpandable"><span class="rpOut"><span class="rpText">Birim Evrak İşlemleri</span></span></a><div class="rpSlide">
			<ul class="rpGroup rpLevel1 ">
				<li class="rpItem rpFirst"><a href="/Evrak/Birim/BirimdeKayitBekleyen.aspx" title="Birimde Kayıt Bekleyen Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Birimde Kayıt Bekleyen (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/Birim/BirimdeKayitBekleyenDisKurumElektronikGelen.aspx" title="Birimde Dış Kurumdan Elektronik Olarak Gelmiş Kayıt Bekleyen Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Dış Kurumdan Elektronik Gelen (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/Birim/BirimdeKaydedilmis.aspx" title="Birimde Kaydedilmiş Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Birimde Kaydedilmiş (0)</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/Birim/BirimdenTeslimAldigim.aspx" title="Birimden Teslim Aldığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Birimden Teslim Aldığım (0)</span></span></a></li>
			</ul>
		</div></li><li class="rpItem"><a href="#" title="Postalama İşlemi Yapılacak Evraklar Listesi" class="rpLink MainItem rpExpandable"><span class="rpOut"><span class="rpText">Postalama İşlemleri</span></span></a><div class="rpSlide">
			<ul class="rpGroup rpLevel1 ">
				<li class="rpItem rpFirst"><a href="/Evrak/Posta/PostalanmayiBekleyen.aspx" title="Postalanacak Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Postalanacak (1)</span></span></a></li><li class="rpItem"><a href="/Evrak/Posta/Postaladiklarim.aspx" title="Son On Beş Gün İçerisinde Postaladığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Postaladıklarım (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/Posta/TeslimAldiklarim.aspx" title="Teslim Alınan Postalanacak Evraklar" class="rpLink"><span class="rpOut"><span class="rpText">Teslim Alınanlar (0)</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/Posta/PostaIadeBekleyenEvraklar.aspx" title="İade Edilen Postalanmış Evrak Listesi" class="rpLink"><span class="rpOut"><span class="rpText">İade Edilmiş Postalar  (0)</span></span></a></li>
			</ul>
		</div></li><li class="rpItem"><a href="#" title="Süreli/Süresiz Kapatma İşlemlerindeki Evrak Listesi" class="rpLink MainItem rpExpandable"><span class="rpOut"><span class="rpText">Kapatma İşlemleri</span></span></a><div class="rpSlide">
			<ul class="rpGroup rpLevel1 ">
				<li class="rpItem rpFirst"><a href="/Evrak/EvrakKapatma/KapatmaOnayiOnayaSunduklarimListesi.aspx" title="Kapatma Onayında Süreci Devam Eden Evrak Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Onaya Sunduklarım (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/EvrakKapatma/KapatmaOnayiParaflanacakListesi.aspx" title="Kapatma Onayında Paraflanması Bekleyen Evrak Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Paraflayacaklarım (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/EvrakKapatma/KapatmaOnayiImzalanacakListesi.aspx" title="Kapatma Onayı Bekleyen Evrak Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Kapatma Onaylayacaklarım (0)</span></span></a></li><li class="rpItem"><a href="/Evrak/EvrakKapatma/EvrakDolabinaKaldirdigim.aspx" title="Son On Beş Gün İçerisinde Evrak Dolabına Kaldırdığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Evrak Dolabına Kaldırdıklarım</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/EvrakKapatma/TakipliEvrakListesi.aspx" title="Süreli Kapatılan Evrak Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Süreli Kapatılanlar (0)</span></span></a></li>
			</ul>
		</div></li><li class="rpItem"><a href="#" title="Daha Önce İşlem Yapmış Olduğunuz Evraklar Listesi" class="rpLink MainItem rpExpandable"><span class="rpOut"><span class="rpText">İşlem Yaptıklarım</span></span></a><div class="rpSlide">
			<ul class="rpGroup rpLevel1 ">
				<li class="rpItem rpFirst"><a href="/Evrak/Gelen/TakipEttiklerim.aspx" title="Takip Ettiğim Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Takip Ettiklerim</span></span></a></li><li class="rpItem"><a href="/Evrak/IslemYaptiklarim/Hazirladiklarim.aspx" title="Son On Beş Gün İçerisinde Hazırladığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Hazırladıklarım</span></span></a></li><li class="rpItem"><a href="/Evrak/IslemYaptiklarim/Parafladiklarim.aspx" title="Son On Beş Gün İçerisinde Parafladığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Parafladıklarım</span></span></a></li><li class="rpItem"><a href="/Evrak/IslemYaptiklarim/Imzaladiklarim.aspx" title="Son On Beş Gün İçerisinde İmzaladığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">İmzaladıklarım</span></span></a></li><li class="rpItem"><a href="/Evrak/IslemYaptiklarim/HavaleEttiklerim.aspx" title="Son On Beş Gün İçerisinde Havale Ettiğim Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Havale Ettiklerim</span></span></a></li><li class="rpItem"><a href="/Evrak/IslemYaptiklarim/HavaleOnayinaGonderdiklerim.aspx" title="Son On Beş Gün İçerisinde Havale Onayına Gönderdiğım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Havale Onayına Gönderdiklerim</span></span></a></li><li class="rpItem"><a href="/Evrak/IslemYaptiklarim/CevapYazdiklarim.aspx" title="Son On Beş Gün İçerisinde Cevap Yazdığım Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Cevap Yazdıklarım</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/IslemYaptiklarim/GeriGonderdiklerim.aspx" title="Son On Beş Gün İçerisinde Geri Gönderdiğim Evraklar Listesi" class="rpLink"><span class="rpOut"><span class="rpText">Geri Gönderdiklerim</span></span></a></li>
			</ul>
		</div></li><li class="rpItem rpLast"><a href="#" title="Arama İşlemleri" class="rpLink MainItem rpExpandable rpExpanded"><span class="rpOut"><span class="rpText">Arama İşlemleri</span></span></a><div class="rpSlide" style="display:block;">
			<ul class="rpGroup rpLevel1 " style="display: block; width: 100%;">
				<li class="rpItem rpFirst"><a href="/Evrak/Arama/HizliEvrakAra.aspx" title="Evrak Arama" class="rpLink"><span class="rpOut"><span class="rpText">Evrak Arama</span></span></a></li><li class="rpItem"><a href="/Evrak/Arama/GelismisEvrakAra.aspx" title="Gelişmiş Evrak Arama" class="rpLink"><span class="rpOut"><span class="rpText">Gelişmiş Evrak Arama</span></span></a></li><li class="rpItem"><a href="/Evrak/Arama/ArsivdenEvrakAra.aspx" title="Arşivden Evrak Arama" class="rpLink"><span class="rpOut"><span class="rpText">Arşivden Evrak Arama</span></span></a></li><li class="rpItem"><a href="/Evrak/EvrakGorebilmeOzelDurum/OzelDurumTakip.aspx" title="İstisnai durum belirlenerek görebildiğiniz ve engellendiğiniz evrakların takibi" class="rpLink"><span class="rpOut"><span class="rpText">Evrak Görebilme İstisna Takip</span></span></a></li><li class="rpItem"><a href="/Evrak/EvrakGorebilmeOzelDurum/EvrakGorebilmeTalep.aspx" title="Birim aramalarından ulaşamadığınız, İdari Birim genelindeki evrakları görebilmek için talepte bulunma" class="rpLink"><span class="rpOut"><span class="rpText">Evrak Görebilme Talebi</span></span></a></li><li class="rpItem rpLast"><a href="/Evrak/EvrakArsivGorebilmeTalep/EvrakArsivGorebilmeTakip.aspx" title="Arşivden Evrak Görebilme İstisna Takip" class="rpLink"><span class="rpOut"><span class="rpText">Arşiv Evrak Görebilme İstisna Takip</span></span></a></li>
			</ul>
		</div></li>
	</ul><input id="ctl00_ctl00_cph1_RadPanelBarGelenGiden_ClientState" name="ctl00_ctl00_cph1_RadPanelBarGelenGiden_ClientState" type="hidden" autocomplete="off" value="{&quot;expandedItems&quot;:[&quot;0&quot;,&quot;1&quot;,&quot;6&quot;],&quot;logEntries&quot;:[],&quot;selectedItems&quot;:[]}">
</div>
                        </td>
                    </tr>
                </tbody></table>
            </td>
            <td style="width: 85%" align="left" valign="top">
                <table width="100%">
                    <tbody><tr>
                        <td valign="top" style="height: 299px" id="cphGelenGidenWrapper">
                            
    <style type="text/css">
        a {
            outline: 0;
        }

        h3 {
            font-size: 16px;
            margin: 0px 0px 10px;
            padding: 0px;
            color: #666;
        }

        .TabContainer {
            position: relative;
            width: 950px;
            padding-top: 25px;
        }

            .TabContainer .TumunuGoster {
                position: absolute;
                top: 75px;
                right: 10px;
                border: 1px solid #ccc;
                padding: 5px;
                color: #333;
                text-decoration: none;
            }

        ul.tabbaslik {
            list-style-type: none;
            margin: 0px;
            padding: 0px;
            position: absolute;
        }

            ul.tabbaslik li {
                float: left;
                position: relative;
                margin: 2px 5px 0px 0px;
            }

                ul.tabbaslik li a, .TabAktifLink, .TabBaslikIlemYapilacaklar, .TabBaslikUyari, .TabBaslikHaberler, .TabBaslikBaglantilar {
                    display: block;
                    background: #9CF;
                    color: #fff;
                    text-decoration: none;
                    height: 38px;
                    width: 172px;
                    background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakislemyaptiklarimtabbaslik.png);
                }

        .TabBaslikIlemYapilacaklar {
            background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakislemyapilacaklartabbaslik.png) !important;
        }

        .TabBaslikUyari {
            background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakuyarilartabbaslik.png) !important;
        }

        .TabBaslikHaberler {
            background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakhaberlertabbaslik.png) !important;
        }

        .TabBaslikBaglantilar {
            background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakbaglantilartabbaslik.png) !important;
        }

        .TabIcerik {
            padding: 40px 0px 0px 5px;
        }

            .TabIcerik > div {
                display: none;
                border: 1px solid #cbcbcb;
                background: #fff;
                padding: 25px 5px 5px;
            }

        .TabAktifLink {
            height: 57px !important;
        }

        .Listeler, .BildirimListe, .UyariListe, .HaberListe {
            list-style-type: none;
            margin: 0px;
            padding: 0px;
        }

            .Listeler li, .BildirimListe li, .UyariListe li, .HaberListe li {
                background: url(../../App_Themes/Main/Images/EvrakAnasayfa/satirBulletBg.png) no-repeat 5px center #fffbe8;
                margin: 0px 0px 2px 0px;
                border: 1px solid #d8ab12;
                position: relative;
            }

            .BildirimListe li {
                background: url(../../App_Themes/Main/Images/EvrakAnasayfa/bildirimikon.png) no-repeat 5px 15px #fffbe8;
            }

            .UyariListe li {
                background: url(../../App_Themes/Main/Images/EvrakAnasayfa/uyarikon.png) no-repeat 5px 15px #fffbe8;
            }

            .HaberListe li {
                background-image: none;
            }

                .Listeler li .TimeStamp, .BildirimListe li .TimeStamp, .UyariListe li .TimeStamp, .HaberListe li .TimeStamp {
                    position: absolute;
                    top: 0px;
                    right: 0px;
                    padding: 0px 2px;
                    display: inline-block;
                    background: #fff;
                    border: 1px solid #d8ab12;
                    border-top: none;
                    border-right: none;
                }

                .Listeler li a, .BildirimListe li a, .UyariListe li a, .HaberListe li a {
                    display: block;
                    color: #000;
                    text-decoration: none;
                    padding: 15px 0px 7px 30px;
                }

                .HaberListe li a {
                    padding-left: 5px;
                }

                    .Listeler li:hover, .BildirimListe li:hover, .UyariListe li:hover, .HaberListe li a:hover {
                        background-color: #fff;
                    }

        .Yenile {
            background: url(../../App_Themes/Main/Images/EvrakAnasayfa/yenilebg.jpg);
            width: 279px;
            height: 25px;
            position: absolute;
            right: 0px;
            top: 0px;
        }

            .Yenile a {
                position: absolute;
                right: 0px;
                background: url(../../App_Themes/Main/Images/EvrakAnasayfa/yenilebtn.png) center center no-repeat;
                width: 19px;
                height: 25px;
            }

            .Yenile span {
                position: absolute;
                left: 65px;
                top: 5px;
                font-weight: bold;
            }

            .Yenile .BilgiPopUp {
                position: absolute;
                top: 5px;
                left: 5px;
            }

        .PersonelBildirim {
            background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakanasayfa-personel-bildirim-bg.png) left top repeat-x;
            border: 1px solid #b3b3b3;
            cursor: pointer;
        }

            .PersonelBildirim span {
                padding: 3px;
                display: inline-block;
                cursor: pointer;
            }

                .PersonelBildirim span.sayi {
                    background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakanasayfa-personel-bildirim-sayi-bg.png) left top repeat-x;
                    color: #fff;
                }

            .PersonelBildirim a {
                text-decoration: none;
                color: #333;
            }

        .BaglantiListePanel {
            margin: 0 0 10px 0;
        }

            .BaglantiListePanel h4 {
                margin: 0;
                padding: 5px 10px;
                background: url(../../App_Themes/Main/Images/EvrakAnasayfa/evrakanasayfa-personel-bildirim-sayi-bg.png) repeat-x #e46f11;
                color: #fff;
                position: relative;
                cursor: pointer;
            }

                .BaglantiListePanel h4 span {
                    position: absolute;
                    right: 5px;
                    top: 5px;
                }

            .BaglantiListePanel .BaglantiListeBody {
                display: none;
            }

        .BaglantiListeBody ul {
            list-style-type: none;
            margin: 0 0 0 30px;
            padding: 0;
        }

        .BaglantiListePanel .BaglantiListeBody ul li {
            background: #fffbe8;
            margin: 0px 0px 2px 0px;
            border: 1px solid #d8ab12;
            position: relative;
            margin: 10px 0;
            position: relative;
        }

            .BaglantiListePanel .BaglantiListeBody ul li:hover {
                background: #fff;
            }

            .BaglantiListePanel .BaglantiListeBody ul li a {
                color: #333;
                display: block;
                padding: 5px;
            }

            .BaglantiListePanel .BaglantiListeBody ul li img {
                position: absolute;
                right: 5px;
                top: 5px;
            }

                .BaglantiListePanel .BaglantiListeBody ul li img:hover {
                    cursor: help;
                }
    </style>
    <script type="text/javascript">

        $(document).ready(function () {
            $(".ToolTip").hover(function (e) {
                var ToolTipText = $(this).attr("data-tooltip");
                $("<div id='ToolTip'></div>")
                    .html(ToolTipText)
                    .stop()
                    .fadeIn(150)
                    .css({
                        "top": e.pageY + 20,
                        "left": e.pageX + 20
                    })
                    .appendTo("body");

                $(this).mousemove(function (e) {


                    $("#ToolTip")
                        .css({
                            "top": e.pageY + 20,
                            "left": e.pageX + 20
                        });
                });


            }, function () {
                $("#ToolTip").remove();
            });
        })

        $(function () {
            $(".TabIcerik>div:first").toggle();
            $(".tabbaslik>li:first>a").addClass("TabAktifLink");
            $(".tabbaslik>li>a").click(function () {
                $(".tabbaslik a").removeClass("TabAktifLink")
                $(this).addClass("TabAktifLink");
                var rel = $(this).attr("rel");
                $(".TabIcerik>div").hide();
                $(".TabIcerik>div." + rel).toggle().addClass("AktifIcerik");
            });

            $(".BaglantiListePanel h4").click(function () {
                $(".BaglantiListePanel h4").next(".BaglantiListeBody").hide();
                $(this).next(".BaglantiListeBody").show();

            });
        });

        function RunOnPageLoad() {
            display_c(G('HiddenRefreshSuresi').value);
        }

        function display_c(start) {
            window.start = parseFloat(start);
            var end = 0
            var refresh = 1000;
            if (window.start >= end) {
                mytime = setTimeout('display_ct()', refresh)
            }
            else {
                __doPostBack('ctl00$ctl00$cph1$cphGelenGiden$ButtonHiddenDoPostback', '');
            }
        }

        function display_ct() {

            var minutes = Math.floor(window.start / 60);
            var secs = Math.floor((window.start - (minutes * 60)));

            if (secs.toString().length == 1) {
                secs = '0' + secs;
            }
            var x = minutes + ":" + secs;

            document.getElementById('ct').innerHTML = x;
            window.start = window.start - 1;

            tt = display_c(window.start);
        }

    </script>
    <div class="TabContainer">
        <input type="hidden" name="ctl00$ctl00$cph1$cphGelenGiden$HiddenRefreshSuresi" id="ctl00_ctl00_cph1_cphGelenGiden_HiddenRefreshSuresi" value="300">
        <table style="position: absolute; left: 15px; top: 0px;">
            <tbody><tr>
                <td>
                    
                </td>
                <td>
                    
                </td>
                <td>
                    
                </td>
            </tr>
        </tbody></table>
        <div class="Yenile">
            <div class="BilgiPopUp">
                


<script type="text/javascript" src="/Javascript/highslide/highslide-full.js"></script>

<link rel="stylesheet" type="text/css" href="/App_Themes/Main/highslide/highslide.css">

<script type="text/javascript">
    hs.graphicsDir = '/App_Themes/Main/highslide/graphics/';
    hs.outlineType = 'rounded-white';
    hs.wrapperClassName = 'draggable-header';

    function BilgiYardimMetniniWebMethodIleAl(sender, primaryKey) {
        var dizin = ObjeDizini(sender.id);
        var lblMetin = getObj(dizin + 'LabelMetin');
        if (lblMetin.innerText == '') {
            ShowProgress();
            PageMethods.BilgiYardimMetniniWebMethodIleAl(primaryKey, sender.id, OnBilgiYardimMetniAlindi, OnBilgiYardimMetniAlinirkenHataOlustu, sender.id);
        }
        else
            return hs.htmlExpand(sender);
    }
    
    function BilgiYardimMetniniWebServiceIleAl(sender, primaryKey, modulAdi) {
        var dizin = ObjeDizini(sender.id);
        var lblMetin = getObj(dizin + 'LabelMetin');
        if (lblMetin.innerText == '') {
            ShowProgress();
            BilgiYardimMetni.BilgiYardimMetniniWebServiceIleAl(primaryKey, sender.id, modulAdi, OnBilgiYardimMetniAlindi, OnBilgiYardimMetniAlinirkenHataOlustu, sender.id);
        }
        else
            return hs.htmlExpand(sender);
    }
    function OnBilgiYardimMetniAlindi(result, userContext, methodName) {
        var dizin = ObjeDizini(userContext);
        var lblMetin = getObj(dizin + 'LabelMetin');
        lblMetin.innerHTML = result;
        var imgButton = getObj(userContext);
        HideProgress();
        return hs.htmlExpand(imgButton);
    }
    function OnBilgiYardimMetniAlinirkenHataOlustu(error, userContext, methodName) {
        HideProgress();
        var errMsg = "Bilgi yardım metni alınırken hata oluştu !";
        var hdnObj = getObj(ObjeDizini(userContext) + 'HiddenFieldHataMesaji');
        if (hdnObj.value != '') errMsg = hdnObj.value;
        alert(errMsg);
    }

    function ShowProgress() {
        $("#spanBilgiYardimYukleniyorGif").css("display", "block");
    }

    function HideProgress() {
        $("#spanBilgiYardimYukleniyorGif").css("display", "none");
    }
    
</script>

<input type="hidden" name="ctl00$ctl00$cph1$cphGelenGiden$BilgiYardimAciklama$HiddenFieldHataMesaji" id="ctl00_ctl00_cph1_cphGelenGiden_BilgiYardimAciklama_HiddenFieldHataMesaji">
<span id="spanBilgiYardimYukleniyorGif" style="display: none; text-align: center;
    position: absolute; margin-top: 2px;">
    <img src="../../App_Themes/Main/Images/Ortak/yukleniyor.gif" alt="Yukleniyor">
</span>
<img id="ctl00_ctl00_cph1_cphGelenGiden_BilgiYardimAciklama_ImageBilgiYardim" title="Bilgi İçin Tıklayın" onclick="return hs.htmlExpand(this);" src="../../App_Themes/Main/Images/Ikonlar/bilgi.png" align="absmiddle" style="border-width:0px;cursor: pointer;">
<div class="highslide-maincontent" style="display: none;">
    <table id="ctl00_ctl00_cph1_cphGelenGiden_BilgiYardimAciklama_tableBilgiYardim">
	<tbody><tr>
		<td>
                <img id="ctl00_ctl00_cph1_cphGelenGiden_BilgiYardimAciklama_ImageBaslik" src="../../App_Themes/Main/Images/MessageBox/basari.gif" style="border-width:0px;">
                <span id="ctl00_ctl00_cph1_cphGelenGiden_BilgiYardimAciklama_LabelBaslik" style="font-size:Medium;font-weight:bold;">Açıklama</span>
                <br>
                <br>
                <span id="ctl00_ctl00_cph1_cphGelenGiden_BilgiYardimAciklama_LabelMetin"><ul><li>Size ait en son 10 adet görev ve bildirim listelenmektedir. Hepsini görmek için 'Tümünü Göster' linkine tıklayınız.</li>
                                          <li>15 günden eski olan bildirimler sistem tarafından otomatik olarak silinmektedir.</li>
                                          <li>Evrak ana sayfasını aşağıda bulunan 'Açılış Sayfam Yap' butonu ile ana sayfanız yapabilirsiniz.</li>
                                          <li>Görev ve Bildirimler şu an için giden, onay ve görüş tipindeki evraklar için çalışmaktadır.</li>
                                          <li>Hatırlamak amacıyla uyarı tarihleri ve saatlerini girdiğiniz evraklarınız Uyarılar menüsünde listelenecektir.</li> 
                                          <li>Çıktıların PDF çevirme işlemi, Sistemde Saklansın özelliği ile sistem tarafından PDF çevirme sırasına alınmakta, sonrasında Haberler menüsünden sırasıyla bu çıktılara ulaşılmaktadır</li>
                                          <li>Açıklama metinleri ilgili alana sığmadığı durumlarda fare imleci ile alan üzerine gelerek tamamını okuyabilirsiniz.</li>
                                      </ul></span>
                <br>
                <br>
            </td>
	</tr>
</tbody></table>

</div>

            </div>
            <span id="ct">5:00</span>
            <a id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonYenile" title="Yenile" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$LinkButtonYenile&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))"></a>
        </div>
        <ul class="tabbaslik">
            <li><a href="javascript:void(0)" rel="icerik1" class="TabBaslikIlemYapilacaklar TabAktifLink"></a>
            </li>
            <li><a href="javascript:void(0)" rel="icerik2"></a></li>
            <li><a href="javascript:void(0)" rel="icerik3" class="TabBaslikUyari"></a></li>
            <li><a href="javascript:void(0)" rel="icerik4" class="TabBaslikHaberler"></a></li>
            <li><a href="#1" rel="icerik5" class="TabBaslikBaglantilar"></a></li>
        </ul>
        <div style="clear: both">
        </div>
        <div class="TabIcerik">
            <div class="icerik1" style="display: block;">
                <a id="ctl00_ctl00_cph1_cphGelenGiden_HyperLinkTumunuGosterGorev" class="TumunuGoster" href="javascript:PopUp('/Evrak/EvrakAnaSayfa/BildirimlerPopUp.aspx', 'Bildirimler',  800, 800)">Tümünü Göster</a>
                <h3>
                    GÖREVLER
                </h3>
                
            </div>
            <div class="icerik2">
                <a id="ctl00_ctl00_cph1_cphGelenGiden_HyperLinkTumunuGosterBildirim" class="TumunuGoster" href="javascript:PopUp('/Evrak/EvrakAnaSayfa/BildirimlerPopUp.aspx', 'Bildirimler',  750, 680)">Tümünü Göster</a>
                <h3>
                    BİLDİRİMLER
                </h3>
                
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl00_LabelBildirimTarihi">21.10.20 09:39</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl00_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz NES Yenileme Talebi(Safiye Yüksek) konulu evrak Aysun KOLİVAR YURTSEVER tarafından paraflanmıştır." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl00$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>NES Yenileme Talebi(Safiye Yüksek)</b> konulu evrak Aysun KOLİVAR YURTSEVER tarafından paraflanmıştır.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl01_LabelBildirimTarihi">19.10.20 10:23</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl01_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Yerel Yönetici Yetki Talebi(Sadi BOLAT) konulu 92268 sayılı evrak Eyüp KANBEROĞLU tarafından postalanmıştır." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl01$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Yerel Yönetici Yetki Talebi(Sadi BOLAT)</b> konulu <font color="red">92268</font> sayılı evrak Eyüp KANBEROĞLU tarafından postalanmıştır.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl02_LabelBildirimTarihi">19.10.20 09:58</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl02_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Yerel Yönetici Yetki Talebi(Sadi BOLAT) konulu 92268 sayılı giden evrak Uğur ALADAĞ tarafından elektronik olarak imzalanmış ve evrak posta birimine düşmüştür." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl02$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Yerel Yönetici Yetki Talebi(Sadi BOLAT)</b> konulu <font color="red">92268</font> sayılı giden evrak Uğur ALADAĞ tarafından elektronik olarak imzalanmış ve evrak posta birimine düşmüştür.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl03_LabelBildirimTarihi">19.10.20 09:57</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl03_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Yerel Yönetici Yetki Talebi(Sadi BOLAT) konulu giden evrak Uğur ALADAĞ tarafından imzalanarak 92268 sayısını almıştır. Elektronik imza süreci devam etmektedir." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl03$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Yerel Yönetici Yetki Talebi(Sadi BOLAT)</b> konulu giden evrak Uğur ALADAĞ tarafından imzalanarak <font color="red">92268</font> sayısını almıştır. Elektronik imza süreci devam etmektedir.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl04_LabelBildirimTarihi">19.10.20 09:48</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl04_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Yerel Yönetici Yetki Talebi(Sadi BOLAT) konulu evrak Aysun KOLİVAR YURTSEVER tarafından paraflanmıştır." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl04$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Yerel Yönetici Yetki Talebi(Sadi BOLAT)</b> konulu evrak Aysun KOLİVAR YURTSEVER tarafından paraflanmıştır.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl05_LabelBildirimTarihi">16.10.20 16:56</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl05_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Soyadı Güncelleme Talebi(Buket ÇELİK) konulu 92224 sayılı evrak Bilal YILDIRIM tarafından postalanmıştır." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl05$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Soyadı Güncelleme Talebi(Buket ÇELİK)</b> konulu <font color="red">92224</font> sayılı evrak Bilal YILDIRIM tarafından postalanmıştır.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl06_LabelBildirimTarihi">16.10.20 16:56</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl06_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Yerel Yönetici Yetki Talebi konulu 92223 sayılı evrak Bilal YILDIRIM tarafından postalanmıştır." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl06$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Yerel Yönetici Yetki Talebi</b> konulu <font color="red">92223</font> sayılı evrak Bilal YILDIRIM tarafından postalanmıştır.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl07_LabelBildirimTarihi">16.10.20 16:38</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl07_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Soyadı Güncelleme Talebi(Buket ÇELİK) konulu 92224 sayılı giden evrak Uğur ALADAĞ tarafından elektronik olarak imzalanmış ve evrak posta birimine düşmüştür." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl07$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Soyadı Güncelleme Talebi(Buket ÇELİK)</b> konulu <font color="red">92224</font> sayılı giden evrak Uğur ALADAĞ tarafından elektronik olarak imzalanmış ve evrak posta birimine düşmüştür.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl08_LabelBildirimTarihi">16.10.20 16:38</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl08_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Yerel Yönetici Yetki Talebi konulu 92223 sayılı giden evrak Uğur ALADAĞ tarafından elektronik olarak imzalanmış ve evrak posta birimine düşmüştür." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl08$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Yerel Yönetici Yetki Talebi</b> konulu <font color="red">92223</font> sayılı giden evrak Uğur ALADAĞ tarafından elektronik olarak imzalanmış ve evrak posta birimine düşmüştür.</a></li>
                        </ul>
                    
                        <ul class="BildirimListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl09_LabelBildirimTarihi">16.10.20 16:37</span>
                            </span>
                                <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterBildirimler_ctl09_LinkButtonEvrakDetay" title=" Paraflamış olduğunuz Soyadı Güncelleme Talebi(Buket ÇELİK) konulu giden evrak Uğur ALADAĞ tarafından imzalanarak 92224 sayısını almıştır. Elektronik imza süreci devam etmektedir." href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterBildirimler$ctl09$LinkButtonEvrakDetay','')" style="display:inline-block;width:650px;"> Paraflamış olduğunuz <b>Soyadı Güncelleme Talebi(Buket ÇELİK)</b> konulu giden evrak Uğur ALADAĞ tarafından imzalanarak <font color="red">92224</font> sayısını almıştır. Elektronik imza süreci devam etmektedir.</a></li>
                        </ul>
                    
            </div>
            <div class="icerik3">
                <a id="ctl00_ctl00_cph1_cphGelenGiden_HyperLinkTumunuGosterUyari" class="TumunuGoster" href="javascript:PopUp('/Evrak/EvrakAnaSayfa/BildirimlerPopUp.aspx', 'Uyarilar',  800, 800)">Tümünü Göster</a>
                <h3>
                    EVRAK UYARILARI
                </h3>
                
            </div>
            <div class="icerik4">
                <a id="ctl00_ctl00_cph1_cphGelenGiden_HyperLinkTumunuGosterHaberler" class="TumunuGoster" href="javascript:PopUp('/Evrak/EvrakAnaSayfa/BildirimlerPopUp.aspx', 'Haberler',  800, 800)">Tümünü Göster</a>
                <h3>
                    HABERLER
                </h3>
                
                        <ul class="HaberListe">
                            <li><span class="TimeStamp">
                                <span id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterEvrakHaberleri_ctl00_LabelHaberTarihi">25.01.18 09:36</span>
                            </span>
                                <table>
                                    <tbody><tr>
                                        <td>
                                            <img id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterEvrakHaberleri_ctl00_ImageHaber" src="../../Resim/ikonlar/pdf.gif" style="border-width:0px;">
                                        </td>
                                        <td>
                                            <a id="ctl00_ctl00_cph1_cphGelenGiden_RepeaterEvrakHaberleri_ctl00_LinkButtonEvrakIcerikDetay" title="24.01.2018 tarihli ve 54608038-719-7857 sayılı, konusu Personel Arasındaki Görev Bölümü olan evrakın PDF çıktısı indirilebilir durumdadır.(Sayfa sayısı görünmesin,Sadece kağıt ortamında gidecekler görünsün, 8. versiyon)" href="javascript:__doPostBack('ctl00$ctl00$cph1$cphGelenGiden$RepeaterEvrakHaberleri$ctl00$LinkButtonEvrakIcerikDetay','')" style="display:inline-block;width:650px;">24.01.2018 tarihli ve 54608038-719-7857 sayılı, konusu Personel Arasındaki Görev Bölümü olan evrakın PDF çıktısı indirilebilir durumdadır.(Sayfa sayısı görünmesin,Sadece kağıt ortamında gidecekle...</a>
                                        </td>
                                    </tr>
                                </tbody></table>
                            </li>
                        </ul>
                    
            </div>
            <div class="icerik5">
                <a id="ctl00_ctl00_cph1_cphGelenGiden_lorem" class="TumunuGoster" href="#1">Tümünü Göster</a>
                <h3>
                    BAĞLANTILAR
                </h3>
                 <div class="BaglantiListePanel"><h4>Defterler ve Raporlar<span>Göster</span></h4><div class="BaglantiListeBody"><ul>  <li><a href="/Evrak/Rapor/Zimmet.aspx">Evrak Zimmet Raporu</a><img src="../../App_Themes/Main/Images/Ikonlar/aciklama.gif" class="CheckBox ToolTip" data-tooltip="Evrak zimmet raporu"></li> <li><a href="/Evrak/Rapor/GelenEvrakKayitDefteri.aspx">Gelen Evrak Kayıt Defteri</a><img src="../../App_Themes/Main/Images/Ikonlar/aciklama.gif" class="CheckBox ToolTip" data-tooltip="Gelen evrak kayıt defteri"></li> <li><a href="/Evrak/Rapor/KagitOrtamindaGelenEvrakRaporu.aspx">Kağıt Ortamında Gelen Evrak Dökümü</a><img src="../../App_Themes/Main/Images/Ikonlar/aciklama.gif" class="CheckBox ToolTip" data-tooltip="Kağıt ortamında gelen evrak dökümü"></li> <li><a href="/Evrak/Rapor/Posta.aspx">Giden Evrak Posta ve Postane Raporu</a><img src="../../App_Themes/Main/Images/Ikonlar/aciklama.gif" class="CheckBox ToolTip" data-tooltip="Giden evrak posta ve postane raporu"></li></ul></div></div>
            </div>
            <input type="submit" name="ctl00$ctl00$cph1$cphGelenGiden$ButtonHiddenDoPostback" value="" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$ButtonHiddenDoPostback&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" id="ctl00_ctl00_cph1_cphGelenGiden_ButtonHiddenDoPostback" style="display: none">
            <input type="hidden" name="ctl00$ctl00$cph1$cphGelenGiden$HiddenKalanSessionSuresi" id="ctl00_ctl00_cph1_cphGelenGiden_HiddenKalanSessionSuresi" value="30">
            <a id="ctl00_ctl00_cph1_cphGelenGiden_LinkButtonAcilisSayfamYap" title="Bu sayfayı açılış sayfası yapmak için tıklayınız" class="EvrakAnasayfaYapBtn" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$cph1$cphGelenGiden$LinkButtonAcilisSayfamYap&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))">Acılış Sayfam Yap</a>
        </div>
    </div>
    <script type="text/javascript">
        var trigger;
        $(document).ready(function () {
            var attr = $("#aspnetForm").attr("ShowSurveyPupup");
            if (typeof attr !== 'undefined' && attr !== false && attr === "true") {
                var surveyUrl = $("#aspnetForm").attr("SurveyUrl")
                var windobj = window.open(surveyUrl, '_blank', 'height=480,width=650,scrollbars');
                trigger = setInterval(function () { focuswindow(windobj) }, 100);
            }
        });

        $(document).ready(function () {
            var attr = $("#aspnetForm").attr("ShowAmirIzinOnayPupup");
            if (typeof attr !== 'undefined' && attr !== false && attr === "true") {
                var surveyUrl = $("#aspnetForm").attr("AmirIzinOnayUrl")
                var windobj = window.open(surveyUrl, '_blank', 'height=400,width=500,top=350,left=700 scrollbars');
                trigger = setInterval(function () { focuswindow(windobj) }, 100);
            }
        });

        function focuswindow(windobj) {
            windobj.focus();
            clearInterval(trigger);
        }
    </script>

                        </td>
                    </tr>
                </tbody></table>
            </td>
        </tr>
    </tbody></table>
    
<link href="/App_Themes/Main/Main.css" rel="stylesheet" type="text/css">

<script language="javascript" type="text/javascript" src="/Javascript/UserControlTextBox.js"></script>

<script language="javascript" type="text/javascript">

    function MsgBoxKapatModal(sender) {
        var objDivModal = getObj("ctl00_ctl00_cph1_MessageBoxModalInstance_DivMessageBoxModal");
        objDivModal.style.display = 'none';
        return false;
    }

    $(document).ready(function () { ResizeDivMsgBoxModal(); })
    window.onresize = function () { ResizeDivMsgBoxModal(); }
    function ResizeDivMsgBoxModal() {
        var objDivMsgBoxModal = getObj("ctl00_ctl00_cph1_MessageBoxModalInstance_DivMessageBoxModal");
        if (objDivMsgBoxModal.style.display == 'block') {
            objDivMsgBoxModal.style.width = GetPageWidth();
            objDivMsgBoxModal.style.height = GetPageHeight();
        }
    }
   
    /* Iframe Shim (Iframe perdeleme) - START */
    /* Gönderilen objenin boyutlarında ve koordinatlarında bir Iframe oluşturup, ondan sonra 
    parametre olarak gönderilen objeyi Iframe in üzerinde görüntülenecek şekilde yerleştirir. */
    function IframeShim(objID) {
        if ($("#" + objID).length) {
            var obj = $("#" + objID);
            var w = obj.width();
            var h = obj.height();
            var l = obj.offset().left;
            var t = obj.offset().top;
            obj.css("position", "absolute");
            obj.css("left", l + "px");
            obj.css("top", t + "px");
            obj.css("z-index", "1");
            $("<iframe style='position:absolute; z-index:0' frameborder='0' scrolling='no'></iframe>").css("left", l + "px").css("top", t + "px").css("width", w + "px").css("height", h + "px").insertAfter(obj);
        }
    }
    /* Iframe Shim (Iframe perdeleme) - END */

</script>

<div id="ctl00_ctl00_cph1_MessageBoxModalInstance_DivMessageBoxModal" style="height: 100%; position: fixed; top: 291px; left: 391px; width: 100%; z-index: 97; display: none;">
    <table style="height: 100%; width: 100%; opacity: 0.5; filter: alpha(opacity=50); background-color: #000;">
	<tbody><tr align="center">
		<td>
       <table id="TableMessageBoxModal">
        <tbody><tr>
         <td>
            <div id="ctl00_ctl00_cph1_MessageBoxModalInstance_PanelMsgBoxModal">
			
                <table border="0" cellspacing="0" cellpadding="0" class="uyarimesajlari">
                    <tbody><tr>
                        <td class="mesajkutusubaslik">
                            <div class="mesajkutusubasliksol">
                                <div class="mesajkutusubasliksolsag">
                                    <div>
                                        <span id="ctl00_ctl00_cph1_MessageBoxModalInstance_LabelBaslik"></span>
                                    </div>
                                    <div style="text-align:right; margin-top:-15px;margin-right:3px;">
                                        <input type="image" name="ctl00$ctl00$cph1$MessageBoxModalInstance$ButtonBasariClose" id="ctl00_ctl00_cph1_MessageBoxModalInstance_ButtonBasariClose" title="Kapat" src="../../App_Themes/Main/Images/Ikonlar/kapat.gif" onclick="return MsgBoxKapatModal(this);" style="border-width:0px;">
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td id="ctl00_ctl00_cph1_MessageBoxModalInstance_tdMesaj">
                            <table border="0" cellspacing="0" cellpadding="0" align="center">
                                <tbody><tr>
                                    <td>
                                        <div id="ctl00_ctl00_cph1_MessageBoxModalInstance_PanelMesaj" style="height:15px;overflow:auto;padding-right: 10px;">
				
                                            <span id="ctl00_ctl00_cph1_MessageBoxModalInstance_LabelMesaj"></span>
                                        
			</div>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding-right:20px;" align="center">
                                        <br>
                                        <input type="submit" name="ctl00$ctl00$cph1$MessageBoxModalInstance$ButtonTamam" value="Tamam" onclick="return MsgBoxKapatModal(this);" id="ctl00_ctl00_cph1_MessageBoxModalInstance_ButtonTamam">
                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
			
                    </tr>
                </tbody></table>
            
		</div>
         </td>
        </tr>
       </tbody></table>
      </td>
	</tr>
</tbody></table>

</div>



                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>&nbsp;
                            </td>
                            <td style="width: 100%; text-align: center;">
                                <div>
                                    
                                    
                                </div>
                            </td>
                        </tr>
                    </tbody></table>
                </div>
            </div>
            <div id="divBosluk" style="height: 50px; width: 100%;">
            </div>
            <div id="divFooter" style="background: url(/App_Themes/Main/Images/Master/2011/masterfooterbg.jpg) #273649 repeat-x; color: White; width: 100%; height: 50px; text-align: center; font-family: Segoe UI; position: fixed; bottom: 0;">
                <div style="width: 100%;">
                    <center>
                        
<link href="/App_Themes/Main/Main.css" rel="stylesheet" type="text/css">
<table style="color: White; font-size: smaller;">
    <tbody><tr>
        <td>
            <a id="ctl00_ctl00_FooterMenuControl1_ButtonMulkiIdari" class="FooterMenuCss" href="javascript:CreateWnd('/Anasayfa/MulkiIdariBolumleri.aspx?popup=Qo1B7YPyD6nGU6iDqj|deg==', 800, 600, true);">Mülki İdare Birimleri</a>
            |
            <a id="ctl00_ctl00_FooterMenuControl1_ButtonHaberlesmeKodlari" class="FooterMenuCss" href="javascript:CreateWnd('/Anasayfa/YazismaKodlari.aspx?popup=Qo1B7YPyD6nGU6iDqj|deg==', 800, 600, true);">Haberleşme Kodları</a>
            |
            <a id="ctl00_ctl00_FooterMenuControl1_ButtonTelefonRehberi" class="FooterMenuCss" href="javascript:CreateWnd('/Anasayfa/BirimTelefonDefteri/BirimTelefonDefteriArama.aspx?popup=Qo1B7YPyD6nGU6iDqj|deg==', 950, 600, true);">Telefon Rehberi</a>
            |
            <a id="ctl00_ctl00_FooterMenuControl1_ButtonBirimSecimi" class="FooterMenuCss" href="javascript:CreateWnd('https://www.e-icisleri.gov.tr/IBYetki/BirimYetkiDurumuPopUp.aspx', 1024, 600, true);">Birim Seçimi</a>
            
            |
            <a id="ctl00_ctl00_FooterMenuControl1_ButtonIletisim" class="FooterMenuCss" href="javascript:CreateWnd('/Iletisim.aspx?popup=Qo1B7YPyD6nGU6iDqj|deg==', 800, 600, true);" style="color:AliceBlue;">İletişim</a>
            |
        </td>
        <td>
            <img id="imgHideFooter" alt="Dipnot Sakla" src="../../App_Themes/Main/Images/Genel/crossblue.ico" style="cursor: pointer; padding-top: 3px;" onclick="HideMainMasterFooter();">
        </td>
    </tr>
</tbody></table>

                    </center>
                </div>
                <div style="height: 5px;">
                </div>
                <div style="width: 100%;">
                    <font style="color: #3caadd; font-weight: bold; font-size: small; font-stretch: wider;">T.C. İçişleri Bakanlığı</font> - Bilgi İşlem Dairesi Başkanlığı - © 2011
                &nbsp;&nbsp;-&nbsp;&nbsp; <font style="color: #a4cbf6;">Sürüm:
                    4.4.26.12122722</font>
                </div>
            </div>
        </div>
        
        
        <input type="hidden" name="ctl00$ctl00$hdnEvrakYetkiDurum" id="ctl00_ctl00_hdnEvrakYetkiDurum">
        <div id="ctl00_ctl00_SayiKontrolPanel">
	
                <a id="ctl00_ctl00_ButonSayilariKontrolEt" href="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$ButonSayilariKontrolEt&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, true))"></a>
                <input type="hidden" name="ctl00$ctl00$HiddenFieldDegisiklikOlduMu" id="ctl00_ctl00_HiddenFieldDegisiklikOlduMu">
                <input type="hidden" name="ctl00$ctl00$HiddenFieldUyariGoruntulemeSuresi" id="ctl00_ctl00_HiddenFieldUyariGoruntulemeSuresi">
                <input type="hidden" name="ctl00$ctl00$HiddenFieldSonucHtml" id="ctl00_ctl00_HiddenFieldSonucHtml">
                <input type="hidden" name="ctl00$ctl00$HiddenFieldTimerTimeout" id="ctl00_ctl00_HiddenFieldTimerTimeout">
            
</div>
        <div id="divMesajGetir" style="display: none; width: 452px; height: 102px;">
            
        </div>
        <input type="hidden" name="ctl00$ctl00$HiddenFieldOnEk" id="ctl00_ctl00_HiddenFieldOnEk" value="ctl00_">
        <input type="hidden" name="ctl00$ctl00$HiddenFieldInnerHtml" id="ctl00_ctl00_HiddenFieldInnerHtml">
        <input type="hidden" name="ctl00$ctl00$HiddenFieldPageOrientation" id="ctl00_ctl00_HiddenFieldPageOrientation">
        <input type="hidden" name="ctl00$ctl00$HiddenFieldSetBodyMinSize" id="ctl00_ctl00_HiddenFieldSetBodyMinSize">
        <input type="hidden" name="ctl00$ctl00$HiddenFieldResizeScreenWidth" id="ctl00_ctl00_HiddenFieldResizeScreenWidth">
    

<script type="text/javascript">
//<![CDATA[
Sys.Application.add_init(function() {
    $create(Sys.UI._UpdateProgress, {"associatedUpdatePanelId":"ctl00_ctl00_DropDownSayfaAra_UpdatePanelGenelDropDown","displayAfter":50,"dynamicLayout":true}, null, null, $get("ctl00_ctl00_DropDownSayfaAra_UpdateProgressGenelDropDown"));
});
Sys.Application.add_init(function() {
    $create(AjaxControlToolkit.AlwaysVisibleControlBehavior, {"HorizontalSide":1,"id":"ctl00_ctl00_MasterHeader_AlwaysVisibleControlExtender"}, null, null, $get("ctl00_ctl00_divMasterHeader"));
});
Sys.Application.add_init(function() {
    $create(AjaxControlToolkit.AlwaysVisibleControlBehavior, {"HorizontalSide":1,"VerticalSide":1,"id":"ctl00_ctl00_PanelProgressMain_AlwaysVisibleControlExtender"}, null, null, $get("ctl00_ctl00_PanelProgressMain"));
});
Sys.Application.add_init(function() {
    $create(Sys.UI._UpdateProgress, {"associatedUpdatePanelId":null,"displayAfter":10,"dynamicLayout":true}, null, null, $get("ctl00_ctl00_UpdateProgressMain"));
});
Sys.Application.add_init(function() {
    $create(Telerik.Web.UI.RadPanelBar, {"_skin":"Web20","clientStateFieldID":"ctl00_ctl00_cph1_RadPanelBarGelenGiden_ClientState","collapseAnimation":"{\"type\":0,\"duration\":100}","expandAnimation":"{\"duration\":450}","itemData":[{"items":[{"postBack":0,"value":"101"},{"postBack":0,"value":"106"},{"postBack":0,"value":"102"},{"postBack":0,"value":"103"},{"postBack":0,"value":"104"},{"postBack":0,"value":"108"}],"postBack":0,"value":"1","expanded":true,"cssClass":"MainItem"},{"items":[{"postBack":0,"value":"602"},{"postBack":0,"value":"605"},{"postBack":0,"value":"601"},{"postBack":0,"value":"601"},{"postBack":0,"value":"603"}],"postBack":0,"value":"6","expanded":true,"cssClass":"MainItem"},{"items":[{"postBack":0,"value":"202"},{"postBack":0,"value":"205"},{"postBack":0,"value":"203"},{"postBack":0,"value":"201"}],"postBack":0,"value":"2","cssClass":"MainItem"},{"items":[{"postBack":0,"value":"301"},{"postBack":0,"value":"302"},{"postBack":0,"value":"304"},{"postBack":0,"value":"303"}],"postBack":0,"value":"3","cssClass":"MainItem"},{"items":[{"postBack":0,"value":"703"},{"postBack":0,"value":"702"},{"postBack":0,"value":"701"},{"postBack":0,"value":"704"},{"postBack":0,"value":"705"}],"postBack":0,"value":"7","cssClass":"MainItem"},{"items":[{"postBack":0,"value":"404"},{"postBack":0,"value":"405"},{"postBack":0,"value":"401"},{"postBack":0,"value":"402"},{"postBack":0,"value":"403"},{"postBack":0,"value":"408"},{"postBack":0,"value":"406"},{"postBack":0,"value":"410"}],"postBack":0,"value":"4","cssClass":"MainItem"},{"items":[{"postBack":0,"value":"501"},{"postBack":0,"value":"502"},{"postBack":0,"value":"503"},{"postBack":0,"value":"505"},{"postBack":0,"value":"506"},{"postBack":0,"value":"507"}],"postBack":0,"value":"5","expanded":true,"cssClass":"MainItem"}]}, null, null, $get("ctl00_ctl00_cph1_RadPanelBarGelenGiden"));
});
Sys.Application.add_init(function() {
    $create(AjaxControlToolkit.AlwaysVisibleControlBehavior, {"HorizontalSide":1,"VerticalSide":1,"id":"ctl00_ctl00_cph1_MessageBoxModalInstance_MsgBoxModal_AlwaysVisibleControlExtender"}, null, null, $get("ctl00_ctl00_cph1_MessageBoxModalInstance_DivMessageBoxModal"));
});
Sys.Application.add_init(function() {
    $create(AjaxControlToolkit.ModalPopupBehavior, {"BackgroundCssClass":"ModalPopupBackground","CancelControlID":"ctl00_ctl00_ImageButtonKapatSikKullanilanlar","DropShadow":true,"PopupControlID":"ctl00_ctl00_PanelSikKullanilanlar","dynamicServicePath":"/Evrak/EvrakAnaSayfa/EvrakAnaSayfa.aspx","id":"ctl00_ctl00_ModalPopupExtenderHyperLinkSikKullanilanlar"}, null, null, $get("ctl00_ctl00_HyperLinkSikKullanilanlar"));
});
//]]>
</script>
<div id="ctl00_ctl00_ModalPopupExtenderHyperLinkSikKullanilanlar_foregroundElement" style="display: none; position: fixed; z-index: 100001;"><div id="ctl00_ctl00_PanelSikKullanilanlar" style="background-color:AliceBlue;border-color:RoyalBlue;border-width:2px;border-style:Solid;width:500px;">
	
            <table style="width: 100%" class="AnaTablo">
                <tbody><tr>
                    <td style="text-align: right; background-color: #99b4d1;">
                        <input type="image" name="ctl00$ctl00$ImageButtonKapatSikKullanilanlar" id="ctl00_ctl00_ImageButtonKapatSikKullanilanlar" title="Kapat" src="../../Resim/Ortak/kapat.gif" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$ImageButtonKapatSikKullanilanlar&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))" style="border-width:0px;">
                    </td>
                </tr>
                <tr>
                    <td align="left" style="font-size: medium; font-weight: bold; color: Black;">Sık Kullanılan Sayfalarım
                    <hr style="height: 1px; color: Navy">
                    </td>
                </tr>
                <tr>
                    <td align="center" style="width: 80%;">
                        <span id="ctl00_ctl00_LabelSikKullanilanlar" style="background-color:White;">Sık kullanılan sayfanız bulunmamaktadır</span>
                        <hr style="height: 1px; color: Navy">
                    </td>
                </tr>
                <tr>
                    <td align="right" style="padding-right: 5px; padding-bottom: 5px;">
                        <img id="ctl00_ctl00_ImageSikKullanilanlarDuzenle" title="Sık kullanılan sayfalarınızı düzenlemek için tıklayınız" src="../../App_Themes/Main/Images/Genel/list_bullets.ico" align="absmiddle" style="border-width:0px;cursor: pointer;">
                        <a id="ctl00_ctl00_HyperLinkSikKullanilanlarDuzenle" title="Sık kullanılan sayfalarınızı düzenlemek için tıklayınız" class="LinkHover">Düzenle</a>
                    </td>
                </tr>
            </tbody></table>
        
</div></div><div id="ctl00_ctl00_ModalPopupExtenderHyperLinkSikKullanilanlar_backgroundElement" class="ModalPopupBackground" style="display: none; position: fixed; left: 0px; top: 0px; z-index: 10000;"></div></form>
    <script type="text/javascript">
        $(document).ready(function () {
            document.getElementById("aspnetForm").disabled = false;
            RunOtherNecessaryJsFunctionsOnLoad();
            SetPageSize();
        })
        $(document).mousemove(function () {
            window.status = 'e-icisleri';
            return true;
        });

        function RunOtherNecessaryJsFunctionsOnLoad() {
            /* Bu JS fonksiyonu istemci tarafında gösterilen uyarı penceresi için kullanılıyordu. 
            Ama performansı olumsuz etkilediği için şimdilik kapatıldı
            */
            //uyariTimeoutSetle();

            /* Buraya yazılan fonksiyon isimleri bu masterdan türeyen sayfalara JS fonksiyonu olarak konulur 
            ve sayfa yüklendiğinde devereye girer. Sayfada bu fonksiyon yoksa hataya düşer ve catch bloğunda hata yutulur.
            */
            try { SetTimersOnLoad(); } catch (exception) { /*Do Nothing*/ }
            try { RunOnPageLoad(); } catch (exception) { /*Do Nothing*/ }
        }

        function HideMainMasterFooter() {
            GetFooterObject().style.display = "none";
        }
        function ShowMainMasterFooter() {
            GetFooterObject().style.display = "block";
        }
        function GetFooterObject() {
            var obj = getObj('divFooter');
            return obj;
        }

    </script>


<div class="highslide-container" style="padding: 0px; border: none; margin: 0px; position: absolute; left: 0px; top: 0px; width: 100%; z-index: 1001; direction: ltr;"><a class="highslide-loading" title="İptal etmek için tıklayın" href="javascript:;" style="position: absolute; top: -9999px; opacity: 0.75; z-index: 1;">Yükleniyor...</a><div style="display: none;"></div><div class="highslide-viewport highslide-viewport-size" style="padding: 0px; border: none; margin: 0px; visibility: hidden;"></div><table cellspacing="0" style="padding: 0px; border: none; margin: 0px; visibility: hidden; position: absolute; border-collapse: collapse; width: 0px;"><tbody style="padding: 0px; border: none; margin: 0px;"><tr style="padding: 0px; border: none; margin: 0px; height: auto;"><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) 0px 0px; height: 20px; width: 20px;"></td><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) 0px -40px; height: 20px; width: 20px;"></td><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) -20px 0px; height: 20px; width: 20px;"></td></tr><tr style="padding: 0px; border: none; margin: 0px; height: auto;"><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) 0px -80px; height: 20px; width: 20px;"></td><td class="rounded-white highslide-outline" style="padding: 0px; border: none; margin: 0px; position: relative;"></td><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) -20px -80px; height: 20px; width: 20px;"></td></tr><tr style="padding: 0px; border: none; margin: 0px; height: auto;"><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) 0px -20px; height: 20px; width: 20px;"></td><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) 0px -60px; height: 20px; width: 20px;"></td><td style="padding: 0px; border: none; margin: 0px; line-height: 0; font-size: 0px; background: url(&quot;https://www.e-icisleri.gov.tr/App_Themes/Main/highslide/graphics/outlines/rounded-white.png&quot;) -20px -20px; height: 20px; width: 20px;"></td></tr></tbody></table><img src="/App_Themes/Main/highslide/graphics/outlines/rounded-white.png" style="padding: 0px; border: none; margin: 0px; position: absolute; top: -9999px;"></div></body></html>"""

from bs4 import BeautifulSoup as bs
def getHMTLSourceCode(k):
    source = k
    # print(source)
    html_source = bs(source, 'html.parser')
    all_ul = html_source.find_all('span', class_="rpText")
    # k=0
    # for i in all_ul:
    #     print(k,i)
    #     k+=1


        # if len(all_ul) >= 18:
    counter_values = all_ul[1].get_text(), all_ul[2].get_text(), all_ul[16].get_text(), all_ul[14].get_text(),all_ul[15].get_text(), all_ul[19].get_text()
    print(counter_values)
        # if len(counter_values) != 6:
        #     time.sleep(10)
        #     self.clickEvrakPage()
        #     self.getHMTLSourceCode()
        # else:
        #     return counter_values
    # else:
    #     time.sleep(10)
    #     self.clickEvrakPage()
    #     self.getHMTLSourceCode()

getHMTLSourceCode(code)
