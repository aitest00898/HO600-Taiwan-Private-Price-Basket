

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1" /><meta name="description" /><meta name="author" /><link rel="icon" href="../../LOGO.ico" type="image/x-icon" /><title>
	FamilyMart 全家企業-最新消息
</title>
    <!--js-->

    <script src="../js/jquery-1.8.2.min.js"></script>

    <script src="../js/common.js"></script>

    <script src="../js/jquery.easing.1.3.js"></script>

    <script src="../js/ddsmoothmenu.js"></script>

    <script src="../js/jquery.flexslider.js"></script>

    <script src="../js/jquery.elastislide.js"></script>

    <script src="../js/jquery.jcarousel.min.js"></script>

    <script src="../js/jquery.accordion.js"></script>

    <script src="../js/light_box.js"></script>

    <script src="../js/popform.js"></script>

    <script type="text/javascript">        $(document).ready(function() { $(".inline").colorbox({ inline: true, width: "50%" }); });</script>

    <!--end js-->
    <!-- Mobile Specific Metas ================================================== -->
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
    <!-- CSS ================================================== -->
    <link rel="stylesheet" href="../css/bootstrap.css" type="text/css" />
    <!-- Owl Carousel Assets -->
    <link rel="stylesheet" href="../css/zerogrid.css" /><link rel="stylesheet" href="../css/sb-admin-2.css" /><link rel="stylesheet" href="../css/metisMenu.min.css" /><link rel="stylesheet" href="../css/style.css" /><link rel="stylesheet" href="../css/colors.css" /><link rel="stylesheet" href="../css/skeleton.css" /><link rel="stylesheet" href="../css/layout.css" /><link rel="stylesheet" href="../css/ddsmoothmenu.css" /><link rel="stylesheet" href="../css/elastislide.css" /><link rel="stylesheet" href="../css/home_flexslider.css" /><link rel="stylesheet" href="../css/light_box.css" /><link href="../owl-carousel/owl.carousel.css" rel="stylesheet" /><link href="../owl-carousel/owl.theme.css" rel="stylesheet" /><link rel="stylesheet" href="../font-awesome-4.4.0/css/font-awesome.css" type="text/css" /><link rel="stylesheet" href="../css/media.css" /><link rel="stylesheet" href="../css/borderwid.css" /><link rel="stylesheet" href="../css/custom.css" />
    <!-- jQuery and Modernizr-->
    <!-- Core JavaScript Files -->

    <script type="text/javascript" src="../js/bootstrap.min.js"></script>

    <script type="text/javascript" src="../js/html5.js"></script>

    <script type="text/javascript">
        $(function() {
            $("#gotop").click(function() {
                jQuery("html,body").animate({
                    scrollTop: 0
                }, 1000);
            });
            $(window).scroll(function() {
                if ($(this).scrollTop() > 100) {
                    $('#gotop').fadeIn("fast");
                } else {
                    $('#gotop').stop().fadeOut("fast");
                }
            });
        });
    </script>

    <script src="../js/fontawesome-all.5.0.8.min.js"></script>

    <!--Alertify CSS-->
    <link rel="stylesheet" href="../js/Alertify/alertify.core.css" /><link id="ctl00_toggleCSS" rel="stylesheet" href="../js/Alertify/alertify.default.css" />
    <!--Alertify JS-->

    <script type="text/javascript" src="../js/Alertify/alertify.min.js"></script>

    <script type="text/javascript">
        function reset() {
            $("#toggleCSS").attr("href", "js/Alertify/alertify.default.css");
            alertify.set({
                labels: {
                    ok: "確認",
                    cancel: "取消"
                },
                delay: 5000,
                buttonReverse: false,
                buttonFocus: "ok"
            });
        }

    </script>

    <!--傳值給Google搜尋-->

    <script type="text/javascript">
        function SearchURL1() {
            var GetValue = document.getElementById("txt1").value;
            location.href = "SearchList.aspx?SerchText=" + GetValue;
        }
        function SearchURL2() {
            var GetValue = document.getElementById("txt2").value;
            location.href = "SearchList.aspx?SerchText=" + GetValue;
        }
        function fouceClick1() {
            if (event.keyCode == 13) {
                document.getElementById("btn1").focus();
            }
        }
        function fouceClick2() {
            if (event.keyCode == 13) {
                document.getElementById("btn2").focus();
            }
        }
    </script>

    <!--傳值給Google搜尋 END-->
    <style type="text/css">
        @media only screen and (min-device-width: 1024px) and (max-device-width: 1366px)
        {
            .item iframe
            {
                height: 215px;
            }
        }
        @media only screen and (min-device-width : 768px) and (max-device-width : 1023px)
        {
            .item iframe
            {
                height: 158px;
            }
        }
        @media only screen and (min-width:768px)
        {
            .cis
            {
                float: left;
                padding: 0 0 0 0;
            }
            .logo-pc
            {
                display: inline-block;
            }
            .logo-m
            {
                display: none;
            }
            li.more
            {
                display: block;
            }
            .glyphicon-search
            {
                margin-left: 5px;
            }
        }
        @media only screen and (max-width: 812px)
        {
            .logo-pc
            {
                display: none;
            }
            .logo-m
            {
                display: inline-block;
                margin: 0 auto;
                width: 100px;
                max-width: 100px;
                vertical-align: middle;
            }
            .cis
            {
                width: 100%;
            }
            .col-lg-6-more
            {
                display: none;
            }
            .btn-group
            {
                display: none;
            }
        }
        @media only screen and (max-width: 480px)
        {
            .item iframe
            {
                height: 238px;
            }
            .payment-block
            {
                margin-top: 0;
            }
        }
        /*footer*/
        .dpmarkseal
        {
            font-family: 'Arial';
            font-size: 11pt;
            color: gray;
            font-weight: bold;
            float: left;
        }
        .lh
        {
            line-height: 23px;
            text-align: left;
        }
        .social-links
        {
            /*padding: 30px 0px 0px;*/
            margin: 0;
            width: auto;
        }
        .payment-block
        {
            /*padding: 8px 0px 0px;margin-right:100px;*/
            margin-top: -27px;
        }
         .pd
        {
            padding: 5px 0 0 5px;
            text-align: left;
        }
    </style>
    
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-MFB6BG3KK6"></script>
        <script>
            window.dataLayer = window.dataLayer || [];

            function gtag() {
                dataLayer.push(arguments);
            }
            gtag('js', new Date());

            gtag('config', 'G-MFB6BG3KK6');
        </script>
        <style type="text/css">
            .row {
                margin: 0px;
            }

            .video-container {
                position: relative;
                padding-bottom: 60%;
                right: -20px padding-top: 30px;
                height: 0;
                overflow: hidden;
            }

            .video-container iframe,
            .video-container object,
            .video-container embed {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                text-align: center;
            }

            #gotop {
                display: none;
                position: fixed;
                right: 20px;
                bottom: 20px;
                padding: 10px 15px;
                font-size: 16px;
                font-family: 'Arial';
                font-weight: bold;
                background: #008cd6;
                color: white;
                cursor: pointer;
                z-index: 3;
            }

            .circle_in_black1 {
                width: 270px;
                height: auto;
                border-radius: 10px;
                background-color: rgba(0, 204, 102, 0.8);
            }

            .circle_in_black2 {
                width: 270px;
                height: auto;
                border-radius: 10px;
                background-color: rgba(0, 153, 255, 0.8);
            }

            .circle_in_black3 {
                width: 270px;
                height: auto;
                border-radius: 10px;
                background-color: rgba(255, 80, 80, 0.8);
            }

            .circle_in_black4 {
                width: 270px;
                height: auto;
                border-radius: 10px;
                background-color: #ffc34d;
            }

            .special-text {
                font-size: 60px;
                color: #fff;
                font-weight: bolder;
                text-align: center;
                float: left;
                padding: 50px 0;
                width: 270px;
            }

            .special-text2 {
                font-size: 60px;
                color: #fff;
                font-weight: bolder;
                text-align: center;
                float: left;
                padding: 60px 0;
                width: 270px;
            }

            .banner-gd {
                float: left;
                width: 50%;
                padding: 0px 0px 0px 10px;
            }

            .banner-gd2 {
                float: left;
                width: 50%;
                height: auto;
                padding: 10px 0px 10px 12px;
            }

            #img_al {
                float: center;
                max-width: 100%;
                height: auto;
                padding: 0 0 0 0;
            }

            #img_vd {
                float: center;
                max-width: 100%;
                height: auto;
                padding: 0px 15px 0 0px;
            }

            .glyph-icon {
                width: 60px;
                height: 60px;
            }

            .tab_w {
                padding: 0 0px 0 10px;
            }

            .header-right {
                padding: 0;
                float: right;
            }

            .header-left {
                width: 28%;
                float: left;
            }

            .ft {
                padding: 0 0 0 0;
            }

            /*navtitle*/
            h1.page-title {
                font-size: 24px;
                color: #737373;
                margin: 0 0 18px;
                line-height: 24px;
                font-weight: bold;
                margin-top: 9px;
            }

            .navtitle {
                font-size: 24px;
                padding: 0px 0 15px 0px;
                font-family: "微軟正黑體", "新細明體", Arial;
                font-weight: bold;
                color: #666666;
            }

            /*navtab*/
            .nav-pills>li {
                margin-right: 5px;
            }

            .nav-pills>li>a {
                font-size: 10pt;
                color: #00b347;
                background-color: #eeeeee;
            }

            .nav-pills>li.active>a,
            .nav-pills>li.active>a:hover,
            .nav-pills>li.active>a:focus {
                background-color: #00b347;
            }

            /*invest*/
            .invest_info {
                font-size: 14px;
            }

            .invest_info table {
                margin-bottom: 5px;
            }

            .subtitle {
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 10px;
            }

            .fa-angle-double-right {
                color: #00b347;
                font-size: 18px;
            }

            .more {
                float: right;
                font-size: 14px;
                margin-top: 11px;
            }

            .heading .col-sm-6 {
                margin-bottom: 10px;
            }

            .heading ul {
                padding-top: 10px;
            }

            .heading ul li {
                list-style: disc;
            }

            .hr_2 {
                border: none;
                height: 20px;
                margin-top: -15px;
                border-bottom: 3px solid #00b347;
                box-shadow: 0 10px 10px -10px #333;
            }

            .heading h2 {
                color: #737373;
                font-size: 24px;
            }

            .top_img {
                text-align: center;
                margin-top: 10px;
            }

            .sort {
                display: block;
                background: #999999;
                padding: 2px 0px 3px 0px;
                border-color: #cccccc;
                border-radius: 2px;
                color: #FFFFFF;
                width: 90px;
                text-align: center;
                font-weight: bold;
            }

            /*newstable*/
            .css-table {
                display: table;
                width: 100%;
                margin-bottom: 15px;
            }

            .css-table .thead {
                display: table-header-group;
                background-color: #EFEFEF;
            }

            .css-table .tbody {
                display: table-row-group;
                font-size: 10pt;
            }

            .css-table .tr {
                display: table-row;
            }

            .css-table .th {
                font-weight: bold;
                font-size: 14px;
                padding: 4px;
                border-bottom: 1px solid #CCCCCC;
            }

            .css-table .th,
            .css-table .td {
                display: table-cell;
            }

            .css-table .td {
                padding: 6px;
                border-bottom: 1px dashed #CCCCCC;
            }

            .css-table .td-right {
                text-align: right;
            }

            .css-table .td-center {
                text-align: center;
                width: 20%;
            }

            /*for editor*/
            .editor {
                font-family: "微軟正黑體", "新細明體", Arial;
                font-size: 11pt;
                text-align: justify;
                margin-bottom: 15px;
            }

            .editor p {
                font-size: 11pt;
            }

            .editor img {
                float: left;
                margin: 8px;
            }

            .editor table tbody tr td {
                border: 1px solid #cccccc;
            }

            .editor ul li {
                margin-left: 2rem;
            }

            /*img thumbnail*/
            img.thumbnail {
                display: unset;
                margin-bottom: 0;
            }

            .glyphicon-search {
                margin-left: 5px;
            }

            /*logo*/
            .item iframe {
                height: 238px;
            }

            @media only screen and (min-device-width: 1024px) and (max-device-width: 1366px) {
                .item iframe {
                    height: 215px;
                }
            }

            @media only screen and (min-device-width : 768px) and (max-device-width : 1023px) {
                .item iframe {
                    height: 158px;
                }
            }

            @media only screen and (min-width:768px) {
                .cis {
                    float: left;
                    padding: 0 0 0 0;
                }

                .logo-m {
                    display: none;
                }

                li.more {
                    display: block;
                }

                .glyphicon-search {
                    margin-left: 5px;
                }
            }

            @media only screen and (max-width: 768px) {
                .logo-pc {
                    display: none;
                }

                .logo-m {
                    display: block;
                    margin: 0 auto;
                }

                .cis {
                    width: 100%;
                }

                .col-lg-6-more {
                    display: none;
                }

                .btn-group {
                    display: none;
                }
            }

            @media only screen and (max-width: 480px) {
                .item iframe {
                    height: 238px;
                }
            }

            @media only screen and (max-width: 812px) {
                .payment-block {
                    margin-top: 0;
                }
            }
        </style>
    </head>
