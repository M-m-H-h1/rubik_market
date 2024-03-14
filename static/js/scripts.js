$(function () {
    /* encode4365gbf265g43d Range Slider */
    if ($('#steps-slider').length) {
        var slider = document.getElementById('steps-slider');
        // پایان محدوده
        if (min_price_t && max_price_t) {
            noUiSlider.create(slider, {
                direction: 'rtl',
                start: [min_price_t, max_price_t],
                connect: true,
                step: 100000,
                range: {
                    'min': 0,
                    'max': 100000000
                }
            });
        } else {
            noUiSlider.create(slider, {
                direction: 'rtl',
                start: [0, 100000000],
                connect: true,
                step: 100000,
                range: {
                    'min': 0,
                    'max': 100000000
                }
            });
        }


        slider.noUiSlider.on('update', function (values) {
            $('#encode4365gbf265g43d-range-from').text(numFormat(Math.round(values[0])));
            $('#encode4365gbf265g43d-range-to').text(numFormat(Math.round(values[1])));

            var min_price = Math.round(values[0]);
            var max_price = Math.round(values[1]);


            document.getElementById('min_price').value = min_price;
            document.getElementById('max_price').value = max_price;
        });
    }


    /* encode4365gbf265g43d Range Slider */

    /* On Sale Counter */
    try {
        function countDown() {
            var tarikh = new persianDate().toLocale('en').format('YYYY-M-D HH:mm:ss');
            var today = new Date(tarikh); // تاریخ فعلی
            var eventDate = endTime - today; // محاسبه تفاوت بین endTime و تاریخ فعلی

            if (eventDate > 0) {
                var seconds = Math.floor(eventDate / 1000);
                var minutes = Math.floor(seconds / 60);
                var hours = Math.floor(minutes / 60);
                var days = Math.floor(hours / 24);

                hours %= 24;
                minutes %= 60;
                seconds %= 60;

                // قسمت‌های مربوط به نمایش زمان در تایمر
                var elTimeCounter = $('.time-counter');
                var elDays = $('.days', elTimeCounter);
                var elHours = $('.hours', elTimeCounter);
                var elMinutes = $('.minutes', elTimeCounter);
                var elSeconds = $('.seconds', elTimeCounter);

                $('.num', elDays).html(days);
                $('.num', elHours).html(hours);
                $('.num', elMinutes).html(minutes);
                $('.num', elSeconds).html(seconds);

                setTimeout(countDown, 1000);

            } else {
                fetch(`http://127.0.0.1:8000/product/special-product/${product_id}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({}),
                })
            }
        }

        countDown();
    } catch (e) {

    }


    /* /On Sale Counter */

    /* Initialize menu */
    $('.droopmenu-navbar').droopmenu({
        dmArrow: true,
        dmArrowDirection: 'dmarrowdown'
    });
    /* /Initialize menu */

    /* Featured Products Filter */
    if ($('.featured-categories').length) {
        $('.featured-categories').click(function () {
            var category = $(this).data('val');
            $('.featured-product').each(function () {
                if ($(this).hasClass(category))
                    $(this).fadeIn();
                else
                    $(this).fadeOut(0);
            })

            /* Update Active Menu */
            $('.featured-categories').each(function () {
                $(this).removeClass('active');
                if ($(this).data('val') == category)
                    $(this).addClass('active');
            })
        })
        $('.featured-categories').eq(0).trigger('click');
    }
    /* /Featured Products Filter */

    /* Most Sold Products Filter */
    if ($('.most-sales-categories').length) {
        $('.most-sales-categories').click(function () {
            var category = $(this).data('val');
            $('.most-sales-product').each(function () {
                if ($(this).hasClass(category))
                    $(this).fadeIn();
                else
                    $(this).fadeOut(0);
            })

            /* Update Active Menu */
            $('.most-sales-categories').each(function () {
                $(this).removeClass('active');
                if ($(this).data('val') == category)
                    $(this).addClass('active');
            })
        })
        $('.most-sales-categories').eq(0).trigger('click');
    }
    /* /Most Sold Products Filter */

    /* Collapse In Mobile */
    if ($('.collapse').length) {
        if (($(window).width()) < 992) {
            $('.collapse').removeClass('show');
        }
    }
    /* /Collapse In Mobile */

    /* Num Format Functions */
    function intFormat(number) {
        var regex = /(\d)((\d{3},?)+)$/;
        number = number + '';
        number = number.split(',').join('');

        while (regex.test(number)) {
            number = number.replace(regex, '$1,$2');
        }
        return number;
    }

    function numFormat(number) {
        var pointReg = /([\d,\.]*)\.(\d*)$/, f;
        if (pointReg.test(number)) {
            f = RegExp.$2;
            return intFormat(RegExp.$1) + '.' + f;
        }
        return intFormat(number);
    }

    /* /Num Format Functions */

    /* Products Carousel */
    if ($('.products-carousel').length > 0) {
        var owl = $('.products-carousel');
        owl.owlCarousel({
            rtl: true,
            autoplay: true,
            autoplayHoverPause: true,
            margin: 25,
            nav: false,
            dots: false,
            loop: true,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 3
                },
                1000: {
                    items: 4
                }
            }
        })
    }
    /* /Products Carousel */

    /* Product Order Number */
    if ($('.btn-plus').length > 0) {
        $('.btn-plus').click(function () {
            var index = $(this).index('.btn-plus');
            var orderNumber = Number($('input.order-number').eq(index).val());
            $('input.order-number').eq(index).val(orderNumber + 1);
        })

        $('.btn-minus').click(function () {
            var index = $(this).index('.btn-minus');
            var orderNumber = Number($('input.order-number').eq(index).val());
            if (orderNumber > 1)
                $('input.order-number').eq(index).val(orderNumber - 1);
        })
    }

    AOS.init();
});

function set_value(id, name) {
    document.getElementById('parent_id').value = id;
    window.location.href = '#c_input'
    document.getElementById('input').placeholder = `در پاسخ به ${name}`
    document.getElementById('reply_s').classList.remove('d-none');
    document.getElementById('replay-mas').textContent = `در پاسخ به ${name}`
}

function delete_vlue() {
    document.getElementById('parent_id').value = '';
    document.getElementById('reply_s').classList.add('d-none');
    document.getElementById('input').placeholder = 'نظر خود را وارد کنید'
}


var alertBox = $('.alert');

// تنظیم تایمر برای پنهان کردن پیام با انیمیشن fadeOut
setTimeout(function () {
    alertBox.slideUp(900, function () {
        alertBox.remove();
    });
}, 3000);

$('.closebtn').click(function () {
    // اعمال انیمیشن fadeOut به المان .alert
    $(this).parent('.alert').slideUp(400, function () {
        // حذف المان .alert
        $(this).remove();
    });
});

$('.quantity button').on('click', function () {
    var button = $(this);
    var oldValue = button.parent().parent().find('input').val();
    var newVal;

    if (button.hasClass('btn-plus')) {
        newVal = parseFloat(oldValue) + 1;
    } else {
        if (oldValue > 1) {
            newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 1;
        }
    }

    // محدود کردن مقدار ورودی به حداکثر 10
    if (newVal > 10) {
        newVal = 10;
    }

    button.parent().parent().find('input').val(newVal);
});


