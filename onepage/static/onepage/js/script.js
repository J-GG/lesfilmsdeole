$(document).ready(function () {

    /*=====================================
    RGPD
    =====================================*/

    tarteaucitron.init({
        "privacyUrl": "", /* Privacy policy url */

        "hashtag": "#tarteaucitron", /* Open the panel with this hashtag */
        "cookieName": "tarteaucitron", /* Cookie name */

        "orientation": "bottom", /* Banner position (top - bottom) */
        "showAlertSmall": true, /* Show the small banner on bottom right */
        "cookieslist": true, /* Show the cookie list */

        "adblocker": false, /* Show a Warning if an adblocker is detected */
        "AcceptAllCta": true, /* Show the accept all button when highPrivacy on */
        "highPrivacy": false, /* Disable auto consent */
        "handleBrowserDNTRequest": false, /* If Do Not Track == 1, disallow all */

        "removeCredit": false, /* Remove credit link */
        "moreInfoLink": true, /* Show more info link */
        "useExternalCss": false, /* If false, the tarteaucitron.css file will be loaded */
    });

    let analytics_url = $("script[src*='www.googletagmanager.com']").attr("src");
    tarteaucitron.user.gtagUa = analytics_url.substr(analytics_url.indexOf("UA"));
    (tarteaucitron.job = tarteaucitron.job || []).push('gtag');

    /*=====================================
    Tooltip
    =====================================*/

    $('[data-toggle="tooltip"]').tooltip();

    /*=====================================
    Smooth Scroll
    =====================================*/

    $("a").click(function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            let hash = this.hash;
            $("html, body").animate({
                scrollTop: $(hash).offset().top
            });
        }
    });

    /*=====================================
    Scroll To Top
    =====================================*/

    let $scrollTop = $("#scroll-top");
    $(window).scroll(() => $(this).scrollTop() >= 300 ? $scrollTop.fadeIn(700) : $scrollTop.fadeOut(700));

    $scrollTop.on('click', () => $("html, body").animate({scrollTop: 0}, 900));


    /*=====================================
    Portfolio
    =====================================*/

    $('#grid').mediaBoxes({
        filterContainer: '#filter',
        LoadingWord: "Chargement...",
        loadMoreWord: "En voir plus",
        noMoreEntriesWord: "Tout est affiché",
        boxesToLoadStart: 8,
        lazyLoad: false,
        fancybox: {
            transitionEffect: 'slide',
            transitionDuration: 750,
            thumbs: {autoStart: true},
            buttons: [
                "share",
                "slideShow",
                "fullScreen",
                "thumbs",
                "close"
            ],
        },
        animation_on_thumbnail_overlay_hover: [
            {item: '.media-box-title', animation: 'from-top'},
            {item: '.media-box-date', animation: 'from-bottom'}
        ]
    });

    $.fancyboxMB.defaults.lang = "fr";
    $.fancyboxMB.defaults.i18n.fr = {
        CLOSE: "Fermer",
        NEXT: "Suivant",
        PREV: "Précédent",
        ERROR: "Le contenu ne peut pas être chargé. <br/> Veuillez réessayer plus tard.",
        PLAY_START: "Démarrer le diaporama",
        PLAY_STOP: "Mettre en pause le diaporama",
        FULL_SCREEN: "Plein écran",
        THUMBS: "Miniatures",
        DOWNLOAD: "Téléchargement",
        SHARE: "Partager",
        ZOOM: "Zoom"
    };

    $.fancyboxMB.defaults.share.tpl = '<div class="fancyboxMB-share"><h1>{{SHARE}}</h1><p><a class="fancyboxMB-share__button fancyboxMB-share__button--fb" href="https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.host + '#(grid|popup)=') + '{{url}}' + encodeURIComponent(";") + '"><svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="m287 456v-299c0-21 6-35 35-35h38v-63c-7-1-29-3-55-3-54 0-91 33-91 94v306m143-254h-205v72h196"/></svg><span>Facebook</span></a><a class="fancyboxMB-share__button fancyboxMB-share__button--tw" href="https://twitter.com/intent/tweet?url=' + encodeURIComponent(window.location.host + '#(grid|popup)=') + '{{url}}' + encodeURIComponent(";") + '&text=' + encodeURIComponent(document.title + ' | ') + '{{descr}} ' + encodeURIComponent(window.location.host + '#(grid|popup)=') + '{{url}}' + encodeURIComponent(";") + '"><svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="m456 133c-14 7-31 11-47 13 17-10 30-27 37-46-15 10-34 16-52 20-61-62-157-7-141 75-68-3-129-35-169-85-22 37-11 86 26 109-13 0-26-4-37-9 0 39 28 72 65 80-12 3-25 4-37 2 10 33 41 57 77 57-42 30-77 38-122 34 170 111 378-32 359-208 16-11 30-25 41-42z"/></svg><span>Twitter</span></a><a class="fancyboxMB-share__button fancyboxMB-share__button--pt" href="https://www.pinterest.com/pin/create/button/?url=' + encodeURIComponent(window.location.host + '#(grid|popup)=') + '{{url}}' + encodeURIComponent(";") + '&description=' + encodeURIComponent(document.title + ' | ') + '{{descr}}&media={{media}}"><svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="m265 56c-109 0-164 78-164 144 0 39 15 74 47 87 5 2 10 0 12-5l4-19c2-6 1-8-3-13-9-11-15-25-15-45 0-58 43-110 113-110 62 0 96 38 96 88 0 67-30 122-73 122-24 0-42-19-36-44 6-29 20-60 20-81 0-19-10-35-31-35-25 0-44 26-44 60 0 21 7 36 7 36l-30 125c-8 37-1 83 0 87 0 3 4 4 5 2 2-3 32-39 42-75l16-64c8 16 31 29 56 29 74 0 124-67 124-157 0-69-58-132-146-132z" fill="#fff"/></svg><span>Pinterest</span></a></p><p><input class="fancyboxMB-share__input" type="text" value="' + window.location.host + '#(grid|popup)={{url_raw}};" onclick="select()"/></p></div>';

    /*=====================================
    Testimonials
    =====================================*/

    $("#owl-testimonials").owlCarousel({
        loop: true,
        nav: false,
        items: 1,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        autoplaySpeed: 1000
    });

    /*=====================================
    Regulations
    =====================================*/

    $("#distance").ionRangeSlider({
        values: ["100m", "200m", "400m", "1000m", "∞"],
        grid: true
    });

    $("#altitude").ionRangeSlider({
        values: ["50m", "150m"],
        grid: true
    });

    $("#weight").ionRangeSlider({
        values: ["2kg", "8kg", "25kg"],
        grid: true
    });

    let isScenario1Suitable = (inhabited, inSight, distance, altitude, weight) => !inhabited && inSight && distance <= 200 && altitude <= 150 && weight <= 25;
    let isScenario2Suitable = (inhabited, inSight, distance, altitude, weight) => !inhabited && distance <= 1000 && ((weight <= 25 && altitude <= 50) || (weight <= 2 && altitude <= 150));
    let isScenario3Suitable = (inhabited, inSight, distance, altitude, weight) => inhabited && inSight && distance <= 100 && altitude <= 150 && weight <= 8;
    let isScenario4Suitable = (inhabited, inSight, distance, altitude, weight) => !inhabited && altitude <= 150 && weight <= 2;

    $(".scenario_inputs :input").on("change", function () {
        let inhabited = $("#inhabited").prop("checked") === true
        let inSight = $("#in-sight").prop("checked") === true
        let distance = $("#distance").val();
        distance = distance === "∞" ? "∞" : distance.substring(0, distance.length - 1);
        let altitude = $("#altitude").val().substring(0, $("#altitude").val().length - 1);
        let weight = $("#weight").val().substring(0, $("#weight").val().length - 2);

        if (inhabited) {
            $(".scenario_city").addClass("scenario_visible");
            $(".scenario_countryside").removeClass("scenario_visible");
        } else {
            $(".scenario_city").removeClass("scenario_visible");
            $(".scenario_countryside").addClass("scenario_visible");
        }

        if (!inSight) {
            $(".scenario_tree, .scenario_tree2").addClass("scenario_visible");
        } else {
            $(".scenario_tree, .scenario_tree2").removeClass("scenario_visible");
        }

        $(".scenario_distance").removeClass("scenario_distance_100 scenario_distance_200 scenario_distance_400 scenario_distance_1000 scenario_distance_∞");
        $(".scenario_drone").removeClass("scenario_drone_distance_100 scenario_drone_distance_200 scenario_drone_distance_400 scenario_drone_distance_1000 scenario_drone_distance_∞");
        $(".scenario_distance").addClass("scenario_distance_" + distance);
        $(".scenario_drone").addClass("scenario_drone_distance_" + distance);
        $(".scenario_distance_text").text($("#distance").val());

        $(".scenario_altitude").removeClass("scenario_altitude_50 scenario_altitude_150");
        $(".scenario_drone").removeClass("scenario_drone_altitude_50 scenario_drone_altitude_150");
        $(".scenario_altitude").addClass("scenario_altitude_" + altitude);
        $(".scenario_drone").addClass("scenario_drone_altitude_" + altitude);
        $(".scenario_altitude_text").text($("#altitude").val());

        $(".scenario_drone").removeClass("scenario_drone_weight_2 scenario_drone_weight_8 scenario_drone_weight_25");
        $(".scenario_drone").addClass("scenario_drone_weight_" + weight);


        $(".scenario_explanation_text").addClass("d-none");
        if (isScenario1Suitable(inhabited, inSight, distance, altitude, weight)) {
            $(".scenario_1").removeClass("d-none");
        } else if (isScenario2Suitable(inhabited, inSight, distance, altitude, weight)) {
            $(".scenario_2").removeClass("d-none");
        } else if (isScenario3Suitable(inhabited, inSight, distance, altitude, weight)) {
            $(".scenario_3").removeClass("d-none");
        } else if (isScenario4Suitable(inhabited, inSight, distance, altitude, weight)) {
            $(".scenario_4").removeClass("d-none");
        } else {
            $(".scenario_no").removeClass("d-none");
        }
    });

    /*=====================================
    Partnership
    =====================================*/

    $('#owl-partnership').owlCarousel({
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            160: {
                items: 2
            },
            320: {
                items: 3
            },
            500: {
                items: 5
            },
            700: {
                items: 6
            },
            992: {
                items: 7
            }
        },
        margin: 10,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true
    });

    /*=====================================
    Pricing
    =====================================*/

    $(".price a").click(function () {
        let name = $(this).siblings("h3").text().trim();
        $("#form-subject").val("Demande d'informations à propos de " + name);
        $("#form-subject").trigger("focusin");
        $("#form-message").val("Bonjour,\nje voudrais avoir plus d'informations concernant une prestation de type " + name + ".");
        $("#form-message").trigger("focusin");
    });

    /*=====================================
    Contact
    =====================================*/

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $("#contact-form").submit(function (event) {
        event.preventDefault();
        let $form = $(this);
        if (!$form.hasClass("was-validated")) {
            $form.addClass("was-validated");
        }
        $form.find(".g-recaptcha + .invalid-feedback").removeClass("captcha-feedback");

        $.ajax({
            type: "POST",
            url: $form.attr("action"),
            data: $form.serialize(),
            beforeSend: function (xhr) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            },
            success: function (data) {
                if (data.success) {
                    $form.trigger("reset");
                    $form.removeClass("was-validated");
                    toastr.success(data.message);
                    grecaptcha.reset();
                }
            },
            error: function (xhr) {
                if (!xhr || !xhr.responseJSON || !xhr.responseJSON.error || xhr.responseJSON.error === "email") {
                    toastr.error(xhr.responseJSON.message);
                }
                else if (xhr.responseJSON.error === "captcha") {
                    $form.find(".g-recaptcha + .invalid-feedback").addClass("captcha-feedback");
                    grecaptcha.reset();
                }
            }
        });
    });
});