<body>
    <form name="aspnetForm" method="post" action="NewsContent.aspx?ID=696" id="aspnetForm">
<div>
<input type="hidden" name="ctl00_ToolkitScriptManager1_HiddenField" id="ctl00_ToolkitScriptManager1_HiddenField" value="" />
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTI5MjE5MTcyOA8WAh4DX0lEBQM2OTYWAmYPZBYCAgQPZBYGAgMPDxYCHgRUZXh0BQQ0NTA2ZGQCBQ8WAh4EaHJlZgVHaHR0cDovL3d3dy5mYW1pbHkuY29tLnR3L1dlYl9FbnRlclByaXNlL3BhZ2UvTmV3c0NvbnRlbnRfZW4uYXNweD9JRD02OTZkAgcPZBYGAgEPDxYCHwEFQOOAjOWFqOWutuOAjeWJteWIhuecvuWMlumbu+WVhumWi+W6l+W5s+WPsCDliqnmlLvlsI/os6PlrrbljYfntJpkZAIDDw8WAh8BBeqMAjxwPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuekvue+pOmbu+WVhuOAgee2sue0hee2k+a/n+eVtumBk++8jOaHiemBi+iAjOeUn+ecvuWkmuWPr+iHquW4tua1gemHj+eahOWAi+S6uuWMluizo+WutuOAgueehOa6luaWsOmbu+WVhuaZguS7o+S+huiHqO+8jOWFqOWutuS+v+WIqeWVhuW6l+aJk+mAoOWFqOaWsOmbtuaIkOacrOOAgeWIhuecvuWMlueahOmWi+W6l+W5s+WPsOKUgOOAjOWlvemWi+W6l+OAjeOAgeOAjOWlveW6l++8i+OAje+8jOS4u+aJk2xpbmXlpb3lj4vlnIjjgIFGYWNlYm9va+ekvuWcmOOAgeebtOaSremgu+mBk+S4iueahOWwj+izo+Wutu+8jOa7v+i2s+mBi+eHn+majuauteS4jeWQjOeahOmWi+W6l+mcgOaxgu+8jOW+nuWfuuekjueahOmHkea1geOAgeeJqea1geOAgeizh+ioiua1geaVtOWQiOacjeWLmeWklu+8jOWIsOS4ieWIhumQmOWTgeeJjOWumOe2suW7uue9ruOAgUNSTee2k+eHn+WIhuaekOOAgeihjOmKt+a0u+WLleaooee1hOetieWKn+iDveS4gOaHieS/seWFqO+8jOabtOelreWHuuWFjeenn+mHkeOAgeWFjeaIkOS6pOaJi+e6jOiyu++8jOmgkOioiOS4ieW5tOWwh+WKqeaUuzHokKzlrrbllYblrrbvvIzoo5zliqnnuL3lg7nlgLzpq5jpgZQxMOWEhOWFg+OAgjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+Jm5ic3A7PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+44CM5YWo5a6244CNPC9zcGFuPuWOu+W5tOaOqOWHuuOAjOWlveizozxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+77yL44CNQzJDPC9zcGFuPumbu+WVhuW5s+WPsOS7peS+hu+8jDxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5LiN5Yiw5LiA5bm05YWx5ZC45byVMTLokKzos6PlrrbjgIHplovoqK3otoXpgY4zMOiQrOWAi+izo+WgtOOAguOAjOWFqOWutuOAjUUtUmV0YWls5LqL5qWt6YOo6YOo6ZW3546L5ZWf5Lie6KGo56S677yMPC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5b6M55ar5oOF5pmC5Luj6YCy5LiA5q2l5Yqg5rqr57ay6LO85biC5aC077yM6aCQ5LywPC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+44CM5aW96ZaL5bqX44CN44CB44CM5aW95bqX77yL44CN6ZuZ5bmz5Y+w5LiK57ea5b6M77yM5LiJ5aSn6Ieq5pyJ5bmz5Y+wRUPku7bmr5TkvovlsIfmnInmnJvkuIDoiInmjqjljYfjgIHkvZTmlbTpq5TkuInmiJA8L3NwYW4+44CC5q2k5aSW77yM54K65omT6YCg5YWo5pa55L2N55qE6LOj5a6255Sf5oWL5ZyI77yM6Zm457qM6Yed5bCN6LOj5a6255eb6bue77yM5o6o5Ye644CM5oiR55qE5YyF6KO544CNKGFwcOWNs+aZguiyqOaFi+afpeipoinjgIHjgIzos6M8c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPu+8izwvc3Bhbj7oo5zntabnq5njgI0o5YyF5p2Q5YKZ5ZOB57ea5LiK6LO8KeOAgeOAjOaUtuiyqOmAmuOAjSjlpKfllq7liLDlupzmlLbku7Yp562J6YWN5aWX5Yqf6IO977yM5o+Q5L6b5b6e5YmN5Y+w5Lqk5piT5LuL6Z2i5Yiw5b6M5Y+w5pSv5o+057O757Wx55qE5LiA5qKd6b6N5pyN5YuZ44CCPC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPiZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48aT48dT7jgIzlhajlrrbjgI3lloTnlKjjgIzkuInmtYHmnI3li5njgI0g5omT6YCg5LiA56uZ5byP57ay6Lev6ZaL5bqX5bmz5Y+wPC91PjwvaT48L2I+PC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PGI+PGk+PHU+5aW96LOj77yL44CB5aW96ZaL5bqX44CB5aW95bqX77yLIOS4ieeurem9iueZvOWKqeaUu+Wwj+izo+WutumbtuaIkOacrOWNh+e0mjwvdT48L2k+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+5qC55pOa44CM5YWo5a6244CN5YWn6YOo6LOH5paZ55m854++77yM5Lul5ouN6LOj6aGe5Z6L54K65Li755qEQzJD5Lqk5piT5Lu25pW45Y2g5pW0PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7pq5Tlupflj5bljIXoo7k35oiQ5Lul5LiK77yMPC9zcGFuPuS4lOatpOmhnuizo+WutuaVuOaciemAkOW5tOaIkOmVt+eahOi2qOWLou+8jOmhr+ekukMyQ+mbu+WVhuaZguS7o+S+huiHqOOAgjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+546L5ZWf5Lie5oyH5Ye677yMPHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7jgIzlhajlrrbjgI3plbfmnJ/mia7mvJRFQ+WMheijueacgOW+jOS4gOWTqei3r++8jOi/keW5tOWJh+mAsuS4gOatpemBi+eUqOaXouacieWEquWLou+8jOi3qOi2s+W5s+WPsOe2k+a/n++8jOmWi+ioreOAjDwvc3Bhbj7lpb3os6M8c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPu+8i+OAje+8jOaPkOS+m+ekvue+pOizo+WutuewoeaYk+eahOaOpeWWruW5s+WPsO+8jDwvc3Bhbj48YSBuYW1lPSJfSGxrNDE4Mzc2MzciPumHkea1geOAgeeJqea1geOAgeizh+ioiua1gTwvYT7nm7jkupLmlbTlkIjnmoTjgIzkuInmtYHmnI3li5njgI3jgILph5HmtYHpg6jliIbvvIzmj5Dkvpvos6PlrrblpJrlhYPnmoTku5jmrL7mlrnlvI/oiIfluLPli5nkuLLmjqXnmoTmn6XoqaLoiIflvZnmlbTvvJvnianmtYHliYfmmK/mlbTlkIjlhajlj7DotoXpgY4zLDYwMOWutuW6l+iIluWEquWLou+8jOWFqOWPsOeahuWPr+WvhOWPluS7tu+8m+izh+ioiua1geWJh+iIh+OAjOWFqOWutuOAjeacgzxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5ZOh57O757Wx57aB5a6a77yM6LaF6YGOMTIwMOiQrOacg+WToeeahOaVuOmHj+WEquWLou+8jOiuk+iyt+izo+mbmeaWueWPquimgemWi+WVn+OAjOWFqOWutuOAjWFwcO+8jOWNs+acg+aWvOmmlumggeOAjOaIkeeahOWMheijueOAjeiZlemhr+ekuuWNs+aZguiyqOaFi+i/vei5pOOAgjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+Jm5ic3A7PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxhIG5hbWU9Il9IbGs0MTg0NTA3MiI+PC9hPjxhIG5hbWU9Il9IbGs0MTk1MDkwMSI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7jgIzlhajlrrbjgI3pgLLkuIDmraXop4Dlr5/lsI/os6PlrrbntrLot6/plovlupfnmoTnmbzlsZXmrbfnqIvvvIzpmqjokZfosqnllK7llYblk4HoiIfosrflrrbmlbjph4/lop7liqDvvIzlsIflvp7npL7nvqTlnJjos7zos6PlrrbvvIzljYfntJrngrrlvq7lnovpm7vllYbos6PlrrbvvIznlJroh7PmmK/pnIDopoHlu7rnq4vlk4HniYzlvaLosaHnmoTlk4HniYzpm7vllYbos6PlrrbjgILph53lsI3kuI3lkIzpmo7mrrXnmoTos6PlrrbplovlupfpnIDmsYLvvIzjgIzlhajlrrbjgI3lu7rnq4vliIbnnL7ljJbnmoTlubPlj7DvvI3jgIzlpb3os6PvvIvjgI3jgIHjgIzlpb3plovlupfjgI3jgIHjgIzlpb3lupfvvIvjgI3vvIzmj5DkvpvkuIDnq5nlvI/jgIHlpJrlhYPnmoTplovlupfmlrnmoYjjgII8L3NwYW4+PC9hPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7pn7/mh4nmlL/lupzmlrzlvoznlqvmg4Xpmo7mrrXntJPlm7Dlr6bpq5TlupfoiJbovYnlnovpm7vllYbntpPnh5/mlL/nrZbvvIzjgIzlhajlrrbjgI3ljbPml6Xotbfmjqjlh7rjgIzlpb3plovlupfjgI3jgIHjgIzlpb3lupfvvIvjgI3pm7vllYbplovlupflubPlj7DvvIzpoJDoqIjkuInlubTlsIfovJTlsI4x6JCs5ZCN6LOj5a6277yM5o+Q5L6b5YWN56ef6YeR44CB5YWN5oiQ5Lqk5omL57qM6LK7562J6Zu25oiQ5pys6ZaL5bqX5pyN5YuZ77yM6KOc5Yqp57i95YO55YC85pyA6auY6YGUMTDlhITlhYPjgII8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPiZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48aT48dT7lpb3os6PvvIvvvJrlhaXploDmrL7lubPlj7AmbmJzcDsgUTPlsIjlsaxBUFDkuIrnt5o8L3U+PC9pPjwvYj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48aT48dT7pganlkIjlsI3osaHvvJrnpL7nvqTlnJjos7zos6PlrrY8L3U+PC9pPjwvYj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+Jm5ic3A7PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5Y675bm0OOaciOS4iue3mueahOOAjDwvc3Bhbj7lpb3os6M8c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPu+8i+OAjeW5s+WPsO+8jOS4jeWIsOS4gOW5tDwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuW3suWQuOW8lei2hemBjjEy6JCs6LOj5a625L2/55So77yM5Lqk5piT562G5pW456qB56C0MzAw6JCs5Lu277yM57Sw56m26LOj5a626Lyq5buT77yM5aSa5Lul5Li75pS75q+N5ayw5biC5aC055qE56S+576k5ZyY6LO86LOj5a6254K65Li777yM5Y+N5oeJ5Zyo54ax6Yq35YmN5LiJ5ZCN5YiG5Yil54K655Sf5rS755So5ZOB44CB5YWS56ul5pyNPC9zcGFuPumjvuiIh+WFkuerpeeOqeWFt+OAgjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7ngrrmj5DkvpvlsI/os6PlrrbljYfntJrmnI3li5nvvIzjgIw8L3NwYW4+5aW96LOjPHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7vvIvjgI08L3NwYW4+5bCH5pa85LuK5bm056ys5LiJ5a2j5paw5aKe6LOj5a625bCI5bGsQVBQ77yM5ru/6Laz6LOj5a625YCR5L2/55So5omL5qmf5oiW6KGM5YuV6KOd572u5pmC55qE5L6/5Yip5oCn77yM6Zmk5LqG5pei5pyJ5Yqf6IO95aSW77yMQVBQ5LiK57ea5b6M5bCH5paw5aKe5o+Q6YaS6KiK5oGv5o6o5pKt44CB6LK36LOj5a626IGv57mr5Y+K6Yq35ZSu5pW45pOa5YiG5p6Q562J5Yqf6IO944CCPC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPiZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48aT48dT7lpb3plovlupfvvJrpgLLpmo7mrL7lubPlj7AgM+WIhumQmOWTgeeJjOe2suermeaQnuWumjwvdT48L2k+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxiPjxpPjx1PumBqeWQiOWwjeixoe+8mumWi+W6l+W5s+WPsOaWsOaJi+OAgeW+ruWei+mbu+WVhjwvdT48L2k+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+55W25bCP6LOj5a6257Sv56mN5pei5pyJ5a6i576k77yM6YCQ5q2l5oOz5pOB5pyJ5Yid5Ym155qE5ZOB54mM5a6Y57ay77yM6YCy6ZqO5qy+55qE44CM5aW96ZaL5bqX44CN5bmz5Y+w5bCx5piv5pyA5aW955qE5Y2H57Sa6YG45pOH77yM5bmz5Y+w5o+Q5L6b6LOj5a625pyA5L6/5o2344CB57Ch5Zau55qE6ZaL5bqX5pa55byP77yM5b6e57ay56uZ55Sz6KuL44CB6Kit5a6a57ay56uZbG9nb+OAgeeJiOWei+mBuOaTh+OAgemmlumggeS4u+WcluWIsOWVhuWTgeS4iuaetu+8jOewoeWWrjPmraXpqZ/jgIHlj6ropoEz5YiG6ZCY5Y2z5Y+v5b+r6YCf5LiK57ea44CCPC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPiZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWFtuasoe+8jDwvc3Bhbj7jgIzlpb3plovlupfjgI08c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuizo+WgtOWPr+mAj+mBjue2sui3r+aQnOWwi+W8leaTjuiiq+aJvuWIsO+8jOaTtOWkp+WVhuW6l+eahOabneWFie+8jOWinuWKoOmKt+WUruapn+acg++8m+izo+WgtOS5n+WPr+WBmuewoeaYk+eahOacg+WToee2k+eHn++8jOS+neeFp+mcgOaxguaOqOWHuuS/g+mKt+WEquaDoOa0u+WLlTwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuOAgjwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWPpuS4gOaWuemdou+8jOeCuuS6huaPkOWNh+iyt+WutuS9v+eUqOeahOS+v+WIqeaAp++8jOaPkOS+m+ioquWuouaIluacg+WToeWFqeeorueZu+WFpeaWueW8j++8jOacquS+huS5n+Wwh+mWi+eZvOS7peOAjOWFqOWutuOAjeacg+WToeW4s+iZn+aIluaYr+S4suaOpeekvue+pOW4s+iZn+ebtOaOpeeZu+WFpeS9v+eUqOOAgjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+Jm5ic3A7PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxiPjxpPjx1PuWlveW6l++8i++8muaXl+iJpuasvuW5s+WPsCBDUk3oiIfooYzpirflip/og73kuIDmh4nkv7Hlhag8L3U+PC9pPjwvYj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48aT48dT7pganlkIjlsI3osaHvvJrlr6bpq5Tlupflrrbot6jntrLot6/luILloLTjgIHlpKflnovlk4HniYzpm7vllYY8L3U+PC9pPjwvYj48L3NwYW4+PC9zcGFuPjwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+Jm5ic3A7PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+55W25bCP6LOj5a626YCQ5ry46ZW35aSn54K65pOB5pyJ6b6Q5aSn5a6i576k55qE5aSn6LOj5a6277yM5oiW5piv5a+m6auU5bqX5a625oOz6Leo6Laz57ay6Lev55qE5ZWG5a625YCR77yM5peX6Imm5qy+55qE44CM5aW95bqX77yL44CN5bmz5Y+w5bCH5Y2U5Yqp5qWt6ICF6YCy6KGMQ1JN57aT54ef77yM5o+Q5L6b5pyD5ZOh5YiG57Sa5Yi25bqm44CB5aSa5YWD6KGM6Yq35qih57WE44CB54ef6Yq35aCx6KGo5YiG5p6Q77yM5oiQ54K65q2k5bmz5Y+w55qE5LiJ5aSn5Lqu6bue5Yqf6IO944CC6LOj5a625Y+v6Ieq6KGM5bCH5YW25pyD5ZOh5YiG57Sa6Kit5a6a5YSq5oOg5pa55byP77yb5Y+m5aSW5Lmf5o+Q5L6b57ea5LiK5oqY5YO55Yi444CB57SF5Yip56mN6bue44CB57ea5LiK5rS75YuV562J6KGM6Yq35qih57WE5L6b6LOj5a625L2/55So77yb6ICM54ef6YGL5aCx6KGo5YmH5o+Q5L6b6LOj5a626Yq35ZSu44CB6KiC5Zau562J5pW45pOa5L6b54ef6YGL5L2/55So44CCPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PGI+PGk+PHU+5Lqk5piT5bmz5Y+wK+aUr+aPtOW5s+WPsDwvdT48L2k+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxiPjxpPjx1PuWFqOaWueS9jeaJk+mAoOOAjOWFqOWutuOAjeizo+WutueUn+aFi+WciDwvdT48L2k+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+6Zmk5LqG5YmN56uv5Lqk5piT5bmz5Y+w5Yqp5pS75bCP6LOj5a625LmL5aSW77yM44CM5YWo5a6244CN5pa85Y675bm06Zm457qM5LiK57ea5b6M56uv5pSv5o+05bmz5Y+w5ZCM5qij5Yqf5LiN5Y+v5rKS44CC44CM5oiR55qE5YyF6KO544CN5Yqf6IO95pa85Y675bm05bqV5LiK57ea77yM6LK36LOj6ZuZ5pa55Y+q6KaB5piv44CM5YWo5a6244CN5pyD5ZOh5L2/55So5a+E5Lu25pyN5YuZ77yM5Y2z5Y+v6YCP6YGOYXBw6aaW6aCB5Y2z5pmC5p+l6Kmi6LKo54mp5Yiw5YCJ44CB5Ye65YCJ44CB5Yiw5bqX562J6LKo5oWL77yb5Y+m5aSW44CM6LOjPHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7vvIs8L3NwYW4+6KOc57Wm56uZ44CN5YmH5piv5o+Q5L6b5YyF6KO55YKZ5ZOB57ea5LiK6LO85pyN5YuZ77yM6LOj5a625Y+v5LulPHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+Nn43PC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5oqY6LO85YWl5aSa5YWl5pW455qE5YKZ5ZOB77yM5pyq5L6G5Lmf5bCH5oyB57qM5pO05aKe5ZOB6aCF77yM5ru/6Laz6LOj5a626ZyA5rGC77yb5Y+m6Yed5bCN5pyJ5aSn6YeP5a+E6LKo6ZyA5rGC55qE6LOj5a6277yM5Lmf5bCH5o+Q5L6bPC9zcGFuPuOAjOaUtuiyqOmAmuOAjeacjeWLme+8jOmgkOioiFEz5LiK57eaPHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7jgILntbHmlbTliY3nq6/kuqTmmJPlubPlj7DoiIflvoznq6/mlK/mj7TlubPlj7DvvIzjgIzlhajlrrbjgI3nqY3mpbXmt7HogJXos6PlrrbmnI3li5nvvIzmnJ/mnJvlu7rmp4vkuIDmop3pvo3mnI3li5nnmoTjgIzos6PlrrbnlJ/mhYvlnIjjgI3jgII8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPiZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48aT48dT7mraHmhbbkuIrnt5og6ZmQ5pmC6ZmQ6aGN5YWN6YGL6LK7PC91PjwvaT48L2I+PC9zcGFuPjwvc3Bhbj48L3A+Cgo8cCBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPiZuYnNwOzwvcD4KCjxwIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPueCuuatoeaFtuaWsOW5s+WPsOS4iue3mu+8jDwvc3Bhbj7jgIzlhajlrrbjgI3mlrDplovlupflubPlj7Dnq6/lh7rpm5nph43lhKrmg6DvvIzlhKrmg6DkuIDvvJrpmZDmmYLpmZDpoY3lhY3pgYvosrvvvIzmlrw2LzExLTYvMzDmnJ/plpPlhafvvIzliY0xMOiQrOethuaWvDxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+44CMPC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5aW96ZaL5bqX44CNPC9zcGFuPuW5s+WPsOioguWWruaIkOeri+S5i+WVhuWTge+8jOWNs+WPr+S6q+acieWFjemBi+WEquaDoCjmu78xMOiQrOS7tuWNs+a0u+WLlee1kOadnynvvJvlj6blpJbjgIw8c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWlveW6l++8izwvc3Bhbj7jgI3mlrw2LzExLTYvMzDmnJ/plpPlhafvvIzliY0xLDAwMOWQjemWi+W6l+aIkOWKn+S5i+WVhuWutu+8jOavj+S9jemAgTEwMOS7tuWFjemBi+iyu++8jOWFsTEw6JCs5Lu2KOmcgOaWvDEwOS84LzMx5LmL5YmN5L2/55So5a6M55WiKe+8m+WEquaDoOS6jO+8muWNs+aXpei1t+iHszYvMzDnq6/lh7rnianmtYHlhKrmg6Dlg7nvvIzjgIzlpb3os6PvvIvjgI3mr4/ku7blhKrmg6Dlg7kzOeWFg+OAgeOAjOWlvemWi+W6l+OAjeWPiuOAjOWlveW6l++8i+OAjeWJh+aOqOWHuuavj+S7tjQ8c3BhbiBsYW5nPSJFTi1VUyIgc3R5bGU9ImNvbG9yOmJsYWNrIj45PC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWD5YSq5oOg5YO544CCPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoKPHAgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij4mbmJzcDs8L3A+Cgo8b2wgc3RhcnQ9IjEyIiBzdHlsZT0ibGlzdC1zdHlsZS10eXBlOmxvd2VyLWFscGhhIj4KCTxsaSBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQgMjRwdCIgdmFsdWU9IjUwIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWo5a626ZaL5bqX5bmz5Y+w5LuL57S5PC9zcGFuPjwvc3Bhbj48L2I+PC9zcGFuPjwvc3Bhbj4KCgk8dWw+CgkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPuWlveizozwvc3Bhbj48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPu+8i++8mjwvc3Bhbj48L3NwYW4+PGEgaHJlZj0iaHR0cHM6Ly9mYW1pc3RvcmUuZmFtaXBvcnQuY29tLnR3L2ZhbWlzdG9yZS8iIHN0eWxlPSJjb2xvcjojMDU2M2MxOyB0ZXh0LWRlY29yYXRpb246dW5kZXJsaW5lIj5odHRwczovL2ZhbWlzdG9yZS5mYW1pcG9ydC5jb20udHcvZmFtaXN0b3JlLzwvYT48L3NwYW4+PC9zcGFuPjwvbGk+CgkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPuWlvemWi+W6l++8mjwvc3Bhbj48YSBocmVmPSJodHRwczovL2ZhbWlzaG9wLmZhbWkubGlmZS8iIHN0eWxlPSJjb2xvcjojMDU2M2MxOyB0ZXh0LWRlY29yYXRpb246dW5kZXJsaW5lIiB0YXJnZXQ9Il9ibGFuayI+aHR0cHM6Ly9mYW1pc2hvcC5mYW1pLmxpZmUvPC9hPjwvc3Bhbj48L3NwYW4+PC9saT4KCQk8bGkgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0IDI0cHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OkNhbGlicmksc2Fucy1zZXJpZiI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+5aW95bqXPC9zcGFuPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+77yL77yaPC9zcGFuPjwvc3Bhbj48YSBocmVmPSJodHRwczovL2hhb3N0b3JlLmZhbWkubGlmZS9oYW9zdG9yZS8iIHN0eWxlPSJjb2xvcjojMDU2M2MxOyB0ZXh0LWRlY29yYXRpb246dW5kZXJsaW5lIj5odHRwczovL2hhb3N0b3JlLmZhbWkubGlmZS9oYW9zdG9yZS88L2E+PC9zcGFuPjwvc3Bhbj48L2xpPgoJPC91bD4KCTwvbGk+Cjwvb2w+Cgo8cCBzdHlsZT0ibWFyZ2luLWxlZnQ6NDIuMHB0OyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij4mbmJzcDs8L3A+Cgo8dGFibGUgY2xhc3M9Ik1zb1RhYmxlR3JpZCIgc3R5bGU9ImJvcmRlci1jb2xsYXBzZTpjb2xsYXBzZTsgYm9yZGVyOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQiPgoJPHRib2R5PgoJCTx0cj4KCQkJPHRkIGNvbHNwYW49IjIiIHN0eWxlPSJib3JkZXI6c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6OTEuOXB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSIxMjMiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5bmz5Y+wPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlcjpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo5Mi4xNXB0OyBib3JkZXItbGVmdDpub25lOyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHZhbGlnbj0idG9wIiB3aWR0aD0iMTIzIj4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj7lpb3os6M8c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPu+8izwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXI6c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6NC4wY207IGJvcmRlci1sZWZ0Om5vbmU7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgdmFsaWduPSJ0b3AiIHdpZHRoPSIxNTEiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5aW96ZaL5bqXPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlcjpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDoxMTcuMzVwdDsgYm9yZGVyLWxlZnQ6bm9uZTsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjE1NiI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+5aW95bqXPHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7vvIs8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJPC90cj4KCQk8dHI+CgkJCTx0ZCBjb2xzcGFuPSIyIiBzdHlsZT0iYm9yZGVyOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjkxLjlwdDsgYm9yZGVyLXRvcDpub25lOyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSIxMjMiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5a6a5L2NPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6OTIuMTVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjEyMyI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+5YWl6ZaA5qy+5bmz5Y+wPC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo0LjBjbTsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjE1MSI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+6YCy6ZqO5qy+5bmz5Y+wPC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDoxMTcuMzVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjE1NiI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+5peX6Imm5qy+5bmz5Y+wPC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJPC90cj4KCQk8dHI+CgkJCTx0ZCBjb2xzcGFuPSIyIiBzdHlsZT0iYm9yZGVyOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjkxLjlwdDsgYm9yZGVyLXRvcDpub25lOyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSIxMjMiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+6YGp5ZCI5bCN6LGhPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6OTIuMTVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjEyMyI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PGI+PHU+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7npL7nvqTlnJjos7zos6PlrrY8L3NwYW4+PC91PjwvYj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuS7peekvue+pOWcmOizvOeCuuS4u+imgemKt+WUrueuoemBkzwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjQuMGNtOyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHZhbGlnbj0idG9wIiB3aWR0aD0iMTUxIj4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48dT48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuW+ruWei+mbu+WVhuizo+Wutjwvc3Bhbj48L3U+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj7ntK/nqY3lrqLnvqTvvIzmg7Pmk4HmnInliJ3libXnmoTpm7vllYbos6PloLQ8L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjExNy4zNXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHZhbGlnbj0idG9wIiB3aWR0aD0iMTU2Ij4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48Yj48dT48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWTgeeJjOmbu+WVhuizo+Wutjwvc3Bhbj48L3U+PC9iPjwvc3Bhbj48L3NwYW4+PC9wPgoKCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuaTgeaciem+kOWkp+Wuoue+pOeahOWkp+izo+WutuOAgeWvpumrlOW6l+Wutui3qOi2s+e2sui3rzwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQk8L3RyPgoJCTx0cj4KCQkJPHRkIGNvbHNwYW49IjIiIHN0eWxlPSJib3JkZXI6c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6OTEuOXB0OyBib3JkZXItdG9wOm5vbmU7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgd2lkdGg9IjEyMyI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7plovlupfosrvnlKg8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBjb2xzcGFuPSIzIiBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDozMjIuOXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSI0MzEiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWN56ef6YeR44CB5YWN5oiQ5Lqk5omL57qM6LK7PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCTwvdHI+CgkJPHRyIHN0eWxlPSJoZWlnaHQ6MzQuMnB0Ij4KCQkJPHRkIHJvd3NwYW49IjMiIHN0eWxlPSJib3JkZXI6c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6NDkuNHB0OyBib3JkZXItdG9wOm5vbmU7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdDsgaGVpZ2h0OjM0LjJwdCIgd2lkdGg9IjY2Ij4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPumHkea1gTwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjQyLjVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0OyBoZWlnaHQ6MzQuMnB0IiB3aWR0aD0iNTciPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWo5a625Y+W6LKo5LuY5qy+PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6OTIuMTVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0OyBoZWlnaHQ6MzQuMnB0IiB3aWR0aD0iMTIzIj4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBsYW5nPSJFTi1VUyIgc3R5bGU9ImNvbG9yOmJsYWNrIj5WPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6NC4wY207IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdDsgaGVpZ2h0OjM0LjJwdCIgd2lkdGg9IjE1MSI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+Vjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjExNy4zNXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQ7IGhlaWdodDozNC4ycHQiIHdpZHRoPSIxNTYiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPlY8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJPC90cj4KCQk8dHI+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo0Mi41cHQ7IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgd2lkdGg9IjU3Ij4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuS7o+eivOe5s+iyuzwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjkyLjE1cHQ7IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgd2lkdGg9IjEyMyI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+Vjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjQuMGNtOyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSIxNTEiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTEuMHB0Ij48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPumZuOe6jOS4iue3mjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDoxMTcuMzVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB3aWR0aD0iMTU2Ij4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOjExLjBwdCI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7pmbjnuozkuIrnt5o8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCTwvdHI+CgkJPHRyPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6NDIuNXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSI1NyI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7nt5rkuIrliLfljaE8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo5Mi4xNXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSIxMjMiPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPlY8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo0LjBjbTsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB3aWR0aD0iMTUxIj4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOjExLjBwdCI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7pmbjnuozkuIrnt5o8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6MTE3LjM1cHQ7IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgd2lkdGg9IjE1NiI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+Vjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQk8L3RyPgoJCTx0cj4KCQkJPHRkIHN0eWxlPSJib3JkZXI6c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6NDkuNHB0OyBib3JkZXItdG9wOm5vbmU7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgd2lkdGg9IjY2Ij4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPueJqea1gTwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjQyLjVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB3aWR0aD0iNTciPgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWo5a625bqX5Yiw5bqXPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6OTIuMTVwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjEyMyI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+Ni8zMDwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWJjeWEquaDoOWDuTM55YWDL+S7tjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+KDwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWOn+WDuTYw5YWDKTwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjQuMGNtOyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHZhbGlnbj0idG9wIiB3aWR0aD0iMTUxIj4KCQkJPG9sPgoJCQkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij42LzExLTYvMzA8L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7vvIzliY08L3NwYW4+PC9zcGFuPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPjEwPC9zcGFuPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+6JCs562G6KiC5Zau5oiQ56uL5Y2z5Y+v5Lqr5pyJ5YWN6YGL5YSq5oOgPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvbGk+CgkJCQk8bGkgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0IDI0cHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OkNhbGlicmksc2Fucy1zZXJpZiI+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+Ni8zMDwvc3Bhbj48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWJjeWEquaDoOWDuTwvc3Bhbj48L3NwYW4+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+NDk8L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7lhYM8L3NwYW4+PC9zcGFuPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPi88L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7ku7Y8L3NwYW4+PC9zcGFuPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPig8L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7ljp/lg7k8L3NwYW4+PC9zcGFuPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPjYwPC9zcGFuPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWDPC9zcGFuPjwvc3Bhbj48c3BhbiBsYW5nPSJFTi1VUyIgc3R5bGU9ImNvbG9yOmJsYWNrIj4pPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9saT4KCQkJPC9vbD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjExNy4zNXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHZhbGlnbj0idG9wIiB3aWR0aD0iMTU2Ij4KCQkJPG9sPgoJCQkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij42LzExLTYvMzA8L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+77yM5YmNMSwwMDDlkI3plovlupfllYblrrbvvIzmr4/kvY3pgIExMDDku7blhY3pgYvosrs8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L2xpPgoJCQkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPjYvMzA8L3NwYW4+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7liY3lhKrmg6Dlg7k8L3NwYW4+PC9zcGFuPjxzcGFuIGxhbmc9IkVOLVVTIiBzdHlsZT0iY29sb3I6YmxhY2siPjQ5PC9zcGFuPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5YWDPC9zcGFuPjwvc3Bhbj48c3BhbiBsYW5nPSJFTi1VUyIgc3R5bGU9ImNvbG9yOmJsYWNrIj4vPC9zcGFuPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5Lu2PC9zcGFuPjwvc3Bhbj48c3BhbiBsYW5nPSJFTi1VUyIgc3R5bGU9ImNvbG9yOmJsYWNrIj4oPC9zcGFuPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5Y6f5YO5PC9zcGFuPjwvc3Bhbj48c3BhbiBsYW5nPSJFTi1VUyIgc3R5bGU9ImNvbG9yOmJsYWNrIj42MDwvc3Bhbj48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuWFgzwvc3Bhbj48L3NwYW4+PHNwYW4gbGFuZz0iRU4tVVMiIHN0eWxlPSJjb2xvcjpibGFjayI+KTwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvbGk+CgkJCTwvb2w+CgkJCTwvdGQ+CgkJPC90cj4KCQk8dHI+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjQ5LjRwdDsgYm9yZGVyLXRvcDpub25lOyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHdpZHRoPSI2NiI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7os4foqIrmtYE8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgkJCTwvdGQ+CgkJCTx0ZCBzdHlsZT0iYm9yZGVyLWJvdHRvbTpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo0Mi41cHQ7IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgd2lkdGg9IjU3Ij4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+Jm5ic3A7PC9wPgoJCQk8L3RkPgoJCQk8dGQgY29sc3Bhbj0iMyIgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6MzIyLjlwdDsgYm9yZGVyLXRvcDpub25lOyBib3JkZXItbGVmdDpub25lOyBib3JkZXItcmlnaHQ6c29saWQgd2luZG93dGV4dCAxLjBwdDsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB2YWxpZ249InRvcCIgd2lkdGg9IjQzMSI+CgkJCTxwIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJ0ZXh0LWFsaWduOmNlbnRlcjsgbWFyZ2luOjBjbSAwY20gMC4wMDAxcHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OuaWsOe0sOaYjumrlCxzZXJpZiI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7osrfos6Ppm5nmlrnoi6XngrrjgIzlhajlrrbjgI3mnIPlk6HvvIw8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3A+CgoJCQk8cCBhbGlnbj0iY2VudGVyIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IG1hcmdpbjowY20gMGNtIDAuMDAwMXB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTrmlrDntLDmmI7pq5Qsc2VyaWYiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5Y+v5pa844CM5oiR55qE5YyF6KO544CN5p+l6KiK5YyF6KO56LKo5oWLPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9wPgoJCQk8L3RkPgoJCTwvdHI+CgkJPHRyPgoJCQk8dGQgY29sc3Bhbj0iMiIgc3R5bGU9ImJvcmRlcjpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyB3aWR0aDo5MS45cHQ7IGJvcmRlci10b3A6bm9uZTsgcGFkZGluZzowY20gNS40cHQgMGNtIDUuNHB0IiB3aWR0aD0iMTIzIj4KCQkJPHAgYWxpZ249ImNlbnRlciIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyOyBtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk65paw57Sw5piO6auULHNlcmlmIj48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPueJueiJsjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvcD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjkyLjE1cHQ7IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgdmFsaWduPSJ0b3AiIHdpZHRoPSIxMjMiPgoJCQk8dWw+CgkJCQk8bGkgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0IDI0cHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OkNhbGlicmksc2Fucy1zZXJpZiI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7nsKHmmJPlibXmpa3lubPlj7DvvIzllYblk4Hlj6/ljbPmmYLkuIrmnrbjgIHliIbkuqvpgKPntZDoh7PnpL7nvqTlubPlj7A8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9saT4KCQkJCTxsaSBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQgMjRwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6Q2FsaWJyaSxzYW5zLXNlcmlmIj48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPuiyt+izo+mbmeaWueeCuuOAjOWFqOWutuOAjeacg+WToTwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvc3Bhbj48L2xpPgoJCQk8L3VsPgoJCQk8L3RkPgoJCQk8dGQgc3R5bGU9ImJvcmRlci1ib3R0b206c29saWQgd2luZG93dGV4dCAxLjBwdDsgd2lkdGg6NC4wY207IGJvcmRlci10b3A6bm9uZTsgYm9yZGVyLWxlZnQ6bm9uZTsgYm9yZGVyLXJpZ2h0OnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHBhZGRpbmc6MGNtIDUuNHB0IDBjbSA1LjRwdCIgdmFsaWduPSJ0b3AiIHdpZHRoPSIxNTEiPgoJCQk8dWw+CgkJCQk8bGkgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0IDI0cHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OkNhbGlicmksc2Fucy1zZXJpZiI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+57Ch5ZauM+atpempn++8jDPliIbpkJjplovlupc8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L2xpPgoJCQk8L3VsPgoKCQkJPHVsPgoJCQkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPuizo+WgtOWPr+iiq+aQnOWwi+OAgeiyt+WutuWinuWKoOioquWuoui6q+WIhu+8jOaTtOWkp+Wuoue+pOinuOWPiuaApzwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvbGk+CgkJCQk8bGkgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0IDI0cHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OkNhbGlicmksc2Fucy1zZXJpZiI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+5Yid5q2l5pyD5ZOh57aT54ef77yM5o+Q5L6b5L+D6Yq357WE5ZCI5bel5YW3PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9saT4KCQkJPC91bD4KCQkJPC90ZD4KCQkJPHRkIHN0eWxlPSJib3JkZXItYm90dG9tOnNvbGlkIHdpbmRvd3RleHQgMS4wcHQ7IHdpZHRoOjExNy4zNXB0OyBib3JkZXItdG9wOm5vbmU7IGJvcmRlci1sZWZ0Om5vbmU7IGJvcmRlci1yaWdodDpzb2xpZCB3aW5kb3d0ZXh0IDEuMHB0OyBwYWRkaW5nOjBjbSA1LjRwdCAwY20gNS40cHQiIHZhbGlnbj0idG9wIiB3aWR0aD0iMTU2Ij4KCQkJPHVsPgoJCQkJPGxpIHN0eWxlPSJtYXJnaW46MGNtIDBjbSAwLjAwMDFwdCAyNHB0Ij48c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHQiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTpDYWxpYnJpLHNhbnMtc2VyaWYiPjxzcGFuIHN0eWxlPSJmb250LWZhbWlseTomcXVvdDvmlrDntLDmmI7pq5QmcXVvdDssJnF1b3Q7c2VyaWYmcXVvdDsiPjxzcGFuIHN0eWxlPSJjb2xvcjpibGFjayI+5pyD5ZOh5YiG57Sa566h55CGPC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvbGk+CgkJCQk8bGkgc3R5bGU9Im1hcmdpbjowY20gMGNtIDAuMDAwMXB0IDI0cHQiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6MTJwdCI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OkNhbGlicmksc2Fucy1zZXJpZiI+PHNwYW4gc3R5bGU9ImZvbnQtZmFtaWx5OiZxdW90O+aWsOe0sOaYjumrlCZxdW90OywmcXVvdDtzZXJpZiZxdW90OyI+PHNwYW4gc3R5bGU9ImNvbG9yOmJsYWNrIj7lpJrlhYPooYzpirfmqKHntYQ8L3NwYW4+PC9zcGFuPjwvc3Bhbj48L3NwYW4+PC9saT4KCQkJCTxsaSBzdHlsZT0ibWFyZ2luOjBjbSAwY20gMC4wMDAxcHQgMjRwdCI+PHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB0Ij48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6Q2FsaWJyaSxzYW5zLXNlcmlmIj48c3BhbiBzdHlsZT0iZm9udC1mYW1pbHk6JnF1b3Q75paw57Sw5piO6auUJnF1b3Q7LCZxdW90O3NlcmlmJnF1b3Q7Ij48c3BhbiBzdHlsZT0iY29sb3I6YmxhY2siPueHn+mKt+WgseihqOWIhuaekDwvc3Bhbj48L3NwYW4+PC9zcGFuPjwvc3Bhbj48L2xpPgoJCQk8L3VsPgoJCQk8L3RkPgoJCTwvdHI+Cgk8L3Rib2R5Pgo8L3RhYmxlPgoKPHA+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PC9wPmRkAgUPFgIeC18hSXRlbUNvdW50AhMWJmYPZBYCZg8VAwAEMjAyNgQyMDI2ZAIBD2QWAmYPFQMABDIwMjUEMjAyNWQCAg9kFgJmDxUDAAQyMDI0BDIwMjRkAgMPZBYCZg8VAwAEMjAyMwQyMDIzZAIED2QWAmYPFQMABDIwMjIEMjAyMmQCBQ9kFgJmDxUDAAQyMDIxBDIwMjFkAgYPZBYCZg8VAwZhY3RpdmUEMjAyMAQyMDIwZAIHD2QWAmYPFQMABDIwMTkEMjAxOWQCCA9kFgJmDxUDAAQyMDE4BDIwMThkAgkPZBYCZg8VAwAEMjAxNwQyMDE3ZAIKD2QWAmYPFQMABDIwMTYEMjAxNmQCCw9kFgJmDxUDAAQyMDE1BDIwMTVkAgwPZBYCZg8VAwAEMjAxNAQyMDE0ZAIND2QWAmYPFQMABDIwMTMEMjAxM2QCDg9kFgJmDxUDAAQyMDEyBDIwMTJkAg8PZBYCZg8VAwAEMjAxMQQyMDExZAIQD2QWAmYPFQMABDIwMTAEMjAxMGQCEQ9kFgJmDxUDAAQyMDA5BDIwMDlkAhIPZBYCZg8VAwAEMjAwOAQyMDA4ZGSNO+jxygkhUevlWlp5lHbLqV8hAw==" />
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


<script src="/Web_EnterPrise/WebResource.axd?d=d8ymoA_QprkrkGdufpEW_IJWAgkiFs3iwaxHiFHijqwyiOvblUl7rpLe9oNlEJIHWIGwaXkChcqnyq1rEd5zwxpcxoU1&amp;t=639191805418915853" type="text/javascript"></script>


<script src="/Web_EnterPrise/ScriptResource.axd?d=047F5LsRjw9traQW3pDCsOVqNJ8Vlc3kqBkBe_PwU2nfZSNL6fKK-xpzXXyapkjcZ1JLTX279zhLKST1U5V7-O-lzvXSO6GWfpOhBmAqnlE8y2phHK05WKsinFNaTsnPGfRCJw2&amp;t=ffffffffba82e54e" type="text/javascript"></script>
<script src="/Web_EnterPrise/ScriptResource.axd?d=fOC2mN7HV0wJyW32xt9-2nVf4xJOU1gPzjGEm0Ic5bLwFX60jDZuqz1-ijse_rx50LWsHWtlDh4wCcHAG74igg355rJ4tEQPvQYW28CR1BVbadbtQD0785crR9Wsiq4w4OBqbA2&amp;t=ffffffffba82e54e" type="text/javascript"></script>
<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="39673AF0" />
</div>
    <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ToolkitScriptManager1', document.getElementById('aspnetForm'));
Sys.WebForms.PageRequestManager.getInstance()._updateControls([], [], [], 90);
//]]>
</script>

    <div>
        <!--Top-->
        <div id="gotop">
            Top</div>
        <div class="mainContainer sixteen container">
            <!--Header Block-->
            <div class="header-wrapper">
                <header class="container">
      <div class="row" style="margin: 0;position: relative">
        <div class="head-right" style="text-align: right;"> 			
			<div class="row">		
				<div class="col-md-12">
					<ol class="breadcrumb top-link2" style="font-size:12px;">
					  <li><a href="https://www.family.com.tw/marketing/inquiry.aspx"><i class="fa fa-home" aria-hidden="true" style="font-size:11pt;"></i>店數:<span id="ctl00_LabCount">4506</span></a></li>
					  <li><a href="http://www.family.com.tw/Web_EnterPrise/page/NewsContent_en.aspx?ID=696" id="ctl00_aURL"><i class="fas fa-globe" aria-hidden="true" style="font-size:11pt;"></i>English</a></li>
					</ol>

				</div>
			</div>
        </div>
      </div>
      <!--PC-->
      <div class="row hidden-sm hidden-xs">
        <div class="col-md-12" style="padding: 0px;">
          <div class="logo col-lg-6"><a href="index.aspx" title="Logo"> <img title="Logo" alt="Logo" src="../images/logo_2024.png" /><span class="divider"></span><span class="logo-text">投資人關係</span></a></div>
          <div class="col-lg-6 text-right " style="float:right;padding: 25px 0 0 0;">
            <div class="btn-group">
				<button type="button" class="btn-drop" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">更多全家<span class="caret"></span></button>
			<ul class="dropdown-menu">
              <li><a href="https://www.family.com.tw/marketing/" target="_blank">全家首頁</a></li>
              <li><a href="https://www.family.com.tw/ESG/" target="_blank">企業永續</a></li>
              <li><a href="https://www.family.com.tw/Web_Franchise/page/index.aspx" target="_blank">加盟網站</a></li>
              <li><a href="https://hrrecruit.family.com.tw/" target="_blank">人力資源</a></li>
              <li><a href="https://www.family.com.tw/enterprise/mall/" target="_blank">全家商場</a></li>
            </ul>
				</div>
          </div>
        </div>
      </div>
		
      <!--Mobile-->
      <div class="row hidden-md hidden-lg">
        <div class="col-lg-3 cis" ><a href="index.aspx" title="Logo" > <img class="logo-pc" title="Logo" alt="Logo" src="../images/logo.png" /><img class="logo-m" title="Logo" alt="Logo" src="../images/logo-m_2024.png" /><span class="divider-m"></span><span class="logo-text-m">投資人關係</span></a></div>
        <div class="col-lg-6 text-right col-lg-6-more" style="float:right;padding: 25px 0 0 0;">
         <div class="btn-group">
				<button type="button" class="btn-drop" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">更多全家<span class="caret"></span></button>
			<ul class="dropdown-menu">
              <li><a href="https://www.family.com.tw/marketing/" target="_blank">全家首頁</a></li>
              <li><a href="https://www.family.com.tw/ESG/" target="_blank">企業永續</a></li>
              <li><a href="https://www.family.com.tw/Web_Franchise/page/index.aspx" target="_blank">加盟網站</a></li>
              <li><a href="https://hrrecruit.family.com.tw/" target="_blank">人力資源</a></li>
              <li><a href="https://www.family.com.tw/enterprise/mall/" target="_blank">全家商場</a></li>
            </ul>
				</div>
        </div>
      </div>
      <nav id="smoothmenu1" class="ddsmoothmenu mainMenu">
        <ul id="nav">
			<li id="li1" class="" ><a href="index.aspx"  title="首頁">首頁</a>
            </li>
			<li id="li2" class="" ><a href="aboutus.aspx"  title="關於全家" >關於全家</a>
            <ul>
              <li><a href="information.aspx" style="border-color:#cccccc;border:1px; float:left">公司資訊</a></li>
              <li><a href="business.aspx" style="border-color:#cccccc;">品牌願景與經營理念</a></li>
              <li><a href="operations.aspx" style="border-color:#cccccc;border:1px; float:left">營運績效</a></li>
              <li><a href="advantage.aspx" style="border-color:#cccccc;">經營優勢</a></li>
              <li><a href="people_service.aspx" style="border-color:#cccccc;border:1px; float:left">有故事的全家人</a></li>
              <li><a href="introduction.aspx" style="border-color:#cccccc">業務及商品介紹</a></li>
            </ul>
            </li>
            <li id="li3" class=""><a href="invest.aspx"  title="投資人專區">投資人專區</a>
            <ul>
              <li><a href="directors.aspx" style="border-color:#cccccc;border:1px">公司治理</a></li>
              <li><a href="invest_finance.aspx" style="border-color:#cccccc;">財務資訊</a></li>
              <li><a href="material.aspx" style="border-color:#cccccc;border:1px">股東訊息</a></li>
            </ul>
            </li>
            <li id="li4" class=""><a href="https://www.family.com.tw/ESG/" target="_blank" title="ESG">企業永續</a></li>
            <li id="li5" class=""><a href="https://www.family.com.tw/ESG/Newslist" target="_blank" title="NEWS">最新消息</a></li>
            <li id="li6" class=""><a href="contact_us.aspx" title="contact">利害關係人專區</a></li>
            <li class="col-xs-3 text-left" style="padding-top:25px;">
			  <div class="list-inline top-link link">				
			   <input id="txt1" type="text"  onkeydown="fouceClick1();" placeholder="Search" />								
			    &nbsp;
			   <button id="btn1" class="glyphicon" style="padding: 4px;border: none;border-radius: 4px;background-color: snow;" type="button" onclick="SearchURL1();">
			    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
			   </button>
			  </div>
          </li>
        </ul>
      </nav>
      <div class="mobMenu">
        <h1> <span>Menu</span> <a class="menuBox highlight" href="javascript:void(0);">ccc</a> <span class="clearfix"></span> </h1>
        <div id="menuInnner" style="display:none;">
          <ul class="accordion">
			<li class=""><a href="index.aspx" title="首頁">首頁</a></li>
            <li class="parent"><a href="aboutus.aspx" title="about">關於全家</a>
              <ul>
                <li><a href="Information.aspx">公司資訊</a></li>
                <li><a href="business.aspx">品牌願景與經營理念</a></li>
                <li><a href="operations.aspx">營運績效</a></li>
                <li><a href="advantage.aspx">經營優勢</a></li>
                <li><a href="people_service.aspx">有故事的全家人</a></li>
				<li><a href="introduction.aspx">業務及商品介紹</a></li>
              </ul>
            </li>
            <li class="parent"><a href="invest.aspx" title="投資人專區">投資人專區</a>
              <ul>
                <li><a href="directors.aspx">公司治理</a></li>
                <li><a href="invest_finance.aspx">財務資訊</a></li>
                <li><a href="material.aspx">股東訊息</a></li>
              </ul>
            </li>
            <li class=""><a href="https://www.family.com.tw/ESG/" target="_blank" title="ESG">企業永續</a></li>
            <li class=""><a href="https://www.family.com.tw/ESG/Newslist" target="_blank" title="NEWS">最新消息</a></li>
            <li class=""><a href="contact_us.aspx" title="contact">利害關係人專區</a></li>
			 <li class="parent more"><a href="#" title="more">更多全家</a>
              <ul>
                <li><a href="https://www.family.com.tw/marketing/" target="_blank">全家首頁</a></li>
                <li><a href="https://www.family.com.tw/ESG/" target="_blank">企業永續</a></li>
                <li><a href="https://www.family.com.tw/Web_Franchise/page/index.aspx" target="_blank">加盟網站</a></li>
                <li><a href="https://hrrecruit.family.com.tw/" target="_blank">人力資源</a></li>
                <li><a href="https://www.family.com.tw/enterprise/mall/" target="_blank">全家商場</a></li>
              </ul>
            </li>
            <span class="clearfix"></span>
            
            <li><a class="btn btn-lg show-layer" data-show-layer="hw-layer" role="button" style="border-radius: 0" aria-hidden="true">
                <input id="txt2" type="text"  onkeydown="fouceClick2();" placeholder="Search" />						
								&nbsp;
				<button id="btn2" class="glyphicon" style="padding: 4px;border: none;border-radius: 4px;background-color: snow;" type="button" onclick="SearchURL2();">
				<span class="glyphicon glyphicon-search" aria-hidden="true"></span>
				</button>
                </a></li>
          </ul>
        </div>
      </div>
    </header>
            </div>
            
        <!--變更按鈕背景色展開-->

        <script type="text/javascript">
            $('#li5').attr('class', 'active');
        </script>

        <!--變更按鈕背景色展開 END-->
        <!--------------Content--------------->
        <div class="top_img">
            <img src="../images/banner03.jpg" class="thumbnail">
        </div>
        <h1 class="page-title">
            <i class="glyphicon glyphicon-bullhorn"></i>最新消息
        </h1>
        <hr class="hr">
        <div id="content">
            <div class="wrap-content zerogrid">
                <div style="width: 100%">
                    <div id="main-content" class="col-3-4">
                        <div class="wrap-col">
                            <div class="col-lg-offset-0 col-lg-12">
                                <div class="heading">
                                    <h4>
                                        <span id="ctl00_ContentPlaceHolder1_Labtitle">「全家」創分眾化電商開店平台 助攻小賣家升級</span>
                                    </h4>
                                    <!--<h3>跨店取、分次領，買多更優惠</h3>-->
                                    <hr class="hr">
                                    <div class="editor">
                                        <span id="ctl00_ContentPlaceHolder1_LabContent"><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">社群電商、網紅經濟當道，應運而生眾多可自帶流量的個人化賣家。瞄準新電商時代來臨，全家便利商店打造全新零成本、分眾化的開店平台─「好開店」、「好店＋」，主打line好友圈、Facebook社團、直播頻道上的小賣家，滿足運營階段不同的開店需求，從基礎的金流、物流、資訊流整合服務外，到三分鐘品牌官網建置、CRM經營分析、行銷活動模組等功能一應俱全，更祭出免租金、免成交手續費，預計三年將助攻1萬家商家，補助總價值高達10億元。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">「全家」</span>去年推出「好賣<span style="color:black">＋」C2C</span>電商平台以來，<span style="color:black">不到一年共吸引12萬賣家、開設超過30萬個賣場。「全家」E-Retail事業部部長王啟丞表示，</span><span style="color:black">後疫情時代進一步加溫網購市場，預估</span><span style="color:black">「好開店」、「好店＋」雙平台上線後，三大自有平台EC件比例將有望一舉推升、佔整體三成</span>。此外，為打造全方位的賣家生態圈，陸續針對賣家痛點，推出「我的包裹」(app即時貨態查詢)、「賣<span style="color:black">＋</span>補給站」(包材備品線上購)、「收貨通」(大單到府收件)等配套功能，提供從前台交易介面到後台支援系統的一條龍服務。</span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>「全家」善用「三流服務」 打造一站式網路開店平台</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>好賣＋、好開店、好店＋ 三箭齊發助攻小賣家零成本升級</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">根據「全家」內部資料發現，以拍賣類型為主的C2C交易件數占整<span style="color:black">體店取包裹7成以上，</span>且此類賣家數有逐年成長的趨勢，顯示C2C電商時代來臨。</span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">王啟丞指出，<span style="color:black">「全家」長期扮演EC包裹最後一哩路，近年則進一步運用既有優勢，跨足平台經濟，開設「</span>好賣<span style="color:black">＋」，提供社群賣家簡易的接單平台，</span><a name="_Hlk41837637">金流、物流、資訊流</a>相互整合的「三流服務」。金流部分，提供賣家多元的付款方式與帳務串接的查詢與彙整；物流則是整合全台超過3,600家店舖優勢，全台皆可寄取件；資訊流則與「全家」會<span style="color:black">員系統綁定，超過1200萬會員的數量優勢，讓買賣雙方只要開啟「全家」app，即會於首頁「我的包裹」處顯示即時貨態追蹤。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><a name="_Hlk41845072"></a><a name="_Hlk41950901"><span style="color:black">「全家」進一步觀察小賣家網路開店的發展歷程，隨著販售商品與買家數量增加，將從社群團購賣家，升級為微型電商賣家，甚至是需要建立品牌形象的品牌電商賣家。針對不同階段的賣家開店需求，「全家」建立分眾化的平台－「好賣＋」、「好開店」、「好店＋」，提供一站式、多元的開店方案。</span></a></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">響應政府於後疫情階段紓困實體店舖轉型電商經營政策，「全家」即日起推出「好開店」、「好店＋」電商開店平台，預計三年將輔導1萬名賣家，提供免租金、免成交手續費等零成本開店服務，補助總價值最高達10億元。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>好賣＋：入門款平台&nbsp; Q3專屬APP上線</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>適合對象：社群團購賣家</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">去年8月上線的「</span>好賣<span style="color:black">＋」平台，不到一年</span><span style="color:black">已吸引超過12萬賣家使用，交易筆數突破300萬件，細究賣家輪廓，多以主攻母嬰市場的社群團購賣家為主，反應在熱銷前三名分別為生活用品、兒童服</span>飾與兒童玩具。</span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">為提供小賣家升級服務，「</span>好賣<span style="color:black">＋」</span>將於今年第三季新增賣家專屬APP，滿足賣家們使用手機或行動裝置時的便利性，除了既有功能外，APP上線後將新增提醒訊息推播、買賣家聯繫及銷售數據分析等功能。</span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>好開店：進階款平台 3分鐘品牌網站搞定</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>適合對象：開店平台新手、微型電商</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">當小賣家累積既有客群，逐步想擁有初創的品牌官網，進階款的「好開店」平台就是最好的升級選擇，平台提供賣家最便捷、簡單的開店方式，從網站申請、設定網站logo、版型選擇、首頁主圖到商品上架，簡單3步驟、只要3分鐘即可快速上線。</span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">其次，</span>「好開店」<span style="color:black">賣場可透過網路搜尋引擎被找到，擴大商店的曝光，增加銷售機會；賣場也可做簡易的會員經營，依照需求推出促銷優惠活動</span><span style="color:black">。</span><span style="color:black">另一方面，為了提升買家使用的便利性，提供訪客或會員兩種登入方式，未來也將開發以「全家」會員帳號或是串接社群帳號直接登入使用。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>好店＋：旗艦款平台 CRM與行銷功能一應俱全</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>適合對象：實體店家跨網路市場、大型品牌電商</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">當小賣家逐漸長大為擁有龐大客群的大賣家，或是實體店家想跨足網路的商家們，旗艦款的「好店＋」平台將協助業者進行CRM經營，提供會員分級制度、多元行銷模組、營銷報表分析，成為此平台的三大亮點功能。賣家可自行將其會員分級設定優惠方式；另外也提供線上折價券、紅利積點、線上活動等行銷模組供賣家使用；而營運報表則提供賣家銷售、訂單等數據供營運使用。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>交易平台+支援平台</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>全方位打造「全家」賣家生態圈</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">除了前端交易平台助攻小賣家之外，「全家」於去年陸續上線後端支援平台同樣功不可沒。「我的包裹」功能於去年底上線，買賣雙方只要是「全家」會員使用寄件服務，即可透過app首頁即時查詢貨物到倉、出倉、到店等貨態；另外「賣<span style="color:black">＋</span>補給站」則是提供包裹備品線上購服務，賣家可以<span lang="EN-US" style="color:black">6~7</span><span style="color:black">折購入多入數的備品，未來也將持續擴增品項，滿足賣家需求；另針對有大量寄貨需求的賣家，也將提供</span>「收貨通」服務，預計Q3上線<span style="color:black">。統整前端交易平台與後端支援平台，「全家」積極深耕賣家服務，期望建構一條龍服務的「賣家生態圈」。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><i><u>歡慶上線 限時限額免運費</u></i></b></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<p style="margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">為歡慶新平台上線，</span>「全家」新開店平台端出雙重優惠，優惠一：限時限額免運費，於6/11-6/30期間內，前10萬筆於<span style="color:black">「</span><span style="color:black">好開店」</span>平台訂單成立之商品，即可享有免運優惠(滿10萬件即活動結束)；另外「<span style="color:black">好店＋</span>」於6/11-6/30期間內，前1,000名開店成功之商家，每位送100件免運費，共10萬件(需於109/8/31之前使用完畢)；優惠二：即日起至6/30端出物流優惠價，「好賣＋」每件優惠價39元、「好開店」及「好店＋」則推出每件4<span lang="EN-US" style="color:black">9</span><span style="color:black">元優惠價。</span></span></span></p>

<p style="margin:0cm 0cm 0.0001pt">&nbsp;</p>

<ol start="12" style="list-style-type:lower-alpha">
	<li style="margin:0cm 0cm 0.0001pt 24pt" value="50"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><b><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">全家開店平台介紹</span></span></b></span></span>

	<ul>
		<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">好賣</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">＋：</span></span><a href="https://famistore.famiport.com.tw/famistore/" style="color:#0563c1; text-decoration:underline">https://famistore.famiport.com.tw/famistore/</a></span></span></li>
		<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">好開店：</span><a href="https://famishop.fami.life/" style="color:#0563c1; text-decoration:underline" target="_blank">https://famishop.fami.life/</a></span></span></li>
		<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">好店</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">＋：</span></span><a href="https://haostore.fami.life/haostore/" style="color:#0563c1; text-decoration:underline">https://haostore.fami.life/haostore/</a></span></span></li>
	</ul>
	</li>
</ol>

<p style="margin-left:42.0pt; margin:0cm 0cm 0.0001pt 24pt">&nbsp;</p>

<table class="MsoTableGrid" style="border-collapse:collapse; border:solid windowtext 1.0pt">
	<tbody>
		<tr>
			<td colspan="2" style="border:solid windowtext 1.0pt; width:91.9pt; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">平台</span></span></span></p>
			</td>
			<td style="border:solid windowtext 1.0pt; width:92.15pt; border-left:none; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">好賣<span style="color:black">＋</span></span></span></p>
			</td>
			<td style="border:solid windowtext 1.0pt; width:4.0cm; border-left:none; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="151">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">好開店</span></span></span></p>
			</td>
			<td style="border:solid windowtext 1.0pt; width:117.35pt; border-left:none; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="156">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">好店<span style="color:black">＋</span></span></span></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="border:solid windowtext 1.0pt; width:91.9pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">定位</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">入門款平台</span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="151">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">進階款平台</span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="156">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">旗艦款平台</span></span></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="border:solid windowtext 1.0pt; width:91.9pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">適合對象</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><u><span style="color:black">社群團購賣家</span></u></b><span style="color:black">以社群團購為主要銷售管道</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="151">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><u><span style="color:black">微型電商賣家</span></u></b></span></span></p>

			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif">累積客群，想擁有初創的電商賣場</span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="156">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><b><u><span style="color:black">品牌電商賣家</span></u></b></span></span></p>

			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">擁有龐大客群的大賣家、實體店家跨足網路</span></span></span></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="border:solid windowtext 1.0pt; width:91.9pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">開店費用</span></span></span></p>
			</td>
			<td colspan="3" style="border-bottom:solid windowtext 1.0pt; width:322.9pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="431">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">免租金、免成交手續費</span></span></span></p>
			</td>
		</tr>
		<tr style="height:34.2pt">
			<td rowspan="3" style="border:solid windowtext 1.0pt; width:49.4pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt; height:34.2pt" width="66">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">金流</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:42.5pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt; height:34.2pt" width="57">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">全家取貨付款</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt; height:34.2pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">V</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt; height:34.2pt" width="151">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">V</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt; height:34.2pt" width="156">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">V</span></span></span></p>
			</td>
		</tr>
		<tr>
			<td style="border-bottom:solid windowtext 1.0pt; width:42.5pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="57">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">代碼繳費</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">V</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="151">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="font-size:11.0pt"><span style="color:black">陸續上線</span></span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="156">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="font-size:11.0pt"><span style="color:black">陸續上線</span></span></span></span></p>
			</td>
		</tr>
		<tr>
			<td style="border-bottom:solid windowtext 1.0pt; width:42.5pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="57">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">線上刷卡</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">V</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="151">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="font-size:11.0pt"><span style="color:black">陸續上線</span></span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="156">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">V</span></span></span></p>
			</td>
		</tr>
		<tr>
			<td style="border:solid windowtext 1.0pt; width:49.4pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt" width="66">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">物流</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:42.5pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="57">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">全家店到店</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">6/30</span><span style="color:black">前優惠價39元/件</span></span></span></p>

			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span lang="EN-US" style="color:black">(</span><span style="color:black">原價60元)</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="151">
			<ol>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span lang="EN-US" style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">6/11-6/30</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">，前</span></span><span lang="EN-US" style="color:black">10</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">萬筆訂單成立即可享有免運優惠</span></span></span></span></li>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span lang="EN-US" style="color:black">6/30</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">前優惠價</span></span><span lang="EN-US" style="color:black">49</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">元</span></span><span lang="EN-US" style="color:black">/</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">件</span></span><span lang="EN-US" style="color:black">(</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">原價</span></span><span lang="EN-US" style="color:black">60</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">元</span></span><span lang="EN-US" style="color:black">)</span></span></span></li>
			</ol>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="156">
			<ol>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span lang="EN-US" style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">6/11-6/30</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">，前1,000名開店商家，每位送100件免運費</span></span></span></li>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span lang="EN-US" style="color:black">6/30</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">前優惠價</span></span><span lang="EN-US" style="color:black">49</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">元</span></span><span lang="EN-US" style="color:black">/</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">件</span></span><span lang="EN-US" style="color:black">(</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">原價</span></span><span lang="EN-US" style="color:black">60</span><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">元</span></span><span lang="EN-US" style="color:black">)</span></span></span></li>
			</ol>
			</td>
		</tr>
		<tr>
			<td style="border:solid windowtext 1.0pt; width:49.4pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt" width="66">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">資訊流</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:42.5pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" width="57">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt">&nbsp;</p>
			</td>
			<td colspan="3" style="border-bottom:solid windowtext 1.0pt; width:322.9pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="431">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">買賣雙方若為「全家」會員，</span></span></span></p>

			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">可於「我的包裹」查訊包裹貨態</span></span></span></p>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="border:solid windowtext 1.0pt; width:91.9pt; border-top:none; padding:0cm 5.4pt 0cm 5.4pt" width="123">
			<p align="center" style="text-align:center; margin:0cm 0cm 0.0001pt"><span style="font-size:12pt"><span style="font-family:新細明體,serif"><span style="color:black">特色</span></span></span></p>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:92.15pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="123">
			<ul>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">簡易創業平台，商品可即時上架、分享連結至社群平台</span></span></span></span></li>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">買賣雙方為「全家」會員</span></span></span></span></li>
			</ul>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:4.0cm; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="151">
			<ul>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">簡單3步驟，3分鐘開店</span></span></span></li>
			</ul>

			<ul>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">賣場可被搜尋、買家增加訪客身分，擴大客群觸及性</span></span></span></li>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;">初步會員經營，提供促銷組合工具</span></span></span></li>
			</ul>
			</td>
			<td style="border-bottom:solid windowtext 1.0pt; width:117.35pt; border-top:none; border-left:none; border-right:solid windowtext 1.0pt; padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="156">
			<ul>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">會員分級管理</span></span></span></span></li>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">多元行銷模組</span></span></span></span></li>
				<li style="margin:0cm 0cm 0.0001pt 24pt"><span style="font-size:12pt"><span style="font-family:Calibri,sans-serif"><span style="font-family:&quot;新細明體&quot;,&quot;serif&quot;"><span style="color:black">營銷報表分析</span></span></span></span></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="sidebar" class="col-1-4">
                    <div class="wrap-col">
                        <div id="page-wrapper" class="col-lg-11">
                            <!--<div class="navtitle">新聞室</div>-->
                            <!-- /.navbar-top-links -->
                            <div class="navbar-default sidebar" role="navigation">
                                <div class="sidebar-nav navbar-collapse">
                                    <ul class="nav" id="side-menu">
                                        
                                                <li><a class=''
                                                        href='news.aspx?Y=2026'><i
                                                            class="fas fa-caret-right"></i>
                                                        2026
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2025'><i
                                                            class="fas fa-caret-right"></i>
                                                        2025
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2024'><i
                                                            class="fas fa-caret-right"></i>
                                                        2024
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2023'><i
                                                            class="fas fa-caret-right"></i>
                                                        2023
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2022'><i
                                                            class="fas fa-caret-right"></i>
                                                        2022
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2021'><i
                                                            class="fas fa-caret-right"></i>
                                                        2021
                                                    </a></li>
                                            
                                                <li><a class='active'
                                                        href='news.aspx?Y=2020'><i
                                                            class="fas fa-caret-right"></i>
                                                        2020
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2019'><i
                                                            class="fas fa-caret-right"></i>
                                                        2019
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2018'><i
                                                            class="fas fa-caret-right"></i>
                                                        2018
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2017'><i
                                                            class="fas fa-caret-right"></i>
                                                        2017
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2016'><i
                                                            class="fas fa-caret-right"></i>
                                                        2016
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2015'><i
                                                            class="fas fa-caret-right"></i>
                                                        2015
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2014'><i
                                                            class="fas fa-caret-right"></i>
                                                        2014
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2013'><i
                                                            class="fas fa-caret-right"></i>
                                                        2013
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2012'><i
                                                            class="fas fa-caret-right"></i>
                                                        2012
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2011'><i
                                                            class="fas fa-caret-right"></i>
                                                        2011
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2010'><i
                                                            class="fas fa-caret-right"></i>
                                                        2010
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2009'><i
                                                            class="fas fa-caret-right"></i>
                                                        2009
                                                    </a></li>
                                            
                                                <li><a class=''
                                                        href='news.aspx?Y=2008'><i
                                                            class="fas fa-caret-right"></i>
                                                        2008
                                                    </a></li>
                                            
                                    </ul>
                                </div>
                                <!-- /.sidebar-collapse -->
                            </div>
                            <!-- /.navbar-static-side -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--content end-->
    
        </div>
        <!--Quick view Block-->

        <script type="text/javascript">
            jQuery(function() {
                var tabContainers = jQuery('div.tabs > div');
                tabContainers.hide().filter(':first').show();
                jQuery('div.tabs ul.tabNavigation a').click(function() {
                    tabContainers.hide();
                    tabContainers.filter(this.hash).show();
                    jQuery('div.tabs ul.tabNavigation a').removeClass('selected');
                    jQuery(this).addClass('selected');
                    return false;
                }).filter(':first').click();
            });
        </script>

        <script type="text/javascript">
            // Javascript to enable link to tab
            var hash = document.location.hash;
            var prefix = "tab_";
            if (hash) {
                $('.nav-pills a[href=' + hash.replace(prefix, "") + ']').tab('show');
            }

            // Change hash for page-reload
            $('.nav-pills a').on('shown.bs.tab', function(e) {
                window.location.hash = e.target.hash.replace("#", "#" + prefix);
            });
        </script>

        <!--Footer Block-->
        <section class="footer-wrapper">
    <footer class="container">
    <div class="row">
      <div class="col-lg-7 col-md-7" style="padding: 0px;">
        <div class="col-lg-7 col-md-7 col-xs-7 pd">
          <div class="lh">全家便利商店股份有限公司</div>
          <div class="lh"><span class="glyphicon glyphicon-map-marker" aria-hidden="true" style="font-size:12pt;"></span>&nbsp;104台北市中山區中山北路二段61號7F</div>
        </div>
        <div class="col-lg-5  col-md-5 col-xs-5 pd">
          <div class="lh"><i class="fa fa-phone"  style="font-size:12pt;"></i>&nbsp;TEL&nbsp;02-25239588</div>
          <div class="lh"><i class="fa fa-phone-square"  style="font-size:12pt;"></i>&nbsp;客服專線&nbsp;0800-221-363</div>
        </div>
      </div>
      <div class="col-lg-5 col-md-5">
        <div class="col-lg-7 col-md-7 col-xs-7 pd">
          <div  class="lh"><a href="https://www.family.com.tw/marketing/faq_consumer.aspx" target="_blank"><i class="fa fa-question-circle" style="font-size:12pt;"></i>&nbsp;&nbsp;常見問題</a></div>
          <div  class="lh"><a href="contact_us.aspx"><i class="fa fa-envelope-square" style="font-size:12pt;"></i>&nbsp;&nbsp;聯絡我們</a></div>
        </div>
        <div class="col-lg-5 col-md-5 col-xs-5 pd">
          <div class="lh"><a href="https://www.family.com.tw/marketing/inquiry.aspx" target="_blank"><span class="glyphicon glyphicon-search" aria-hidden="true" style="font-size:11pt;"></span>&nbsp;店舖查詢</a></div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-9 col-md-9 col-xs-12 lh"> 
    <a href="https://www.family.com.tw/marketing/famiclub/famiclub_privacy.aspx" target="_blank">隱私權聲明</a> &nbsp;
    <a href="https://www.family.com.tw/marketing/privacy/pop.html" target="_blank">個資告知事項</a>
        <p class="copyright-block social-links">Copyright(c) ©Family Co.,Ltd. All Rights Reserved <a href="https://www.family.com.tw/Marketing/" target="_blank">全家便利商店</a></p>
      </div>
      <div class="col-lg-3 col-md-3 col-xs-12 payment-block">
        <div class="" style="margin-bottom: -5px"> <a href="https://www.tpipas.org.tw/DPmark/ShowCertData.aspx?id=B000002(01)" target="_blank"><img src="../images/ShowImage.gif" alt="payment" id="img_al"/></a></div>
        <div class="col-xs-12 dpmarkseal"> B 0 0 0 0 0 2 ( 0 1 ) </div>
      </div>
    </div>
    </footer>
    </section>
        <!-- for media -->
        <div id="mediaOverlay">
            <div id="youtubeWrap">
                <a href="">X</a>
                <div id="youtubePlayer">
                </div>
            </div>
        </div>

        <script type="text/javascript" src="../js/media.js"></script>

        <!-- JS -->

        <script type="text/javascript" src="../owl-carousel/owl.carousel.js"></script>

        <script type="text/javascript">
		$(document).ready(function () {
			$("#owl-demo-1").owlCarousel({
				autoPlay: 3000,
				items: 1,
				itemsDesktop: [1199, 1],
				itemsDesktopSmall: [400, 1]
			});
			$("#owl-demo-2").owlCarousel({
				autoPlay: 3000,
				items: 3,

			});
		});
        </script>

        <script type="text/javascript">
            $(document).ready(function() {
                $("#carousel-example-generic").carousel({
                    interval: false
                });
            });
        </script>

        <script type="text/javascript" src="../js/flexible-bootstrap-carousel.js"></script>

        <script type="text/javascript" src="../js/script.js"></script>

        <script type="text/javascript" src="../js/metisMenu.min.js"></script>

        <script type="text/javascript" src="../js/sb-admin-2.min.js"></script>

    </div>
    

<script type="text/javascript">
//<![CDATA[
(function() {var fn = function() {$get("ctl00_ToolkitScriptManager1_HiddenField").value = '';Sys.Application.remove_init(fn);};Sys.Application.add_init(fn);})();Sys.Application.initialize();
//]]>
</script>
</form>
</body>
</html>
